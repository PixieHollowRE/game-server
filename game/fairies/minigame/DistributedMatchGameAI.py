from game.fairies.minigame.DistributedMeadowGameAI import DistributedMeadowGameAI

CARD_COUNT = 24

MEADOW_GAME_MEMORY_PLAYTYPE_NONE = 0
MEADOW_GAME_MEMORY_PLAYTYPE_FLIP_FIRST = 2
MEADOW_GAME_MEMORY_PLAYTYPE_NOMATCH = 3
MEADOW_GAME_MEMORY_PLAYTYPE_MATCH = 4
MEADOW_GAME_MEMORY_PLAYTYPE_SHUFFLE = 5

class DistributedMatchGameAI(DistributedMeadowGameAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.lastPlayType: int = MEADOW_GAME_MEMORY_PLAYTYPE_FLIP_FIRST # p1
        self.deckStyle: int = 0 # p2
        self.lastFlipOffset: int = 0 # p3
        self.cardStates: list[int] = [-1 for _ in range(CARD_COUNT)] # p4
        self.matchCounts: list[int] = [] # p5
        self.lastPlayer: int = 0 # p6
        self.whoseTurn: int = 0 # p7

    def setGameData(self, lastPlayType, deckStyle, lastFlipOffset, cardStates, matchCounts, lastPlayer, whoseTurn) -> None:
        self.lastPlayType = lastPlayType
        self.deckStyle = deckStyle
        self.lastFlipOffset = lastFlipOffset
        self.cardStates = cardStates
        self.matchCounts = matchCounts
        self.lastPlayer = lastPlayer
        self.whoseTurn = whoseTurn

    def d_setGameData(self) -> None:
        self.sendUpdate("setGameData", [self.lastPlayType, self.deckStyle, self.lastFlipOffset, self.cardStates, self.matchCounts, self.lastPlayer, self.whoseTurn])

    def joinRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        if self.whoseTurn == 0:
            self.whoseTurn = avatarId

        self.d_setGameData()

        super().joinRequest(avatarId)
