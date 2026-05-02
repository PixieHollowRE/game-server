from game.fairies.minigame.DistributedMeadowGameAI import DistributedMeadowGameAI

class DistributedMatchGameAI(DistributedMeadowGameAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.lastPlayType: int # p1
        self.deckStyle: int # p2
        self.lastFlipOffset: int # p3
        self.cardStates: list[int] # p4
        self.matchCounts: list[int] # p5
        self.lastPlayer: int # p6
        self.whoseTurn: int # p7

    def setGameData(self, lastPlayType, deckStyle, lastFlipOffset, cardStates, matchCounts, lastPlayer, whoseTurn):
        self.lastPlayType = lastPlayType
        self.deckStyle = deckStyle
        self.lastFlipOffset = lastFlipOffset
        self.cardStates = cardStates
        self.matchCounts = matchCounts
        self.lastPlayer = lastPlayer
        self.whoseTurn = whoseTurn

    

