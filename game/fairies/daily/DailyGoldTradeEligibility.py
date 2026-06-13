from __future__ import annotations

from datetime import datetime, timedelta, timezone

from game.fairies.daily.DailyChanceEligibility import _pacific_tz_at, _to_pacific_local

DAILY_GOLD_TRADE_CAP = 200


def next_pacific_midnight_utc(now: datetime | None = None) -> int:
    """Unix epoch (UTC) of the next Pacific midnight strictly after ``now``."""
    if now is None:
        now = datetime.now(timezone.utc)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    local = _to_pacific_local(now)
    next_day = (local + timedelta(days=1)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    tz = _pacific_tz_at(next_day.astimezone(timezone.utc))
    next_midnight = next_day.replace(tzinfo=tz)
    return int(next_midnight.timestamp())


def refresh_gold_trade_window(
    amount: int,
    reset_at: int,
    now: datetime | None = None,
) -> tuple[int, int]:
    """Return updated (amount, reset_at) for the current Pacific-day window."""
    if now is None:
        now = datetime.now(timezone.utc)
    elif now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)

    now_epoch = int(now.timestamp())
    if reset_at <= 0 or now_epoch >= reset_at:
        return 0, next_pacific_midnight_utc(now)
    return amount, reset_at
