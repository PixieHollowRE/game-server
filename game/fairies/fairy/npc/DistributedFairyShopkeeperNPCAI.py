from collections.abc import Sequence

from game.fairies.fairy.structs.ShopTriedOnItems import ShopTriedOnItems

from .DistributedFairyNPCAI import DistributedFairyNPCAI

from game.fairies.fairy.structs.ShopCollection import ShopCollection

from game.fairies.fairy.structs.FairyDNA import FairyDNA
from game.fairies.fairy.structs.PurchaseType import PurchaseType
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.OutfitItem import OutfitItem

from game.fairies.housing.HomeItems import clearPlacedHomeItems
from game.fairies.shop.data import getShopByZone, getShopOutfitByOutfitId, getShopItemByIndex
from game.fairies.ai import FairiesConstants as fc

PURCHASE_FAIL = 0
PURCHASE_SUCCESS = 1

EQUIP_SLOTS = {
    1: "setHeadItem",
    2: "setNecklace",
    3: "setChestItem",
    4: "setBelt",
    5: "setSkirt",
    6: "setWrist",
    7: "setAnkle",
    8: "setShoes",
}

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

    def setRequestDyeItem(self, invId, color1, color2, type, unk2):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        price: int = 0

        fields = {}
        dyes = []

        if color1 != -1:
            fields["avatar.items.$.color1"] = color1
            price += self.dye1Price
            dyes.append(color1)
        if color2 != -1:
            fields["avatar.items.$.color2"] = color2
            price += self.dye2Price
            dyes.append(color2)

        if not fields:
            return False  # Nothing to update

        ing_type = self.dyeCostItemId
        success = self.air.inventoryManager.removeIngredientsFromPouch(avId, ing_type, price)
        avatar.d_syncPouchAfterChanges()

        if success:
            for d in dyes:
                dye_id = d + 14000
                self.air.inventoryManager.removeIngredientsFromPouch(avId, dye_id, 1)
                avatar.d_syncPouchAfterChanges()

            result = self.air.mongoInterface.mongodb.fairies.update_one(
                {"_id": avId, "avatar.items.inv_id": invId},
                {"$set": fields}
            )

            if result.modified_count > 0 and avatar:
                self._refreshAfterDye(avatar, invId)

            self.d_setPurchaseResponse(avId, result.modified_count > 0)
        else:
            # Send failure purchase response back to the client.
            self.d_setPurchaseResponse(avId, success)

    def _refreshAfterDye(self, avatar, invId) -> None:
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {
                "_id": avatar.doId,
                "avatar.items": {
                    "$elemMatch": {"inv_id": invId, "location": "Equipped"}
                },
            },
            {"avatar.items.$": 1},
        )
        if not fairy:
            return

        items = fairy.get("avatar", {}).get("items")
        if not items:
            return

        item = items[0]
        slot = item.get("slot")
        method = EQUIP_SLOTS.get(slot)
        if not method:
            return

        payload = [invId, item["item_id"], item["color1"], item["color2"]]
        avatar.sendUpdate(method, [payload])
        avatar.redrawFairy()

    def setRequestPurchase(self, items, usingGold) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setRequestPurchase: {avId}")
            return

        shop = getShopByZone(self.zoneId)

        purchaseRequests: list = []

        priceTotal: int = 0

        for itemData in items:
            itemIndex, amount, collectionId = itemData

            # The collection is what says how this purchase gets fulfilled, so
            # it rides along with the request rather than just its id.
            collection = shop.collectionsById.get(collectionId)

            if itemIndex == -1:
                # Outfits have the amount set as the outfitId for some reason...
                requestItems = list(getShopOutfitByOutfitId(shop, collectionId, amount).items)

                requestPrice = sum(
                    outfitItem.goldPrice if usingGold else outfitItem.price
                    for outfitItem in requestItems
                )
            else:
                item = getShopItemByIndex(shop, collectionId, itemIndex)
                if item:
                    requestItems = [item]
                    requestPrice = (item.goldPrice if usingGold else item.price) * amount
                else:
                    # Item from outfit handler
                    all_items = [item for outfit in collection.outfits for item in outfit.items]
                    item = all_items[itemIndex]
                    requestItems = [item]
                    requestPrice = (item.goldPrice if usingGold else item.price) * amount

            purchaseRequests.append((requestItems, amount, collection))
            priceTotal += requestPrice

        if usingGold:
            success = avatar.takeGold(priceTotal)
        else:
            ing_type = purchaseRequests[0][2].currencyId
            success = self.air.inventoryManager.removeIngredientsFromPouch(avId, ing_type, priceTotal)
            avatar.d_syncPouchAfterChanges()

        if not success:
            # Send failure purchase response back to the client.
            self.d_setPurchaseResponse(avId, success)
            return

        for requestItems, amount, collection in purchaseRequests:
            for item in requestItems:
                self.fulfillPurchase(avId, avatar, item, amount, collection, usingGold)

        self.d_setPurchaseResponse(avId, True)

    def fulfillPurchase(self, avId: int, avatar, item: ShopItem | OutfitItem, amount: int, collection: ShopCollection, usingGold: bool) -> None:
        purchaseType = collection.purchaseType

        if purchaseType is PurchaseType.POUCH:
            self.purchasePouchItemsHelper(avId, item.itemId, amount)
        elif purchaseType is PurchaseType.DNA:
            self.purchaseDNA(avatar, item, collection)
        elif purchaseType is PurchaseType.HOME_TYPE:
            self.purchaseHomeType(avId, avatar, item)
        elif purchaseType is PurchaseType.HOME_ITEM:
            self.handleItemPurchase(avId, item, usingGold, location="Storage", updateName="storageItem")
        else:
            self.handleItemPurchase(avId, item, usingGold)

    def purchaseDNA(self, avatar, item: ShopItem | OutfitItem, collection: ShopCollection) -> None:
        dna = FairyDNA.unpackFromTuple(avatar.getFairyDNA())

        # An expression changes two fields at once (the face and its matching
        # eye), so apply the whole collection's edits before redrawing.
        for fieldName, offset in collection.dnaFields:
            setattr(dna, fieldName, item.itemId + offset)

        avatar.b_setFairyDNA(dna.asTuple())

        avatar.redrawFairy()

    def purchaseHomeType(self, avId: int, avatar, item: ShopItem | OutfitItem) -> None:
        homeType = item.itemId - fc.HOME_ITEM_ID_OFFSET

        # Moving house empties the old one out. Guard on the home actually
        # changing: the client won't sell you the home you already live in, but
        # if one ever asked, taking payment is a smaller sin than clearing out a
        # home the fairy never left.
        if avatar.getHomeType() != homeType:
            clearPlacedHomeItems(self.air, avId)

        # A home isn't an inventory item -- it's a field on the fairy. The
        # broadcast only reaches the client, so persist it ourselves or
        # _defaultHomeType hands back the old home on the next login.
        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {"$set": {"homeType": homeType}}
        )

        avatar.b_setHomeType(homeType)

    def handleItemPurchase(self, avId: int, item: ShopItem | OutfitItem, usingGold: bool, location: str = "Wardrobe", updateName: str = "wardrobeItem") -> None:
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
        # howAcquired > 10 takes up a wardrobe spot; items bought with gold use 1
        howAcquired = 1 if usingGold else 11

        itemType = item.itemType
        if not itemType and location == "Storage":
            # The furniture shops don't spell their types out, and get_item_type
            # is reliable over their id range. It isn't over every shop's --
            # Farden's seeds raise and Beck's pets come back as "AnkleItem" --
            # so leave those alone and keep this to the storage path.
            itemType = fc.get_item_type(itemId)

        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId},
            {
                "$push": {
                    "avatar.items": {
                        "inv_id": invId,
                        "type": itemType,
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
                        "location": location
                    }
                }
            }
        )

        self.air.inventoryManager.sendUpdateToAvatarId(avId, updateName, [
            itemId,
            [invId, itemId, slot, createdById, createdByName, giftedById, giftedByName, quality, color1, color2, howAcquired
        ]])

    def d_setPurchaseResponse(self, avId: int, success: bool) -> None:
        self.sendUpdateToAvatarId(avId, "setPurchase", [PURCHASE_SUCCESS if success else PURCHASE_FAIL])

    def purchasePouchItemsHelper(self, avId, itemId, amount):
        avatar = self.air.doId2do.get(avId)

        itemCount = amount
        itemSlot = -1

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))
