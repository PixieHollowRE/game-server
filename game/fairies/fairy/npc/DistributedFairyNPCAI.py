from ..DistributedFairyBaseAI import DistributedFairyBaseAI

class DistributedFairyNPCAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.famousFairyId: int = 0

    def setFamousFairyId(self, famousFairyId: int) -> None:
        self.famousFairyId = famousFairyId

    def getFamousFairyId(self) -> int:
        return self.famousFairyId
