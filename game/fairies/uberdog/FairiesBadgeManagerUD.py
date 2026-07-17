from datetime import datetime

from pymongo import ReturnDocument

from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

from game.fairies.badges import badge_events, badge_lookup, badge_xml
from game.fairies.badges.badge_state import STATUS_ACTIVE, STATUS_EARNED

# Chapters tracked from a fairy's first login. Everything else in the book is
# left alone for now.
#
# Chapter 1  - Starter Badges
# Chapter 2  - Friendship
# Chapter 3  - Exploration (seasonal Meadow Explorer badges)
# Chapter 7  - Talent Games
# Chapter 10 - Ingredients
# Chapter 18 - Baking     (practice + personal ladders; tier-1 Helper is in ch.1)
# Chapter 19 - Tinkering  (practice + personal ladders; tier-1 Helper is in ch.1)
# Chapter 20 - Tailoring  (practice + personal ladders; tier-1 Helper is in ch.1)
# Chapter 21 - Donations  (wardrobe + storage ladders; the Royal honor that tops
#                          both out is 10821, tracked via INCLUDED_BADGES)
TRACKED_CHAPTER_IDS = (1, 2, 3, 7, 10, 18, 19, 20, 21)

# Badges inside a tracked chapter to leave off the page entirely, for content
# that is unused.
EXCLUDED_BADGE_IDS = frozenset({
    10822,  # Mainland Sorter
    10823,  # Super Mainland Sorter
    10824,  # Flitterific Mainland Sorter
})

# Badges tracked one at a time outside TRACKED_CHAPTER_IDS: each gets its own
# row and its own page unlocks, but the rest of that badge's chapter does not
# come along for the ride. The mirror image of EXCLUDED_BADGE_IDS, which
# subtracts a badge from a chapter that *is* tracked -- this adds one from a
# chapter that isn't.
#
# Value is the status the row is created with:
#   STATUS_EARNED - granted the moment the fairy is first seen, the way
#                    Founding Fairy always has been. Use this for something
#                    there is no way to earn after the fact.
#   STATUS_ACTIVE  - given a row and a visible page, then left to accumulate
#                    normally through badge_events, same as anything in a
#                    tracked chapter.
FOUNDING_FAIRY = 10573
NEW_FAIRY = 10574

INCLUDED_BADGES: dict[int, str] = {
    FOUNDING_FAIRY: STATUS_EARNED,
    NEW_FAIRY: STATUS_EARNED,
    # Royal Wardrobe and Storage Donation -- an Honors badge (chapter 0, page
    # 12042) rather than part of the tracked Donations chapter. Given a row and
    # its page so it can be earned after the fact, then granted outright by
    # _maybeAwardRoyalDonation once both Flitterific tiers are.
    badge_events.ROYAL_DONATION_BADGE: STATUS_ACTIVE,
}

def _badgeIdsIn(chapterIds) -> tuple[int, ...]:
    return tuple(
        badge["id"]
        for chapterId in chapterIds
        for badge in badge_lookup.get_badges_for_chapter(chapterId)
        if badge["id"] not in EXCLUDED_BADGE_IDS
    )


def _pageIdsIn(chapterIds) -> tuple[int, ...]:
    return tuple(
        page["id"]
        for chapterId in chapterIds
        for page in badge_lookup.get_pages_for_chapter(chapterId)
    )


def _pageIdsForBadges(badgeIds) -> tuple[int, ...]:
    seen = set()
    pageIds = []

    for badgeId in badgeIds:
        page = badge_lookup.get_page_for_badge(badgeId)

        if page is None or page["id"] in seen:
            continue

        seen.add(page["id"])
        pageIds.append(page["id"])

    return tuple(pageIds)


TRACKED_BADGE_IDS = _badgeIdsIn(TRACKED_CHAPTER_IDS)
TRACKED_PAGE_IDS = _pageIdsIn(TRACKED_CHAPTER_IDS)
INCLUDED_PAGE_IDS = _pageIdsForBadges(INCLUDED_BADGES)


class FairiesBadgeManagerUD(DistributedObjectGlobalUD):
    """
    Owns every fairy's badge progress.

    The districts have no badge state of their own: they raise events (see
    badge_events) and this object decides what that means, writes it to
    badgeData on the fairy, and tells the client.
    """

    def __init__(self, air) -> None:
        super().__init__(air)

    def announceGenerate(self) -> None:
        DistributedObjectGlobalUD.announceGenerate(self)

        try:
            badge_xml.load()
        except (OSError, ValueError) as e:
            self.notify.warning(
                f"Could not read badge data from {badge_xml.BADGES_XML} ({e}). "
                f"No badge can be awarded until this is fixed. On Windows, run "
                f"startup/win32/symlink.bat to link the XML data into place."
            )

        self.accept("avatarOnline", self.avatarOnline)

    def avatarOnline(self, avatarId, avatarType) -> None:
        # avatarType is unused, but it is sent over the messenger anyways.
        rows, unlockedPages = self._ensureTrackedBadges(avatarId)

        if rows is None:
            return

        # A fairy who logged in before a badge was excluded still has its row.
        # Drop it on the way out rather than deleting it, so that un-excluding
        # the badge later hands them back the progress they had.
        rows = [row for row in rows if row["badgeId"] not in EXCLUDED_BADGE_IDS]

        earnedBadges = [
            [row["badgeId"], self._formatDateEarned(row.get("dateEarned"))]
            for row in rows
            if row.get("status") == STATUS_EARNED
        ]
        badgeProgress = [
            [row["badgeId"], row.get("progress", 0)]
            for row in rows
            if row.get("status") == STATUS_ACTIVE
        ]

        self.sendUpdateToAvatarId(
            avatarId, "setBadges", [earnedBadges, unlockedPages, badgeProgress]
        )

    def accumulateForMe(self, eventId: int) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        if eventId not in badge_events.CLIENT_RAISED_EVENTS:
            self.notify.warning(
                f"accumulateForMe: avId={avatarId} sent unexpected eventId={eventId}"
            )
            return

        self._accumulate(avatarId, eventId, 1)

    def accumulate(self, avatarId: int, eventId: int, amount: int) -> None:
        # Meadow Explorer badges count distinct zones rather than occurrences, so
        # their visits arrive over this same field (see
        # FairiesBadgeManagerAI.d_exploreMeadow) with the zoneId in the amount
        # slot, and branch off to a path that dedupes them.
        if eventId == badge_events.EVENT_EXPLORE_MEADOW:
            self._exploreMeadow(avatarId, amount)
            return

        self._accumulate(avatarId, eventId, amount)

    def giveBadge(self, avatarId: int, badgeId: int) -> None:
        """
        Award a badge the district has already decided is earned (see
        FairiesBadgeManagerAI.d_giveBadge) -- currently only minigame High
        Scores, whose threshold is checked on the AI.

        There is no progress to bank, so this jumps straight to earned, but it
        still goes through the same guards as _addProgress: an excluded or
        Member-only badge is refused here too, and _awardBadge only touches a
        tracked ACTIVE row, so re-beating the score after earning it no-ops.
        """
        if badgeId in EXCLUDED_BADGE_IDS:
            return

        if badge_xml.is_velvet_rope_restricted(badgeId) and not self.air.isAvatarPaid(avatarId):
            return

        # Store the goal as progress for a tidy book, the way an accumulated
        # award lands on its goal. High Score badges render "Keep working!"
        # until earned rather than "#CURRENT# of #GOAL#", so the exact number
        # never shows; fall back to 0 if the badge somehow has no goal.
        goal = badge_xml.get_goal(badgeId) or 0
        self._awardBadge(avatarId, badgeId, goal)

    def _accumulate(self, avatarId: int, eventId: int, amount: int) -> None:
        if amount <= 0:
            return

        for badgeId in badge_events.get_badges_for_event(eventId):
            self._addProgress(avatarId, badgeId, amount)

    def _addProgress(self, avatarId: int, badgeId: int, amount: int) -> None:
        # An excluded badge must not accumulate even where an old row survives:
        # left alone it would fill up unseen and eventually award itself, and
        # badgeAcquired is enough to put it back on the page.
        if badgeId in EXCLUDED_BADGE_IDS:
            return

        goal = badge_xml.get_goal(badgeId)

        if goal is None:
            self.notify.warning(f"No goal for badgeId={badgeId}, cannot award it")
            return

        if badge_xml.is_velvet_rope_restricted(badgeId) and not self.air.isAvatarPaid(avatarId):
            return

        fairy = self.air.mongoInterface.mongodb.fairies.find_one_and_update(
            {
                "_id": avatarId,
                "badgeData.badges": {
                    "$elemMatch": {"badgeId": badgeId, "status": STATUS_ACTIVE}
                },
            },
            {"$inc": {"badgeData.badges.$.progress": amount}},
            projection={"badgeData.badges.$": 1},
            return_document=ReturnDocument.BEFORE,
        )

        if fairy is None:
            # Badge already earned, or not tracked for this fairy.
            return

        previous = fairy["badgeData"]["badges"][0]["progress"]
        progress = previous + amount

        # The client does `progress += delta` rather than taking an absolute, so
        # send what actually landed, and never count past the goal. The max()
        # matters if a goal is ever lowered in the XML below what someone has
        # already banked -- without it the client would be sent a negative.
        applied = max(0, min(amount, goal - previous))

        if applied:
            self.sendUpdateToAvatarId(avatarId, "progressUpdate", [badgeId, applied])

        if progress >= goal:
            self._awardBadge(avatarId, badgeId, goal)

    def _exploreMeadow(self, avatarId: int, zoneId: int) -> None:
        """
        Advance a seasonal Meadow Explorer badge for visiting one of its meadows.

        Unlike the accumulated badges these count *distinct* zones: the meadows a
        fairy has already stood in are kept as a set on the badge row, so
        re-entering one can never advance it twice. The district fires this on
        every entry and leaves the deduping to us, since we are the one writer
        that sees every district.
        """
        badgeId = badge_events.get_meadow_badge_for_zone(zoneId)

        if badgeId is None:
            self.notify.warning(f"_exploreMeadow: zoneId={zoneId} is not a meadow")
            return

        goal = badge_xml.get_goal(badgeId)

        if goal is None:
            self.notify.warning(f"No goal for badgeId={badgeId}, cannot award it")
            return

        # Every current explorer badge is free; the gate is here for parity with
        # the other award paths, should a later season badge be Member-only.
        if badge_xml.is_velvet_rope_restricted(badgeId) and not self.air.isAvatarPaid(avatarId):
            return

        # $addToSet makes the visit idempotent; reading the row as it stood
        # BEFORE is how we tell a first visit from a revisit.
        fairy = self.air.mongoInterface.mongodb.fairies.find_one_and_update(
            {
                "_id": avatarId,
                "badgeData.badges": {
                    "$elemMatch": {"badgeId": badgeId, "status": STATUS_ACTIVE}
                },
            },
            {"$addToSet": {"badgeData.badges.$.zones": zoneId}},
            projection={"badgeData.badges.$": 1},
            return_document=ReturnDocument.BEFORE,
        )

        if fairy is None:
            # Badge already earned, or not tracked for this fairy.
            return

        visitedBefore = set(fairy["badgeData"]["badges"][0].get("zones") or [])

        if zoneId in visitedBefore:
            # A meadow already visited -- nothing changed, so say nothing.
            return

        progress = len(visitedBefore) + 1
        self.sendUpdateToAvatarId(avatarId, "progressUpdate", [badgeId, 1])

        if progress >= goal:
            self._awardBadge(avatarId, badgeId, goal)
            return

        # Keep the numeric progress mirror in step with the visited set, so the
        # badge book shows the right count when avatarOnline reads it next login.
        self.air.mongoInterface.mongodb.fairies.update_one(
            {
                "_id": avatarId,
                "badgeData.badges": {
                    "$elemMatch": {"badgeId": badgeId, "status": STATUS_ACTIVE}
                },
            },
            {"$set": {"badgeData.badges.$.progress": progress}},
        )

    def _awardBadge(self, avatarId: int, badgeId: int, goal: int) -> None:
        dateEarned = datetime.now()

        # Clamping progress to the goal keeps an overshoot (collecting 60 twigs
        # in one go against a goal of 50) from being stored as 60 of 50.
        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {
                "_id": avatarId,
                "badgeData.badges": {
                    "$elemMatch": {"badgeId": badgeId, "status": STATUS_ACTIVE}
                },
            },
            {
                "$set": {
                    "badgeData.badges.$.status": STATUS_EARNED,
                    "badgeData.badges.$.dateEarned": dateEarned,
                    "badgeData.badges.$.progress": goal,
                }
            },
        )

        if result.modified_count == 0:
            # Someone else got there first; they will send badgeAcquired.
            return

        self.sendUpdateToAvatarId(
            avatarId, "badgeAcquired", [[badgeId, self._formatDateEarned(dateEarned)]]
        )

        # Completing either donation ladder's top tier may complete the combined
        # Royal honor. Only the two Flitterific tiers can, so nothing else pays
        # the read.
        if badgeId in badge_events.DONATION_TOP_TIERS:
            self._maybeAwardRoyalDonation(avatarId)

    def _maybeAwardRoyalDonation(self, avatarId: int) -> None:
        """
        Grant the Royal Wardrobe and Storage Donation honor once both the
        Flitterific Wardrobe and Flitterific Storage tiers are earned.

        The honor has no goal of its own (goal 0), so it is not accumulated --
        it is handed over outright the moment both prerequisites are met.
        _awardBadge only touches a tracked ACTIVE row, so a fairy who already
        has it no-ops here.
        """
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": avatarId}, {"badgeData.badges": 1}
        )

        if fairy is None:
            return

        earned = {
            row["badgeId"]
            for row in fairy["badgeData"]["badges"]
            if row.get("status") == STATUS_EARNED
        }

        if all(tier in earned for tier in badge_events.DONATION_TOP_TIERS):
            self._awardBadge(avatarId, badge_events.ROYAL_DONATION_BADGE, 0)

    def _ensureTrackedBadges(self, avatarId: int):
        """
        Make sure this fairy has a row for every badge in a tracked chapter or
        in INCLUDED_BADGES, and can see the pages they live on, then return
        (rows, unlockedPages) as they now stand.

        The client will not render progress for a badge it has not been told
        about, so the rows have to exist before anything can accumulate. A fairy
        who last logged in before a chapter was tracked, or before a badge was
        added to INCLUDED_BADGES, picks up its row here.

        Every fairy gets every tracked row regardless of membership -- see
        TRACKED_CHAPTER_IDS. Nothing is ever taken away either, so a lapsed
        member keeps their pages and whatever they earned; their Member badges
        just stop accumulating, which _addProgress handles.
        """
        fairies = self.air.mongoInterface.retrieveDocs("fairies", avatarId, "_id")

        if not fairies:
            self.notify.warning(f"avatarOnline: no fairy document for avId={avatarId}")
            return None, None

        badgeData = fairies[0].get("badgeData") or {}
        rows = badgeData.get("badges") or []
        unlockedPages = list(badgeData.get("unlockedPages") or [])

        tracked = {row["badgeId"] for row in rows}
        newRows = [
            self._newRow(badgeId, STATUS_ACTIVE)
            for badgeId in TRACKED_BADGE_IDS
            if badgeId not in tracked
        ]

        for badgeId, status in INCLUDED_BADGES.items():
            if badgeId not in tracked:
                newRows.append(
                    self._newRow(
                        badgeId,
                        status,
                        dateEarned=datetime.now() if status == STATUS_EARNED else None,
                    )
                )

        newPages = [
            pageId
            for pageId in (*TRACKED_PAGE_IDS, *INCLUDED_PAGE_IDS)
            if pageId not in unlockedPages
        ]

        update = {}

        if newRows:
            update["$push"] = {"badgeData.badges": {"$each": newRows}}

        if newPages:
            update["$addToSet"] = {"badgeData.unlockedPages": {"$each": newPages}}

        if update:
            self.air.mongoInterface.mongodb.fairies.update_one({"_id": avatarId}, update)

        return rows + newRows, unlockedPages + newPages

    def _newRow(self, badgeId: int, status: str, dateEarned=None) -> dict:
        return {
            "badgeId": badgeId,
            "status": status,
            "progress": 0,
            "dateEarned": dateEarned,
        }

    def _formatDateEarned(self, dateEarned) -> str:
        # The badge panel substitutes this straight into "Earned on #DATE#"
        # without parsing it, so the format is ours to choose.
        if not dateEarned:
            return ""

        return f"{dateEarned.strftime('%B')} {dateEarned.day}, {dateEarned.year}"
