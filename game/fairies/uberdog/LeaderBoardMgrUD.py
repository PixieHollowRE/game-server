from datetime import datetime, timedelta, timezone

from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

from game.fairies.leaderboard import leaderboard_xml
from game.fairies.leaderboard.leaderboard_period import (
    TYPE_SEASONAL,
    TYPE_WEEKLY,
    period_end,
    period_key,
)

# lbResponse returns at most a top ten -- Leaderboards.showTopTenFairies lays the
# entries out in two columns of five and has nowhere to put an eleventh.
TOP_N = 10

# How long a row outlives its period before the TTL index sweeps it. The board
# already stops showing it the moment the period rolls (the key stops matching);
# this is only cleanup, so a day's slack past the boundary is plenty and covers
# minor clock skew between here and the mongod.
TTL_GRACE = timedelta(days=1)


class LeaderBoardMgrUD(DistributedObjectGlobalUD):
    """
    Owns every game's weekly and seasonal high-score boards.

    The districts never hold board state: a minigame AI reports a finished run
    through the AI-side LeaderBoardMgrAI (putToLeaderBoard for a high score,
    addToLeaderBoard for a win count) and this object decides whether it places,
    writes it to the `leaderboards` collection, and answers the client's
    lbRequest with the ranked top ten.

    Boards never need resetting: every read and write is scoped to the key of
    the period it falls in (see leaderboard_period), so a new week or season just
    starts empty. A run counts toward both the weekly and the seasonal board, so
    a submission writes to both periods at once.
    """

    def __init__(self, air) -> None:
        super().__init__(air)

    def announceGenerate(self) -> None:
        DistributedObjectGlobalUD.announceGenerate(self)

        try:
            leaderboard_xml.load()
        except (OSError, ValueError) as e:
            self.notify.warning(
                f"Could not read leaderboard data from "
                f"{leaderboard_xml.LEADERBOARDS_XML} ({e}). No score can be "
                f"recorded until this is fixed. On Windows, run "
                f"startup/win32/symlink.bat to link the XML data into place."
            )

        # One row per fairy per board per period, and a ranked lookup for
        # lbRequest. Both are idempotent, so this is safe to run every startup.
        boards = self.air.mongoInterface.mongodb.leaderboards
        boards.create_index(
            [("periodKey", 1), ("gameId", 1), ("avId", 1)], unique=True
        )
        boards.create_index([("periodKey", 1), ("gameId", 1), ("score", -1)])
        # Housekeeping: drop each row once its period is well and truly over. The
        # row stores its own expiry (period end + grace), so a short-lived weekly
        # entry and a season-long one each clear on their own schedule -- see
        # _writeEachPeriod. expireAfterSeconds=0 means "delete when expiresAt
        # passes" rather than a fixed lifetime from it.
        boards.create_index("expiresAt", expireAfterSeconds=0)


    def putToLeaderBoard(self, avatarId: int, gameId: int, score: int) -> None:
        """
        Record a high score. Kept only if it beats the fairy's own best this
        period, and only if it clears the game's threshold at all -- a single run
        below the minimum can never place, so it is dropped rather than stored.
        """
        threshold = leaderboard_xml.get_threshold(gameId)

        if threshold is None:
            # Not a game with a board; nothing to record.
            return

        if score < threshold:
            return

        self._writeEachPeriod(avatarId, gameId, {"$max": {"score": score}})

    def addToLeaderBoard(self, avatarId: int, gameId: int, amount: int) -> None:
        """
        Add to a running win count (the three Meadow games). Unlike a high score
        these accumulate one win at a time and are gated against the threshold on
        read instead -- see lbRequest -- since they could never reach it if each
        sub-threshold win were dropped here.
        """
        if amount <= 0:
            return

        if not leaderboard_xml.is_leaderboard_game(gameId):
            return

        self._writeEachPeriod(avatarId, gameId, {"$inc": {"score": amount}})

    def _writeEachPeriod(self, avatarId: int, gameId: int, scoreUpdate: dict) -> None:
        now = datetime.now(timezone.utc)
        boards = self.air.mongoInterface.mongodb.leaderboards

        for boardType in (TYPE_WEEKLY, TYPE_SEASONAL):
            pk = period_key(boardType, now)

            if pk is None:
                continue

            # expiresAt is fixed to this period's end (plus grace) and re-set to
            # the same value on every write, so a row playing all season keeps its
            # end date rather than sliding forward each time it's touched.
            expiresAt = period_end(boardType, now) + TTL_GRACE

            # The (periodKey, gameId, avId) query fields land in the doc on
            # insert, so a first submission this period creates the row and the
            # $max/$inc applies to it straight away.
            boards.update_one(
                {"periodKey": pk, "gameId": gameId, "avId": avatarId},
                {**scoreUpdate, "$set": {"updatedAt": now, "expiresAt": expiresAt}},
                upsert=True,
            )

    def lbRequest(self, gameId: int, boardType: int) -> None:
        requesterId = self.air.getAvatarIdFromSender()

        threshold = leaderboard_xml.get_threshold(gameId)
        pk = period_key(boardType)

        if threshold is None or pk is None:
            # Unknown game or board type -- answer with an empty board rather
            # than leave the panel spinning on its loading clip.
            self.sendUpdateToAvatarId(
                requesterId, "lbResponse", [gameId, boardType, []]
            )
            return

        boards = self.air.mongoInterface.mongodb.leaderboards
        rows = list(
            boards.find(
                {"periodKey": pk, "gameId": gameId, "score": {"$gte": threshold}},
                {"avId": 1, "score": 1},
            )
            .sort("score", -1)
            .limit(TOP_N)
        )

        names = self._namesFor(rows)
        entries = [
            # LbEntry: avId, score, avName, addrNum, addrStr. The client reads
            # only the first three; the address pair is unused, so send it empty.
            [row["avId"], row["score"], names.get(row["avId"], ""), 0, ""]
            for row in rows
        ]

        self.sendUpdateToAvatarId(
            requesterId, "lbResponse", [gameId, boardType, entries]
        )

    def _namesFor(self, rows: list) -> dict:
        avIds = [row["avId"] for row in rows]
        fairies = self.air.mongoInterface.mongodb.fairies.find(
            {"_id": {"$in": avIds}}, {"name": 1}
        )
        return {fairy["_id"]: fairy.get("name", "") for fairy in fairies}

# ─────────────────────────────────────── ADMIN ────────────────────────────────────── #

    def forceRollover(self, boardType: int) -> None:
        """
        Clear the current period of a board early. Because the period key is
        derived from the date rather than an incrementing counter, this ends the
        running period by emptying it; the next submission starts it fresh.
        """
        pk = period_key(boardType)

        if pk is None:
            return

        self.air.mongoInterface.mongodb.leaderboards.delete_many({"periodKey": pk})
