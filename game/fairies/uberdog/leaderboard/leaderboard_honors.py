"""Grant weekly game-champion honors badges on Sunday rollover."""

from __future__ import annotations

import logging

from game.fairies.badges.BadgeProgressService import grant_great_games_honors_badge
from game.fairies.uberdog.leaderboard.leaderboard_registry import (
    LEADERBOARD_DATA_COLLECTION,
    LEADERBOARD_WEEKLY,
    SUPPORTED_GAME_IDS,
    WEEKLY_LEADERBOARD_REWARDS_ENABLED,
    leaderboard_doc_id,
)

logger = logging.getLogger(__name__)


def grant_weekly_game_champion_badges(air, closing_week_id: str) -> list[int]:
    """Grant badge 10869 to each supported game's #1 weekly finisher for closing_week_id."""
    if not WEEKLY_LEADERBOARD_REWARDS_ENABLED:
        return []

    badge_manager = getattr(air, "badgeManager", None)
    if badge_manager is None:
        logger.warning(
            "grant_weekly_game_champion_badges skipped: no badgeManager on air"
        )
        return []

    granted: list[int] = []
    seen: set[int] = set()
    collection = air.mongoInterface.mongodb[LEADERBOARD_DATA_COLLECTION]

    for game_id in sorted(SUPPORTED_GAME_IDS):
        doc_id = leaderboard_doc_id(LEADERBOARD_WEEKLY, game_id, closing_week_id)
        doc = collection.find_one({"_id": doc_id}) or {}
        entries = doc.get("entries") or []
        if not entries:
            continue

        av_id = int(entries[0]["avId"])
        if av_id in seen:
            continue
        if grant_great_games_honors_badge(badge_manager, av_id):
            seen.add(av_id)
            granted.append(av_id)
            logger.info(
                "Great Games Honors granted avId=%s gameId=%s weekId=%s",
                av_id,
                game_id,
                closing_week_id,
            )

    return granted
