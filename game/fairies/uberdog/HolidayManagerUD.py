from datetime import datetime, timezone
from direct.distributed.DistributedObjectUD import DistributedObjectUD
from game.fairies.daily.TimeUtils import get_season

def getActiveTags() -> list[str]:
    """
    The tag set the client's TagManager runs on, which decides which tagged
    <image>/<hotspot> variants in a meadow's config.xml are live right now.

    Module-level because the AI needs the same answer the uberdog hands the
    client -- meadow_xml resolves hotspots against it, and the two drifting
    apart would mean the server acting on a hotspot the player can't see.
    """
    tags = [
        "Meadow_Theater_Camp",
        "Meadow_Camp2013",
        "Meadow_Decorations_SummmerSplash",
        "Meadow_SummerSplash",
        "Meadow_CampPixie2012",
        "Emote_Camp",
    ]

    # Handle Seasonal changes for PP/Tearoom automatically
    current_season = get_season(datetime.now(timezone.utc))
    cap_season = current_season.capitalize()
    tags.append(f"Meadow_{cap_season}")
    tags.append(f"Tearoom_{cap_season}")

    return tags

class HolidayManagerUD(DistributedObjectUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def getTimeSpan(self) -> list[str]:
        return getActiveTags()

    def getTimeSpanMessage(self) -> str:
        return "Welcome to the test server. Missing features and bugs are to be expected. Enjoy!"

    def getShopsOpen(self) -> int:
        return 1
