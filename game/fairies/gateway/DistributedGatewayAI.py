from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedGatewayAI(DistributedObjectAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.gatewayName: str = ""
        self.gatewayPosition: tuple[int, int] = (0, 0)
        self.positionByName: str = ""
        self.targetLocationName: str = ""
        self.targetZoneID: int = 0
        self.openState: str = "open"
        self.velvetRope: int = 0
        self.rewardList: list[int] = []

    def setName(self, gatewayName: str) -> None:
        self.gatewayName = gatewayName

    def getName(self) -> str:
        return self.gatewayName

    def setPosition(self, x: int, y: int) -> None:
        self.gatewayPosition = (x, y)

    def getPosition(self) -> tuple[int, int]:
        return self.gatewayPosition

    def setPositionByName(self, positionByName: str) -> None:
        self.positionByName = positionByName

    def getPositionByName(self) -> str:
        return self.positionByName

    def setTargetLocationName(self, targetLocationName: str) -> None:
        self.targetLocationName = targetLocationName

    def getTargetLocationName(self) -> str:
        return self.targetLocationName

    def setTargetZoneID(self, targetZoneID: int) -> None:
        self.targetZoneID = targetZoneID

    def getTargetZoneID(self) -> int:
        return self.targetZoneID

    def setOpenState(self, openState: str) -> None:
        self.openState = openState

    def getOpenState(self) -> str:
        return self.openState

    def setVelvetRope(self, velvetRope: int) -> None:
        self.velvetRope = velvetRope

    def getVelvetRope(self) -> int:
        return self.velvetRope

    def setRewardList(self, rewardList: list[int]) -> None:
        self.rewardList = rewardList

    def getRewardList(self) -> list[int]:
        return self.rewardList
