from game.fairies.ai.FairiesConstants import get_item_type
from game.fairies.badges import badge_events
from game.fairies.fairy.structs.RewardExt import RewardExt
from .DailyChancePool import PoolItem
from .DailyChanceConstants import Category, INGR_RARITY_TO_PRIZE_AMOUNT, COOKIE_RARITY_TO_PRIZE_AMOUNT

def grant_prize(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    if prize.category in (Category.DYE, Category.INGREDIENT, Category.COOKIE):
        return _grant_pouch(air, avId, prize)
    elif prize.category == Category.WARDROBE:
        return _grant_wardrobe(air, avId, prize)
    elif prize.category == Category.HOME:
        return _grant_home(air, avId, prize)
    elif prize.category == Category.BADGE:
        return _grant_badge(air, avId, prize)
    return False, None

def _prize_as_reward_ext(prize: PoolItem, prize_amount=1) -> RewardExt:
    return RewardExt.unpackFromTuple((prize.id, prize_amount, prize.c1 or 0, prize.c2 or 0))

# NOTE: We don't have a self here so we gotta pass in air itself
def _grant_pouch(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    if prize.category == Category.DYE:
        give_amount = 1
    elif prize.category == Category.INGREDIENT:
        give_amount = INGR_RARITY_TO_PRIZE_AMOUNT[prize.prize_rarity]
    else:
        give_amount = COOKIE_RARITY_TO_PRIZE_AMOUNT[prize.prize_rarity]

    avatar = air.doId2do.get(avId)

    if avatar is None: return False, None # bail fast

    if air.inventoryManager.addIngredientsToPouch(avId, prize.id, give_amount, -1):
        avatar.d_setPouch(air.inventoryManager.getPouch(avId))
        return True, _prize_as_reward_ext(prize, give_amount)

    return False, None

# Mirrored with edits from DistributedCraftingMinigameAI
def _grant_item(air, avId, prizeId, color1, color2, location, update_name) -> bool:
    inv_id = air.mongoInterface.getNextDoId()
    itemType = get_item_type(prizeId)
    how_acquired = 11

    inv_item_ext = [
        inv_id,
        prizeId,
        -1,
        0,
        "",
        0,
        "",
        0,
        color1,
        color2,
        how_acquired,
    ]

    result = air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId},
        {
            "$push": {
                "avatar.items": {
                    "inv_id": inv_id,
                    "type": itemType,
                    "item_id": prizeId,
                    "slot": -1,
                    "createdById": 0,
                    "createdByName": "",
                    "giftedById": 0,
                    "giftedByName": "",
                    "quality": 0,
                    "color1": color1,
                    "color2": color2,
                    "howAcquired": how_acquired,
                    "location": location,
                }
            }
        },
    )

    if result.modified_count == 0:
        return False

    air.inventoryManager.sendUpdateToAvatarId(
        avId, update_name, [prizeId, inv_item_ext]
    )
    return True

def _grant_wardrobe(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    success = _grant_item(air, avId, prize.id, prize.c1, prize.c2, "Wardrobe", "wardrobeItem")
    return (True, _prize_as_reward_ext(prize)) if success else (False, None)

def _grant_home(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    success = _grant_item(air, avId, prize.id, prize.c1, prize.c2, "Storage", "storageItem")
    return (True, _prize_as_reward_ext(prize)) if success else (False, None)

def _grant_badge(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    # A badge prize isn't an inventory item -- the id only rides along in the
    # RewardExt so the client has something to draw in the bowl. The badge
    # itself is the uberdog's to hand out, so all this can do is say it happened.
    #
    # It never hears back, and doesn't need to: the spin only ever offers a badge
    # the fairy hasn't earned (see _dailyChanceExcludedBadges), and _awardBadge
    # ignores a second award of one they have.
    eventId = badge_events.SPIN_BADGE_TO_EVENT.get(prize.id)

    if eventId is None:
        return False, None

    air.badgeManager.d_accumulate(avId, eventId)
    return True, _prize_as_reward_ext(prize)