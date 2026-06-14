"""Starter badge category (chapter 1, pages 12051–12052)."""

from game.fairies.badges.CraftBadgeRegistry import (
    CRAFT_HELPER_BADGES,
    CRAFT_PROFESSION_BAKING,
    CRAFT_PROFESSION_TAILORING,
    CRAFT_PROFESSION_TINKERING,
    CRAFT_STYLE_PERSONAL,
    CRAFT_STYLE_PRACTICE,
    CRAFT_TRACK_BAKING,
    CRAFT_TRACK_KEYS,
    CRAFT_TRACK_TAILORING,
    CRAFT_TRACK_TINKERING,
)

STARTER_PAGE_IDS = [12051, 12052]

# Tier-1 starter badges already driven by game / ingredient registries.
STARTER_PLAY_BADGE_IDS = frozenset({10576, 10584, 10592, 10740, 10785})
STARTER_COLLECTION_BADGE_IDS = frozenset({10658, 10662, 10666, 10674, 10686})

# Party Guest — bootstrap only until party minigame hooks exist.
PARTY_GUEST_BADGE_ID = 10727

ALL_STARTER_ONLY_BADGE_IDS = frozenset(
    {PARTY_GUEST_BADGE_ID}
    | {entry["badge_id"] for entry in CRAFT_HELPER_BADGES.values()}
)
