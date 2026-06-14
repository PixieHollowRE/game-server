"""Validate wardrobe/storage login sync helpers (hotfix regression guard)."""

from __future__ import annotations

import sys
from pathlib import Path

GAME_SERVER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(GAME_SERVER))

from game.fairies.badges.BadgeProgressService import (  # noqa: E402
    build_login_payload,
    ensure_badges_bootstrapped,
)


def _item_inv_ext(item: dict) -> list:
    return [
        int(item.get("inv_id") or 0),
        int(item.get("item_id") or 0),
        int(item.get("slot") or 0),
        int(item.get("createdById") or 0),
        str(item.get("createdByName") or ""),
        int(item.get("giftedById") or 0),
        str(item.get("giftedByName") or ""),
        int(item.get("quality") or 0),
        int(item.get("color1") or 0),
        int(item.get("color2") or 0),
        int(item.get("howAcquired") or 0),
    ]


def test_corrupt_badge_rows_skipped() -> None:
    doc = {
        "_id": 1,
        "earnedBadges": [{"badgeId": 10530, "dateEarned": "01/01/2026"}, {"oops": 1}],
        "badgeProgress": [{"badgeId": 10576, "progress": 3}, {"progress": 5}],
        "unlockedPages": [12005],
    }
    earned, pages, progress = build_login_payload(doc)
    assert earned == [[10530, "01/01/2026"]]
    assert pages == [12005]
    assert progress == [[10576, 3]]


def test_item_inv_ext_defaults() -> None:
    ext = _item_inv_ext({"inv_id": 99, "item_id": 75, "color1": 1})
    assert ext[0] == 99
    assert ext[1] == 75
    assert ext[2] == 0  # slot default
    assert ext[10] == 0  # howAcquired default


def test_bootstrap_build_login_payload() -> None:
    doc, _ = ensure_badges_bootstrapped({"_id": 1})
    earned, pages, progress = build_login_payload(doc)
    assert len(earned) >= 1
    assert len(pages) >= 1
    assert len(progress) >= 200


def main() -> None:
    test_corrupt_badge_rows_skipped()
    test_item_inv_ext_defaults()
    test_bootstrap_build_login_payload()
    print("All inventory login sync validation checks passed.")


if __name__ == "__main__":
    main()
