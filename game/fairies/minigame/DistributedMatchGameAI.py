from game.fairies.minigame.DistributedMeadowGameAI import DistributedMeadowGameAI
import math
import random

CARD_COUNT = 24

MEADOW_GAME_MEMORY_PLAYTYPE_NONE = 0
MEADOW_GAME_MEMORY_PLAYTYPE_FLIP_FIRST = 2
MEADOW_GAME_MEMORY_PLAYTYPE_NOMATCH = 3
MEADOW_GAME_MEMORY_PLAYTYPE_MATCH = 4
MEADOW_GAME_MEMORY_PLAYTYPE_SHUFFLE = 5

CARD_POINTS = {**{i: 1 for i in range(1, 13)}, **{i: 2 for i in range(21, 26)}, 42: 3}

class DistributedMatchGameAI(DistributedMeadowGameAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.card_ids = []

        self.lastPlayType: int = 0 # p1
        self.deckStyle: int = 0 # p2
        self.lastFlipOffset: int = -1 # p3
        self.cardStates: list[int] = [-1 for _ in range(CARD_COUNT)] # p4
        self.matchCounts: list[int] = [0, 0] # p5 # Player Scores
        self.lastPlayer: int = 0 # p6 
        self.whoseTurn: int = 0 # p7 

    def init_game(self) -> None:
        valid_cards = list(range(1, 13)) + list(range(21, 26)) + [41]
        chosen = random.sample(valid_cards, 12)
        cards = chosen * 2
        random.shuffle(cards)

        # Store the shuffled IDs but initialize everything as face down
        self.card_ids = cards  # remember the actual IDs server-side
        self.cardStates = [-1 for _ in range(CARD_COUNT)] # Reset card states

        # Init the rest of the vars in-case we're in a dirty state.
        self.lastPlayType = 0
        self.deckStyle = 0
        self.lastFlipOffset = -1
        self.matchCounts = [0, 0]
        self.lastPlayer = 0 # lastPlayer is 0 on init

        self.d_setGameData()

    def setGameData(self, lastPlayType, deckStyle, lastFlipOffset, cardStates, matchCounts, lastPlayer, whoseTurn) -> None:
        print("Got Sent Data from client")
        self.lastPlayType = lastPlayType
        self.deckStyle = deckStyle
        self.lastFlipOffset = lastFlipOffset
        self.cardStates = cardStates
        self.matchCounts = matchCounts
        self.lastPlayer = lastPlayer
        self.whoseTurn = whoseTurn

    def d_setGameData(self) -> None:
        print("setGameData sent")
        self.sendUpdate("setGameData", [self.lastPlayType, self.deckStyle, self.lastFlipOffset, self.cardStates, self.matchCounts, self.lastPlayer, self.whoseTurn])

    def joinRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        if self.whoseTurn == 0:
            self.whoseTurn = avatarId
            
        self.d_setGameData()

        super().joinRequest(avatarId)

        if len(self.players) == 2:
            self.init_game()

    def turnRequest(self, unkn, card_index):
        player_id = self.air.getAvatarIdFromSender()

        card_id = self.card_ids[card_index]

        if self.lastFlipOffset == -1:
            # First Flip
            self.lastFlipOffset = card_index
            self.lastPlayer = player_id
            self.cardStates[card_index] = card_id # reveal card
            self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_FLIP_FIRST

            self.d_setGameData()
            self.setGameState(2, 0)
            self.d_setGameState()

        else:
            if card_index == self.lastFlipOffset:
                return
            
            # Second Flip - check for match
            first_card_index = self.lastFlipOffset
            first_card_id = self.cardStates[first_card_index]
            self.cardStates[card_index] = card_id # reveal card
            self.lastFlipOffset = card_index

            if first_card_id == card_id:
                # Match!
                self.cardStates[first_card_index] = first_card_id
                self.cardStates[card_index] = card_id
                # whoseTurn stays the same - player goes again
                self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_MATCH

            else:
                # No Match
                self.cardStates[first_card_index] = first_card_id
                self.cardStates[card_index] = card_id 

                self.whoseTurn = self.get_other_player(self.whoseTurn) # whoseTurn holds doid for the turn player
                self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NOMATCH

            self.lastPlayer = player_id
        
            self.d_setGameData() # send data to client

            if self.lastPlayType == MEADOW_GAME_MEMORY_PLAYTYPE_MATCH:
                self.cardStates[first_card_index] = 0
                self.cardStates[card_index] = 0

                # Check if all cards are matched
                if all(st == 0 for st in self.cardStates):
                    self.whoseTurn = 0  # triggers gameEnd on client
                    self.lastPlayType == MEADOW_GAME_MEMORY_PLAYTYPE_NONE
                    self.d_setGameData()

            else:
                self.cardStates[first_card_index] = -1
                self.cardStates[card_index] = -1

            self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NONE
            self.lastFlipOffset = -1

            

    def get_other_player(self, current_doid):
        print(next(p for p in self.players if p != current_doid))
        return next(p for p in self.players if p != current_doid) # Grab it from DMG
    




