from __future__ import annotations

from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.badges.BadgeProgressService import apply_craft_progress
from game.fairies.badges.CraftBadgeRegistry import (
    CRAFT_HELPER_BADGES,
    CRAFT_PROFESSION_BAKING,
    CRAFT_STYLE_PERSONAL,
    CRAFT_STYLE_PRACTICE,
    CRAFT_TRACK_KEYS,
)

_CRAFT_STATS_FIELDS = {
    "_id": 1,
    "craftStats": 1,
    "personalCraftStats": 1,
}


def _default_craft_stats() -> dict[str, int]:
    return {track_key: 0 for track_key in CRAFT_TRACK_KEYS}


def _craft_stats_totals(doc: dict) -> dict[str, int]:
    totals = _default_craft_stats()
    raw = doc.get("craftStats") or {}
    for track_key in CRAFT_TRACK_KEYS:
        if track_key in raw:
            totals[track_key] = int(raw[track_key])
    return totals


def _personal_craft_stats_totals(doc: dict) -> dict[str, int]:
    totals = _default_craft_stats()
    raw = doc.get("personalCraftStats") or {}
    for track_key in CRAFT_TRACK_KEYS:
        if track_key in raw:
            totals[track_key] = int(raw[track_key])
    return totals


def load_craft_stats_doc(air, av_id: int) -> dict:
    return (
        air.mongoInterface.mongodb.fairies.find_one(
            {"_id": av_id},
            _CRAFT_STATS_FIELDS,
        )
        or {"_id": av_id}
    )


def persist_craft_stats(air, av_id: int, doc: dict) -> None:
    fields = {"craftStats": _craft_stats_totals(doc)}
    if "personalCraftStats" in doc:
        fields["personalCraftStats"] = _personal_craft_stats_totals(doc)
    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {"$set": fields},
        upsert=True,
    )


def _craft_counts_toward_badge(profession_id: int, recipe_id: int) -> bool:
    if profession_id not in CRAFT_HELPER_BADGES:
        return False

    if profession_id == CRAFT_PROFESSION_BAKING:
        baked = BAKED_ITEMS.get(recipe_id)
        return bool(baked and baked.get("bakedType") == "cookie")

    return recipe_id not in BAKED_ITEMS


def apply_craft_result(
    badge_manager,
    av_id: int,
    profession_id: int,
    recipe_id: int,
    crafting_style: int,
) -> None:
    if crafting_style not in (CRAFT_STYLE_PRACTICE, CRAFT_STYLE_PERSONAL):
        return
    if not _craft_counts_toward_badge(profession_id, recipe_id):
        return

    air = badge_manager.air
    doc = load_craft_stats_doc(air, av_id)
    track_key = CRAFT_HELPER_BADGES[profession_id]["track_key"]

    if crafting_style == CRAFT_STYLE_PRACTICE:
        totals = _craft_stats_totals(doc)
        totals[track_key] += 1
        doc["craftStats"] = totals
    else:
        totals = _personal_craft_stats_totals(doc)
        totals[track_key] += 1
        doc["personalCraftStats"] = totals

    persist_craft_stats(air, av_id, doc)
    apply_craft_progress(badge_manager, av_id, profession_id, crafting_style)
