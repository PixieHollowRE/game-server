from __future__ import annotations

import logging
import re
import traceback
from datetime import datetime, timezone
from typing import Any

from game.fairies.uberdog.leaderboard.leaderboard_registry import (
    CLIENT_SEASONAL_BOARD_TYPE,
    CLIENT_WEEKLY_BOARD_TYPE,
    LEADERBOARD_SEASONAL,
    LEADERBOARD_WEEKLY,
    LEADERBOARD_DATA_COLLECTION,
    META_DOC_ID,
    SUPPORTED_GAME_IDS,
    TOP_N,
    is_seasonal_board_request,
    is_weekly_board_request,
    leaderboard_doc_id,
    threshold_for_game,
)
from game.fairies.uberdog.leaderboard.leaderboard_refresh import get_current_season_id, get_current_week_id

logger = logging.getLogger(__name__)

_ADDRESS_RE = re.compile(r"^(\d+)(.*)$")
_WHITESPACE_RE = re.compile(r"\s+")

# Legacy weekly rows without achievedAt sort after timed rows on equal scores.
_MISSING_ACHIEVED_AT = "9999-12-31T23:59:59.999999+00:00"

_SCORE_CACHES: list[dict] = []

_FAIRY_LB_FIELDS = {
    "_id": 1,
    "name": 1,
    "address": 1,
    "weeklyGameStats": 1,
    "seasonalGameStats": 1,
}

_WEEKLY_CACHE_KEY = "_weekly"
_SEASONAL_CACHE_KEY = "_seasonal"


def bind_score_cache(cache: dict) -> None:
    if cache not in _SCORE_CACHES:
        _SCORE_CACHES.append(cache)


def _invalidate_all_caches() -> None:
    for cache in _SCORE_CACHES:
        cache.clear()


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def achieved_at_sort_key(raw: str | None) -> str:
    if not raw:
        return _MISSING_ACHIEVED_AT
    return str(raw)


def leaderboard_rank_key(row: dict) -> tuple[int, str, int]:
    """Sort key: higher score first, earlier achievedAt first, lower avId last."""
    return (
        -int(row["score"]),
        achieved_at_sort_key(row.get("achievedAt")),
        int(row["avId"]),
    )


def normalize_fairy_display_name(raw: str | None) -> str:
    """Return the fairy display name from fairies.name (never ownerAccount)."""
    if raw is None:
        return ""
    return _WHITESPACE_RE.sub(" ", str(raw).strip())


def parse_address(address: str | None) -> tuple[int, str]:
    if not address:
        return 0, ""
    match = _ADDRESS_RE.match(address)
    if match:
        return int(match.group(1)), match.group(2)
    return 0, address


def is_avatar_bust_ready(avatar: dict | None) -> bool:
    if not avatar or not isinstance(avatar, dict):
        return False
    proportions = avatar.get("proportions")
    if not isinstance(proportions, dict):
        return False
    for key in ("head", "height", "body"):
        if proportions.get(key) is None:
            return False
    for key in ("face", "eye", "wing"):
        if avatar.get(key) is None:
            return False
    return True


def display_profile_snapshot(row: dict) -> dict | None:
    """Capture bust-relevant profile fields for leaderboard_data storage."""
    avatar = row.get("avatar")
    if not is_avatar_bust_ready(avatar):
        return None
    return {
        "gender": int(row.get("gender") or 0),
        "talent": int(row.get("talent") or 0),
        "avatar": avatar,
    }


def _wire_entry(entry: dict[str, Any]) -> list:
    if "addrNum" in entry and "addrStr" in entry:
        return [
            int(entry["avId"]),
            int(entry["score"]),
            str(entry.get("avName") or ""),
            int(entry.get("addrNum") or 0),
            str(entry.get("addrStr") or ""),
        ]

    addr_num, addr_str = parse_address(entry.get("address"))
    return [
        int(entry["avId"]),
        int(entry["score"]),
        str(entry.get("avName") or ""),
        addr_num,
        addr_str,
    ]


def _leaderboard_entry(
    av_id: int,
    score: int,
    name: str | None,
    address: str | None,
    *,
    achieved_at: str | None = None,
    profile_row: dict | None = None,
) -> dict | None:
    av_name = normalize_fairy_display_name(name)
    if not av_name:
        return None

    addr_num, addr_str = parse_address(address)
    entry: dict[str, Any] = {
        "avId": av_id,
        "score": score,
        "avName": av_name,
        "addrNum": addr_num,
        "addrStr": addr_str,
    }
    if achieved_at:
        entry["achievedAt"] = achieved_at

    if profile_row is not None:
        profile = display_profile_snapshot(profile_row)
        entry["profileReady"] = profile is not None
        if profile is not None:
            entry["displayProfile"] = profile

    return entry


def _leaderboard_data(air) -> Any:
    return air.mongoInterface.mongodb[LEADERBOARD_DATA_COLLECTION]


def _weekly_stats_map(doc: dict) -> dict[str, dict]:
    raw = doc.get("weeklyGameStats") or {}
    stats: dict[str, dict] = {}
    for key, value in raw.items():
        row: dict[str, Any] = {
            "bestScore": int(value.get("bestScore") or 0),
            "weekId": str(value.get("weekId") or ""),
        }
        achieved_at = value.get("achievedAt")
        if achieved_at:
            row["achievedAt"] = str(achieved_at)
        stats[str(key)] = row
    return stats


def _seasonal_stats_map(doc: dict) -> dict[str, dict]:
    raw = doc.get("seasonalGameStats") or {}
    stats: dict[str, dict] = {}
    for key, value in raw.items():
        row: dict[str, Any] = {
            "bestScore": int(value.get("bestScore") or 0),
            "seasonId": str(value.get("seasonId") or ""),
        }
        achieved_at = value.get("achievedAt")
        if achieved_at:
            row["achievedAt"] = str(achieved_at)
        stats[str(key)] = row
    return stats


def _board_cache_root(cache: dict, board_type: int) -> dict:
    key = (
        _SEASONAL_CACHE_KEY
        if board_type == CLIENT_SEASONAL_BOARD_TYPE
        else _WEEKLY_CACHE_KEY
    )
    root = cache.setdefault(key, {})
    return root


def load_meta(air) -> dict:
    return _leaderboard_data(air).find_one({"_id": META_DOC_ID}) or {}


def persist_meta(air, meta: dict) -> None:
    meta["_id"] = META_DOC_ID
    _leaderboard_data(air).replace_one({"_id": META_DOC_ID}, meta, upsert=True)


def load_leaderboard_doc(air, game_id: int, week_id: str | None = None) -> dict | None:
    if week_id is None:
        week_id = get_current_week_id()
    doc_id = leaderboard_doc_id(LEADERBOARD_WEEKLY, game_id, week_id)
    return _leaderboard_data(air).find_one({"_id": doc_id})


def load_seasonal_leaderboard_doc(
    air, game_id: int, season_id: str | None = None
) -> dict | None:
    if season_id is None:
        season_id = get_current_season_id()
    doc_id = leaderboard_doc_id(LEADERBOARD_SEASONAL, game_id, season_id)
    return _leaderboard_data(air).find_one({"_id": doc_id})


def persist_leaderboard_doc(air, game_id: int, week_id: str, entries: list[dict]) -> None:
    doc_id = leaderboard_doc_id(LEADERBOARD_WEEKLY, game_id, week_id)
    _leaderboard_data(air).replace_one(
        {"_id": doc_id},
        {
            "_id": doc_id,
            "boardType": LEADERBOARD_WEEKLY,
            "gameId": game_id,
            "weekId": week_id,
            "refreshedAt": datetime.now(timezone.utc),
            "entries": entries,
        },
        upsert=True,
    )


def persist_seasonal_leaderboard_doc(
    air, game_id: int, season_id: str, entries: list[dict]
) -> None:
    doc_id = leaderboard_doc_id(LEADERBOARD_SEASONAL, game_id, season_id)
    _leaderboard_data(air).replace_one(
        {"_id": doc_id},
        {
            "_id": doc_id,
            "boardType": LEADERBOARD_SEASONAL,
            "gameId": game_id,
            "seasonId": season_id,
            "refreshedAt": datetime.now(timezone.utc),
            "entries": entries,
        },
        upsert=True,
    )


def aggregate_weekly_top_entries(air, game_id: int, week_id: str | None = None) -> list[dict]:
    """Build top-N rows from fairies.weeklyGameStats for a single week.

    Only entries whose per-game ``weekId`` exactly matches ``week_id`` are
    eligible. Lifetime ``gameStats.bestScore`` is never read here, so a fairy
    who set a record weeks ago but has not played this week will not appear.
    """
    if game_id not in SUPPORTED_GAME_IDS:
        return []

    if week_id is None:
        week_id = get_current_week_id()

    game_key = str(game_id)
    threshold = threshold_for_game(game_id)
    score_field = f"weeklyGameStats.{game_key}.bestScore"
    week_field = f"weeklyGameStats.{game_key}.weekId"
    achieved_field = f"weeklyGameStats.{game_key}.achievedAt"

    pipeline = [
        {
            "$match": {
                week_field: week_id,
                score_field: {"$gte": threshold},
            }
        },
        {
            "$project": {
                "avId": "$_id",
                "score": f"${score_field}",
                "achievedAt": {
                    "$ifNull": [f"${achieved_field}", _MISSING_ACHIEVED_AT],
                },
                "avName": {"$ifNull": ["$name", ""]},
                "address": {"$ifNull": ["$address", ""]},
                "avatar": {"$ifNull": ["$avatar", None]},
                "gender": {"$ifNull": ["$gender", 0]},
                "talent": {"$ifNull": ["$talent", 0]},
            }
        },
        {"$sort": {"score": -1, "achievedAt": 1, "avId": 1}},
        {"$limit": TOP_N * 3},
    ]

    rows = list(air.mongoInterface.mongodb.fairies.aggregate(pipeline))
    entries: list[dict] = []
    for row in rows:
        achieved_raw = str(row.get("achievedAt") or "")
        achieved_at = (
            achieved_raw
            if achieved_raw and achieved_raw != _MISSING_ACHIEVED_AT
            else None
        )
        entry = _leaderboard_entry(
            int(row["avId"]),
            int(row["score"]),
            row.get("avName"),
            row.get("address"),
            achieved_at=str(row.get("achievedAt") or ""),
            profile_row=row,
        )
        if entry is None:
            logger.warning(
                "leaderboard skip avId=%s missing fairies.name for gameId=%s",
                row.get("avId"),
                game_id,
            )
            continue
        entries.append(entry)
        if len(entries) >= TOP_N:
            break
    return entries


def aggregate_seasonal_top_entries(
    air, game_id: int, season_id: str | None = None
) -> list[dict]:
    """Build top-N rows from fairies.seasonalGameStats for the active season."""
    if game_id not in SUPPORTED_GAME_IDS:
        return []

    if season_id is None:
        season_id = get_current_season_id()

    game_key = str(game_id)
    threshold = threshold_for_game(game_id)
    score_field = f"seasonalGameStats.{game_key}.bestScore"
    season_field = f"seasonalGameStats.{game_key}.seasonId"
    achieved_field = f"seasonalGameStats.{game_key}.achievedAt"

    pipeline = [
        {
            "$match": {
                season_field: season_id,
                score_field: {"$gte": threshold},
            }
        },
        {
            "$project": {
                "avId": "$_id",
                "score": f"${score_field}",
                "achievedAt": {
                    "$ifNull": [f"${achieved_field}", _MISSING_ACHIEVED_AT],
                },
                "avName": {"$ifNull": ["$name", ""]},
                "address": {"$ifNull": ["$address", ""]},
                "avatar": {"$ifNull": ["$avatar", None]},
                "gender": {"$ifNull": ["$gender", 0]},
                "talent": {"$ifNull": ["$talent", 0]},
            }
        },
        {"$sort": {"score": -1, "achievedAt": 1, "avId": 1}},
        {"$limit": TOP_N * 3},
    ]

    rows = list(air.mongoInterface.mongodb.fairies.aggregate(pipeline))
    entries: list[dict] = []
    for row in rows:
        entry = _leaderboard_entry(
            int(row["avId"]),
            int(row["score"]),
            row.get("avName"),
            row.get("address"),
            achieved_at=str(row.get("achievedAt") or ""),
            profile_row=row,
        )
        if entry is None:
            logger.warning(
                "seasonal skip avId=%s missing fairies.name for gameId=%s",
                row.get("avId"),
                game_id,
            )
            continue
        entries.append(entry)
        if len(entries) >= TOP_N:
            break
    return entries


def rebuild_game_leaderboard_data(air, game_id: int, week_id: str | None = None) -> list[dict]:
    if week_id is None:
        week_id = get_current_week_id()
    entries = aggregate_weekly_top_entries(air, game_id, week_id)
    persist_leaderboard_doc(air, game_id, week_id, entries)
    return entries


def rebuild_game_seasonal_data(
    air, game_id: int, season_id: str | None = None
) -> list[dict]:
    if season_id is None:
        season_id = get_current_season_id()
    entries = aggregate_seasonal_top_entries(air, game_id, season_id)
    persist_seasonal_leaderboard_doc(air, game_id, season_id, entries)
    return entries


def rebuild_leaderboard_data(air, week_id: str | None = None, *, rollover: bool = False) -> None:
    if week_id is None:
        week_id = get_current_week_id()
    season_id = get_current_season_id()

    game_ids = sorted(SUPPORTED_GAME_IDS)
    logger.info(
        "Rebuilding leaderboard snapshots weekId=%s seasonId=%s games=%s",
        week_id,
        season_id,
        game_ids,
    )

    failed_games: list[int] = []
    for game_id in game_ids:
        try:
            rebuild_game_leaderboard_data(air, game_id, week_id)
            rebuild_game_seasonal_data(air, game_id, season_id)
            logger.info("  [OK] gameId=%s weekly+seasonal snapshots written", game_id)
        except Exception:
            failed_games.append(game_id)
            logger.warning(
                "leaderboard rebuild failed gameId=%s weekId=%s seasonId=%s:\n%s",
                game_id,
                week_id,
                season_id,
                traceback.format_exc(),
            )

    if failed_games:
        logger.warning(
            "leaderboard rebuild completed with failures gameIds=%s weekId=%s seasonId=%s",
            failed_games,
            week_id,
            season_id,
        )
    else:
        logger.info(
            "Leaderboard rebuild done — all %d game(s) OK weekId=%s seasonId=%s",
            len(game_ids),
            week_id,
            season_id,
        )

    meta = load_meta(air)
    meta["currentWeeklyId"] = week_id
    meta["currentSeasonId"] = season_id
    meta["lastRefreshAt"] = datetime.now(timezone.utc)
    if rollover:
        meta["lastRolloverAt"] = datetime.now(timezone.utc)
    persist_meta(air, meta)
    _invalidate_all_caches()


def rebuild_seasonal_leaderboard_data(
    air, season_id: str | None = None, *, rollover: bool = False
) -> None:
    if season_id is None:
        season_id = get_current_season_id()

    failed_games: list[int] = []
    for game_id in sorted(SUPPORTED_GAME_IDS):
        try:
            rebuild_game_seasonal_data(air, game_id, season_id)
        except Exception:
            failed_games.append(game_id)
            logger.warning(
                "seasonal rebuild failed gameId=%s seasonId=%s:\n%s",
                game_id,
                season_id,
                traceback.format_exc(),
            )

    if failed_games:
        logger.warning(
            "seasonal rebuild completed with failures gameIds=%s seasonId=%s",
            failed_games,
            season_id,
        )

    meta = load_meta(air)
    meta["currentSeasonId"] = season_id
    meta["lastRefreshAt"] = datetime.now(timezone.utc)
    if rollover:
        meta["lastSeasonRolloverAt"] = datetime.now(timezone.utc)
    persist_meta(air, meta)
    _invalidate_all_caches()


def resolve_lb_request(
    air,
    game_id: int,
    board_type: int,
    cache: dict[int, list] | None = None,
) -> list[list]:
    if game_id not in SUPPORTED_GAME_IDS:
        return []
    if is_weekly_board_request(board_type):
        return get_weekly_top_ten(air, game_id, cache)
    if is_seasonal_board_request(board_type):
        return get_seasonal_top_ten(air, game_id, cache)
    return []


def get_weekly_top_ten(air, game_id: int, cache: dict | None = None) -> list[list]:
    if game_id not in SUPPORTED_GAME_IDS:
        return []

    week_id = get_current_week_id()
    board_cache = _board_cache_root(cache, CLIENT_WEEKLY_BOARD_TYPE) if cache is not None else None
    if board_cache is not None and game_id in board_cache:
        if board_cache.get("_periodId") == week_id:
            return list(board_cache[game_id])

    doc = load_leaderboard_doc(air, game_id, week_id)
    entries = (doc or {}).get("entries") or []
    wire_entries = [_wire_entry(entry) for entry in entries]

    if board_cache is not None:
        board_cache["_periodId"] = week_id
        board_cache[game_id] = wire_entries
    return wire_entries


def get_seasonal_top_ten(air, game_id: int, cache: dict | None = None) -> list[list]:
    if game_id not in SUPPORTED_GAME_IDS:
        return []

    season_id = get_current_season_id()
    board_cache = (
        _board_cache_root(cache, CLIENT_SEASONAL_BOARD_TYPE) if cache is not None else None
    )
    if board_cache is not None and game_id in board_cache:
        if board_cache.get("_periodId") == season_id:
            return list(board_cache[game_id])

    doc = load_seasonal_leaderboard_doc(air, game_id, season_id)
    entries = (doc or {}).get("entries") or []
    wire_entries = [_wire_entry(entry) for entry in entries]

    if board_cache is not None:
        board_cache["_periodId"] = season_id
        board_cache[game_id] = wire_entries
    return wire_entries


def preload_weekly_wire_cache(air, cache: dict) -> None:
    """Load wire rows for every supported game into a shared response cache."""
    week_id = get_current_week_id()
    board_cache = _board_cache_root(cache, CLIENT_WEEKLY_BOARD_TYPE)
    if board_cache.get("_periodId") == week_id and board_cache.get("_allGamesLoaded"):
        return

    for game_id in sorted(SUPPORTED_GAME_IDS):
        get_weekly_top_ten(air, game_id, cache)

    board_cache["_periodId"] = week_id
    board_cache["_allGamesLoaded"] = True


def preload_seasonal_wire_cache(air, cache: dict) -> None:
    """Load seasonal wire rows for every supported game into the shared cache."""
    season_id = get_current_season_id()
    board_cache = _board_cache_root(cache, CLIENT_SEASONAL_BOARD_TYPE)
    if board_cache.get("_periodId") == season_id and board_cache.get("_allGamesLoaded"):
        return

    for game_id in sorted(SUPPORTED_GAME_IDS):
        get_seasonal_top_ten(air, game_id, cache)

    board_cache["_periodId"] = season_id
    board_cache["_allGamesLoaded"] = True


def preload_board_wire_cache(air, cache: dict, board_type: int) -> None:
    if is_seasonal_board_request(board_type):
        preload_seasonal_wire_cache(air, cache)
    else:
        preload_weekly_wire_cache(air, cache)


PANEL_LOAD_GUARD_BASE_SECONDS = 4.0
PANEL_LOAD_GUARD_PER_ENTRY_SECONDS = 0.55
PANEL_LOAD_GUARD_MAX_SECONDS = 14.0
PANEL_LOAD_GUARD_DEFAULT_ENTRY_COUNT = 10


def panel_load_guard_seconds(entry_count: int) -> float:
    """Seconds to ignore follow-up lbRequests while the panel loads bust rows."""
    if entry_count <= 0:
        return 1.0
    guard = (
        PANEL_LOAD_GUARD_BASE_SECONDS
        + entry_count * PANEL_LOAD_GUARD_PER_ENTRY_SECONDS
    )
    return min(guard, PANEL_LOAD_GUARD_MAX_SECONDS)


def panel_guard_entry_count(state: dict, game_id: int, board_type: int) -> int:
    """Entry count used for guard/drain timing (never under-estimate a full board)."""
    wire_key = (
        "seasonWireByGame"
        if is_seasonal_board_request(board_type)
        else "weeklyWireByGame"
    )
    wire_by_game = state.get(wire_key) or state.get("wireByGame") or {}
    pending = len(wire_by_game.get(int(game_id)) or [])
    prior = int(state.get("lastEntryCount") or 0)
    return max(pending, prior, PANEL_LOAD_GUARD_DEFAULT_ENTRY_COUNT)


def prewarm_busts_for_entries(entries: list) -> None:
    """Warm web-api bust XML cache for avIds about to be delivered to the panel."""
    import json
    import urllib.error
    import urllib.request

    from panda3d.core import ConfigVariableString

    fairy_ids: list[int] = []
    for entry in entries:
        if not entry:
            continue
        try:
            fairy_ids.append(int(entry[0]))
        except (IndexError, TypeError, ValueError):
            continue
    if not fairy_ids:
        return

    token = ConfigVariableString("api-token", "").getValue()
    if not token:
        return
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:8013/fairies/api/internal/warmLeaderboardBustCache",
            data=json.dumps({"fairyIds": fairy_ids}).encode("utf-8"),
            headers={
                "Authorization": token,
                "Content-Type": "application/json",
            },
            method="POST",
        )
        urllib.request.urlopen(req, timeout=3)
    except (urllib.error.URLError, OSError, ValueError):
        pass


def record_weekly_score(air, av_id: int, game_id: int, score: int) -> None:
    if game_id not in SUPPORTED_GAME_IDS:
        return

    week_id = get_current_week_id()
    game_key = str(game_id)
    threshold = threshold_for_game(game_id)
    score = int(score)

    doc = (
        air.mongoInterface.mongodb.fairies.find_one(
            {"_id": av_id},
            _FAIRY_LB_FIELDS,
        )
        or {"_id": av_id}
    )
    stats = _weekly_stats_map(doc)
    entry = stats.get(game_key, {"bestScore": 0, "weekId": week_id})

    if entry.get("weekId") != week_id:
        entry = {"bestScore": 0, "weekId": week_id}

    if score < threshold and entry["bestScore"] < threshold:
        return

    new_best = max(entry["bestScore"], score)
    if new_best == entry["bestScore"]:
        return

    entry["bestScore"] = new_best
    entry["achievedAt"] = _utc_now_iso()
    stats[game_key] = entry
    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {"$set": {"weeklyGameStats": stats}},
        upsert=True,
    )


def record_seasonal_score(air, av_id: int, game_id: int, score: int) -> None:
    if game_id not in SUPPORTED_GAME_IDS:
        return

    season_id = get_current_season_id()
    game_key = str(game_id)
    threshold = threshold_for_game(game_id)
    score = int(score)

    doc = (
        air.mongoInterface.mongodb.fairies.find_one(
            {"_id": av_id},
            _FAIRY_LB_FIELDS,
        )
        or {"_id": av_id}
    )
    stats = _seasonal_stats_map(doc)
    entry = stats.get(game_key, {"bestScore": 0, "seasonId": season_id})

    if entry.get("seasonId") != season_id:
        entry = {"bestScore": 0, "seasonId": season_id}

    if score < threshold and entry["bestScore"] < threshold:
        return

    new_best = max(entry["bestScore"], score)
    if new_best == entry["bestScore"]:
        return

    entry["bestScore"] = new_best
    entry["achievedAt"] = _utc_now_iso()
    stats[game_key] = entry
    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {"$set": {"seasonalGameStats": stats}},
        upsert=True,
    )


def sort_entries_for_display(entries: list[dict]) -> list[dict]:
    return sorted(entries, key=leaderboard_rank_key)


def filter_by_threshold(entries: list[dict], game_id: int) -> list[dict]:
    threshold = threshold_for_game(game_id)
    return [entry for entry in entries if int(entry["score"]) >= threshold]


def is_weekly_score_eligible(
    game_entry: dict | None,
    week_id: str,
    threshold: int,
) -> bool:
    """True when a stored weeklyGameStats row counts for the requested week."""
    if not game_entry:
        return False
    if str(game_entry.get("weekId") or "") != week_id:
        return False
    return int(game_entry.get("bestScore") or 0) >= threshold


def is_seasonal_score_eligible(
    game_entry: dict | None,
    season_id: str,
    threshold: int,
) -> bool:
    """True when a stored seasonalGameStats row counts for the requested season."""
    if not game_entry:
        return False
    if str(game_entry.get("seasonId") or "") != season_id:
        return False
    return int(game_entry.get("bestScore") or 0) >= threshold
