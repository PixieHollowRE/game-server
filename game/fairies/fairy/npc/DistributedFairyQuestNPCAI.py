from .DistributedFairyNPCAI import DistributedFairyNPCAI

class DistributedFairyQuestNPCAI(DistributedFairyNPCAI):
    def __init__(self, air) -> None:
        DistributedFairyNPCAI.__init__(self, air)

        self.questGiverId: int = 0

    def setQuestGiverId(self, questGiverId: int) -> None:
        self.questGiverId = questGiverId

    def getQuestGiverId(self) -> int:
        return self.questGiverId

    def requestQuestChoices(self, questSeed: int) -> None:
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), "setQuestChoices", [[], []])
