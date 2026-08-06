from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class FairyInventoryMgrUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def announceGenerate(self) -> None:
        DistributedObjectGlobalUD.announceGenerate(self)

        self.accept("avatarOnline", self.avatarOnline)

    def avatarOnline(self, avatarId, avatarType) -> None:
        # avatarType is unused, but it is sent over the messenger anyways.
        fairy = self.air.mongoInterface.retrieveDocs(
            "fairies", avatarId, "_id", {"avatar.items": 1}
        )[0]

        for item in fairy["avatar"]["items"]:
            if item["location"] in ("Wardrobe", "Equipped"):
                fieldName = "wardrobeItem"
            elif item["location"] == "Storage":
                fieldName = "storageItem"
            else:
                continue

            invItemExt = [
                item["inv_id"],
                item["item_id"],
                item["slot"],
                item["createdById"],
                item["createdByName"],
                item["giftedById"],
                item["giftedByName"],
                item["quality"],
                item["color1"],
                item["color2"],
                item["howAcquired"]
            ]

            self.sendUpdateToAvatarId(avatarId, fieldName, [
                item["item_id"],
                invItemExt
            ])

    def setStorageSlot(self, invId, slot) -> None:
        self._setItemSlot(invId, slot)

    def setWardrobeSlot(self, invId, slot) -> None:
        self._setItemSlot(invId, slot)

    def _setItemSlot(self, invId, slot) -> None:
        avId = self.air.getAvatarIdFromSender()

        if not avId:
            self.notify.warning(f"setItemSlot: no avatar for sender, invId={invId}")
            return

        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": avId, "avatar.items.inv_id": invId},
            {"$set": {"avatar.items.$.slot": slot}}
        )
