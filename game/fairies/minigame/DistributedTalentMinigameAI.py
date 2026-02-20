from direct.distributed.DistributedObjectAI import DistributedObjectAI
from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedTalentMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air):
        DistributedInstanceBaseAI.__init__(self, air)
        self.gameID = 0

    def setGameID(self, gameID):
        self.gameID = gameID

    def getGameID(self):
        return self.gameID

    def reportScore(self, score):
        print("reportScore", score)

    def endGame(self, finalScore):
        print("endGame", finalScore)

        avatarId = self.air.getAvatarIdFromSender()

        rewards = []
        self.sendUpdateToAvatarId(avatarId, "setRewards", [rewards])
