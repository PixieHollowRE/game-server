from direct.distributed.DistributedObjectAI import DistributedObjectAI
from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedTalentMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air):
        DistributedInstanceBaseAI.__init__(self, air)
        self.gameID: int = 0
        self.totalScore: int = 0

    def setGameID(self, gameID):
        self.gameID = gameID

    def getGameID(self):
        return self.gameID

    def reportScore(self, score):
        self.totalScore += score
        print("reportScore", score, self.totalScore)

    def endGame(self, unknown):
        print("endGame", unknown)

        avatarId = self.air.getAvatarIdFromSender()

        rewards = []
        self.sendUpdateToAvatarId(avatarId, "setRewards", [rewards])
