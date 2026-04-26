from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.minigame.MinigameRewards import calc_rewards

class DistributedTalentMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.gameID: int = 0
        self.totalScore: int = 0
        self.rewards = []

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

        self.rewards = calc_rewards(self.gameID, self.totalScore)
        self.sendUpdateToAvatarId(avatarId, "setRewards", [self.rewards])
        self.totalScore = 0

    def chooseReward(self, rewardId):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for chooseReward: {avId}")
            return
        
        chosenReward = self.rewards[rewardId]

        itemID, itemCount = chosenReward.asTuple()
        itemSlot = -1

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemID, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))