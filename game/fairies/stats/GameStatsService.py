from __future__ import annotations

from typing import TYPE_CHECKING

from game.fairies.badges.BadgeProgressService import (
    apply_daily_spin_play,
    apply_daily_spin_rock_win,
    apply_game_play,
    apply_high_score_badge,
    load_fairy_doc,
)
from game.fairies.badges.GameBadgeRegistry import (
    PLAY_COUNT_GAME_IDS,
)

if TYPE_CHECKING:
    from game.fairies.daily.DailyChanceData import DailyChancePrize

RIVER_ROCK_ITEM_ID = 7665

_GAME_STATS_FIELDS = {
    "_id": 1,
    "gameStats": 1,
    "dailySpinStats": 1,
}


def _default_daily_spin_stats() -> dict:
    return {"spins": 0, "rockWins": 0}


def _game_stats_map(doc: dict) -> dict[str, dict]:
    raw = doc.get("gameStats") or {}
    stats: dict[str, dict] = {}
    for key, value in raw.items():
        game_key = str(key)
        stats[game_key] = {
            "timesPlayed": int(value.get("timesPlayed") or 0),
            "bestScore": int(value.get("bestScore") or 0),
        }
    return stats


def _daily_spin_stats(doc: dict) -> dict:
    raw = doc.get("dailySpinStats") or {}
    return {
        "spins": int(raw.get("spins") or 0),
        "rockWins": int(raw.get("rockWins") or 0),
    }


def load_game_stats_doc(air, av_id: int) -> dict:
    return (
        air.mongoInterface.mongodb.fairies.find_one(
            {"_id": av_id},
            _GAME_STATS_FIELDS,
        )
        or {"_id": av_id}
    )


def persist_game_stats(air, av_id: int, doc: dict) -> None:
    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {
            "$set": {
                "gameStats": doc.get("gameStats") or {},
                "dailySpinStats": doc.get("dailySpinStats") or _default_daily_spin_stats(),
            }
        },
        upsert=True,
    )


def sync_game_stats_to_client(inventory_manager, av_id: int, doc: dict | None = None) -> None:
    if doc is None:
        doc = load_game_stats_doc(inventory_manager.air, av_id)

    for game_key, entry in _game_stats_map(doc).items():
        inventory_manager.sendUpdateToAvatarId(
            av_id,
            "putToGameStats",
            [int(game_key), entry["timesPlayed"], entry["bestScore"]],
        )


def apply_minigame_result(
    badge_manager,
    inventory_manager,
    av_id: int,
    game_id: int,
    score: int,
) -> None:
    if game_id not in PLAY_COUNT_GAME_IDS:
        return

    air = badge_manager.air
    doc = load_game_stats_doc(air, av_id)
    stats = _game_stats_map(doc)
    game_key = str(game_id)
    entry = stats.setdefault(game_key, {"timesPlayed": 0, "bestScore": 0})
    entry["timesPlayed"] += 1
    entry["bestScore"] = max(entry["bestScore"], int(score))
    doc["gameStats"] = stats
    persist_game_stats(air, av_id, doc)

    apply_game_play(badge_manager, av_id, game_id)
    apply_high_score_badge(badge_manager, av_id, game_id, entry["bestScore"])

    inventory_manager.sendUpdateToAvatarId(
        av_id,
        "putToGameStats",
        [game_id, entry["timesPlayed"], entry["bestScore"]],
    )

    from leaderboard.leaderboard_service import record_seasonal_score, record_weekly_score

    record_weekly_score(air, av_id, game_id, score)
    record_seasonal_score(air, av_id, game_id, score)


def apply_daily_spin(
    badge_manager,
    inventory_manager,
    av_id: int,
    granted_prizes: list | None = None,
) -> None:
    air = badge_manager.air
    doc = load_game_stats_doc(air, av_id)
    spin_stats = _daily_spin_stats(doc)
    spin_stats["spins"] += 1
    doc["dailySpinStats"] = spin_stats
    persist_game_stats(air, av_id, doc)

    apply_daily_spin_play(badge_manager, av_id)

    for prize in granted_prizes or []:
        if prize.item_id == RIVER_ROCK_ITEM_ID:
            doc = load_game_stats_doc(air, av_id)
            spin_stats = _daily_spin_stats(doc)
            spin_stats["rockWins"] += 1
            doc["dailySpinStats"] = spin_stats
            persist_game_stats(air, av_id, doc)
            apply_daily_spin_rock_win(badge_manager, av_id)


def get_earned_badge_ids_from_doc(air, av_id: int) -> set[int]:
    doc = load_fairy_doc(air, av_id)
    return {int(entry["badgeId"]) for entry in (doc.get("earnedBadges") or [])}
