"""Repair corrupt badge rows and normalize missing inventory item fields."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from pymongo import MongoClient

GAME_SERVER = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(GAME_SERVER))

VALID_LOCATIONS = frozenset({"Equipped", "Wardrobe", "Storage"})
HOME_ITEM_TYPES = frozenset({"Furniture", "Lamp", "Decoration"})


def _default_location(item: dict) -> str:
    item_type = str(item.get("type") or "")
    if item_type in HOME_ITEM_TYPES:
        return "Storage"
    return "Wardrobe"


def _clean_badge_rows(rows: list | None) -> tuple[list, int]:
    cleaned: list = []
    removed = 0
    for entry in rows or []:
        if isinstance(entry, dict) and "badgeId" in entry:
            cleaned.append(entry)
        else:
            removed += 1
    return cleaned, removed


def repair_fairy(fairy: dict, dry_run: bool) -> dict:
    update: dict = {}
    item_changes = 0
    avatar = fairy.get("avatar") or {}
    items = avatar.get("items")
    if isinstance(items, list):
        new_items = []
        for item in items:
            if not isinstance(item, dict):
                item_changes += 1
                continue
            row = dict(item)
            if row.get("location") not in VALID_LOCATIONS:
                row["location"] = _default_location(row)
                item_changes += 1
            for field, default in (
                ("slot", 0),
                ("createdById", 0),
                ("createdByName", ""),
                ("giftedById", 0),
                ("giftedByName", ""),
                ("quality", 0),
                ("color1", 0),
                ("color2", 0),
                ("howAcquired", 0),
            ):
                if field not in row:
                    row[field] = default
                    item_changes += 1
            new_items.append(row)
        if item_changes:
            update["avatar.items"] = new_items

    earned, earned_removed = _clean_badge_rows(fairy.get("earnedBadges"))
    if earned_removed:
        update["earnedBadges"] = earned

    progress, progress_removed = _clean_badge_rows(fairy.get("badgeProgress"))
    if progress_removed:
        update["badgeProgress"] = progress

    if update and not dry_run:
        pass  # write happens in main()

    return {
        "item_changes": item_changes,
        "earned_removed": earned_removed,
        "progress_removed": progress_removed,
        "update": update,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mongo-uri", default="mongodb://127.0.0.1:27017")
    parser.add_argument("--name", help="Repair one fairy by name (exact, case-insensitive)")
    parser.add_argument("--av-id", type=int, help="Repair one fairy by _id")
    parser.add_argument("--all", action="store_true", help="Repair every fairy document")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing")
    args = parser.parse_args()

    if not args.all and args.name is None and args.av_id is None:
        parser.error("Specify --all, --name, or --av-id")

    db = MongoClient(args.mongo_uri)["PixieHollow"]
    query: dict = {}
    if args.av_id is not None:
        query["_id"] = args.av_id
    elif args.name:
        query["name"] = {"$regex": f"^{re.escape(args.name)}$", "$options": "i"}
    elif not args.all:
        parser.error("Specify --all, --name, or --av-id")

    fairies = list(db.fairies.find(query))
    if not fairies:
        print("No fairies matched.")
        return 1

    repaired = 0
    for fairy in fairies:
        result = repair_fairy(fairy, args.dry_run)
        if not result["update"]:
            continue
        repaired += 1
        label = f"{fairy.get('name')} ({fairy['_id']})"
        print(
            f"{args.dry_run and 'would repair' or 'repairing'} {label}: "
            f"item_field_fixes={result['item_changes']} "
            f"earned_removed={result['earned_removed']} "
            f"progress_removed={result['progress_removed']}"
        )
        if not args.dry_run:
            db.fairies.update_one({"_id": fairy["_id"]}, {"$set": result["update"]})

    print(f"matched={len(fairies)} repaired={repaired}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
