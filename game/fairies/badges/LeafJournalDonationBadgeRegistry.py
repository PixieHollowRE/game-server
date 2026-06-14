"""Wardrobe and storage donation badges (Leaf Journal, chapter 21)."""

LEAF_JOURNAL_DONATION_PAGE_ID = 12044

WARDROBE = "wardrobe"
STORAGE = "storage"

DONATION_TRACKS = {
    WARDROBE: {
        "tiers": [
            {"badge_id": 10811, "threshold": 5},
            {"badge_id": 10812, "threshold": 25},
            {"badge_id": 10813, "threshold": 100},
        ],
    },
    STORAGE: {
        "tiers": [
            {"badge_id": 10814, "threshold": 5},
            {"badge_id": 10815, "threshold": 25},
            {"badge_id": 10816, "threshold": 100},
        ],
    },
}

ALL_LEAF_JOURNAL_DONATION_BADGE_IDS = frozenset(
    tier["badge_id"]
    for entry in DONATION_TRACKS.values()
    for tier in entry["tiers"]
)
