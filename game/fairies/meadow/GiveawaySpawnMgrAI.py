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

            definition = GIVEAWAY_DEFS.get(placement.giveaway_id)

            if definition is None:
                self.notify.warning(
                    "no giveaway %d to place in zone %d"
                    % (placement.giveaway_id, placement.zone_id)
                )
                continue

            self.giveaways.append(self.place(definition, placement))

        self.notify.info("Placed %d giveaways" % len(self.giveaways))

    def place(self, definition, placement) -> DistributedGiveawayAI:
        giveaway = DistributedGiveawayAI(self.air)

        giveaway.setGiveawayID(definition.giveaway_id)
        giveaway.setEventID(definition.event_id)
        giveaway.setHolidayBit(definition.holiday_bit)
        giveaway.setItemEventId(definition.item_event_id)
        giveaway.setMembersOnly(definition.members_only)
        giveaway.setRewardColors(
            definition.reward_color1, definition.reward_color2
        )

        # Inherited spawn stack fields. itemID is the *reward*, not the art --
        # the client picks the art off giveawayID and only uses itemID to decide
        # which inventory limit to size-check before letting the fairy click.
        giveaway.setItemID(definition.reward_item_id)
        giveaway.setName(definition.display_name)
        giveaway.setPosition(placement.x, placement.y)
        giveaway.setColorIDs(list(definition.color_ids))

        # One item, one serving: a giveaway is always a single thing, and the
        # client never renders a count on giveaway art.
        giveaway.setItemCount(1)
        giveaway.setServingSize(1)

        # Deliberately no spawnMgr. That hook is how a collected ingredient
        # stack tells its pool to delete and respawn it; a giveaway does neither.
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
