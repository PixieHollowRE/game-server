"""
Pixie Hollow badge <-> page/chapter lookup.

Badges Data model - so I don't forget lol
----------
- A "chapter" is a tab/category in the badge book (e.g. "Talent Games",
  "Winter 2012 Challenges") with a name + description.
- A "page" is one screen within a chapter (chapters can span multiple pages,
  ordered by `order`), and holds a list of badge ids.
- A "badge" has a name and a velvetRope flag (True = Member-only,
  False = free, None = not specified in source data).

You can regenerate this file's data by re-running the parser against
badges.json (from the badge definitions XML) and badgePages.xml
(from the badge page/chapter XML) if the source data changes.
"""

import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent


def _load(filename: str):
    with open(_DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)


BADGES = _load("badges.json")                       # list of {id, name, velvetRope}
BADGES_BY_ID = {b["id"]: b for b in BADGES}

PAGES = _load("badge_pages.json")                   # {page_id(str): {...}}
PAGES = {int(k): v for k, v in PAGES.items()}

BADGE_TO_PAGE = _load("badge_to_page.json")         # {badge_id(str): page_id}
BADGE_TO_PAGE = {int(k): v for k, v in BADGE_TO_PAGE.items()}


def get_badge(badge_id: int) -> dict | None:
    """Return {id, name, velvetRope} for a badge id, or None if unknown."""
    return BADGES_BY_ID.get(badge_id)


def get_page_for_badge(badge_id: int) -> dict | None:
    """
    Return the page a badge lives on, with chapter context, e.g.:
    {id, name, chapter_id, chapter_name, chapter_desc, order, badge_ids}
    Returns None if the badge isn't placed on any page (e.g. placeholder badges).
    """
    page_id = BADGE_TO_PAGE.get(badge_id)
    if page_id is None:
        return None
    return PAGES[page_id]


def get_badges_for_page(page_id: int) -> list[dict]:
    """Return the full badge dicts (id, name, velvetRope) for a given page id."""
    page = PAGES.get(page_id)
    if page is None:
        return []
    return [BADGES_BY_ID[bid] for bid in page["badge_ids"] if bid in BADGES_BY_ID]


def get_pages_for_chapter(chapter_id: int) -> list[dict]:
    """Return all pages belonging to a chapter, sorted by their order."""
    pages = [p for p in PAGES.values() if p["chapter_id"] == chapter_id]
    return sorted(pages, key=lambda p: p["order"])


def get_badges_for_chapter(chapter_id: int) -> list[dict]:
    """Return all badges (across all pages) belonging to a chapter."""
    badges = []
    for page in get_pages_for_chapter(chapter_id):
        badges.extend(get_badges_for_page(page["id"]))
    return badges
