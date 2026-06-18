"""Leaderboard constants and per-game qualification thresholds."""

from datetime import date

from game.fairies.badges.GameBadgeRegistry import PLAY_COUNT_GAME_IDS

LEADERBOARD_WEEKLY = 0
LEADERBOARD_SEASONAL = 1

# Sunday rollover honors badges (10869); boards and scoring are unaffected.
WEEKLY_LEADERBOARD_REWARDS_ENABLED = False

# Flash leaderboards panel sends tabId + 1 (see Leaderboards.showLeaderBoardForGame).
CLIENT_WEEKLY_BOARD_TYPE = 1
CLIENT_SEASONAL_BOARD_TYPE = 2

TOP_N = 10

LEADERBOARD_DATA_COLLECTION = "leaderboard_data"
META_DOC_ID = "meta"

# Season ends end-of-day Pacific on this date (temporary hardcode).
SEASON_END_DATE = date(2026, 8, 31)
CURRENT_SEASON_ID = "2026-08-31"

# Minimum scores from web-main/xml/panels/leaderboards.xml (working games only).
GAME_THRESHOLDS: dict[int, int] = {
    1: 10000,
    2: 10000,
    7: 10000,
    8: 10000,
    9: 10000,
    10: 10000,
    11: 10000,
    14: 10000,
    15: 20000,
    43: 10000,
    44: 10000,
    45: 10000,
    47: 10000,
    48: 10000,
    49: 10000,
}

SUPPORTED_GAME_IDS = frozenset(
    game_id for game_id in PLAY_COUNT_GAME_IDS if game_id in GAME_THRESHOLDS
)


def leaderboard_doc_id(board_type: int, game_id: int, week_id: str) -> str:
    label = "weekly" if board_type == LEADERBOARD_WEEKLY else "seasonal"
    return f"{label}:{game_id}:{week_id}"


def threshold_for_game(game_id: int) -> int:
    return GAME_THRESHOLDS.get(game_id, 10000)


def is_weekly_board_request(board_type: int) -> bool:
    """True when the client requested the weekly tab leaderboard."""
    return board_type in (LEADERBOARD_WEEKLY, CLIENT_WEEKLY_BOARD_TYPE)


def is_seasonal_board_request(board_type: int) -> bool:
    """True for client seasonal tab (boardType=2). LEADERBOARD_SEASONAL is doc storage only."""
    return board_type == CLIENT_SEASONAL_BOARD_TYPE
