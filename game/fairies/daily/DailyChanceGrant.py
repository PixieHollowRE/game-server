"""Apply Daily Spin wins to mongo and push live updates to the client."""
from __future__ import annotations

from typing import TYPE_CHECKING

from game.fairies.badges.BadgeProgressService import grant_badge_direct
from game.fairies.daily.DailyChanceData import (
    CATEGORY_BADGE,
    CATEGORY_HOME,
    CATEGORY_INGREDIENT,
    CATEGORY_POUCH,
    CATEGORY_WARDROBE,
    DailyChancePrize,
    SPIN_BADGE_IDS,
    is_gender_eligible,
    is_ingredient_item,
    is_spin_winnable_badge,
)

if TYPE_CHECKING:
    from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI


from game.fairies.stats.GameStatsService import get_earned_badge_ids_from_doc


def get_earned_spin_badge_ids(air, avId: int) -> set[int]:
    earned = get_earned_badge_ids_from_doc(air, avId)
    return {badge_id for badge_id in earned if badge_id in SPIN_BADGE_IDS}


def grant_badge_prize(air, avId: int, badge_id: int) -> bool:
    if not is_spin_winnable_badge(badge_id):
        return False

    badge_manager = getattr(air, "badgeManager", None)
    if badge_manager is None:
        return False
    return grant_badge_direct(badge_manager, avId, badge_id)


def grant_uses_pouch(item_id: int) -> bool:
    return (
        is_ingredient_item(item_id)
        or 14000 <= item_id < 15000
        or 22500 <= item_id < 23000
    )


def grant_prize(
    air,
    avId: int,
    avatar: DistributedFairyPlayerAI,
    prize: DailyChancePrize,
) -> bool:
    if prize.category == CATEGORY_BADGE or is_spin_winnable_badge(prize.item_id):
        return grant_badge_prize(air, avId, prize.item_id)

    if prize.category == CATEGORY_WARDROBE:
        if not is_gender_eligible(prize, avatar.fairyDNA.gender):
            return False

    if prize.category in (CATEGORY_POUCH, CATEGORY_INGREDIENT):
        return _grant_pouch(air, avId, avatar, prize)

    if prize.category == CATEGORY_WARDROBE:
        return _grant_wardrobe(air, avId, prize)

    if prize.category == CATEGORY_HOME:
        return _grant_home(air, avId, prize)

    return False


def _grant_pouch(air, avId: int, avatar, prize: DailyChancePrize) -> bool:
    if not grant_uses_pouch(prize.item_id):
        return False

    if air.inventoryManager.addIngredientsToPouch(
        avId, prize.item_id, prize.amount, -1
    ):
        avatar.d_setPouch(air.inventoryManager.getPouch(avId))
        return True

    return False


def _grant_wardrobe(air, avId: int, prize: DailyChancePrize) -> bool:
    inv_id = air.mongoInterface.getNextDoId()
    how_acquired = 11

    result = air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId},
        {
            "$push": {
                "avatar.items": {
                    "inv_id": inv_id,
                    "type": prize.item_type,
                    "item_id": prize.item_id,
                    "slot": -1,
                    "createdById": 0,
                    "createdByName": "",
                    "giftedById": 0,
                    "giftedByName": "",
                    "quality": 0,
                    "color1": prize.color1,
                    "color2": prize.color2,
                    "howAcquired": how_acquired,
                    "location": "Wardrobe",
                }
            }
        },
    )

    if result.modified_count == 0:
        return False

    air.inventoryManager.sendUpdateToAvatarId(
        avId,
        "wardrobeItem",
        [
            prize.item_id,
            [
                inv_id,
                prize.item_id,
                -1,
                0,
                "",
                0,
                "",
                0,
                prize.color1,
                prize.color2,
                how_acquired,
            ],
        ],
    )
    return True


def _grant_home(air, avId: int, prize: DailyChancePrize) -> bool:
    inv_id = air.mongoInterface.getNextDoId()
    how_acquired = 1

    inv_item_ext = [
        inv_id,
        prize.item_id,
        -1,
        0,
        "",
        0,
        "",
        0,
        prize.color1,
        prize.color2,
        how_acquired,
    ]

    result = air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId},
        {
            "$push": {
                "avatar.items": {
                    "inv_id": inv_id,
                    "type": prize.item_type,
                    "item_id": prize.item_id,
                    "slot": -1,
                    "createdById": 0,
                    "createdByName": "",
                    "giftedById": 0,
                    "giftedByName": "",
                    "quality": 0,
                    "color1": prize.color1,
                    "color2": prize.color2,
                    "howAcquired": how_acquired,
                    "location": "Storage",
                }
            }
        },
    )

    if result.modified_count == 0:
        return False

    air.inventoryManager.sendUpdateToAvatarId(
        avId, "storageItem", [prize.item_id, inv_item_ext]
    )
    return True
