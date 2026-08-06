from game.fairies.badges import badge_events
from game.fairies.fairy.ItemGrant import STORAGE, WARDROBE, grant_item
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

def _grant_wardrobe(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    success = grant_item(air, avId, prize.id, prize.c1, prize.c2, WARDROBE)
    return (True, _prize_as_reward_ext(prize)) if success else (False, None)

def _grant_home(air, avId, prize: PoolItem) -> tuple[bool, RewardExt | None]:
    success = grant_item(air, avId, prize.id, prize.c1, prize.c2, STORAGE)
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