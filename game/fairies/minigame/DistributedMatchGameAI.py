from game.fairies.minigame.DistributedMeadowGameAI import (
    DistributedMeadowGameAI,
    MEADOW_GAME_JOIN_RESPONSE_ACCEPTED,
    MEADOW_GAME_STATE_GROUPING,
    MEADOW_GAME_STATE_PLAY,
    MEADOW_GAME_STATE_RESET,
    MEADOW_GAME_STATE_REWARD,
)
import game.fairies.ai.FairiesConstants as fc
from game.fairies.daily.TimeUtils import get_season
from direct.task.TaskManagerGlobal import taskMgr
from datetime import datetime, timezone
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
RESET_DELAY = 5.0

# A finished game resets on a longer delay than a broken-up one. Every natural
# finish is deferred on the client until the show that ended it settles (the
# match tween, or the wheel animation, plus any pair popup -- several seconds),
# and resetGame's empty setPlayers must not reach the client before its end-game
# show is built: an empty roster would collapse it to the "below minimum players"
# screen. This outlasts the animation plus a results-viewing window.
DEFERRED_END_RESET_DELAY = 12.0

MEADOW_GAME_MEMORY_REQUEST_NO_MOVE = 0
MEADOW_GAME_MEMORY_REQUEST_FLIP = 1

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

        # Set by the `match-spin-result` magic word and consumed by the next
        # spinner match instead of the random draw. None the rest of the time,
        # which is every game nobody is debugging.
        self.forcedSpinResult: int | None = None

    def init_game(self) -> None:
        # A pending reset belongs to the *previous* game. If a new pair sat down
        # inside RESET_DELAY, letting it fire would wipe the board out from under
        # them mid-play and leave card_ids empty for turnRequest.
        self.cancelReset()

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
        # A forced spin belongs to the game it was asked for; a new pair sitting
        # down must not inherit it.
        self.forcedSpinResult = None

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

    def d_revealBoard(self) -> None:
        """
        Show everyone at the table what every face-down card is.

        Server state is left exactly as it was and only the datagram is doctored,
        so the game stays playable: the next real move sends the true board and
        puts the cards back down. Doing it the other way -- actually setting
        cardStates -- would make validateTurn refuse every remaining flip, since
        a card that isn't -1 is one this turn has already turned over.
        """
        if not self.card_ids:
            return

        revealed = [
            cardId if state == -1 else state
            for state, cardId in zip(self.cardStates, self.card_ids)
        ]

        self.sendUpdate("setGameData", [
            MEADOW_GAME_MEMORY_PLAYTYPE_NONE,
            self.deckStyle,
            self.lastFlipOffset,
            revealed,
            self.matchCounts,
            self.lastPlayer,
            self.whoseTurn,
        ])

    def joinRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        responseCode = super().joinRequest(avatarId)

        if responseCode != MEADOW_GAME_JOIN_RESPONSE_ACCEPTED:
            return

        # First accepted player takes the first turn.
        if self.whoseTurn == 0:
            self.whoseTurn = avatarId

        self.d_setGameData()

        # The pair just filled the table — deal a fresh game.
        if len(self.players) == 2:
            self.init_game()

    def leaveRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        if avatarId not in self.players:
            return

        self.players.remove(avatarId)

        # A mid-game departure is a forfeit: nobody is rewarded, and the table
        # comes down immediately instead of sitting live for RESET_DELAY. That
        # delay only exists to outlast the end-of-game results panel, and a
        # forfeit shows no panel; leaving the board standing was also what let
        # the lone remaining player keep sending turns (the get_other_player
        # crash)

        # whoseTurn == 0 means the round already ended naturally and results are
        # showing, so that case falls through to the normal delayed reset rather
        # than yanking the results panel away from the other player.
        if self.state == MEADOW_GAME_STATE_PLAY and self.whoseTurn != 0:
            self.cancelReset()

            # Broadcast the empty roster *while still in PLAY*: the remaining
            # client's onRemovedPlayer only fires in that state, and it cancels
            # the board (-> endMeadowGame) when it sees the local player gone. A
            # [remaining]-only roster wouldn't remove them, leaving a live-looking
            # board with no opponent.
            self.players = []
            self.d_setPlayers()

            # Now wipe back to a clean grouping state for the next pair. No
            # d_setRewards is sent on this path, so neither player is rewarded.
            self.resetGame()
            return

        # Broadcast the new roster. The leaving client sees itself drop out of
        # the list and closes its game view (DistributedMeadowGame clears its
        # pendingLeave flag, then onRemovedPlayer -> cancelled()).
        self.d_setPlayers()

        # With fewer than two players the game can't continue, so return the
        # hotspot to a clean grouping state ready for the next pair of players.
        # Delayed so the remaining client can finish showing its game-over first.
        if len(self.players) < 2:
            self.scheduleReset()

    @property
    def resetTaskName(self) -> str:
        return f"MatchGameReset-{self.doId}"

    def scheduleReset(self, delay=RESET_DELAY) -> None:
        taskMgr.remove(self.resetTaskName)
        taskMgr.doMethodLater(delay, self._resetTask, self.resetTaskName)

    def cancelReset(self) -> None:
        taskMgr.remove(self.resetTaskName)

    def _resetTask(self, task):
        self.resetGame()
        return task.done

    def delete(self) -> None:
        self.cancelReset()
        super().delete()

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
        self.forcedSpinResult = None

        self.setGameState(MEADOW_GAME_STATE_RESET, 0)
        self.d_setGameState()

        # Then return to GROUPING so the hotspot is joinable again. RESET is not a
        # stable joinable state (the launcher treats it as "clear and close"), so
        # it must be followed by GROUPING. The two are distinct, so the client's
        # setGameState dedup won't swallow either. Ordering GROUPING before the
        # empty setPlayers keeps clients from reading the empty roster as a
        # mid-game player removal.
        self.setGameState(MEADOW_GAME_STATE_GROUPING, 0)
        self.d_setGameState()
        self.d_setPlayers()

    def turnRequest(self, playType, card_index):
        player_id = self.air.getAvatarIdFromSender()

        if playType == MEADOW_GAME_MEMORY_REQUEST_NO_MOVE:
            self.handleNoMove(player_id)
            return

        if not self.validateTurn(player_id, card_index):
            return

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

                # Every match animates, the last one included.
                self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_MATCH
                self.d_setGameData()  # client animates with cards still showing

                self.cardStates[first_card_index] = 0
                self.cardStates[card_index] = 0

                if would_be_last:
                    # That pair emptied the board. End the round on top of the
                    # match show instead of in place of it: the client repaints
                    # the score panel only when a show finishes, so cutting the
                    # last one short is what left the winning points off the
                    # scoreboard the results were then drawn over.
                    self.handleEndGame()
                    return

            else:
                self.whoseTurn = self.get_other_player(self.whoseTurn)
                self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NOMATCH
                self.lastPlayer = player_id
                self.d_setGameData()

                self.cardStates[first_card_index] = -1
                self.cardStates[card_index] = -1

            self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NONE
            self.lastFlipOffset = -1

    def handleNoMove(self, player_id) -> None:
        # The active player's turn timer ran out and their client submitted a
        # no-move. Nothing is revealed, nothing is scored, the turn simply passes.
        #
        # This is handled differently from a flip: the client takes itself out of play
        # as soon as the timer expires, and then waits for a setGameData to drive the
        # next turn.
        if not self.validatePlayer(player_id):
            return

        if self.lastFlipOffset != -1 and self.cardStates[self.lastFlipOffset] != 0:
            self.cardStates[self.lastFlipOffset] = -1

        self.lastFlipOffset = -1

        self.lastPlayType = MEADOW_GAME_MEMORY_PLAYTYPE_NONE
        self.lastPlayer = player_id
        self.whoseTurn = self.get_other_player(self.whoseTurn)

        self.d_setGameData()

    def validatePlayer(self, player_id) -> bool:
        # A client whose board has outlived the server's game
        # it left, the hotspot reset, the round ended, etc. will
        # still happily send flips at an empty table. yay
        if self.state != MEADOW_GAME_STATE_PLAY or len(self.card_ids) != CARD_COUNT:
            self.notify.warning(
                f"turnRequest from {player_id} with no game in play "
                f"(state={self.state}, cards={len(self.card_ids)})")
            return False

        # A player can leave mid-game: the roster shrinks to one immediately but
        # the board isn't wiped until scheduleReset() fires RESET_DELAY later, so
        # state/card_ids still look live. Processing a turn now would leave
        # get_other_player with nobody to switch to (StopIteration -> reader loop
        # crash). Nothing should proceed once we're below two players.
        if len(self.players) != 2:
            self.notify.warning(
                f"turnRequest from {player_id} with {len(self.players)} player(s)")
            return False

        # Log errors instead of throwing a tantrum - we'll see if this fixes the issue.
        if player_id not in self.players:
            self.notify.warning(f"turnRequest from non-player {player_id}")
            return False

        if player_id != self.whoseTurn:
            self.notify.warning(f"turnRequest from {player_id} out of turn")
            return False

        return True

    def validateTurn(self, player_id, card_index) -> bool:
        if not self.validatePlayer(player_id):
            return False

        if not 0 <= card_index < CARD_COUNT:
            self.notify.warning(f"turnRequest from {player_id} for card {card_index}")
            return False

        # -1 is face down. Anything else is already revealed by this turn's first
        # flip, or 0 for a slot whose pair has been matched away.
        if self.cardStates[card_index] != -1:
            return False

        return True

    def get_other_player(self, current_doid):
        # Defensive default: never raise StopIteration into the reader loop if
        # the roster has already dropped below two players. validateTurn should
        # keep us from getting here, but a bad StopIteration crashes the whole
        # district, so fall back to the current player rather than blow up.
        return next((p for p in self.players if p != current_doid), current_doid)

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

        # Did consuming this spinner pair clear the last cards off the board?
        # (The pair's states were zeroed above, so an empty board now means this
        # was the final pair.) If so the game is over, and we must decide that
        # *before* picking a wheel result.
        game_over = all(state == 0 for state in self.cardStates)

        if game_over:
            result = random.choice([
                MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS,     # +2 points
                MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2,  # +3 points
            ])
        else:
            # The power spinner wheel on the client has exactly four slots
            # (PowerSpinner.onPick only maps frames 1-4). One slot is either
            # SHUFFLE or GOLDEN depending on whether the current player is
            # dominating, which the client decides with
            # setPlayerDominating(score > otherScore + 2):
            #   dominating -> SHUFFLE (knock the leader back)
            #   underdog   -> GOLDEN  (help the trailing player)
            # We must pick the same one the wheel is showing or the pointer lands
            # on the wrong result. REVEAL and LOSETURN are NOT real wheel slots —
            # the client leaves stuck cards / a desynced turn for those — so never
            # send them.
            dominating = self.matchCounts[player_index] > self.matchCounts[other_index] + 2
            third_slot = (MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE if dominating
                          else MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN)

            result = random.choice([
                MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS,     # +2 points
                MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2,  # +3 points
                MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS,   # lose a turn
                third_slot,                                 # shuffle or golden pair
            ])

        # A GM asked for a particular wheel result. It overrides the draw once
        # and then clears, so the next spinner match is random again. The end-of
        # -game case above deliberately still wins: with the board empty there is
        # no shuffle or golden pair to award and no turn left to lose.
        if self.forcedSpinResult is not None and not game_over:
            result = self.forcedSpinResult
            self.forcedSpinResult = None

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

        if game_over:
            self.handleEndGame()

    def reshuffle_in_play(self):
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
        """
        End the round, on top of whichever show cleared the board -- the final
        match, or the wheel from a final spinner pair.

        The caller has already sent that show's setGameData with a non-NONE
        lastPlayType. All that's left is to hand out rewards (while we still know
        each player's score) and switch to REWARD, which the client's
        onGameStateUpdatedCalled turns into its deferred _endGameNow flag: the
        animation plays out, turnDisplayAndWait paints the final scores, and only
        then does gameEnd() open the results panel.

        Not whoseTurn == 0. That ends the game the instant the client reads it,
        because turnStart checks it *before* dispatching on lastPlayType, so the
        show never runs -- and the score panel is only repainted at the end of a
        show. The winner banner reads matchCounts straight off the object and was
        always right, so the game looked like it was awarded to the player with
        fewer points: their winning match had never been drawn.

        Rewards must reach the client before the results panel opens; since the
        panel only opens once the animation finishes, sending them now is well
        ahead of it.
        """
        self.d_setRewards()

        self.lastFlipOffset = -1

        self.setGameState(MEADOW_GAME_STATE_REWARD, 0)
        self.d_setGameState()

        # Once the results panel has run its course, wipe the hotspot back to a
        # clean grouping state for the next pair of players.
        self.scheduleReset(DEFERRED_END_RESET_DELAY)

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
            self.creditGamePlayed(avId)

            #TODO: Disable leaderboard for now - Re-enable it later.

            # Record the finished game on the fairy's profile, read back by
            # FairiesInventoryRequest (type "games"). For the multiplayer meadow
            # games the client reads the stat's `total` as the running WINS count
            # (not a score total), so we feed recordStat the win result (1 on a
            # win, 0 on a loss) instead of the match score. That keeps `count`
            # as games played and makes `total` accumulate wins, which is what the
            # client displays. A tie ranks both first, so both are credited,
            # matching the first-place reward above.
            # won = 1 if rank == 0 else 0
            # self.air.mongoInterface.recordStat(avId, "game", self.gameId, won)

            #if rank == 0:
               # self.air.leaderBoardManager.d_addToLeaderBoard(avId, self.gameId, 1)

            # Rank struct order: (fairyId, score, Reward(itemId, amount), rank)
            ranks.append((avId, score, (itemId, amount), rank))

        for avId in self.players:
            self.sendUpdateToAvatarId(avId, "setRewards", [ranks])
