from __future__ import annotations

from game.fairies.badges.BadgeProgressService import apply_meadow_explorer_progress
from game.fairies.badges.MeadowExplorerBadgeRegistry import ALL_EXPLORER_ZONE_IDS

_VISITED_MEADOWS_FIELDS = {
    "_id": 1,
    "visitedMeadows": 1,
}


def load_visited_meadows(air, av_id: int) -> set[int]:
    doc = (
        air.mongoInterface.mongodb.fairies.find_one(
            {"_id": av_id},
            _VISITED_MEADOWS_FIELDS,
        )
        or {"_id": av_id}
    )
    return {int(zone_id) for zone_id in (doc.get("visitedMeadows") or [])}


def persist_visited_meadows(air, av_id: int, visited: set[int]) -> None:
    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {"$set": {"visitedMeadows": sorted(visited)}},
        upsert=True,
    )


def apply_meadow_visit(badge_manager, av_id: int, zone_id: int) -> None:
    if zone_id not in ALL_EXPLORER_ZONE_IDS:
        return

    air = badge_manager.air
    visited = load_visited_meadows(air, av_id)
    if zone_id in visited:
        return

    apply_meadow_explorer_progress(badge_manager, av_id, zone_id)
