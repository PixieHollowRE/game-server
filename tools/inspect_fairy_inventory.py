"""Inspect fairy wardrobe/storage/pouch health and badge row integrity."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pymongo import MongoClient

GAME_SERVER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(GAME_SERVER))

REQUIRED_ITEM_FIELDS = (
    "inv_id",
    "item_id",
    "slot",
    "color1",
    "color2",
    "howAcquired",
    "location",
)


def inspect_fairy(fairy: dict) -> dict:
    av_id = fairy["_id"]
    name = fairy.get("name") or ""
    avatar = fairy.get("avatar") or {}
    items = avatar.get("items")
    pouch = fairy.get("pouch")

    issues: list[str] = []
    location_counts: dict[str, int] = {}
    missing_fields: list[str] = []
    bad_locations: list[tuple[int, str | None]] = []

    if not avatar:
        issues.append("missing avatar subdocument")
        items = []
    elif not isinstance(items, list):
        issues.append("avatar.items is not a list")
        items = []

    wardrobe_sync = 0
    storage_sync = 0
    for item in items:
        if not isinstance(item, dict):
            issues.append("non-dict item row in avatar.items")
            continue
        loc = item.get("location")
        location_counts[str(loc)] = location_counts.get(str(loc), 0) + 1
        if loc in ("Wardrobe", "Equipped"):
            wardrobe_sync += 1
        elif loc == "Storage":
            storage_sync += 1
        elif loc is None:
            bad_locations.append((int(item.get("inv_id") or 0), None))
        else:
            bad_locations.append((int(item.get("inv_id") or 0), str(loc)))
        for field in REQUIRED_ITEM_FIELDS:
            if field not in item:
                missing_fields.append(f"inv_id={item.get('inv_id')} missing {field}")

    for entry in fairy.get("earnedBadges") or []:
        if not isinstance(entry, dict) or "badgeId" not in entry:
            issues.append(f"corrupt earnedBadges row: {entry!r}")

    for entry in fairy.get("badgeProgress") or []:
        if not isinstance(entry, dict) or "badgeId" not in entry:
            issues.append(f"corrupt badgeProgress row: {entry!r}")

    if pouch is not None and not isinstance(pouch, list):
        issues.append("pouch is not a list")

    return {
        "av_id": av_id,
        "name": name,
        "item_count": len(items),
        "wardrobe_sync_count": wardrobe_sync,
        "storage_sync_count": storage_sync,
        "pouch_count": len(pouch or []),
        "location_counts": location_counts,
        "bad_locations": bad_locations,
        "missing_fields": missing_fields,
        "issues": issues,
        "earned_badges": len(fairy.get("earnedBadges") or []),
        "badge_progress": len(fairy.get("badgeProgress") or []),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mongo-uri", default="mongodb://127.0.0.1:27017")
    parser.add_argument("--name", help="Filter by fairy name (exact, case-insensitive)")
    parser.add_argument("--av-id", type=int, help="Filter by fairy _id")
    parser.add_argument("--all", action="store_true", help="Inspect every fairy document")
    args = parser.parse_args()

    db = MongoClient(args.mongo_uri)["PixieHollow"]
    query: dict = {}
    if args.av_id is not None:
        query["_id"] = args.av_id
    elif args.name:
        query["name"] = {"$regex": f"^{args.name}$", "$options": "i"}

    fairies = list(db.fairies.find(query))
    if not fairies:
        print("No fairies matched.")
        return 1

    total_issues = 0
    for fairy in fairies:
        report = inspect_fairy(fairy)
        total_issues += len(report["issues"]) + len(report["bad_locations"]) + len(
            report["missing_fields"]
        )
        print(
            f"{report['name']} ({report['av_id']}): "
            f"items={report['item_count']} "
            f"sync wardrobe={report['wardrobe_sync_count']} storage={report['storage_sync_count']} "
            f"pouch={report['pouch_count']} "
            f"badges earned={report['earned_badges']} progress={report['badge_progress']}"
        )
        if report["location_counts"]:
            print(f"  locations: {report['location_counts']}")
        for issue in report["issues"]:
            print(f"  ISSUE: {issue}")
        for inv_id, loc in report["bad_locations"][:5]:
            print(f"  BAD LOCATION: inv_id={inv_id} location={loc!r}")
        for msg in report["missing_fields"][:5]:
            print(f"  MISSING FIELD: {msg}")

    print(f"inspected={len(fairies)} issue_rows={total_issues}")
    return 0 if total_issues == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
