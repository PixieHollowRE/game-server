from __future__ import annotations

import time
from datetime import date, datetime
from typing import Any

from game.fairies.badges.IngredientBadgeRegistry import (
    ALL_COLLECTION_BADGE_IDS,
    CHAPTER_10_PAGE_IDS,
    COLLECTION_BADGES,
    ITEM_IDS,
    PRETIER_TOTAL,
    ROYAL_CUMULATIVE_THRESHOLD,
    ROYAL_SEGMENT_GOAL,
)
from game.fairies.badges.GameBadgeRegistry import (
    ALL_GAME_BADGE_IDS,
    CHAPTER_7_PAGE_IDS,
    DAILY_SPIN_PLAY_TRACK,
    DAILY_SPIN_PRIZE_BADGE_IDS,
    DAILY_SPIN_ROCK_WIN_TRACK,
    HIGH_SCORE_BADGES,
    PLAY_COUNT_TRACKS,
)
from game.fairies.badges.LeafJournalDonationBadgeRegistry import (
    ALL_LEAF_JOURNAL_DONATION_BADGE_IDS,
    DONATION_TRACKS,
    LEAF_JOURNAL_DONATION_PAGE_ID,
    STORAGE,
    WARDROBE,
)
from game.fairies.badges.MeadowExplorerBadgeRegistry import (
    ALL_EXPLORER_BADGE_IDS,
    ALL_EXPLORER_ZONE_IDS,
    EXPLORER_TRACKS,
    MEADOW_EXPLORER_PAGE_ID,
    ZONE_TO_TRACK,
)
from game.fairies.badges.MoreOptions import resolve_favorite_badge
from game.fairies.badges.StarterBadgeRegistry import (
    ALL_STARTER_ONLY_BADGE_IDS,
    CRAFT_HELPER_BADGES,
    CRAFT_TRACK_KEYS,
    PARTY_GUEST_BADGE_ID,
    STARTER_PAGE_IDS,
)
from game.fairies.badges.CraftBadgeRegistry import (
    ALL_CRAFT_BADGE_IDS,
    CRAFT_CHAPTER_PAGE_IDS,
    CRAFT_PERSONAL_TRACKS,
    CRAFT_PRACTICE_TRACKS,
    CRAFT_STYLE_PERSONAL,
    CRAFT_STYLE_PRACTICE,
)
from game.fairies.badges.FriendBadgeRegistry import (
    ALL_FRIEND_BADGE_IDS,
    FRIEND_BADGE_TRACK,
    FRIEND_PAGE_ID,
)
from game.fairies.badges.HonorBadgeRegistry import (
    ALL_HONOR_BADGE_IDS,
    FOUNDING_FAIRY_BADGE_ID,
    FOUNDING_FAIRY_CUTOFF,
    HONOR_PAGE_ID,
    NEW_FAIRY_BADGE_ID,
    YEAR_BADGES,
)

# Backward-compatible aliases used elsewhere in the codebase.
FOUNDING_FAIRY_PAGE_ID = HONOR_PAGE_ID

_BADGE_DOC_FIELDS = {
    "_id": 1,
    "earnedBadges": 1,
    "badgeProgress": 1,
    "unlockedPages": 1,
    "ingredientCollectionTotals": 1,
    "leafJournalDonationTotals": 1,
    "badgeCount": 1,
    "newestBadge": 1,
    "gameStats": 1,
    "dailySpinStats": 1,
    "visitedMeadows": 1,
    "craftStats": 1,
    "personalCraftStats": 1,
    "friendsAccepted": 1,
    "friends": 1,
    "created": 1,
}

# BadgeProgress.progress and progressUpdate args are int16 in fairy.dc.
_WIRE_PROGRESS_MAX = 32767
_HIGH_SCORE_THRESHOLD_BY_BADGE_ID = {
    entry["badge_id"]: entry["threshold"] for entry in HIGH_SCORE_BADGES.values()
}


def wire_badge_progress(badge_id: int, progress: int) -> int:
    """Map stored badge progress to an int16-safe wire value."""
    progress = max(0, int(progress))
    threshold = _HIGH_SCORE_THRESHOLD_BY_BADGE_ID.get(badge_id)
    if threshold is not None and threshold > 0:
        scaled = int(progress * _WIRE_PROGRESS_MAX / threshold)
        return min(scaled, _WIRE_PROGRESS_MAX)
    return min(progress, _WIRE_PROGRESS_MAX)


def wire_badge_progress_delta(badge_id: int, previous: int, current: int) -> int:
    """Client progressUpdate is additive; send scaled delta for high-score badges."""
    wire_previous = wire_badge_progress(badge_id, previous)
    wire_current = wire_badge_progress(badge_id, current)
    return max(0, wire_current - wire_previous)


def _send_progress_update(badge_manager, av_id: int, badge_id: int, amount: int) -> None:
    wire_amount = min(max(int(amount), 0), _WIRE_PROGRESS_MAX)
    if wire_amount <= 0:
        return
    badge_manager.sendUpdateToAvatarId(av_id, "progressUpdate", [badge_id, wire_amount])


def _badge_earned_date() -> str:
    return time.strftime("%m/%d/%Y")


def _unlocked_page_ids(doc: dict) -> set[int]:
    return {int(page_id) for page_id in (doc.get("unlockedPages") or [])}


def _collection_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if not all(page_id in unlocked for page_id in CHAPTER_10_PAGE_IDS):
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_COLLECTION_BADGE_IDS)


def _leaf_journal_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if LEAF_JOURNAL_DONATION_PAGE_ID not in unlocked:
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_LEAF_JOURNAL_DONATION_BADGE_IDS)


def _game_badges_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if not all(page_id in unlocked for page_id in CHAPTER_7_PAGE_IDS):
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_GAME_BADGE_IDS)


def _meadow_explorer_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if MEADOW_EXPLORER_PAGE_ID not in unlocked:
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_EXPLORER_BADGE_IDS)


def _starter_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if not all(page_id in unlocked for page_id in STARTER_PAGE_IDS):
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_STARTER_ONLY_BADGE_IDS)


def _friend_badges_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if FRIEND_PAGE_ID not in unlocked:
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_FRIEND_BADGE_IDS)


def _craft_badges_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if not all(page_id in unlocked for page_id in CRAFT_CHAPTER_PAGE_IDS):
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_CRAFT_BADGE_IDS)


def _unique_friend_ids(doc: dict) -> list[int]:
    seen: set[int] = set()
    unique: list[int] = []
    for raw in doc.get("friends") or []:
        account_id = int(raw)
        if account_id in seen:
            continue
        seen.add(account_id)
        unique.append(account_id)
    return unique


def _friends_accepted_total(doc: dict) -> int:
    return len(_unique_friend_ids(doc))


def _badge_progress_map(doc: dict) -> dict[int, int]:
    progress: dict[int, int] = {}
    for entry in doc.get("badgeProgress") or []:
        if not isinstance(entry, dict) or "badgeId" not in entry:
            continue
        progress[int(entry["badgeId"])] = int(entry.get("progress") or 0)
    return progress


def _earned_badge_ids(doc: dict) -> set[int]:
    earned: set[int] = set()
    for entry in (doc.get("earnedBadges") or []):
        if not isinstance(entry, dict) or "badgeId" not in entry:
            continue
        earned.add(int(entry["badgeId"]))
    return earned


def _ingredient_totals(doc: dict) -> dict[int, int]:
    totals: dict[int, int] = {}
    raw = doc.get("ingredientCollectionTotals") or {}
    for key, value in raw.items():
        totals[int(key)] = int(value)
    return totals


def _collection_tier_progress(
    total: int,
    tier_index: int,
    entry: dict,
    earned_ids: set[int],
) -> int:
    if tier_index < 3:
        return total

    tier3_id = entry["tiers"][2]["badge_id"]
    if tier3_id not in earned_ids:
        return 0

    return max(0, min(total - PRETIER_TOTAL, ROYAL_SEGMENT_GOAL))


def _collection_tier_can_earn(
    total: int,
    tier_index: int,
    entry: dict,
    earned_ids: set[int],
) -> bool:
    if tier_index < 3:
        return total >= entry["tiers"][tier_index]["threshold"]

    tier3_id = entry["tiers"][2]["badge_id"]
    return tier3_id in earned_ids and total >= ROYAL_CUMULATIVE_THRESHOLD


def _sync_collection_item_badges(
    entry: dict,
    total: int,
    progress: dict[int, int],
    earned_ids: set[int],
) -> set[int]:
    newly_earned: set[int] = set()

    for tier_index, tier in enumerate(entry["tiers"]):
        badge_id = tier["badge_id"]
        progress[badge_id] = _collection_tier_progress(
            total,
            tier_index,
            entry,
            earned_ids,
        )

        if badge_id in earned_ids:
            continue

        if _collection_tier_can_earn(total, tier_index, entry, earned_ids):
            earned_ids.add(badge_id)
            newly_earned.add(badge_id)

    return newly_earned


def _leaf_journal_donation_totals(doc: dict) -> dict[str, int]:
    totals: dict[str, int] = {WARDROBE: 0, STORAGE: 0}
    raw = doc.get("leafJournalDonationTotals") or {}
    for key in (WARDROBE, STORAGE):
        if key in raw:
            totals[key] = int(raw[key])
    return totals


def _game_stats_totals(doc: dict) -> dict[int, int]:
    totals: dict[int, int] = {}
    raw = doc.get("gameStats") or {}
    for key, value in raw.items():
        totals[int(key)] = int(value.get("timesPlayed") or 0)
    return totals


def _game_best_scores(doc: dict) -> dict[int, int]:
    scores: dict[int, int] = {}
    raw = doc.get("gameStats") or {}
    for key, value in raw.items():
        scores[int(key)] = int(value.get("bestScore") or 0)
    return scores


def _daily_spin_stats(doc: dict) -> dict[str, int]:
    raw = doc.get("dailySpinStats") or {}
    return {
        "spins": int(raw.get("spins") or 0),
        "rockWins": int(raw.get("rockWins") or 0),
    }


def _visited_meadows(doc: dict) -> set[int]:
    return {int(zone_id) for zone_id in (doc.get("visitedMeadows") or [])}


def _season_visit_count(visited: set[int], track_key: str) -> int:
    zones = EXPLORER_TRACKS[track_key]["zones"]
    return len(visited.intersection(zones))


def _craft_stats_totals(doc: dict) -> dict[str, int]:
    totals = {track_key: 0 for track_key in CRAFT_TRACK_KEYS}
    raw = doc.get("craftStats") or {}
    for track_key in CRAFT_TRACK_KEYS:
        if track_key in raw:
            totals[track_key] = int(raw[track_key])
    return totals


def _personal_craft_stats_totals(doc: dict) -> dict[str, int]:
    totals = {track_key: 0 for track_key in CRAFT_TRACK_KEYS}
    raw = doc.get("personalCraftStats") or {}
    for track_key in CRAFT_TRACK_KEYS:
        if track_key in raw:
            totals[track_key] = int(raw[track_key])
    return totals


def _serialize_badge_progress(progress: dict[int, int]) -> list[dict[str, int]]:
    return [
        {"badgeId": badge_id, "progress": progress[badge_id]}
        for badge_id in sorted(progress)
    ]


def _serialize_earned_badges(
    earned_ids: set[int],
    doc: dict,
    *,
    newly_earned: set[int] | None = None,
) -> list[dict[str, Any]]:
    existing = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in (doc.get("earnedBadges") or [])
    }
    newly_earned = newly_earned or set()
    earned: list[dict[str, Any]] = []
    for badge_id in sorted(earned_ids):
        if badge_id in newly_earned:
            date_earned = _badge_earned_date()
        else:
            date_earned = existing.get(badge_id, "")
        earned.append({"badgeId": badge_id, "dateEarned": date_earned})
    return earned


def _honor_badges_is_bootstrapped(doc: dict) -> bool:
    unlocked = _unlocked_page_ids(doc)
    if HONOR_PAGE_ID not in unlocked:
        return False
    progress = _badge_progress_map(doc)
    return all(badge_id in progress for badge_id in ALL_HONOR_BADGE_IDS)


def _parse_fairy_created(doc: dict) -> date:
    raw = doc.get("created")
    if raw is None:
        return date.today()

    if isinstance(raw, datetime):
        return raw.date()
    if isinstance(raw, date):
        return raw
    if isinstance(raw, str):
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).date()

    return date.today()


def _completed_tenure_years(created: date, today: date) -> int:
    years = today.year - created.year
    if (today.month, today.day) < (created.month, created.day):
        years -= 1
    return max(0, years)


def ensure_honor_badges_bootstrapped(
    doc: dict,
    *,
    today: date | None = None,
) -> tuple[dict, bool]:
    today = today or date.today()
    created = _parse_fairy_created(doc)
    completed_years = _completed_tenure_years(created, today)

    earned_ids = _earned_badge_ids(doc)
    progress = _badge_progress_map(doc)
    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]

    changed_pages = False
    changed_progress = False
    newly_earned: set[int] = set()

    if HONOR_PAGE_ID not in unlocked_pages:
        unlocked_pages.append(HONOR_PAGE_ID)
        changed_pages = True

    for badge_id in ALL_HONOR_BADGE_IDS:
        if badge_id not in progress:
            progress[badge_id] = 0
            changed_progress = True

    def _award(badge_id: int) -> None:
        nonlocal changed_progress
        if badge_id in earned_ids:
            if progress.get(badge_id) != 1:
                progress[badge_id] = 1
                changed_progress = True
            return

        earned_ids.add(badge_id)
        progress[badge_id] = 1
        newly_earned.add(badge_id)
        changed_progress = True

    _award(NEW_FAIRY_BADGE_ID)

    if created <= FOUNDING_FAIRY_CUTOFF:
        _award(FOUNDING_FAIRY_BADGE_ID)

    for entry in YEAR_BADGES:
        if completed_years >= entry["years"]:
            _award(entry["badge_id"])

    if not changed_pages and not changed_progress and not newly_earned:
        return doc, False

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    if newly_earned:
        doc["earnedBadges"] = _serialize_earned_badges(
            earned_ids,
            doc,
            newly_earned=newly_earned,
        )
        doc["badgeCount"] = len(earned_ids)
        doc["newestBadge"] = max(newly_earned)
    elif changed_progress or changed_pages:
        doc["earnedBadges"] = _serialize_earned_badges(earned_ids, doc)
        doc["badgeCount"] = len(earned_ids)
        if earned_ids:
            doc["newestBadge"] = max(earned_ids)

    return doc, True


def ensure_starter_badge(doc: dict) -> tuple[dict, bool]:
    return ensure_honor_badges_bootstrapped(doc)


def ensure_collection_badges_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _collection_is_bootstrapped(doc):
        return doc, False

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    totals = _ingredient_totals(doc)
    changed_pages = False

    for page_id in CHAPTER_10_PAGE_IDS:
        if page_id not in unlocked_pages:
            unlocked_pages.append(page_id)
            changed_pages = True

    changed_progress = False
    earned_ids = _earned_badge_ids(doc)
    newly_earned: set[int] = set()

    for item_id, entry in COLLECTION_BADGES.items():
        total = totals.get(item_id, 0)
        if total == 0:
            tier_one_id = entry["tiers"][0]["badge_id"]
            total = progress.get(tier_one_id, 0)
            if total:
                totals[item_id] = total

        previous_progress = {
            tier["badge_id"]: progress.get(tier["badge_id"], 0)
            for tier in entry["tiers"]
        }

        item_newly_earned = _sync_collection_item_badges(
            entry,
            total,
            progress,
            earned_ids,
        )
        newly_earned.update(item_newly_earned)

        for tier in entry["tiers"]:
            badge_id = tier["badge_id"]
            if progress.get(badge_id, 0) != previous_progress.get(badge_id, 0):
                changed_progress = True

    if not changed_pages and not changed_progress and not newly_earned:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["ingredientCollectionTotals"] = {
        str(item_id): totals[item_id] for item_id in sorted(totals)
    }
    if newly_earned:
        doc["earnedBadges"] = _serialize_earned_badges(
            earned_ids,
            doc,
            newly_earned=newly_earned,
        )
        doc["badgeCount"] = len(earned_ids)
        doc["newestBadge"] = max(newly_earned)
    return doc, True


def ensure_leaf_journal_donation_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _leaf_journal_is_bootstrapped(doc):
        return doc, False

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    totals = _leaf_journal_donation_totals(doc)
    changed_pages = False

    if LEAF_JOURNAL_DONATION_PAGE_ID not in unlocked_pages:
        unlocked_pages.append(LEAF_JOURNAL_DONATION_PAGE_ID)
        changed_pages = True

    changed_progress = False
    for track_key, entry in DONATION_TRACKS.items():
        total = totals.get(track_key, 0)
        if total == 0:
            tier_one_id = entry["tiers"][0]["badge_id"]
            total = progress.get(tier_one_id, 0)
            if total:
                totals[track_key] = total

        for tier in entry["tiers"]:
            badge_id = tier["badge_id"]
            desired = total
            if badge_id not in progress:
                progress[badge_id] = desired
                changed_progress = True
            elif progress[badge_id] != desired:
                progress[badge_id] = desired
                changed_progress = True

    if not changed_pages and not changed_progress:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["leafJournalDonationTotals"] = {
        key: totals[key] for key in sorted(totals)
    }
    return doc, True


def ensure_game_badges_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _game_badges_is_bootstrapped(doc):
        return doc, False

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    play_totals = _game_stats_totals(doc)
    best_scores = _game_best_scores(doc)
    spin_stats = _daily_spin_stats(doc)
    changed_pages = False

    for page_id in CHAPTER_7_PAGE_IDS:
        if page_id not in unlocked_pages:
            unlocked_pages.append(page_id)
            changed_pages = True

    changed_progress = False

    for game_id, entry in PLAY_COUNT_TRACKS.items():
        total = play_totals.get(game_id, 0)
        if total == 0:
            tier_one_id = entry["tiers"][0]["badge_id"]
            total = progress.get(tier_one_id, 0)

        for tier in entry["tiers"]:
            badge_id = tier["badge_id"]
            if badge_id not in progress:
                progress[badge_id] = total
                changed_progress = True
            elif progress[badge_id] != total:
                progress[badge_id] = total
                changed_progress = True

    for game_id, entry in HIGH_SCORE_BADGES.items():
        badge_id = entry["badge_id"]
        desired = best_scores.get(game_id, 0)
        if badge_id not in progress:
            progress[badge_id] = desired
            changed_progress = True
        elif progress[badge_id] != desired:
            progress[badge_id] = desired
            changed_progress = True

    spin_total = spin_stats["spins"]
    if spin_total == 0:
        spin_total = progress.get(DAILY_SPIN_PLAY_TRACK["tiers"][0]["badge_id"], 0)

    for tier in DAILY_SPIN_PLAY_TRACK["tiers"]:
        badge_id = tier["badge_id"]
        if badge_id not in progress:
            progress[badge_id] = spin_total
            changed_progress = True
        elif progress[badge_id] != spin_total:
            progress[badge_id] = spin_total
            changed_progress = True

    rock_total = spin_stats["rockWins"]
    if rock_total == 0:
        rock_total = progress.get(DAILY_SPIN_ROCK_WIN_TRACK["tiers"][0]["badge_id"], 0)

    for tier in DAILY_SPIN_ROCK_WIN_TRACK["tiers"]:
        badge_id = tier["badge_id"]
        if badge_id not in progress:
            progress[badge_id] = rock_total
            changed_progress = True
        elif progress[badge_id] != rock_total:
            progress[badge_id] = rock_total
            changed_progress = True

    earned_ids = _earned_badge_ids(doc)
    for badge_id in DAILY_SPIN_PRIZE_BADGE_IDS:
        desired = 1 if badge_id in earned_ids else 0
        if badge_id not in progress:
            progress[badge_id] = desired
            changed_progress = True
        elif progress[badge_id] != desired:
            progress[badge_id] = desired
            changed_progress = True

    if not changed_pages and not changed_progress:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    return doc, True


def ensure_meadow_explorer_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _meadow_explorer_is_bootstrapped(doc):
        return doc, False

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    visited = _visited_meadows(doc)
    changed_pages = False

    if MEADOW_EXPLORER_PAGE_ID not in unlocked_pages:
        unlocked_pages.append(MEADOW_EXPLORER_PAGE_ID)
        changed_pages = True

    changed_progress = False
    for track_key, entry in EXPLORER_TRACKS.items():
        badge_id = entry["badge_id"]
        desired = _season_visit_count(visited, track_key)
        if badge_id not in progress:
            progress[badge_id] = desired
            changed_progress = True
        elif progress[badge_id] != desired:
            progress[badge_id] = desired
            changed_progress = True

    if not changed_pages and not changed_progress:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["visitedMeadows"] = sorted(visited)
    return doc, True


def ensure_starter_badges_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _starter_is_bootstrapped(doc):
        return doc, False

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    craft_totals = _craft_stats_totals(doc)
    changed_pages = False

    for page_id in STARTER_PAGE_IDS:
        if page_id not in unlocked_pages:
            unlocked_pages.append(page_id)
            changed_pages = True

    changed_progress = False
    for entry in CRAFT_HELPER_BADGES.values():
        badge_id = entry["badge_id"]
        desired = craft_totals.get(entry["track_key"], 0)
        if badge_id not in progress:
            progress[badge_id] = desired
            changed_progress = True
        elif progress[badge_id] != desired:
            progress[badge_id] = desired
            changed_progress = True

    if PARTY_GUEST_BADGE_ID not in progress:
        progress[PARTY_GUEST_BADGE_ID] = 0
        changed_progress = True

    if not changed_pages and not changed_progress:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["craftStats"] = craft_totals
    return doc, True


def ensure_friend_badges_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _friend_badges_is_bootstrapped(doc):
        total = _friends_accepted_total(doc)
        previous_accepted = int(doc.get("friendsAccepted") or 0)
        progress = _badge_progress_map(doc)
        earned_ids = _earned_badge_ids(doc)
        changed_progress = False
        newly_earned: set[int] = set()

        for tier in FRIEND_BADGE_TRACK["tiers"]:
            badge_id = tier["badge_id"]
            if progress.get(badge_id, 0) != total:
                progress[badge_id] = total
                changed_progress = True

            if badge_id not in earned_ids and total >= tier["threshold"]:
                earned_ids.add(badge_id)
                newly_earned.add(badge_id)

        if not changed_progress and not newly_earned and previous_accepted == total:
            return doc, False

        doc = dict(doc)
        doc["badgeProgress"] = _serialize_badge_progress(progress)
        doc["friendsAccepted"] = total
        if newly_earned:
            doc["earnedBadges"] = _serialize_earned_badges(
                earned_ids,
                doc,
                newly_earned=newly_earned,
            )
            doc["badgeCount"] = len(earned_ids)
            doc["newestBadge"] = max(newly_earned)
        return doc, True

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)
    total = _friends_accepted_total(doc)
    changed_pages = False
    changed_progress = False
    newly_earned: set[int] = set()

    if FRIEND_PAGE_ID not in unlocked_pages:
        unlocked_pages.append(FRIEND_PAGE_ID)
        changed_pages = True

    for tier in FRIEND_BADGE_TRACK["tiers"]:
        badge_id = tier["badge_id"]
        if badge_id not in progress:
            progress[badge_id] = total
            changed_progress = True
        elif progress[badge_id] != total:
            progress[badge_id] = total
            changed_progress = True

        if badge_id not in earned_ids and total >= tier["threshold"]:
            earned_ids.add(badge_id)
            newly_earned.add(badge_id)

    if not changed_pages and not changed_progress and not newly_earned:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["friendsAccepted"] = total
    if newly_earned:
        doc["earnedBadges"] = _serialize_earned_badges(
            earned_ids,
            doc,
            newly_earned=newly_earned,
        )
        doc["badgeCount"] = len(earned_ids)
        doc["newestBadge"] = max(newly_earned)
    return doc, True


def ensure_craft_badges_bootstrapped(doc: dict) -> tuple[dict, bool]:
    if _craft_badges_is_bootstrapped(doc):
        return doc, False

    doc, changed = ensure_starter_badge(doc)

    unlocked_pages = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)
    practice_totals = _craft_stats_totals(doc)
    personal_totals = _personal_craft_stats_totals(doc)
    changed_pages = False
    changed_progress = False
    newly_earned: set[int] = set()

    for page_id in CRAFT_CHAPTER_PAGE_IDS:
        if page_id not in unlocked_pages:
            unlocked_pages.append(page_id)
            changed_pages = True

    for track in CRAFT_PRACTICE_TRACKS.values():
        total = practice_totals.get(track["track_key"], 0)
        for tier in track["tiers"]:
            badge_id = tier["badge_id"]
            if badge_id not in progress:
                progress[badge_id] = total
                changed_progress = True
            elif progress[badge_id] != total:
                progress[badge_id] = total
                changed_progress = True

            if badge_id not in earned_ids and total >= tier["threshold"]:
                earned_ids.add(badge_id)
                newly_earned.add(badge_id)

    for track in CRAFT_PERSONAL_TRACKS.values():
        total = personal_totals.get(track["track_key"], 0)
        for tier in track["tiers"]:
            badge_id = tier["badge_id"]
            if badge_id not in progress:
                progress[badge_id] = total
                changed_progress = True
            elif progress[badge_id] != total:
                progress[badge_id] = total
                changed_progress = True

            if badge_id not in earned_ids and total >= tier["threshold"]:
                earned_ids.add(badge_id)
                newly_earned.add(badge_id)

    if not changed_pages and not changed_progress and not newly_earned:
        return doc, changed

    doc = dict(doc)
    doc["unlockedPages"] = sorted(set(unlocked_pages))
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["craftStats"] = practice_totals
    doc["personalCraftStats"] = personal_totals
    if newly_earned:
        doc["earnedBadges"] = _serialize_earned_badges(
            earned_ids,
            doc,
            newly_earned=newly_earned,
        )
        doc["badgeCount"] = len(earned_ids)
        doc["newestBadge"] = max(newly_earned)
    return doc, True


def ensure_badges_bootstrapped(doc: dict) -> tuple[dict, bool]:
    doc, honor_changed = ensure_honor_badges_bootstrapped(doc)
    doc, collection_changed = ensure_collection_badges_bootstrapped(doc)
    doc, donation_changed = ensure_leaf_journal_donation_bootstrapped(doc)
    doc, game_changed = ensure_game_badges_bootstrapped(doc)
    doc, meadow_changed = ensure_meadow_explorer_bootstrapped(doc)
    doc, starter_changed = ensure_starter_badges_bootstrapped(doc)
    doc, friend_changed = ensure_friend_badges_bootstrapped(doc)
    doc, craft_changed = ensure_craft_badges_bootstrapped(doc)
    return (
        doc,
        honor_changed
        or collection_changed
        or donation_changed
        or game_changed
        or meadow_changed
        or starter_changed
        or friend_changed
        or craft_changed,
    )


def load_fairy_doc(air, av_id: int) -> dict:
    return (
        air.mongoInterface.mongodb.fairies.find_one(
            {"_id": av_id},
            _BADGE_DOC_FIELDS,
        )
        or {"_id": av_id}
    )


def persist_fairy_badge_state(air, av_id: int, doc: dict) -> None:
    earned_ids = _earned_badge_ids(doc)
    fields = {
        "earnedBadges": doc.get("earnedBadges") or [],
        "badgeProgress": doc.get("badgeProgress") or [],
        "unlockedPages": doc.get("unlockedPages") or [],
        "ingredientCollectionTotals": doc.get("ingredientCollectionTotals") or {},
        "leafJournalDonationTotals": doc.get("leafJournalDonationTotals") or {},
        "badgeCount": int(doc.get("badgeCount") or 0),
        "newestBadge": int(doc.get("newestBadge") or 0),
        "gameStats": doc.get("gameStats") or {},
        "dailySpinStats": doc.get("dailySpinStats") or {"spins": 0, "rockWins": 0},
        "visitedMeadows": doc.get("visitedMeadows") or [],
        "craftStats": doc.get("craftStats") or {track_key: 0 for track_key in CRAFT_TRACK_KEYS},
        "personalCraftStats": doc.get("personalCraftStats")
        or {track_key: 0 for track_key in CRAFT_TRACK_KEYS},
        "friendsAccepted": int(doc.get("friendsAccepted") or 0),
    }

    existing = air.mongoInterface.mongodb.fairies.find_one(
        {"_id": av_id},
        {"moreOptions": 1, "favoriteBadgeId": 1},
    ) or {}
    stored_favorite = int(existing.get("favoriteBadgeId") or 0)
    if stored_favorite in earned_ids:
        more_options, favorite_badge_id = resolve_favorite_badge(
            existing.get("moreOptions") or "",
            stored_favorite,
            earned_ids,
        )
        fields["moreOptions"] = more_options
        fields["favoriteBadgeId"] = favorite_badge_id

    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {"$set": fields},
        upsert=True,
    )


def build_login_payload(doc: dict) -> tuple[list, list, list]:
    earned_badges = []
    for entry in (doc.get("earnedBadges") or []):
        if not isinstance(entry, dict) or "badgeId" not in entry:
            continue
        earned_badges.append(
            [int(entry["badgeId"]), str(entry.get("dateEarned") or "")]
        )
    unlocked_page_ids = [int(page_id) for page_id in (doc.get("unlockedPages") or [])]
    badge_progress = []
    for entry in (doc.get("badgeProgress") or []):
        if not isinstance(entry, dict) or "badgeId" not in entry:
            continue
        badge_progress.append(
            [
                int(entry["badgeId"]),
                wire_badge_progress(
                    int(entry["badgeId"]),
                    int(entry.get("progress") or 0),
                ),
            ]
        )
    return earned_badges, unlocked_page_ids, badge_progress


def apply_ingredient_collection(badge_manager, av_id: int, item_id: int, amount: int) -> None:
    if item_id not in ITEM_IDS or amount <= 0:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_collection_badges_bootstrapped(doc)

    totals = _ingredient_totals(doc)
    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)

    previous_total = totals.get(item_id, 0)
    new_total = previous_total + amount
    totals[item_id] = new_total

    entry = COLLECTION_BADGES[item_id]
    previous_progress = {
        tier["badge_id"]: progress.get(tier["badge_id"], 0)
        for tier in entry["tiers"]
    }

    newly_earned_set = _sync_collection_item_badges(
        entry,
        new_total,
        progress,
        earned_ids,
    )
    newly_earned = sorted(newly_earned_set)

    doc["ingredientCollectionTotals"] = {
        str(key): totals[key] for key in sorted(totals)
    }
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["earnedBadges"] = _serialize_earned_badges(
        earned_ids,
        doc,
        newly_earned=set(newly_earned),
    )
    doc["badgeCount"] = len(earned_ids)
    if newly_earned:
        doc["newestBadge"] = max(newly_earned)

    persist_fairy_badge_state(air, av_id, doc)

    earned_dates = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in doc["earnedBadges"]
    }

    for tier_index, tier in enumerate(entry["tiers"]):
        badge_id = tier["badge_id"]
        if tier_index < 3:
            _send_progress_update(badge_manager, av_id, badge_id, amount)
            continue

        previous_royal = previous_progress.get(badge_id, 0)
        new_royal = progress.get(badge_id, 0)
        royal_delta = new_royal - previous_royal
        if royal_delta > 0:
            _send_progress_update(badge_manager, av_id, badge_id, royal_delta)

    for badge_id in newly_earned:
        badge_manager.sendUpdateToAvatarId(
            av_id,
            "badgeAcquired",
            [[badge_id, earned_dates.get(badge_id, "")]],
        )


def apply_leaf_journal_donation(badge_manager, av_id: int, track_key: str, amount: int = 1) -> None:
    if track_key not in DONATION_TRACKS or amount <= 0:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_leaf_journal_donation_bootstrapped(doc)

    totals = _leaf_journal_donation_totals(doc)
    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)

    previous_total = totals.get(track_key, 0)
    new_total = previous_total + amount
    totals[track_key] = new_total

    entry = DONATION_TRACKS[track_key]
    newly_earned: list[int] = []

    for tier in entry["tiers"]:
        badge_id = tier["badge_id"]
        progress[badge_id] = new_total

        if badge_id in earned_ids:
            continue

        if new_total >= tier["threshold"]:
            earned_ids.add(badge_id)
            newly_earned.append(badge_id)

    doc["leafJournalDonationTotals"] = {
        key: totals[key] for key in sorted(totals)
    }
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["earnedBadges"] = _serialize_earned_badges(
        earned_ids,
        doc,
        newly_earned=set(newly_earned),
    )
    doc["badgeCount"] = len(earned_ids)
    if newly_earned:
        doc["newestBadge"] = max(newly_earned)

    persist_fairy_badge_state(air, av_id, doc)

    earned_dates = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in doc["earnedBadges"]
    }

    for tier in entry["tiers"]:
        badge_id = tier["badge_id"]
        _send_progress_update(badge_manager, av_id, badge_id, amount)

    for badge_id in newly_earned:
        badge_manager.sendUpdateToAvatarId(
            av_id,
            "badgeAcquired",
            [[badge_id, earned_dates.get(badge_id, "")]],
        )


def _apply_tier_track(
    badge_manager,
    av_id: int,
    doc: dict,
    track: dict,
    total: int,
    *,
    progress_delta: int,
) -> None:
    air = badge_manager.air
    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)
    newly_earned: list[int] = []

    for tier in track["tiers"]:
        badge_id = tier["badge_id"]
        progress[badge_id] = total

        if badge_id in earned_ids:
            continue

        if total >= tier["threshold"]:
            earned_ids.add(badge_id)
            newly_earned.append(badge_id)

    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["earnedBadges"] = _serialize_earned_badges(
        earned_ids,
        doc,
        newly_earned=set(newly_earned),
    )
    doc["badgeCount"] = len(earned_ids)
    if newly_earned:
        doc["newestBadge"] = max(newly_earned)

    persist_fairy_badge_state(air, av_id, doc)

    earned_dates = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in doc["earnedBadges"]
    }

    for tier in track["tiers"]:
        badge_id = tier["badge_id"]
        _send_progress_update(badge_manager, av_id, badge_id, progress_delta)

    for badge_id in newly_earned:
        badge_manager.sendUpdateToAvatarId(
            av_id,
            "badgeAcquired",
            [[badge_id, earned_dates.get(badge_id, "")]],
        )


def apply_game_play(badge_manager, av_id: int, game_id: int) -> None:
    if game_id not in PLAY_COUNT_TRACKS:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_game_badges_bootstrapped(doc)

    total = _game_stats_totals(doc).get(game_id, 0)
    _apply_tier_track(
        badge_manager,
        av_id,
        doc,
        PLAY_COUNT_TRACKS[game_id],
        total,
        progress_delta=1,
    )


def apply_high_score_badge(badge_manager, av_id: int, game_id: int, best_score: int) -> None:
    if game_id not in HIGH_SCORE_BADGES:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_game_badges_bootstrapped(doc)

    entry = HIGH_SCORE_BADGES[game_id]
    badge_id = entry["badge_id"]
    threshold = entry["threshold"]
    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)
    newly_earned: list[int] = []

    previous_best = progress.get(badge_id, 0)
    progress[badge_id] = best_score

    if badge_id not in earned_ids and best_score >= threshold:
        earned_ids.add(badge_id)
        newly_earned.append(badge_id)

    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["earnedBadges"] = _serialize_earned_badges(
        earned_ids,
        doc,
        newly_earned=set(newly_earned),
    )
    doc["badgeCount"] = len(earned_ids)
    if newly_earned:
        doc["newestBadge"] = max(newly_earned)

    persist_fairy_badge_state(air, av_id, doc)

    earned_dates = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in doc["earnedBadges"]
    }

    wire_delta = wire_badge_progress_delta(badge_id, previous_best, best_score)
    _send_progress_update(badge_manager, av_id, badge_id, wire_delta)

    for earned_badge_id in newly_earned:
        badge_manager.sendUpdateToAvatarId(
            av_id,
            "badgeAcquired",
            [[earned_badge_id, earned_dates.get(earned_badge_id, "")]],
        )


def apply_daily_spin_play(badge_manager, av_id: int, amount: int = 1) -> None:
    if amount <= 0:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_game_badges_bootstrapped(doc)

    total = _daily_spin_stats(doc)["spins"]
    _apply_tier_track(
        badge_manager,
        av_id,
        doc,
        DAILY_SPIN_PLAY_TRACK,
        total,
        progress_delta=amount,
    )


def apply_daily_spin_rock_win(badge_manager, av_id: int, amount: int = 1) -> None:
    if amount <= 0:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_game_badges_bootstrapped(doc)

    total = _daily_spin_stats(doc)["rockWins"]
    _apply_tier_track(
        badge_manager,
        av_id,
        doc,
        DAILY_SPIN_ROCK_WIN_TRACK,
        total,
        progress_delta=amount,
    )


def apply_meadow_explorer_progress(badge_manager, av_id: int, zone_id: int) -> None:
    if zone_id not in ALL_EXPLORER_ZONE_IDS:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_meadow_explorer_bootstrapped(doc)

    visited = _visited_meadows(doc)
    if zone_id in visited:
        return

    visited.add(zone_id)
    track_key = ZONE_TO_TRACK[zone_id]
    entry = EXPLORER_TRACKS[track_key]
    badge_id = entry["badge_id"]
    goal = entry["goal"]
    count = _season_visit_count(visited, track_key)

    progress = _badge_progress_map(doc)
    earned_ids = _earned_badge_ids(doc)
    newly_earned: list[int] = []

    progress[badge_id] = count

    if badge_id not in earned_ids and count >= goal:
        earned_ids.add(badge_id)
        newly_earned.append(badge_id)

    doc["visitedMeadows"] = sorted(visited)
    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["earnedBadges"] = _serialize_earned_badges(
        earned_ids,
        doc,
        newly_earned=set(newly_earned),
    )
    doc["badgeCount"] = len(earned_ids)
    if newly_earned:
        doc["newestBadge"] = max(newly_earned)

    persist_fairy_badge_state(air, av_id, doc)

    earned_dates = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in doc["earnedBadges"]
    }

    _send_progress_update(badge_manager, av_id, badge_id, 1)

    for earned_badge_id in newly_earned:
        badge_manager.sendUpdateToAvatarId(
            av_id,
            "badgeAcquired",
            [[earned_badge_id, earned_dates.get(earned_badge_id, "")]],
        )


def apply_craft_progress(
    badge_manager,
    av_id: int,
    profession_id: int,
    crafting_style: int,
) -> None:
    if crafting_style == CRAFT_STYLE_PRACTICE:
        tracks = CRAFT_PRACTICE_TRACKS
        stats_fn = _craft_stats_totals
    elif crafting_style == CRAFT_STYLE_PERSONAL:
        tracks = CRAFT_PERSONAL_TRACKS
        stats_fn = _personal_craft_stats_totals
    else:
        return

    if profession_id not in tracks:
        return

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_starter_badges_bootstrapped(doc)
    doc, _ = ensure_craft_badges_bootstrapped(doc)

    track = tracks[profession_id]
    total = stats_fn(doc).get(track["track_key"], 0)

    if crafting_style == CRAFT_STYLE_PRACTICE:
        doc["craftStats"] = stats_fn(doc)
        doc["craftStats"][track["track_key"]] = total
    else:
        doc["personalCraftStats"] = stats_fn(doc)
        doc["personalCraftStats"][track["track_key"]] = total

    _apply_tier_track(
        badge_manager,
        av_id,
        doc,
        track,
        total,
        progress_delta=1,
    )


def apply_friend_accepted_progress(badge_manager, av_id: int) -> None:
    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    previous = int(doc.get("friendsAccepted") or 0)
    total = _friends_accepted_total(doc)

    if total <= previous:
        doc, _ = ensure_friend_badges_bootstrapped(doc)
        if int(doc.get("friendsAccepted") or 0) != total:
            doc["friendsAccepted"] = total
            persist_fairy_badge_state(air, av_id, doc)
        return

    doc, _ = ensure_friend_badges_bootstrapped(doc)
    doc["friendsAccepted"] = total

    _apply_tier_track(
        badge_manager,
        av_id,
        doc,
        FRIEND_BADGE_TRACK,
        total,
        progress_delta=total - previous,
    )


def grant_badge_direct(badge_manager, av_id: int, badge_id: int) -> bool:
    if badge_id not in DAILY_SPIN_PRIZE_BADGE_IDS:
        return False

    air = badge_manager.air
    doc = load_fairy_doc(air, av_id)
    doc, _ = ensure_game_badges_bootstrapped(doc)

    earned_ids = _earned_badge_ids(doc)
    if badge_id in earned_ids:
        return True

    progress = _badge_progress_map(doc)
    progress[badge_id] = 1
    earned_ids.add(badge_id)

    doc["badgeProgress"] = _serialize_badge_progress(progress)
    doc["earnedBadges"] = _serialize_earned_badges(
        earned_ids,
        doc,
        newly_earned={badge_id},
    )
    doc["badgeCount"] = len(earned_ids)
    doc["newestBadge"] = badge_id

    persist_fairy_badge_state(air, av_id, doc)

    earned_dates = {
        int(entry["badgeId"]): str(entry.get("dateEarned") or "")
        for entry in doc["earnedBadges"]
    }

    _send_progress_update(badge_manager, av_id, badge_id, 1)
    badge_manager.sendUpdateToAvatarId(
        av_id,
        "badgeAcquired",
        [[badge_id, earned_dates.get(badge_id, "")]],
    )
    return True
