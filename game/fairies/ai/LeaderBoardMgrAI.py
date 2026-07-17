from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

# addToLeaderBoard takes an int16 amount in fairy.dc.
MAX_AMOUNT = 32767


class LeaderBoardMgrAI(DistributedObjectGlobalAI):
    """
    The district AI's handle on the leaderboard uberdog.

    Districts hold no board state; a minigame AI reports a finished run through
    one of these and the uberdog (LeaderBoardMgrUD) decides whether it places.
    The threshold check lives on the uberdog, so callers submit unconditionally.
    """

    def __init__(self, air) -> None:
        super().__init__(air)

    def d_putToLeaderBoard(self, avatarId: int, gameId: int, score: int) -> None:
        """Report a finished high-score run (kept if it beats the fairy's best)."""
        self.sendUpdate("putToLeaderBoard", [avatarId, gameId, score])

    def d_addToLeaderBoard(self, avatarId: int, gameId: int, amount: int = 1) -> None:
        """Report wins for one of the three Meadow games' running win-count boards."""
        if amount <= 0:
            return

        self.sendUpdate("addToLeaderBoard", [avatarId, gameId, min(amount, MAX_AMOUNT)])
