from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
# We have to hardcode the seasonal boundries to make sure the conversions are smooth. 
# The SOLSTICES_EQUINOXES table should be mirrored in seasonsIndex.xml in both the cilent 
# and the bundle.

PACIFIC = ZoneInfo("America/Los_Angeles")

def now_pacific() -> datetime:
    """The current moment on the Pacific clock the game runs on."""
    return datetime.now(PACIFIC)


def to_pacific(dt) -> datetime:
    """
    Move `dt` onto the Pacific clock, reading a naive value as UTC -- that is
    what pymongo hands back for anything stored in Mongo.
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(PACIFIC)

# ════════════════════════════════════════════════════════════════════════════════════ #
#                                     Season Utils                                     #
# ════════════════════════════════════════════════════════════════════════════════════ #
SOLSTICES_EQUINOXES = {
    # (month, day) for: spring equinox, summer solstice, fall equinox, winter solstice
    2026: [(3,20), (6,21), (9,22), (12,21)],
    2027: [(3,20), (6,21), (9,23), (12,22)],
    2028: [(3,20), (6,20), (9,22), (12,21)],
    2029: [(3,20), (6,21), (9,22), (12,21)],
    2030: [(3,20), (6,21), (9,22), (12,21)],
    2031: [(3,20), (6,21), (9,23), (12,22)],
    2032: [(3,20), (6,20), (9,22), (12,21)],
    2033: [(3,20), (6,21), (9,22), (12,21)],
    2034: [(3,20), (6,21), (9,22), (12,21)],
    2035: [(3,20), (6,21), (9,23), (12,22)],
}

SEASON_NAMES = ["spring", "summer", "autumn", "winter"]

def _season_boundaries(year) -> list:
    """The year's four solstice/equinox moments, each at Pacific midnight."""
    boundaries = SOLSTICES_EQUINOXES.get(year)
    if not boundaries:
        raise ValueError(f"No season data for year {year}")

    return [datetime(year, m, d, tzinfo=PACIFIC) for m, d in boundaries]

def get_season(utc_dt) -> str:
    """
    Returns the name of what season we're currently in.
    """
    local_dt = to_pacific(utc_dt)
    dates = _season_boundaries(local_dt.year)

    season = 3  # winter (before spring equinox)
    for i, boundary in enumerate(dates):
        if local_dt >= boundary:
            season = i

    return SEASON_NAMES[season]

def _previous_winter_solstice(year) -> datetime:
    """
    Where the winter running through January started. Falls back to New Year's
    Day only at the bottom edge of the table, where the real date is unknown.
    """
    if year - 1 not in SOLSTICES_EQUINOXES:
        return datetime(year, 1, 1, tzinfo=PACIFIC)

    return _season_boundaries(year - 1)[3]

def get_season_start_utc(utc_dt) -> datetime:
    """
    Returns the UTC datetime of the start of the current season, taken from the
    Pacific-midnight boundary the client also uses.
    """
    local_dt = to_pacific(utc_dt)
    dates = _season_boundaries(local_dt.year)

    # Before the spring equinox we are in the winter that began last December.
    season_start = _previous_winter_solstice(local_dt.year)
    for boundary in dates:
        if local_dt >= boundary:
            season_start = boundary

    return season_start.astimezone(timezone.utc)

def get_season_end_utc(utc_dt) -> datetime:
    """
    Returns the UTC datetime of the end of the current season -- i.e. the next
    solstice/equinox boundary after utc_dt.
    """
    local_dt = to_pacific(utc_dt)
    dates = _season_boundaries(local_dt.year)

    for boundary in dates:
        if local_dt < boundary:
            return boundary.astimezone(timezone.utc)

    # Winter runs into next year, so its end lives in the next year's table.
    spring_equinox = _season_boundaries(local_dt.year + 1)[0]
    return spring_equinox.astimezone(timezone.utc)

# ════════════════════════════════════════════════════════════════════════════ #
#                                 Period Utils                                 #
# ════════════════════════════════════════════════════════════════════════════ #
def get_period_start(utc_dt, period) -> datetime:
    """Returns the start of the current period in UTC."""
    local_dt = to_pacific(utc_dt)

    if period == "daily":
        period_start_local = local_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        return period_start_local.astimezone(timezone.utc)
    
    elif period == "weekly":
        days_since_monday = local_dt.weekday()
        period_start_local = (local_dt - timedelta(days=days_since_monday)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        return period_start_local.astimezone(timezone.utc)
    
    elif period == "seasonal":
        return get_season_start_utc(utc_dt)