from collections.abc import Sequence

from game.fairies.fairy.structs.ShopTriedOnItems import ShopTriedOnItems

from .DistributedFairyNPCAI import DistributedFairyNPCAI

from game.fairies.fairy.structs.ShopCollection import ShopCollection

from game.fairies.shop.ShopData import getShopByZone, getShopItemByIndex

PURCHASE_FAIL = 0
PURCHASE_SUCCESS = 1

class DistributedFairyShopkeeperNPCAI(DistributedFairyNPCAI):
    def __init__(self, air) -> None:
        DistributedFairyNPCAI.__init__(self, air)

        self.shopId: int = 0

        self.shopItems: list[ShopCollection] = []

        self.dyeCostItemId: int = 0
        self.dye1Price: int = 0
        self.dye2Price: int = 0
        self.dye1Gold: int = 0
        self.dye2Gold: int = 0

    def setShopId(self, shopId: int) -> None:
        self.shopId = shopId

    def getShopId(self) -> int:
        return self.shopId

    def setShopItems(self, shopItems: Sequence) -> None:
        self.shopItems = [
            ShopCollection.unpackFromTuple(collectionData)
            for collectionData in shopItems
        ]

    def getShopItems(self) -> list[tuple]:
        return [
            collection.asTuple()
            for collection in self.shopItems
        ]

    def setDyePrice(self, costItemId: int, dye1Price: int, dye2Price: int, dye1Gold: int, dye2Gold: int) -> None:
        self.dyeCostItemId = costItemId
        self.dye1Price = dye1Price
        self.dye2Price = dye2Price
        self.dye1Gold = dye1Gold
        self.dye2Gold = dye2Gold

    def getDyePrice(self) -> tuple[int, int, int, int, int]:
        return (
            self.dyeCostItemId,
            self.dye1Price,
            self.dye2Price,
            self.dye1Gold,
            self.dye2Gold
        )

    def setTryOn(self, items) -> None:
        avId = self.air.getAvatarIdFromSender()
        itemsTriedOn = ShopTriedOnItems.unpackFromTuple((avId, items))
        self.sendUpdateToAvatarId(avId, "setTriedOnItems", [[itemsTriedOn]])

    def setRequestPurchase(self, items, usingGold) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setRequestPurchase: {avId}")
            return

        success: bool = False

        for itemData in items:
            itemIndex, amount, collectionId = itemData
            item = getShopItemByIndex(getShopByZone(self.zoneId), collectionId, itemIndex)

            # TODO: Support non gold item purchases
            success: bool = avatar.takeGold(item.goldPrice) if usingGold else False

            if success:
                invId = self.air.mongoInterface.getNextDoId()
                itemId = item.itemId
                slot = -1
                createdById = 0 # TODO
                createdByName = "" # TODO
                giftedById = 0 # TODO
                giftedByName = "" # TODO
                quality = 0 # TODO
                color1 = item.color1
                color2 = item.color2
                howAcquired = 11 # howAcquired > 10 takes up a wardrobe spot

                self.air.mongoInterface.mongodb.fairies.update_one(
                    {"_id": avId},
                    {
                        "$push": {
                            "avatar.items": {
                                "inv_id": invId,
                                "type": item.itemType,
                                "item_id": itemId,
                                "slot": slot,
                                "createdById": createdById,
                                "createdByName": createdByName,
                                "giftedById": giftedById,
                                "giftedByName": giftedByName,
                                "quality": quality,
                                "color1": color1,
                                "color2": color2,
                                "howAcquired": howAcquired,
                                "location": "Wardrobe"
                            }
                        }
                    }
                )

                self.air.inventoryManager.sendUpdateToAvatarId(avId, "wardrobeItem", [
                    itemId,
                    [invId, itemId, slot, createdById, createdByName, giftedById, giftedByName, quality, color1, color2, howAcquired
                ]])

        self.sendUpdateToAvatarId(avId, "setPurchase", [PURCHASE_SUCCESS if success else PURCHASE_FAIL])
