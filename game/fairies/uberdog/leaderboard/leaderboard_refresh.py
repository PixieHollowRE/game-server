from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from typing import Callable
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from game.fairies.uberdog.leaderboard.leaderboard_registry import SEASON_END_DATE


def _pacific_tz():
    try:
        return ZoneInfo("America/Los_Angeles")
    except ZoneInfoNotFoundError:
        return timezone(timedelta(hours=-8))


PACIFIC = _pacific_tz()

ROLLOVER_TASK_NAME = "leaderboardWeeklyRollover"
SEASON_ROLLOVER_TASK_NAME = "leaderboardSeasonRollover"
HOURLY_REFRESH_TASK_NAME = "leaderboardHourlyRefresh"
HOURLY_REFRESH_SECONDS = 3600.0


def get_current_week_id(now: datetime | None = None) -> str:
    """Return the Sunday-start week key for the given Pacific-local moment."""
    if now is None:
        now = datetime.now(PACIFIC)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=PACIFIC)
    else:
        now = now.astimezone(PACIFIC)

    midnight_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    days_since_sunday = (now.weekday() + 1) % 7
    week_start = midnight_today - timedelta(days=days_since_sunday)
    return week_start.strftime("%Y-%m-%d")


def previous_week_id(now: datetime | None = None) -> str:
    """Return the week key for the Sunday-start week immediately before the current one."""
    current = datetime.strptime(get_current_week_id(now), "%Y-%m-%d").replace(tzinfo=PACIFIC)
    return (current - timedelta(days=7)).strftime("%Y-%m-%d")


def seconds_until_next_sunday_midnight(now: datetime | None = None) -> float:
    if now is None:
        now = datetime.now(PACIFIC)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=PACIFIC)
    else:
        now = now.astimezone(PACIFIC)

    midnight_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    days_ahead = (6 - now.weekday()) % 7
    next_sunday = midnight_today + timedelta(days=days_ahead)
    if days_ahead == 0 and now >= next_sunday:
        next_sunday += timedelta(days=7)
    return max(0.0, (next_sunday - now).total_seconds())


def schedule_next_rollover(task_mgr, callback: Callable[[], None]) -> None:
    delay = seconds_until_next_sunday_midnight()

    def _run(task):
        callback()
        schedule_next_rollover(task_mgr, callback)
        return task.done

    task_mgr.remove(ROLLOVER_TASK_NAME)
    task_mgr.doMethodLater(delay, _run, ROLLOVER_TASK_NAME)


def _season_end_for_year(year: int) -> datetime:
    return datetime(
        year,
        SEASON_END_DATE.month,
        SEASON_END_DATE.day,
        23,
        59,
        59,
        tzinfo=PACIFIC,
    )


def get_current_season_id(now: datetime | None = None) -> str:
    """Return the season key (end-date string) for the active Pacific season."""
    if now is None:
        now = datetime.now(PACIFIC)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=PACIFIC)
    else:
        now = now.astimezone(PACIFIC)

    year = now.year
    if now <= _season_end_for_year(year):
        return f"{year:04d}-{SEASON_END_DATE.month:02d}-{SEASON_END_DATE.day:02d}"
    return f"{year + 1:04d}-{SEASON_END_DATE.month:02d}-{SEASON_END_DATE.day:02d}"


def previous_season_id(now: datetime | None = None) -> str:
    """Return the season key that ended immediately before the current one."""
    current = get_current_season_id(now)
    end_year = int(current[:4])
    return f"{end_year - 1:04d}-{SEASON_END_DATE.month:02d}-{SEASON_END_DATE.day:02d}"


def seconds_until_season_end(now: datetime | None = None) -> float:
    if now is None:
        now = datetime.now(PACIFIC)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=PACIFIC)
    else:
        now = now.astimezone(PACIFIC)

    season_end = _season_end_for_year(int(get_current_season_id(now)[:4]))
    if now >= season_end:
        season_end = _season_end_for_year(int(get_current_season_id(now)[:4]) + 1)
    return max(0.0, (season_end - now).total_seconds())


def schedule_season_rollover(task_mgr, callback: Callable[[], None]) -> None:
    delay = seconds_until_season_end()

    def _run(task):
        callback()
        schedule_season_rollover(task_mgr, callback)
        return task.done

    task_mgr.remove(SEASON_ROLLOVER_TASK_NAME)
    task_mgr.doMethodLater(delay, _run, SEASON_ROLLOVER_TASK_NAME)


def schedule_hourly_refresh(task_mgr, callback: Callable[[], None]) -> None:
    def _run(task):
        callback()
        schedule_hourly_refresh(task_mgr, callback)
        return task.done

    task_mgr.remove(HOURLY_REFRESH_TASK_NAME)
    task_mgr.doMethodLater(HOURLY_REFRESH_SECONDS, _run, HOURLY_REFRESH_TASK_NAME)
