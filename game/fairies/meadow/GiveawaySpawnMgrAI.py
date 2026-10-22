"""
Puts the giveaways in the meadows, once, at startup.

Much less machinery than IngredientSpawnMgrAI, because a giveaway is permanent
scenery rather than a spawn: it stands at a hand-picked coordinate, is never
collected away, and never respawns. Eligibility is per fairy and lives on the
fairy, so there is nothing here to tick, time or re-place.

Started once by FairiesAIRepository.createObjects().
"""

from direct.directnotify import DirectNotifyGlobal

from game.fairies.meadow.DistributedGiveawayAI import DistributedGiveawayAI
from game.fairies.meadow.GiveawaySpawnData import GIVEAWAY_DEFS, PLACEMENTS


class GiveawaySpawnMgrAI:
    notify = DirectNotifyGlobal.directNotify.newCategory("GiveawaySpawnMgrAI")

    def __init__(self, air) -> None:
        self.air = air
        self.giveaways: list[DistributedGiveawayAI] = []

    def start(self) -> None:
        for placement in PLACEMENTS:
            if not placement.enabled:
                continue

            definition = GIVEAWAY_DEFS.get(placement.key)

            if definition is None:
                self.notify.warning(
                    "no giveaway %d to place in zone %d"
                    % (placement.key, placement.zone_id)
                )
                continue

            self.giveaways.append(self.place(definition, placement))

        self.notify.info("Placed %d giveaways" % len(self.giveaways))

    def place(self, definition, placement) -> DistributedGiveawayAI:
        giveaway = DistributedGiveawayAI(self.air)

        giveaway.setGiveawayID(definition.giveaway_id)
        giveaway.setClaimId(definition.key)
        giveaway.setPhraseOnly(definition.phrase_only)
        giveaway.setEventID(definition.event_id)
        giveaway.setHolidayBit(definition.holiday_bit)
        giveaway.setItemEventId(definition.item_event_id)
        giveaway.setMembersOnly(definition.members_only)
        giveaway.setRewardColors(
            definition.reward_color1, definition.reward_color2
        )
        giveaway.setRewardAmount(definition.reward_amount)

        # itemID is the reward, not the art; the client picks art off giveawayID
        giveaway.setItemID(definition.reward_item_id)
        giveaway.setName(definition.display_name)
        giveaway.setPosition(placement.x, placement.y)
        giveaway.setColorIDs(list(definition.color_ids))

        # Client never renders a count on giveaway art, whatever reward_amount is
        giveaway.setItemCount(1)
        giveaway.setServingSize(1)

        # No spawnMgr — that hook respawns collected stacks, which giveaways never do
        giveaway.generateWithRequired(placement.zone_id)

        self.notify.debug(
            "Placed giveaway %d (%s, reward %d) in zone %d at (%d, %d)"
            % (
                definition.giveaway_id,
                definition.display_name,
                definition.reward_item_id,
                placement.zone_id,
                placement.x,
                placement.y,
            )
        )

        return giveaway
