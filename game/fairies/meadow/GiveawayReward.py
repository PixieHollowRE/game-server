"""
Claiming a giveaway and paying it out.

Split out of DistributedGiveawayAI because the magic words hand out the same
giveaways without there being an object in a meadow to click.

The claim and the payout are separate on purpose. Claiming is the part that has
to be exactly once -- two districts, or one impatient double-click, must not
both get through -- so it is a single conditional Mongo update whose result
decides who won. Only the winner goes on to pay out, and a payout that fails
releases the claim again so the fairy is not left having "collected" nothing.
"""

from direct.directnotify import DirectNotifyGlobal

from game.fairies.ai import FairiesConstants as fc
from game.fairies.badges import badge_lookup
from game.fairies.fairy.ItemGrant import STORAGE, WARDROBE, grant_item

notify = DirectNotifyGlobal.directNotify.newCategory("GiveawayReward")

# The field on the fairy document. A plain list of giveaway_id; absent on every
# fairy who has never collected one, which the $ne query below handles for free.
COLLECTED_FIELD = "giveawaysCollected"


def has_collected(air, avId: int, giveawayId: int) -> bool:
    return air.mongoInterface.mongodb.fairies.find_one(
        {"_id": avId, COLLECTED_FIELD: giveawayId}, {"_id": 1}
    ) is not None


def claim(air, avId: int, giveawayId: int) -> bool:
    """
    Take this giveaway for this fairy, if nobody has already.

    True means the caller now owns the payout. False means either the fairy had
    it already or there is no such fairy; both are refusals, and neither should
    hand anything over.
    """
    result = air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId, COLLECTED_FIELD: {"$ne": giveawayId}},
        {"$addToSet": {COLLECTED_FIELD: giveawayId}},
    )

    return result.modified_count > 0


def release(air, avId: int, giveawayId: int) -> None:
    """Undo a claim whose payout did not happen."""
    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId}, {"$pull": {COLLECTED_FIELD: giveawayId}}
    )


def _showPickup(air, avId: int, itemId: int, color1: int = 0, color2: int = 0) -> None:
    """
    Float the thing that was just collected over the fairy's head.
    """
    avatar = air.doId2do.get(avId)

    if avatar is None:
        return

    avatar.sendUpdate("setItemEvent", [itemId, 1, color1, color2])


def award(air, avId: int, giveawayId: int, itemId: int,
          color1: int = 0, color2: int = 0) -> bool:
    """
    Pay a giveaway's reward into whichever inventory it belongs in.
    """
    try:
        typeId = fc.get_type_id(itemId)
    except ValueError:
        notify.warning(
            "giveaway %d: reward item %d is not a valid item id" % (giveawayId, itemId)
        )
        return False

    if typeId in fc.BADGE_TYPE_IDS:
        if not _awardBadge(air, avId, giveawayId, itemId):
            return False

        # Colours deliberately dropped: the bubble draws the badge itself.
        _showPickup(air, avId, itemId)
        return True

    if typeId in fc.POUCH_TYPE_IDS:
        if air.inventoryManager.addIngredientsToPouchWithPickupFeedback(avId, itemId, 1):
            return True

        notify.warning(
            "giveaway %d: could not put reward %d in %d's pouch"
            % (giveawayId, itemId, avId)
        )
        return False

    if typeId in fc.STORAGE_TYPE_IDS:
        where = STORAGE
    elif typeId in fc.WARDROBE_TYPE_IDS:
        where = WARDROBE
    else:
        notify.warning(
            "giveaway %d: reward item %d is type %d, which is not a kind of "
            "reward a giveaway knows how to pay out" % (giveawayId, itemId, typeId)
        )
        return False

    if grant_item(air, avId, itemId, color1, color2, where):
        _showPickup(air, avId, itemId, color1, color2)
        return True

    notify.warning(
        "giveaway %d: could not grant reward %d to %d" % (giveawayId, itemId, avId)
    )
    return False


def _awardBadge(air, avId: int, giveawayId: int, badgeId: int) -> bool:
    if badge_lookup.get_badge(badgeId) is None:
        notify.warning(
            "giveaway %d: reward %d looks like a badge id but no such badge exists"
            % (giveawayId, badgeId)
        )
        return False
    
    page = badge_lookup.get_page_for_badge(badgeId)

    if page is not None:
        air.badgeManager.d_unlockPage(avId, page["id"])

    air.badgeManager.d_unlockBadge(avId, badgeId)
    air.badgeManager.d_giveBadge(avId, badgeId)

    # Fire-and-forget: the uberdog owns every write to badgeData and reports
    # back to the fairy's client itself, so there is no verdict to wait for.
    return True
