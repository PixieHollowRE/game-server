"""Honors / tenure badges (page 12000)."""

from datetime import date

HONOR_PAGE_ID = 12000

FOUNDING_FAIRY_BADGE_ID = 10573
NEW_FAIRY_BADGE_ID = 10574
FOUNDING_FAIRY_CUTOFF = date(2026, 8, 31)

YEAR_BADGES = [
    {"years": 1, "badge_id": 10575},
    {"years": 2, "badge_id": 10615},
    {"years": 3, "badge_id": 10795},
    {"years": 4, "badge_id": 10796},
    {"years": 5, "badge_id": 10797},
    {"years": 6, "badge_id": 11217},
]

ALL_HONOR_BADGE_IDS = frozenset(
    {FOUNDING_FAIRY_BADGE_ID, NEW_FAIRY_BADGE_ID}
    | {entry["badge_id"] for entry in YEAR_BADGES}
)

HONOR_BADGE_PAGE_BY_ID = {badge_id: HONOR_PAGE_ID for badge_id in ALL_HONOR_BADGE_IDS}
