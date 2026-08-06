import datetime
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

# Post Office message types, mirroring the client's DistributedSurprise constants
# (TYPE_POST_OFFICE_POSTCARDS / TYPE_POST_OFFICE_GIFT_SETS). Stored on each message
# record so the archive request and the home surprise can filter by type.
MESSAGE_TYPE_POSTCARD = 4
MESSAGE_TYPE_GIFTSET = 5

# Collections the client renders as postcards rather than gift sets, from
# postOfficeAssets.xml <postCardCollections collectionsIds="7001,7002">. Kept in
# sync with the shop data (pixie_post_office_8.py). Postcards deliver no wearable.
POSTCARD_COLLECTION_IDS = frozenset({7001, 7002})

# howAcquired for a diamond (gold) purchase, matching handleItemPurchase's gold
# path. Post Office gifting is always paid in diamonds.
GIFT_HOW_ACQUIRED = 1

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

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setRequestDyeItem: {avId}")
            return

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
                avatar.d_refreshEquippedItem(invId)

            self.d_setPurchaseResponse(avId, result.modified_count > 0)
        else:
            # Send failure purchase response back to the client.
            self.d_setPurchaseResponse(avId, success)

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

    def setRequestGiftSet(self, items, userId, recipientFairyId, messageId, currency) -> None:
        # The client's PostCardConfirmation and GiftSetConfirmation both call this
        # (dispatchSetRequestGiftSet). There's no type flag on the wire, so we infer
        # postcard-vs-giftset from the item's collection (POSTCARD_COLLECTION_IDS).
        #
        # Behaviour differs by type:
        #   - Gift set: the purchased items go to BOTH the sender (a plain copy) and
        #     the recipient (a copy stamped with the sender as giftedBy). One charge.
        #   - Postcard: nothing is delivered; only a message record is written so the
        #     card shows up in the recipient's home Post Office.
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setRequestGiftSet: {avId}")
            return

        shop = getShopByZone(self.zoneId)
        if not shop:
            self.notify.warning(f"setRequestGiftSet: no shop for zone {self.zoneId}")
            self.d_setPurchaseResponse(avId, False)
            return

        resolvedItems: list[ShopItem] = []
        isPostcard = False
        priceTotal = 0

        for itemData in items:
            itemIndex, amount, collectionId = itemData

            if collectionId in POSTCARD_COLLECTION_IDS:
                isPostcard = True

            shopItem = getShopItemByIndex(shop, collectionId, itemIndex)
            if not shopItem:
                # Same fallback as setRequestPurchase: some items live under a
                # collection's outfits rather than its flat item list. Guard the
                # index so a mismatched collection fails cleanly instead of raising.
                collection = shop.collectionsById.get(collectionId)
                outfitItems = (
                    [it for outfit in collection.outfits for it in outfit.items]
                    if collection else []
                )
                if 0 <= itemIndex < len(outfitItems):
                    shopItem = outfitItems[itemIndex]

            if not shopItem:
                self.notify.warning(
                    f"setRequestGiftSet: bad item {collectionId}/{itemIndex} from {avId}")
                self.d_setPurchaseResponse(avId, False)
                return

            resolvedItems.append(shopItem)
            # Post Office gifting is billed in diamonds (gold); the member price
            # collapses to goldPrice for these collections (see ShopItem defaults).
            priceTotal += shopItem.goldPrice

        # Post Office gifting always pays in diamonds -- SelectFriendAndMessage
        # forces currency to MTX_ITEM_ID, so charge gold regardless of `currency`.
        if not avatar.takeGold(priceTotal):
            self.d_setPurchaseResponse(avId, False)
            return

        # Sender identity, for the gift ribbon and the postcard's "from" fairy.
        senderDoc = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": avId},
            {"name": 1, "address": 1, "talent": 1, "icon": 1}
        ) or {}
        senderName = senderDoc.get("name", "")

        if isPostcard:
            # The postcard design id (88501-88521) rides along as the "background".
            background = resolvedItems[0].itemId
            wordIds: list[int] = []
            messageType = MESSAGE_TYPE_POSTCARD
        else:
            background = 0
            wordIds = []
            messageType = MESSAGE_TYPE_GIFTSET
            for shopItem in resolvedItems:
                # Sender keeps a plain copy; recipient gets the gifted copy.
                self._deliverGiftItem(avId, shopItem, giftedById=0, giftedByName="")
                self._deliverGiftItem(
                    recipientFairyId, shopItem, giftedById=avId, giftedByName=senderName)
                wordIds.append(shopItem.itemId)

        self._writePostOfficeMessage(
            recipientId=recipientFairyId,
            senderId=avId,
            senderDoc=senderDoc,
            senderName=senderName,
            messageType=messageType,
            background=background,
            phrase=messageId,
            wordIds=wordIds,
        )

        # If the recipient's home realm is up (they may be standing in it right
        # now), get the mailbox put out for this kind of mail. The realm only
        # counts messages at generate time, so without this the mailbox would
        # not appear until they left home and came back. Routed via the
        # RealmGuardian because the realm can be hosted by any district AI.
        self.air.sendMailArrivedToRealmGuardian(recipientFairyId, messageType)

        # Light the recipient's HUD gift-box right away. The recipient is very
        # often on a different realm (district AI process) than the sender, so we
        # can't go through doId2do -- that only ever holds objects owned by this
        # process. statusUpdateFromFairy lives on DistributedFairyPlayer, so
        # address the update at the recipient's own object and route it straight
        # to their client connection channel, which the message director resolves
        # no matter which district they're on (same trick as
        # FairiesHomeRealmAI.bootRequest). Harmless no-op if they're offline --
        # nobody is subscribed to that channel, and _pushPendingMailStatus lights
        # the gift-box on their next generate.
        self.air.sendUpdateToDoId(
            "DistributedFairyPlayer", "statusUpdateFromFairy", recipientFairyId,
            [avId, messageType],
            channelId=self.GetPuppetConnectionChannel(recipientFairyId))

        self.d_setPurchaseResponse(avId, True)

    def _deliverGiftItem(self, fairyId: int, item: ShopItem, giftedById: int, giftedByName: str) -> None:
        # Push one wardrobe item onto `fairyId` and live-notify their client. The
        # Mongo write is what an offline recipient picks up on next login (see
        # FairyInventoryMgrUD.avatarOnline re-syncing wardrobe items); the
        # sendUpdateToAvatarId is harmless if nobody is listening on that channel.
        invId = self.air.mongoInterface.getNextDoId()
        itemType = item.itemType or fc.get_item_type(item.itemId)

        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": fairyId},
            {
                "$push": {
                    "avatar.items": {
                        "inv_id": invId,
                        "type": itemType,
                        "item_id": item.itemId,
                        "slot": -1,
                        "createdById": 0,
                        "createdByName": "",
                        "giftedById": giftedById,
                        "giftedByName": giftedByName,
                        "quality": 0,
                        "color1": item.color1,
                        "color2": item.color2,
                        "howAcquired": GIFT_HOW_ACQUIRED,
                        "location": "Wardrobe"
                    }
                }
            }
        )

        self.air.inventoryManager.sendUpdateToAvatarId(fairyId, "wardrobeItem", [
            item.itemId,
            [invId, item.itemId, -1, 0, "", giftedById, giftedByName, 0,
             item.color1, item.color2, GIFT_HOW_ACQUIRED]
        ])

    def _writePostOfficeMessage(self, recipientId: int, senderId: int, senderDoc: dict,
                                senderName: str, messageType: int, background: int,
                                phrase: int, wordIds: Sequence[int]) -> None:
        # One row per received postcard/gift set. Read back by web-api's
        # FairiesMessageArchiveRequest and counted by the home Post Office surprise.
        self.air.mongoInterface.mongodb.messages.insert_one({
            "_id": self.air.mongoInterface.getNextDoId(),
            "recipient_id": recipientId,
            "type": messageType,
            "sender": {
                "fairy_id": senderId,
                "name": senderName,
                "address": senderDoc.get("address", ""),
                "talent": senderDoc.get("talent", 0),
                "icon": senderDoc.get("icon", 0),
            },
            "background": background,
            "phrase": phrase,
            "words": list(wordIds),
            "created": datetime.datetime.utcnow(),
        })
