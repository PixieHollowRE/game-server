from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

from game.fairies.badges import badge_events

# accumulate() takes an int16 amount in fairy.dc.
MAX_AMOUNT = 32767

class FairiesBadgeManagerAI(DistributedObjectGlobalAI):
    def __init__(self, air) -> None:
        super().__init__(air)

    def d_accumulate(self, avatarId: int, eventId: int, amount: int = 1) -> None:
        """Report `amount` occurrences of a badge event (see badge_events)."""
        if amount <= 0:
            return

        self.sendUpdate("accumulate", [avatarId, eventId, min(amount, MAX_AMOUNT)])

    def d_exploreMeadow(self, avatarId: int, zoneId: int) -> None:
        """
        Report that a fairy entered a meadow counting toward a seasonal Meadow
        Explorer badge.

        Rides the `accumulate` field rather than a dclass method of its own:
        adding one would renumber every field after it and break the client
        handshake. The zoneId travels in the amount slot, and the uberdog routes
        EVENT_EXPLORE_MEADOW to its distinct-zone path. Deduping revisits is the
        uberdog's job, so this fires on every entry.
        """
        self.sendUpdate(
            "accumulate", [avatarId, badge_events.EVENT_EXPLORE_MEADOW, zoneId]
        )

    def d_giveBadge(self, avatarId: int, badgeId: int) -> None:
        """
        Award a badge outright, no progress to accumulate.

        For badges the district decides on its own -- e.g. a minigame High Score,
        where the threshold is a score too large for accumulate()'s int16 amount,
        so the comparison happens on the AI and only the verdict is sent here.
        """
        self.sendUpdate("giveBadge", [avatarId, badgeId])
