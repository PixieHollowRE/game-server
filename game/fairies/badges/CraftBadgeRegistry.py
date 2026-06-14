"""Craft profession tier badges (practice + personal, pages 12040–12050)."""

CRAFT_PROFESSION_TAILORING = 0
CRAFT_PROFESSION_BAKING = 1
CRAFT_PROFESSION_TINKERING = 2

CRAFT_TRACK_BAKING = "baking"
CRAFT_TRACK_TINKERING = "tinkering"
CRAFT_TRACK_TAILORING = "tailoring"

CRAFT_TRACK_KEYS = (CRAFT_TRACK_BAKING, CRAFT_TRACK_TINKERING, CRAFT_TRACK_TAILORING)

CRAFT_STYLE_PERSONAL = 1
CRAFT_STYLE_PRACTICE = 2

CRAFT_CHAPTER_PAGE_IDS = [12040, 12041, 12050]

CRAFT_BAKING_PAGE_ID = 12040
CRAFT_TINKERING_PAGE_ID = 12041
CRAFT_TAILORING_PAGE_ID = 12050

STARTER_CRAFT_PAGE_ID = 12051

_CRAFT_THRESHOLDS = (5, 25, 100, 500)

CRAFT_PRACTICE_TRACKS = {
    CRAFT_PROFESSION_BAKING: {
        "track_key": CRAFT_TRACK_BAKING,
        "tiers": [
            {"badge_id": 10772, "threshold": 5},
            {"badge_id": 10773, "threshold": 25},
            {"badge_id": 10774, "threshold": 100},
            {"badge_id": 10804, "threshold": 500},
        ],
    },
    CRAFT_PROFESSION_TINKERING: {
        "track_key": CRAFT_TRACK_TINKERING,
        "tiers": [
            {"badge_id": 10798, "threshold": 5},
            {"badge_id": 10799, "threshold": 25},
            {"badge_id": 10800, "threshold": 100},
            {"badge_id": 11136, "threshold": 500},
        ],
    },
    CRAFT_PROFESSION_TAILORING: {
        "track_key": CRAFT_TRACK_TAILORING,
        "tiers": [
            {"badge_id": 10883, "threshold": 5},
            {"badge_id": 10884, "threshold": 25},
            {"badge_id": 10885, "threshold": 100},
            {"badge_id": 10894, "threshold": 500},
        ],
    },
}

CRAFT_PERSONAL_TRACKS = {
    CRAFT_PROFESSION_BAKING: {
        "track_key": CRAFT_TRACK_BAKING,
        "tiers": [
            {"badge_id": 10775, "threshold": 5},
            {"badge_id": 10776, "threshold": 25},
            {"badge_id": 10777, "threshold": 100},
            {"badge_id": 10805, "threshold": 500},
        ],
    },
    CRAFT_PROFESSION_TINKERING: {
        "track_key": CRAFT_TRACK_TINKERING,
        "tiers": [
            {"badge_id": 10801, "threshold": 5},
            {"badge_id": 10802, "threshold": 25},
            {"badge_id": 10803, "threshold": 100},
            {"badge_id": 11129, "threshold": 500},
        ],
    },
    CRAFT_PROFESSION_TAILORING: {
        "track_key": CRAFT_TRACK_TAILORING,
        "tiers": [
            {"badge_id": 10886, "threshold": 5},
            {"badge_id": 10887, "threshold": 25},
            {"badge_id": 10888, "threshold": 100},
            {"badge_id": 10895, "threshold": 500},
        ],
    },
}

CRAFT_HELPER_BADGES = {
    profession_id: {
        "badge_id": track["tiers"][0]["badge_id"],
        "goal": track["tiers"][0]["threshold"],
        "track_key": track["track_key"],
    }
    for profession_id, track in CRAFT_PRACTICE_TRACKS.items()
}

ALL_CRAFT_BADGE_IDS = frozenset(
    tier["badge_id"]
    for track in list(CRAFT_PRACTICE_TRACKS.values()) + list(CRAFT_PERSONAL_TRACKS.values())
    for tier in track["tiers"]
)

CRAFT_BADGE_PAGE_BY_ID = {
    10772: STARTER_CRAFT_PAGE_ID,
    10798: STARTER_CRAFT_PAGE_ID,
    10883: STARTER_CRAFT_PAGE_ID,
    10773: CRAFT_BAKING_PAGE_ID,
    10774: CRAFT_BAKING_PAGE_ID,
    10804: CRAFT_BAKING_PAGE_ID,
    10775: CRAFT_BAKING_PAGE_ID,
    10776: CRAFT_BAKING_PAGE_ID,
    10777: CRAFT_BAKING_PAGE_ID,
    10805: CRAFT_BAKING_PAGE_ID,
    10799: CRAFT_TINKERING_PAGE_ID,
    10800: CRAFT_TINKERING_PAGE_ID,
    11136: CRAFT_TINKERING_PAGE_ID,
    10801: CRAFT_TINKERING_PAGE_ID,
    10802: CRAFT_TINKERING_PAGE_ID,
    10803: CRAFT_TINKERING_PAGE_ID,
    11129: CRAFT_TINKERING_PAGE_ID,
    10884: CRAFT_TAILORING_PAGE_ID,
    10885: CRAFT_TAILORING_PAGE_ID,
    10894: CRAFT_TAILORING_PAGE_ID,
    10886: CRAFT_TAILORING_PAGE_ID,
    10887: CRAFT_TAILORING_PAGE_ID,
    10888: CRAFT_TAILORING_PAGE_ID,
    10895: CRAFT_TAILORING_PAGE_ID,
}
