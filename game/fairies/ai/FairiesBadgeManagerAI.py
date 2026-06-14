from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

from game.fairies.badges.BadgeProgressService import (
    apply_ingredient_collection,
    apply_leaf_journal_donation,
    grant_badge_direct,
)
from game.fairies.badges.FriendBadgeRegistry import FRIEND_ACCEPT_EVENT_ID
from game.fairies.stats.CraftStatsService import apply_craft_result
from game.fairies.stats.MeadowVisitService import apply_meadow_visit


class FairiesBadgeManagerAI(DistributedObjectGlobalAI):
    def __init__(self, air) -> None:
        super().__init__(air)

    def accumulateForMe(self, eventId: int) -> None:
        av_id = self.air.getAvatarIdFromSender()
        if eventId == FRIEND_ACCEPT_EVENT_ID:
            # Client event 25003 credits the inviter in original SWF; friendship
            # badge progress is applied authoritatively for the accepter only
            # via FMPlayerFriendsManager -> FairiesBadgeManagerUD.accumulate.
            self.notify.debug(
                f"accumulateForMe ignored for friend event avId={av_id}, eventId={eventId}"
            )
            return
        self.notify.debug(
            f"accumulateForMe ignored for avId={av_id}, eventId={eventId} "
            "(badges use inventory / leaf journal hooks)"
        )

    def accumulate(self, avId: int, eventId: int, amount: int) -> None:
        if eventId == FRIEND_ACCEPT_EVENT_ID:
            return

    def applyIngredientCollection(self, avId: int, itemId: int, amount: int) -> None:
        apply_ingredient_collection(self, avId, itemId, amount)

    def applyLeafJournalDonation(self, avId: int, trackKey: str, amount: int = 1) -> None:
        apply_leaf_journal_donation(self, avId, trackKey, amount)

    def grantBadgeDirect(self, avId: int, badgeId: int) -> bool:
        return grant_badge_direct(self, avId, badgeId)

    def applyMeadowVisit(self, avId: int, zoneId: int) -> None:
        apply_meadow_visit(self, avId, zoneId)

    def applyCraftHelper(
        self, avId: int, professionId: int, recipeId: int, craftingStyle: int
    ) -> None:
        apply_craft_result(self, avId, professionId, recipeId, craftingStyle)
