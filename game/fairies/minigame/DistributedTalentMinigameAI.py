from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedTalentMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.gameID: int = 0
        self.totalScore: int = 0

    def setGameID(self, gameID: int) -> None:
        self.gameID = gameID

    def getGameID(self) -> int:
        return self.gameID

    def reportScore(self, score: int) -> None:
        self.totalScore += score
        print("reportScore", score, self.totalScore)

    def endGame(self, unknown: int) -> None:
        print("endGame", unknown)

        avatarId = self.air.getAvatarIdFromSender()

        rewards = []
        self.sendUpdateToAvatarId(avatarId, "setRewards", [rewards])
