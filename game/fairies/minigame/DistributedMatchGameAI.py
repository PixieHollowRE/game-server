from game.fairies.minigame.DistributedMeadowGameAI import DistributedMeadowGameAI
import math
import random

CARD_COUNT = 24

MEADOW_GAME_MEMORY_PLAYTYPE_NONE = 0
MEADOW_GAME_MEMORY_PLAYTYPE_FLIP_FIRST = 2
MEADOW_GAME_MEMORY_PLAYTYPE_NOMATCH = 3
MEADOW_GAME_MEMORY_PLAYTYPE_MATCH = 4
MEADOW_GAME_MEMORY_PLAYTYPE_SHUFFLE = 5

MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS = 6
MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_REVEAL = 7
MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE = 8
MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS = 9
MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_LOSETURN = 11
MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2 = 12
MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN = 13

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

        self.setGameState(2, 0)
        self.d_setGameState()

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
        print("setGameData sent", self.lastPlayType, self.deckStyle, self.lastFlipOffset, self.cardStates, self.matchCounts, self.lastPlayer, self.whoseTurn)
        self.sendUpdate("setGameData", [self.lastPlayType, self.deckStyle, self.lastFlipOffset, self.cardStates, self.matchCounts, self.lastPlayer, self.whoseTurn])

    def joinRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        if self.whoseTurn == 0:
            self.whoseTurn = avatarId

        self.d_setGameData()

        super().joinRequest(avatarId)

        if len(self.players) == 2:
            self.init_game()

    def leaveRequest(self) -> None:
        pass # TODO

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

        else:

            if card_index == self.lastFlipOffset:
                return

            # Second Flip - check for match
            first_card_index = self.lastFlipOffset
            first_card_id = self.card_ids[first_card_index]
            self.cardStates[card_index] = card_id  # reveal second card
            self.lastFlipOffset = card_index

            if first_card_id == card_id:
                # Only award points for normal cards, not spinner card
                if first_card_id != 41:
                    points = CARD_POINTS.get(first_card_id, 1)
                    player_index = self.players.index(player_id)
                    self.matchCounts[player_index] += points
                else:
                    # Spinner match
                    self.handleSpinner()
                    self.cardStates[first_card_index] = 0
                    self.cardStates[card_index] = 0
                    return

                if first_card_id == 11 or first_card_id == 12:
                    # Pumpkin pie or smores
                    self.handlePouchItems(first_card_id)

                other_cards = [st for i, st in enumerate(self.cardStates)
                            if i != first_card_index and i != card_index]
                would_be_last = all(st == 0 for st in other_cards)
                self.lastPlayer = player_id

                if would_be_last:
                    # Last match - skip animation, go straight to end
                    self.cardStates[first_card_index] = 0
                    self.cardStates[card_index] = 0
                    self.handleEndGame()
                    return
                else:
                    # Normal match - cards still visible for animation
                    self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_MATCH
                    self.d_setGameData()  # client animates with cards still showing

                    self.cardStates[first_card_index] = 0
                    self.cardStates[card_index] = 0

            else:
                self.whoseTurn = self.get_other_player(self.whoseTurn)
                self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NOMATCH
                self.lastPlayer = player_id
                self.d_setGameData()

                self.cardStates[first_card_index] = -1
                self.cardStates[card_index] = -1

            self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NONE
            self.lastFlipOffset = -1

    def get_other_player(self, current_doid):
        print(next(p for p in self.players if p != current_doid))
        return next(p for p in self.players if p != current_doid) # Grab it from DMG

    def handleSpinner(self):

        player_index = self.players.index(self.whoseTurn)
        self.lastPlayer = self.whoseTurn

        # Pick a random spinner result
        spinner_outcomes = [
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS,
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_REVEAL,
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE,
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS,
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_LOSETURN,
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2,
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN
        ]
        result = random.choice(spinner_outcomes)
        self.lastPlayType = result

        if result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS:
            # +2 points
            self.matchCounts[player_index] += 2

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_REVEAL:
            # Client handles this entirely - briefly reveals all cards
            pass

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE:
            # Reshuffle all unmatched cards
            unmatched_indices = [i for i, s in enumerate(self.cardStates) if s != 0]
            unmatched_ids = [self.card_ids[i] for i in unmatched_indices]
            random.shuffle(unmatched_ids)
            for i, idx in enumerate(unmatched_indices):
                self.card_ids[idx] = unmatched_ids[i]
                self.cardStates[idx] = -1

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS:
            # Lose a turn - switch to other player
            self.whoseTurn = self.get_other_player(self.whoseTurn)

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_LOSETURN:
            # Lose a turn - switch to other player
            self.whoseTurn = self.get_other_player(self.whoseTurn)

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2:
            # +3 points
            self.matchCounts[player_index] += 3

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN:
            # Find all unmatched pairs still on the board
            unmatched_indices = [i for i, s in enumerate(self.cardStates) if s != 0]

            # Group by card_id to find pairs
            pairs = {}
            for idx in unmatched_indices:
                card = self.card_ids[idx]
                if card not in pairs:
                    pairs[card] = []
                pairs[card].append(idx)

            # Pick a random pair and replace with golden pair
            valid_pairs = [indices for indices in pairs.values() if len(indices) == 2]
            if valid_pairs:
                chosen = random.choice(valid_pairs)
                for idx in chosen:
                    self.card_ids[idx] = 42
                    self.cardStates[idx] = -1  # keep face down

        self.d_setGameData()
        self.lastFlipOffset = -1

    def handlePouchItems(self, card):
        avId = self.whoseTurn
        avatar = self.air.doId2do.get(avId)

        itemCount = 1
        itemSlot = -1

        if card == 11:
            itemID = 22512
        else:
            itemID = 22511

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemID, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))

    def handleEndGame(self):
        # Clean up board state
        self.whoseTurn = 0
        self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NONE
        self.lastFlipOffset = -1
        self.d_setGameData()

        # TODO: Handle leaving, rewards, and resetting game state
