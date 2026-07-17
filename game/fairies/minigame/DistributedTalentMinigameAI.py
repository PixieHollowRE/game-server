from game.fairies.badges import badge_events
from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI
from game.fairies.leaderboard import leaderboard_xml
from game.fairies.minigame.MinigameConstants import MINIGAME_DAILY_CHANCE
from game.fairies.minigame.MinigameRewards import GAMES, calc_rewards

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
    
    def startGame(self, unknown: int):
        pass

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

        self.air.mongoInterface.recordStat(avatarId, "game", self.gameID, totalScore)

        # The helper badges count games played, not points scored, so this fires
        # on finishing regardless of how well it went.
        eventId = badge_events.GAME_TO_EVENT.get(self.gameID)

        if eventId is not None:
            self.air.badgeManager.d_accumulate(avatarId, eventId)

        # The High Score badge, by contrast, is about the points: earned the
        # first time a single run clears the game's threshold. GAMES holds that
        # threshold (from minigames.xml); the badge manager awards it outright.
        game = GAMES.get(self.gameID)
        highScoreBadge = badge_events.GAME_TO_HIGH_SCORE_BADGE.get(self.gameID)

        if game is not None and highScoreBadge is not None and totalScore >= game.badge_threshold:
            self.air.badgeManager.d_giveBadge(avatarId, highScoreBadge)

        # Submit the run to the weekly/seasonal high-score boards. The uberdog
        # drops it if it falls short of the game's leaderboards.xml threshold, so
        # the only gate here is whether the game has a board at all. The three
        # Meadow "wins" games use d_addToLeaderBoard instead and are scored by
        # their own AIs, not here.
        if leaderboard_xml.is_leaderboard_game(self.gameID):
            self.air.leaderBoardManager.d_putToLeaderBoard(avatarId, self.gameID, totalScore)

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
