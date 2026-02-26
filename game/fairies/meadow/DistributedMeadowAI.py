from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedMeadowAI(DistributedObjectAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.assetURL: str = ""
        self.crowdBarriers: int = 0

    def setAssetURL(self, assetURL: int) -> None:
        self.assetURL = assetURL

    def getAssetURL(self) -> str:
        return self.assetURL

    def setCrowdBarriers(self, crowdBarriers: int) -> None:
        self.crowdBarriers = crowdBarriers

    def getCrowdBarriers(self) -> int:
        return self.crowdBarriers
