"""Seasonal meadow explorer badges (chapter 3, Meadows page)."""

from game.fairies.ai import ZoneConstants as zc

MEADOW_EXPLORER_PAGE_ID = 12002

SPRING_MEADOWS = (
    zc.CHERRYBLOSSOM_HEIGHTS,
    zc.SPRINGTIME_ORCHARD,
    zc.DEWDROP_VALE,
    zc.NEVERBERRY_THICKET,
    zc.TREETOP_BEND,
)

AUTUMN_MEADOWS = (
    zc.ACORN_SUMMIT,
    zc.COTTONPUFF_FIELD,
    zc.MAPLE_TREE_HILL,
    zc.PUMPKIN_PATCH,
)

WINTER_MEADOWS = (
    zc.EVERGREEN_OVERLOOK,
    zc.SNOWCAP_GLADE,
    zc.CHILLY_FALLS,
)

SUMMER_MEADOWS = (
    zc.PALM_TREE_COVE,
    zc.SUNFLOWER_GULLY,
    zc.NEVERFRUIT_GROVE,
)

EXPLORER_TRACKS = {
    "spring": {
        "badge_id": 10534,
        "zones": SPRING_MEADOWS,
        "goal": len(SPRING_MEADOWS),
    },
    "autumn": {
        "badge_id": 10554,
        "zones": AUTUMN_MEADOWS,
        "goal": len(AUTUMN_MEADOWS),
    },
    "winter": {
        "badge_id": 10604,
        "zones": WINTER_MEADOWS,
        "goal": len(WINTER_MEADOWS),
    },
    "summer": {
        "badge_id": 10694,
        "zones": SUMMER_MEADOWS,
        "goal": len(SUMMER_MEADOWS),
    },
}

ZONE_TO_TRACK: dict[int, str] = {
    zone_id: track_key
    for track_key, entry in EXPLORER_TRACKS.items()
    for zone_id in entry["zones"]
}

ALL_EXPLORER_BADGE_IDS = frozenset(
    entry["badge_id"] for entry in EXPLORER_TRACKS.values()
)

ALL_EXPLORER_ZONE_IDS = frozenset(ZONE_TO_TRACK)
