"""
Turns the client's board `type` into the period a submission or request belongs
to, and a stable key naming that period.

The client asks for a board with type = _currentTabId + 1 (see
Leaderboards.showLeaderBoardForGame): 1 for the Weekly tab, 2 for the Seasonal
tab. Rather than reset the boards on a schedule, every read and write is scoped
to the key of the period it falls in, so a new week or season simply starts
returning nothing and fills up on its own -- no cron, no rollover job.

The keys are derived from the period *start* (weekly: the Pacific-anchored
Monday; seasonal: the solstice/equinox boundary), so they are unique per
occurrence -- the winter that starts in Dec 2026 and the winter running in Jan
2026 get different keys even though get_season names both "winter". Both
boundaries come from TimeUtils so the server agrees with seasonsIndex.xml.
"""

from datetime import datetime, timedelta, timezone

from game.fairies.daily.TimeUtils import (
    get_period_start,
    get_season,
    get_season_end_utc,
    get_season_start_utc,
)

TYPE_WEEKLY = 1
TYPE_SEASONAL = 2


def period_key(board_type: int, now: datetime | None = None) -> str | None:
    """
    The storage key for the board period `board_type` is in right now, or None
    if board_type isn't one the client sends.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    if board_type == TYPE_WEEKLY:
        start = get_period_start(now, "weekly")
        return f"weekly:{start.date().isoformat()}"

    if board_type == TYPE_SEASONAL:
        start = get_season_start_utc(now)
        return f"seasonal:{get_season(now)}:{start.date().isoformat()}"

    return None


def period_end(board_type: int, now: datetime | None = None) -> datetime | None:
    """
    When the board period `board_type` is in right now ends -- the moment its key
    stops being the current one. Used to expire a row once its period is over
    (see LeaderBoardMgrUD); None for a board type the client doesn't send.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    if board_type == TYPE_WEEKLY:
        return get_period_start(now, "weekly") + timedelta(days=7)

    if board_type == TYPE_SEASONAL:
        return get_season_end_utc(now)

    return None
