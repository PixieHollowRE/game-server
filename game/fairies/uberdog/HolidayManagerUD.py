from datetime import datetime, timezone
from direct.distributed.DistributedObjectUD import DistributedObjectUD
from game.fairies.daily.TimeUtils import get_season

class HolidayManagerUD(DistributedObjectUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def getTimeSpan(self) -> list[str]:
        tags = [
            "Meadow_Theater_Camp",
            "Meadow_Camp2013",
            "Meadow_Decorations_SummmerSplash",
            "Meadow_SummerSplash",
            "Meadow_CampPixie2012",
            "Emote_Camp"
        ]

        # Handle Seasonal changes for PP/Tearoom automatically
        current_season = get_season(datetime.now(timezone.utc))
        cap_season = current_season.capitalize()
        tags.append(f"Meadow_{cap_season}")
        tags.append(f"Tearoom_{cap_season}")

        return tags

    def getTimeSpanMessage(self) -> str:
        return "Welcome to the test server. Missing features and bugs are to be expected. Enjoy!"

    def getShopsOpen(self) -> int:
        return 1
