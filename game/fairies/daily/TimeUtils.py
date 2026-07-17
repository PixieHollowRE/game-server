from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
# We have to hardcode the seasonal boundries to make sure the conversions are smooth. 
# The SOLSTICES_EQUINOXES table should be mirrored in seasonsIndex.xml in both the cilent 
# and the bundle.

PACIFIC = ZoneInfo("America/Los_Angeles")

# ════════════════════════════════════════════════════════════════════════════════════ #
#                                     Season Utils                                     #
# ════════════════════════════════════════════════════════════════════════════════════ #
SOLSTICES_EQUINOXES = {
    # (month, day) for: spring equinox, summer solstice, fall equinox, winter solstice
    2026: [(3,20), (6,21), (9,23), (12,21)],
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

SEASON_NAMES = ["spring", "summer", "fall", "winter"]

def get_season(utc_dt) -> str:
    """
    Returns the name of what season we're currently in.
    """
    year = utc_dt.year
    boundaries = SOLSTICES_EQUINOXES.get(year)
    if not boundaries:
        raise ValueError(f"No season data for year {year}")
    
    dates = [datetime(year, m, d, tzinfo=timezone.utc) for m, d in boundaries]
    
    season = 3  # winter (before spring equinox)
    for i, boundary in enumerate(dates):
        if utc_dt >= boundary:
            season = i
    
    return SEASON_NAMES[season]

def get_season_start_utc(utc_dt) -> datetime:
    """
    Returns the UTC datetime of the start of the current season.
    """
    year = utc_dt.year
    boundaries = SOLSTICES_EQUINOXES.get(year)
    if not boundaries:
        raise ValueError(f"No season data for year {year}")
    
    dates = [datetime(year, m, d, tzinfo=timezone.utc) for m, d in boundaries]
    
    season_start = datetime(year, 1, 1, tzinfo=timezone.utc)  # fallback: start of year (winter)
    for boundary in dates:
        if utc_dt >= boundary:
            season_start = boundary

    return season_start

def get_season_end_utc(utc_dt) -> datetime:
    """
    Returns the UTC datetime of the end of the current season -- i.e. the next
    solstice/equinox boundary after utc_dt.
    """
    year = utc_dt.year
    boundaries = SOLSTICES_EQUINOXES.get(year)
    if not boundaries:
        raise ValueError(f"No season data for year {year}")

    dates = [datetime(year, m, d, tzinfo=timezone.utc) for m, d in boundaries]

    for boundary in dates:
        if utc_dt < boundary:
            return boundary

    # Past the winter solstice: winter runs into next year, ending at its spring
    # equinox, so the boundary we want lives in the following year's table.
    next_boundaries = SOLSTICES_EQUINOXES.get(year + 1)
    if not next_boundaries:
        raise ValueError(f"No season data for year {year + 1}")

    m, d = next_boundaries[0]  # spring equinox
    return datetime(year + 1, m, d, tzinfo=timezone.utc)

# ════════════════════════════════════════════════════════════════════════════════════ #
#                                     Period Utils                                     #
# ════════════════════════════════════════════════════════════════════════════════════ #
def get_period_start(utc_dt, period) -> datetime:
    """Returns the start of the current period in UTC."""
    local_dt = utc_dt.astimezone(PACIFIC)

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