from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ''
        self.DISLid: int = 0
        self.gold: int = 0

    def announceGenerate(self):
        self.air.incrementPopulation()

        # Fill in the missing information from the database (i.e. gold)
        self.air.fillInFairyPlayer(self)

    def delete(self):
        # TODO: Set a post-remove message in case of an AI crash.
        self.air.sendFriendManagerAccountOffline(self.DISLid)

        self.air.decrementPopulation()

        DistributedFairyBaseAI.delete(self)

    def setDISLname(self, DISLname: str):
        self.DISLname = DISLname

    def getDISLname(self) -> str:
        return self.DISLname

    def setDISLid(self, DISLid: int) -> int:
        self.air.sendFriendManagerAccountOnline(DISLid)

        self.DISLid = DISLid

    def getDISLid(self) -> int:
        return self.DISLid

    def setAccess(self, access) -> None:
        if access == OTPGlobals.AccessFull:
            self.sendUpdateToAvatarId(self.doId, "setAccess", [access])

    def requestDailyGoldTradeCapData(self) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [0])
        self.sendUpdateToAvatarId(self.doId, "setAmountGoldTradedForToday", [0])

    def requestGetSavedOutfits(self) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [1])
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [[]])

    def requestAddSavedOutfit(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [[]])

    def setOutfitDB(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        SLOT_METHODS = {
            1: "setHeadItem",
            2: "setNecklace",
            3: "setChestItem",
            4: "setBelt",
            5: "setSkirt",
            6: "setWrist",
            7: "setAnkle",
            8: "setShoes"
        }

        EMPTY_LITE_INV = [0, 0, 0, 0]

        desiredOutfit = {
            1: headId, 2: necklaceId, 3: shirtId, 4: beltId,
            5: skirtId, 6: wristId, 7: ankleId, 8: shoesId
        }
        equippedIds = {invId: slot for slot, invId in desiredOutfit.items() if invId != 0}
        filledSlots = set(equippedIds.values())

        table = self.air.mongoInterface.mongodb.fairies
        fairy = table.find_one({"_id": self.doId})

        if not fairy:
            return

        dirty = False
        for item in fairy["avatar"]["items"]:
            invId = item["inv_id"]

            if invId in equippedIds:
                slot = equippedIds[invId]
                changed = item["location"] != "Equipped" or item["slot"] != slot
                item["location"] = "Equipped"
                item["slot"] = slot

                if changed:
                    dirty = True
                    payload = [invId, item["item_id"], item["color1"], item["color2"]]
                    self.sendUpdate(SLOT_METHODS[slot], [payload])

                    self.air.inventoryManager.sendUpdateToAvatarId(
                        self.doId, "wardrobeRemove", [self.doId, invId]
                    )

            elif item["location"] == "Equipped":
                oldSlot = item["slot"]
                item["location"] = "Wardrobe"
                item["slot"] = 0
                dirty = True

                if oldSlot not in filledSlots:
                    self.sendUpdate(SLOT_METHODS[oldSlot], [EMPTY_LITE_INV])

                self.air.inventoryManager.sendUpdateToAvatarId(
                    self.doId, "wardrobeItem", [
                        item["item_id"],
                        [invId, item["item_id"], item["slot"],
                         item["createdById"], item["createdByName"],
                         item["giftedById"], item["giftedByName"],
                         item["quality"], item["color1"], item["color2"],
                         item["howAcquired"]]
                    ]
                )

        if dirty:
            table.update_one(
                {"_id": self.doId},
                {"$set": {"avatar.items": fairy["avatar"]["items"]}}
            )

            self.sendUpdate("setRedraw", [1])

    def setHotspotTriggered(self, hotspotId, hotspotFrame) -> None:
        if not (meadow := self.air.zoneToMeadow.get(self.zoneId)):
            return

        if self.zoneId == 100 and hotspotId in (0, 10): # CBH TTT Reset - HACK - FIX THIS
            for id in range(hotspotId + 1, hotspotId + 10):
                meadow.sendUpdate("setHotspotFrame", [id, 3])
            hotspotFrame = 1

        meadow.sendUpdate("setHotspotFrame", [hotspotId, hotspotFrame])

    def setGold(self, gold: int) -> None:
        self.gold = gold

    def getGold(self) -> int:
        return self.gold

    def d_setGold(self, gold: int) -> None:
        self.sendUpdate("setGold", [gold])

    def b_setGold(self, gold: int) -> None:
        self.setGold(gold)
        self.d_setGold(gold)

    def addGold(self, deltaGold: int) -> None:
        self.b_setGold(deltaGold + self.getGold())

    def takeGold(self, deltaGold: int) -> bool:
        totalGold = self.gold

        if deltaGold > totalGold:
            return False

        self.b_setGold(self.gold - deltaGold)

        return True
