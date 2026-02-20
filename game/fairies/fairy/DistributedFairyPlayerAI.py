from .DistributedFairyBaseAI import DistributedFairyBaseAI

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air):
        DistributedFairyBaseAI.__init__(self, air)
        self.DISLname = ''
        self.DISLid = 0

    def setDISLname(self, DISLname: str):
        self.DISLname = DISLname
        print(self.DISLname)

    def getDISLname(self) -> str:
        return self.DISLname

    def setDISLid(self, DISLid: int) -> int:
        self.DISLid = DISLid
        self.air.sendFriendManagerAccountOnline(self.DISLid)

    def getDISLid(self) -> int:
        return self.DISLid

    def announceGenerate(self):
        self.air.incrementPopulation()

        # Fill in the missing information from the database (i.e. coins)
        self.air.fillInFairyPlayer(self)

    def delete(self):
        # TODO: Set a post-remove message in case of an AI crash.
        self.air.sendFriendManagerAccountOffline(self.DISLid)

        self.air.decrementPopulation()

        DistributedFairyBaseAI.delete(self)
