from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.minigame.MinigameConstants import MINIGAME_DAILY_CHANCE
from game.fairies.minigame.MinigameRewards import calc_rewards
from game.fairies.stats.GameStatsService import apply_minigame_result

class DistributedTalentMinigameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.gameID: int = 0
        self._scores: dict[int, int] = {}
        self._pendingRewards: dict[int, list] = {}  # avId -> rewards list

    def setGameID(self, gameID: int) -> None:
        self.gameID = gameID

    def getGameID(self) -> int:
        return self.gameID

    def startGame(self, _unknown: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        self._scores.pop(avId, None)
        self._pendingRewards.pop(avId, None)

    def reportScore(self, score: int) -> None:
        if self.gameID == MINIGAME_DAILY_CHANCE:
            return
        avId = self.air.getAvatarIdFromSender()
        self._scores[avId] = self._scores.get(avId, 0) + score

    def endGame(self, unknown: int) -> None:
        if self.gameID == MINIGAME_DAILY_CHANCE:
            # Daily Spin uses DistributedFairyPlayer.requestDailyChance, not minigame rewards.
            return

        print("endGame", unknown)

        avatarId = self.air.getAvatarIdFromSender()
        totalScore = self._scores.pop(avatarId, 0)

        badge_manager = getattr(self.air, "badgeManager", None)
        inventory_manager = getattr(self.air, "inventoryManager", None)
        if badge_manager is not None and inventory_manager is not None:
            apply_minigame_result(
                badge_manager,
                inventory_manager,
                avatarId,
                self.gameID,
                totalScore,
            )

        rewards = calc_rewards(self.gameID, totalScore)
        self._pendingRewards[avatarId] = rewards
        self.sendUpdateToAvatarId(avatarId, "setRewards", [rewards])

    def chooseReward(self, rewardId: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"chooseReward: no avatar on AI for avId={avId}")
            return

        rewards = self._pendingRewards.get(avId)

        if not rewards:
            self.notify.warning(f"chooseReward: no pending rewards for avId={avId}")
            return

        if not isinstance(rewardId, int) or not (0 <= rewardId < len(rewards)):
            self.notify.warning(
                f"chooseReward: invalid rewardId={rewardId} "
                f"(rewards length={len(rewards)}, avId={avId})"
            )
            return

        chosenReward = rewards[rewardId]
        # Clear immediately so the client can't call chooseReward twice
        del self._pendingRewards[avId]

        itemID, itemCount = chosenReward.asTuple()
        itemSlot = -1

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemID, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))
