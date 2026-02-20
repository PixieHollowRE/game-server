from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedGatewayAI(DistributedObjectAI):
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.gatewayName: str = ""
        self.gatewayPosition: tuple = 0, 0
        self.targetLocationName: str = ""
        self.targetZoneID: int = 0
        self.rewardList: list[int] = []

    def setName(self, gatewayName):
        self.gatewayName = gatewayName

    def getName(self):
        return self.gatewayName

    def setPosition(self, x, y):
        self.gatewayPosition = (x, y)

    def getPosition(self):
        return self.gatewayPosition

    def setTargetLocationName(self, targetLocationName):
        self.targetLocationName = targetLocationName

    def getTargetLocationName(self):
        return self.targetLocationName

    def setTargetZoneID(self, targetZoneID):
        self.targetZoneID = targetZoneID

    def getTargetZoneID(self):
        return self.targetZoneID

    # I got lazy filling out setters/getters
    def getPositionByName(self):
        return ""

    def getOpenState(self):
        return "open"

    def getVelvetRope(self):
        return 0

    def setRewardList(self, rewardList):
        self.rewardList = rewardList

    def getRewardList(self):
        return self.rewardList
