from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ''
        self.DISLid: int = 0

    def announceGenerate(self):
        self.air.incrementPopulation()

        # Fill in the missing information from the database (i.e. coins)
        # self.air.fillInFairyPlayer(self)

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

    def setAccess(self, access):
        if access == OTPGlobals.AccessFull:
            self.sendUpdateToAvatarId(self.doId, "setAccess", [access])

    def requestDailyGoldTradeCapData(self):
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [0])
        self.sendUpdateToAvatarId(self.doId, "setAmountGoldTradedForToday", [0])

    def requestGetSavedOutfits(self):
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [1])
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [[]])

    def requestAddSavedOutfit(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int):
        # TODO
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [[]])
