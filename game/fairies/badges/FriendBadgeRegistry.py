"""Chapter 2 friendship tier badges (page 12001)."""

FRIEND_PAGE_ID = 12001
FRIEND_ACCEPT_EVENT_ID = 25003

FRIEND_BADGE_TRACK = {
    "tiers": [
        {"badge_id": 10531, "threshold": 1},
        {"badge_id": 10532, "threshold": 5},
        {"badge_id": 10533, "threshold": 25},
    ],
}

ALL_FRIEND_BADGE_IDS = frozenset(
    tier["badge_id"] for tier in FRIEND_BADGE_TRACK["tiers"]
)
