"""
Handing a wardrobe or storage item to a fairy.

Both kinds live in the same `avatar.items` array and differ only by `location`
and which FairyInventoryMgr field the client is told about it on, so every path
that gives one away outright -- Vidia's daily spin, a magic word -- funnels
through here. DistributedCraftingMinigameAI keeps its own copy because a
crafted item also carries a quality and (eventually) a maker.
"""

from game.fairies.ai.FairiesConstants import get_item_type

# howAcquired the client reads back for an item that was simply given rather
# than bought or crafted. 11 is what the daily spin has always written, and
# nothing downstream distinguishes one kind of gift from another, so everything
# the server hands over outright looks the same in the wardrobe panel.
HOW_ACQUIRED_GRANTED = 11

# (location, FairyInventoryMgr field) pairs -- pass one of these as `where`.
WARDROBE = ("Wardrobe", "wardrobeItem")
STORAGE = ("Storage", "storageItem")


def grant_item(air, avId: int, itemId: int, color1: int = 0, color2: int = 0,
               where=WARDROBE, howAcquired: int = HOW_ACQUIRED_GRANTED) -> int:
    """
    Push one item onto the fairy's `avatar.items` and tell their client.

    Returns the new invId, or 0 if there was no fairy document to push onto.
    The client update is fire-and-forget: an offline fairy simply picks the item
    up from the database on their next login (FairyInventoryMgrUD.avatarOnline).
    """
    location, updateName = where
    invId = air.mongoInterface.getNextDoId()
    itemType = get_item_type(itemId)

    invItemExt = [
        invId,
        itemId,
        -1,
        0,
        "",
        0,
        "",
        0,
        color1,
        color2,
        howAcquired,
    ]

    result = air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId},
        {
            "$push": {
                "avatar.items": {
                    "inv_id": invId,
                    "type": itemType,
                    "item_id": itemId,
                    "slot": -1,
                    "createdById": 0,
                    "createdByName": "",
                    "giftedById": 0,
                    "giftedByName": "",
                    "quality": 0,
                    "color1": color1,
                    "color2": color2,
                    "howAcquired": howAcquired,
                    "location": location,
                }
            }
        },
    )

    if result.modified_count == 0:
        return 0

    air.inventoryManager.sendUpdateToAvatarId(avId, updateName, [itemId, invItemExt])

    return invId
