from game.fairies.minigame.DistributedMeadowGameAI import DistributedMeadowGameAI, MEADOW_GAME_STATE_GROUPING
import game.fairies.ai.FairiesConstants as fc
from game.fairies.daily.TimeUtils import get_season
from direct.task.TaskManagerGlobal import taskMgr
from datetime import datetime, timezone
import math
import random

CARD_COUNT = 24

# End-of-game reward: a seasonal ingredient in a fixed amount by placement
# (first place 30, second 15). Both players are rewarded — the results panel
# shows the item and amount on every card; the winner's card only differs in
# styling. Season keys must match TimeUtils.SEASON_NAMES.
SEASONAL_REWARD_ITEM = {
    "spring": fc.SPIDER_SILK,      # 8008
    "summer": fc.SUNFLOWER_SEEDS,  # 8010
    "fall":   fc.DANDELION_FLUFF,  # 8013
    "winter": fc.SNOWFLAKES,       # 8016
}

REWARD_FIRST_PLACE = 30
REWARD_SECOND_PLACE = 15

# Seconds to leave the finished game standing before wiping it back to grouping.
# Should outlast the client results panel (panel.config.multiplayerResultsDelay).
RESET_DELAY = 12.0

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
        avatarId = self.air.getAvatarIdFromSender()

        if avatarId not in self.players:
            return

        self.players.remove(avatarId)

        # Broadcast the new roster. The leaving client sees itself drop out of
        # the list and closes its game view (DistributedMeadowGame clears its
        # pendingLeave flag, then onRemovedPlayer -> cancelled()); the remaining
        # client ends the match because the player count falls below minPlayers.
        self.d_setPlayers()

        # With fewer than two players the game can't continue, so return the
        # hotspot to a clean grouping state ready for the next pair of players.
        # Delayed so the remaining client can finish showing its game-over first.
        if len(self.players) < 2:
            self.scheduleReset()

    def scheduleReset(self) -> None:
        taskName = f"MatchGameReset-{self.doId}"
        taskMgr.remove(taskName)
        taskMgr.doMethodLater(RESET_DELAY, self._resetTask, taskName)

    def _resetTask(self, task):
        self.resetGame()
        return task.done

    def resetGame(self) -> None:
        # Empty the table and return to grouping so a fresh pair can start.
        # endMeadowGame on the client doesn't send a leaveRequest, so the server
        # has to clear the roster itself or the slots stay occupied forever.
        self.players = []
        self.card_ids = []
        self.cardStates = [-1 for _ in range(CARD_COUNT)]
        self.lastPlayType = 0
        self.deckStyle = 0
        self.lastFlipOffset = -1
        self.matchCounts = [0, 0]
        self.lastPlayer = 0
        self.whoseTurn = 0

        # Set the state first: with the game back in GROUPING the clients won't
        # treat the empty roster as a mid-game player removal.
        self.setGameState(MEADOW_GAME_STATE_GROUPING, 0)
        self.d_setGameState()
        self.d_setPlayers()

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
                    # Spinner match — consume the pair and spin the power wheel.
                    # handleSpinner removes the pair and sends the update itself.
                    self.handleSpinner(first_card_index, card_index)
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

    def handleSpinner(self, first_index, second_index):
        # The matched spinner pair is consumed and removed from the board.
        # Zeroing their state *before* we compute the "still in play" sets keeps
        # them out of the shuffle/golden logic below, and tells the client to
        # render those two slots as empty.
        self.card_ids[first_index] = 0
        self.card_ids[second_index] = 0
        self.cardStates[first_index] = 0
        self.cardStates[second_index] = 0

        player_index = self.players.index(self.whoseTurn)
        other_index = 1 - player_index
        self.lastPlayer = self.whoseTurn

        # The power spinner wheel on the client has exactly four slots
        # (PowerSpinner.onPick only maps frames 1-4). One slot is either SHUFFLE
        # or GOLDEN depending on whether the current player is dominating, which
        # the client decides with setPlayerDominating(score > otherScore + 2):
        #   dominating -> SHUFFLE (knock the leader back)
        #   underdog   -> GOLDEN  (help the trailing player)
        # We must pick the same one the wheel is showing or the pointer lands on
        # the wrong result. REVEAL and LOSETURN are NOT real wheel slots — the
        # client leaves stuck cards / a desynced turn for those — so never send
        # them.
        dominating = self.matchCounts[player_index] > self.matchCounts[other_index] + 2
        third_slot = (MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE if dominating
                      else MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN)

        result = random.choice([
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS,     # +2 points
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2,  # +3 points
            MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS,   # lose a turn
            third_slot,                                 # shuffle or golden pair
        ])
        self.lastPlayType = result

        if result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS:
            # +2 points
            self.matchCounts[player_index] += 2

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2:
            # +3 points
            self.matchCounts[player_index] += 3

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS:
            # Lose a turn - switch to other player
            self.whoseTurn = self.get_other_player(self.whoseTurn)

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE:
            # Reshuffle every card still in play (kept face down).
            self.reshuffle_in_play()

        elif result == MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN:
            # Turn one still-hidden pair into a golden (3-point) pair, then
            # reshuffle so the client's collapse-and-re-deal genuinely scrambles
            # the board (including the new golden pair) rather than laying it
            # back out unchanged.
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

            self.reshuffle_in_play()

        self.d_setGameData()
        self.lastFlipOffset = -1

    def reshuffle_in_play(self):
        # Pull every card still on the board, shuffle it, and re-lay the board
        # from the top-left so the gaps left by matched/removed pairs all collect
        # at the bottom. The client re-deals from DMG.cards in index order, so
        # packing the live cards into the front slots here is what pushes the
        # empty spaces to the end.
        ids = [self.card_ids[i] for i, s in enumerate(self.cardStates) if s != 0]
        random.shuffle(ids)
        for i in range(CARD_COUNT):
            if i < len(ids):
                self.card_ids[i] = ids[i]
                self.cardStates[i] = -1
            else:
                self.card_ids[i] = 0
                self.cardStates[i] = 0

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
        # Hand out rewards while we still know each player's score, then end the
        # round on the clients. whoseTurn == 0 makes the client run its end-game
        # show, which opens the results panel that reads the rewards we just sent
        # (setRewards must arrive before that setGameData, and it does).
        self.d_setRewards()

        self.whoseTurn = 0
        self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NONE
        self.lastFlipOffset = -1
        self.d_setGameData()

        # Once the results panel has run its course, wipe the hotspot back to a
        # clean grouping state for the next pair of players.
        self.scheduleReset()

    def grantReward(self, avId, itemId, amount):
        avatar = self.air.doId2do.get(avId)
        if avatar is None:
            return
        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, amount, -1):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))

    def d_setRewards(self):
        if len(self.players) < 2:
            return

        itemId = SEASONAL_REWARD_ITEM[get_season(datetime.now(timezone.utc))]

        ranks = []
        for i, avId in enumerate(self.players):
            score = self.matchCounts[i]
            opp_score = self.matchCounts[1 - i]
            rank = 0 if score >= opp_score else 1  # a tie ranks both first

            amount = REWARD_FIRST_PLACE if rank == 0 else REWARD_SECOND_PLACE
            self.grantReward(avId, itemId, amount)

            # Record the finished game on the fairy's profile -- games played,
            # best match count, running total -- the way the talent minigames do,
            # read back by FairiesInventoryRequest (type "games"). Then credit a
            # win on the weekly/seasonal board; Two for Tea is a "wins" board
            # (leaderboards.xml threshold is a win count), so this goes through
            # addToLeaderBoard ($inc) rather than a high score. A tie ranks both
            # first, so both are credited, matching the first-place reward above.
            self.air.mongoInterface.recordStat(avId, "game", self.gameId, score)

            if rank == 0:
                self.air.leaderBoardManager.d_addToLeaderBoard(avId, self.gameId, 1)

            # Rank struct order: (fairyId, score, Reward(itemId, amount), rank)
            ranks.append((avId, score, (itemId, amount), rank))

        # Both players get the full ranking so each results panel shows both
        # cards. setRewards isn't a broadcast field, so send it per-avatar.
        for avId in self.players:
            self.sendUpdateToAvatarId(avId, "setRewards", [ranks])
