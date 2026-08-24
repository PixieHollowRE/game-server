from game.fairies.minigame.DistributedMeadowGameAI import (
    DistributedMeadowGameAI,
    MEADOW_GAME_JOIN_RESPONSE_ACCEPTED,
    MEADOW_GAME_JOIN_RESPONSE_GAMEON_FULL,
    MEADOW_GAME_STATE_GROUPING,
    MEADOW_GAME_STATE_INIT,
    MEADOW_GAME_STATE_PLAY,
    MEADOW_GAME_STATE_RESET,
    MEADOW_GAME_STATE_REWARD,
)
from game.fairies.minigame.CrazyEightsConstants import (
    DIRECTION_LEFT,
    DIRECTION_RIGHT,
    LOBBY_COUNTDOWN,
    MAX_PLAYERS,
    MIN_PLAYERS,
    PLAYTYPE_DISCARD,
    PLAYTYPE_DRAW,
    PLAYTYPE_NONE,
    PLAYTYPE_PLAYER_REMOVED,
    PLAYTYPE_SHOW_SPECIAL,
    POWER_SLOTS,
    POWER_SLOT_TO_ACTION,
    STARTING_HAND_SIZE,
    SUIT_CHANGE,
    SUIT_ORANGE,
    SUIT_POWER,
    SUITS,
    TURN_RESPONSE_INVALID_CARD,
    TURN_RESPONSE_INVALID_MOVE,
    TURN_RESPONSE_INVALID_PLAYER,
    TURN_RESPONSE_VALID,
    VALUE_ALL_CHANGE_SUIT,
    VALUE_ALL_DRAW_ONE,
    VALUE_ALL_PASS_ONE,
    VALUE_DRAW_TWO,
    VALUE_REVERSE,
    VALUE_SELF_GO_AGAIN,
    VALUE_SKIP,
    VALUE_UNDECLARED,
    build_deck,
    card_suit,
    card_value,
    is_colour,
    is_playable,
    make_card,
)
import game.fairies.ai.FairiesConstants as fc
from game.fairies.daily.TimeUtils import get_season
from direct.task.TaskManagerGlobal import taskMgr
from datetime import datetime, timezone
import random

# Two extra game-over states the client understands but Two For Tea never uses.
# Controller.gameEndPopUp picks its copy straight off the game state:
#   8 -> "A player has left the game. There are not enough players to continue."
#   9 -> "No more cards to play."
# Neither runs the winner show (setUpEndGameShow only does that for state 7), so
# neither pays out.
MEADOW_GAME_STATE_REWARD_NO_PLAYER = 8
MEADOW_GAME_STATE_REWARD_NO_CARD = 9

# End-of-game reward, mirroring DistributedMatchGameAI: a seasonal ingredient whose
# amount depends on placement. Season keys must match TimeUtils.SEASON_NAMES.
SEASONAL_REWARD_ITEM = {
    "spring": fc.SPIDER_SILK,      # 8008
    "summer": fc.SUNFLOWER_SEEDS,  # 8010
    "fall":   fc.DANDELION_FLUFF,  # 8013
    "winter": fc.SNOWFLAKES,       # 8016
}

# Payout per finishing place (best first), keyed by how many players saw the round
# out -- the table can finish with fewer than it started if somebody walks off and
# the rest are still above minPlayers.
#
# First and last always pay 30 and 15, the two amounts this table has always paid,
# so a two-player game is unchanged; a fuller table spreads the middle places
# evenly between them. Only 2-4 are reachable (MIN_PLAYERS/MAX_PLAYERS), and
# d_setRewards bails below minPlayers before it gets here.
REWARD_BY_PLACE: dict[int, tuple[int, ...]] = {
    2: (30, 15),
    3: (30, 22, 15),
    4: (30, 25, 20, 15),
}

# Seconds to leave the finished table standing before wiping it back to grouping.
# Long enough to outlast the client's end-game show and results panel.
RESET_DELAY = 8.0

# A wild card parks the table until its owner picks a colour (or the spinner
# resolves). If that client never answers -- closed tab, dropped connection -- the
# table would sit wedged forever, so we force a resolution.
#
# The client's own deadlines are changeSuitTime=15s for the picker and
# powerSpinnerShowDelay + powerSpinnerHoldDelay = 3+3s before it auto-sends the spun
# action, all from meadowgameCrazyEight.xml. This has to outlast the slowest of those
# plus round-trip, but not by so much that a table sits dead.
SPECIAL_RESOLVE_TIMEOUT = 25.0

# Drawing a card ends your turn. Crazy Eights is played both ways -- "draw until you
# can play" is the other common rule -- but the client's prompt pairs "Play a card."
# with "Draw a card." as alternatives, which reads as a single draw closing the turn.
# Flip this if that turns out to feel wrong in play; nothing else depends on it.
DRAW_ENDS_TURN = True


class DistributedCrazyEightsAI(DistributedMeadowGameAI):
    """
    Crazy Cakes (gameId 13070) -- the Tearoom's Crazy Eights table, 2-4 players.

    The server owns the deck and every hand. Only *counts* are broadcast, in
    setGameData's handSizes[]; the actual cards go to one player at a time via a
    targeted setPlayerData. That split is the whole reason this class is
    authoritative in a way DistributedMatchGameAI doesn't need to be -- Two For
    Tea's board is face-up public state, a Crazy Cakes hand is not.

    handSizes[] is indexed by the client's DMG_Id, which is a player's position in
    the setPlayers roster (Model.updateGameData reads
    getHandSize(players[id].DMG_Id)). So handSizes[i] must describe self.players[i],
    and the roster order must stay stable for the life of a round.
    """

    # We hold a lobby countdown between minPlayers and maxPlayers, so the base must not
    # deal the moment the fourth seat fills -- startCountdown/_countdownTask own the
    # INIT -> PLAY transition. See DistributedMeadowGameAI.autoStartWhenFull.
    autoStartWhenFull = False

    def __init__(self, air) -> None:
        super().__init__(air)

        self.minPlayers = MIN_PLAYERS
        self.maxPlayers = MAX_PLAYERS

        # globalClock time the lobby countdown expires, or None when it isn't running.
        # Kept so a latecomer can be told how much of the countdown is actually left --
        # the launcher starts its clock from whatever timeOutSecs it last saw, so
        # handing a joiner the full LOBBY_COUNTDOWN would show them a countdown that
        # outlives the deal.
        self.countdownEnds: float | None = None

        self.deck: list[tuple[int, int]] = []
        self.discard: list[tuple[int, int]] = []
        self.hands: dict[int, list[tuple[int, int]]] = {}

        self.lastPlayType: int = PLAYTYPE_NONE
        self.whoseTurn: int = 0
        self.lastPlayer: int = 0
        self.direction: int = DIRECTION_RIGHT

        # A wild has been played and we're waiting for its owner to tell us what it
        # became. Holds (avatarId, card) so a resolving message can be matched
        # against a real pending special instead of trusted on its own say-so.
        self.pendingSpecial: tuple[int, tuple[int, int]] | None = None

        # For a pixie-power wild, the wheel slot *we* picked (50..53). The client
        # translates the slot to an action and sends it back; we check its answer
        # against this rather than accepting whichever power-up it fancies.
        self.pendingPowerSlot: int | None = None

        # Set by the `c8-spin-result` magic word, consumed by the next power card.
        self.forcedPowerSlot: int | None = None

    # ------------------------------------------------------------------ state

    @property
    def topDiscard(self) -> tuple[int, int]:
        # An empty pile can only be seen by a client whose board outlived the
        # server's game. Hand back something renderable rather than raising.
        if not self.discard:
            return make_card(VALUE_UNDECLARED, SUIT_CHANGE)
        return self.discard[-1]

    def getHandSizes(self) -> list[int]:
        """Hand counts in roster order -- index i describes self.players[i]."""
        return [len(self.hands.get(avId, [])) for avId in self.players]

    def d_setGameData(self) -> None:
        # The third field is read and discarded by this client build
        # (DistributedCrazyEights.setGameData never stores param3), so it's always 0.
        self.sendUpdate("setGameData", [
            self.lastPlayType,
            self.topDiscard,
            0,
            self.getHandSizes(),
            self.whoseTurn,
            self.lastPlayer,
            self.direction,
        ])

    def d_setPlayerData(self, avId) -> None:
        self.sendUpdateToAvatarId(avId, "setPlayerData", [self.hands.get(avId, [])])

    def d_setPlayerDataAll(self) -> None:
        """Push every hand to its owner.

        Cheap, and it removes a whole class of bug: a power card can change all four
        hands at once, and sending only the mover's would leave the other three
        rendering a stale fan of cards they can no longer play.
        """
        for avId in self.players:
            self.d_setPlayerData(avId)

    def d_turnResponse(self, avId, code) -> None:
        # Diagnostics only. DistributedCrazyEights.turnResponse just logs -- the
        # client takes no corrective action, so real recovery is the authoritative
        # setGameData/setPlayerData that follows a rejection.
        self.sendUpdateToAvatarId(avId, "turnResponse", [code])

    # ------------------------------------------------------------------ dealing

    def init_game(self) -> None:
        # A pending reset belongs to the *previous* round. If new players sat down
        # inside RESET_DELAY, letting it fire would wipe the table mid-deal.
        self.cancelReset()
        self.cancelSpecialTimeout()

        # We may be here because the table filled early rather than because the clock
        # ran out. Drop the task without touching the game state -- cancelCountdown
        # would bounce us to GROUPING, and we're about to deal.
        taskMgr.remove(self.countdownTaskName)
        self.countdownEnds = None

        self.deck = build_deck()
        random.shuffle(self.deck)

        self.hands = {avId: [self.deck.pop() for _ in range(STARTING_HAND_SIZE)]
                      for avId in self.players}

        # The starting upcard must be an ordinary coloured card. Opening on a wild
        # would leave the table with no colour to match and nobody holding the turn
        # that owes us a declaration.
        self.discard = [self._draw_starting_card()]

        self.lastPlayType = PLAYTYPE_NONE
        self.direction = DIRECTION_RIGHT
        self.whoseTurn = self.players[0]
        self.lastPlayer = 0
        self.pendingSpecial = None
        self.pendingPowerSlot = None
        self.forcedPowerSlot = None

        # INIT then PLAY. Two For Tea gets this transition for free because its table
        # fills at maxPlayers and the base class fires it; we start at *min* players,
        # so the base never does and we have to send it ourselves.
        #
        # Guarded, because driving the GROUPING/INIT -> PLAY edge a second time is not
        # cosmetic: the client's setGameState case PLAY calls playActiveMeadowGame(),
        # which does ActivityManager.pushPause(). That stack is global and cumulative,
        # and only a drain to zero dispatches RESUME -- a partial drain sends
        # RESUME_CHECK, which MeadowPanel ignores, leaving the meadow frozen as a
        # dimmed screencap with no way out but a reload. Every teardown path pops
        # exactly once, so a second push strands the player permanently.
        #
        # We can be reached with the table already in PLAY when the base class has
        # auto-started it (autoStartWhenFull), which it must not do for us -- but a
        # stale DistributedMeadowGameAI without that flag will, and this keeps the
        # damage to a stray INIT rather than a locked-out table.
        if self.state != MEADOW_GAME_STATE_PLAY:
            self.setGameState(MEADOW_GAME_STATE_INIT, 0)
            self.d_setGameState()
            self.setGameState(MEADOW_GAME_STATE_PLAY, 0)
            self.d_setGameState()

        self.d_setGameData()
        self.d_setPlayerDataAll()

        # Re-send the (unchanged) roster. This looks redundant and is load-bearing.
        #
        # MinigameManager.activeMeadowGame is what the end-game results panel needs
        # to exist (showMeadowGameResultsPanel bails silently on null), and closing
        # that panel is the *only* thing that calls endMeadowGame() -- i.e. the only
        # popPause and MEADOWGAME_END. Lose activeMeadowGame and the player is left
        # paused and unable to move, with no way back but a reload.
        #
        # MeadowGameLauncher.onGameStatusUpdated clears it out from under us on the
        # REWARD state: it runs clearRequestedMeadowGame() -> MEADOWGAME_LEAVE ->
        # its own onLeave(), whose guard clears activeMeadowGame for exactly
        # gameState == REWARD, and does so without unpausing. That branch only runs
        # for a client whose requestedMeadowGame still points at this table --
        # setPlayers -> setActiveMeadowGameAndShowMatchmaker nulls it on every roster
        # update the local player is in, and only re-arms it on the first one. So the
        # last fairy to sit down never gets it cleared, and is the one who locks up.
        #
        # One more setPlayers clears it for them too. It has to go out *after* the
        # PLAY state change: the launcher's updatePlayerList re-opens the matchmaker
        # panel on a roster update while gameState < PLAY.
        self.d_setPlayers()

    def _draw_starting_card(self) -> tuple[int, int]:
        for i in range(len(self.deck) - 1, -1, -1):
            if card_suit(self.deck[i]) in SUITS:
                return self.deck.pop(i)

        # Unreachable with the real deck (48 of its 56 cards are coloured), but a
        # tuned deck of nothing but wilds shouldn't crash a district.
        self.notify.warning("no coloured card to start the discard pile")
        return self.deck.pop()

    def draw_cards(self, avId, count) -> int:
        """Move `count` cards from the deck to avId's hand. Returns how many moved."""
        drawn = 0

        for _ in range(count):
            if not self.deck and not self.recycle_discard():
                break
            self.hands.setdefault(avId, []).append(self.deck.pop())
            drawn += 1

        return drawn

    def recycle_discard(self) -> bool:
        """Shuffle the spent discard pile back into the deck. False if there's nothing to recycle."""
        if len(self.discard) <= 1:
            return False

        top = self.discard[-1]
        recycled = self.discard[:-1]
        self.discard = [top]

        # A wild goes back to the deck undeclared. Leaving the colour its last owner
        # picked baked into the card would deal a "wild" that renders as a plain
        # coloured card and matches on the wrong colour.
        self.deck = [
            make_card(VALUE_UNDECLARED, card_suit(c)) if card_suit(c) not in SUITS else c
            for c in recycled
        ]
        random.shuffle(self.deck)

        return True

    # ------------------------------------------------------------------ turn order

    def next_player(self, current, step=1) -> int:
        """The seat `step` places from `current`, following the current direction."""
        if not self.players:
            return 0

        if current not in self.players:
            # The current player left mid-turn. Anyone is better than raising
            # ValueError into the reader loop -- that takes down the whole district.
            return self.players[0]

        offset = 1 if self.direction == DIRECTION_RIGHT else -1
        index = self.players.index(current)

        return self.players[(index + offset * step) % len(self.players)]

    def advance_turn(self, step=1) -> None:
        self.whoseTurn = self.next_player(self.whoseTurn, step)

    def reverseDirection(self) -> None:
        """Flip the turn order, then hand off the turn.

        Head-to-head there's nobody to reverse *towards*, so the standard rule is
        that reverse acts as a skip -- flipping direction alone would just hand the
        turn straight back to the player who played it.
        """
        self.direction = (DIRECTION_LEFT if self.direction == DIRECTION_RIGHT
                          else DIRECTION_RIGHT)

        self.advance_turn(2 if len(self.players) == 2 else 1)

    # ------------------------------------------------------------------ lobby countdown

    @property
    def countdownTaskName(self) -> str:
        return f"CrazyEightsCountdown-{self.doId}"

    def countdownRemaining(self) -> int:
        """Whole seconds left on the lobby countdown, or 0 if it isn't running."""
        if self.countdownEnds is None:
            return 0

        return max(0, int(round(self.countdownEnds - globalClock.getRealTime())))

    def startCountdown(self) -> None:
        """Open the pre-game wait: INIT with a timeOutSecs the launcher counts down."""
        taskMgr.remove(self.countdownTaskName)
        self.countdownEnds = globalClock.getRealTime() + LOBBY_COUNTDOWN
        taskMgr.doMethodLater(LOBBY_COUNTDOWN, self._countdownTask, self.countdownTaskName)

        # INIT is what makes the client load the game swf and start the launcher's
        # clock, so timeOutSecs has to go out *with* the state change -- there is no
        # separate "here is the timer" message.
        self.setGameState(MEADOW_GAME_STATE_INIT, LOBBY_COUNTDOWN)
        self.d_setGameState()

    def cancelCountdown(self) -> None:
        """Abandon the wait and go back to grouping (the client's CANCEL_COUNTDOWN)."""
        taskMgr.remove(self.countdownTaskName)
        self.countdownEnds = None

        # DistributedMeadowGame.setGameState only fires CANCEL_COUNTDOWN on an
        # INIT -> GROUPING edge, so this must not be sent from any other state or the
        # launcher keeps ticking down to a game that never starts.
        if self.state != MEADOW_GAME_STATE_INIT:
            return

        self.setGameState(MEADOW_GAME_STATE_GROUPING, 0)
        self.d_setGameState()

    def _countdownTask(self, task):
        self.countdownEnds = None

        # Players can have drained away in the last few seconds. leaveRequest cancels
        # the countdown when that happens, but a task already in flight for this frame
        # still runs, so re-check rather than deal to one player. Falling back to
        # GROUPING matters more than the check: leaving the table in INIT with no timer
        # would strand it in a state that never starts and never reopens.
        if len(self.players) >= self.minPlayers:
            self.init_game()
        else:
            self.cancelCountdown()

        return task.done

    # ------------------------------------------------------------------ lifecycle

    def joinRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        # A round in progress is closed to newcomers. Hands are already dealt, and
        # every handSizes[] we've broadcast is positional -- seating a latecomer
        # would shift the indices under every client at the table.
        if self.state == MEADOW_GAME_STATE_PLAY and avatarId not in self.players:
            self.sendUpdateToAvatarId(
                avatarId, "joinResponse", [MEADOW_GAME_JOIN_RESPONSE_GAMEON_FULL])
            return

        # Joining a countdown that's already running: everyone else's clock is
        # mid-flight, so hand this client the remainder rather than the full duration.
        # Their DistributedMeadowGame is already in INIT, so setGameState stores the new
        # timeOutSecs and returns without re-dispatching INIT_COUNTDOWN; the launcher
        # picks it up from renderMatchMaker's own onInitCountdown() call.
        #
        # This has to go out BEFORE super() -- super() sends joinResponse, and that is
        # what drives the client through ACCEPT_JOIN -> renderMatchMaker -> reading
        # timeOutSecond. Arriving after it would be a message too late. Sending it to an
        # avatar whose join then gets rejected is harmless: onInitCountdown does nothing
        # unless the local player is actually in the game.
        if self.state == MEADOW_GAME_STATE_INIT and avatarId not in self.players:
            self.sendUpdateToAvatarId(
                avatarId, "setGameState",
                [MEADOW_GAME_STATE_INIT, self.countdownRemaining()])

        responseCode = super().joinRequest(avatarId)

        if responseCode != MEADOW_GAME_JOIN_RESPONSE_ACCEPTED:
            return

        # Push current state to the joiner so a table that's still filling renders
        # something coherent rather than an empty board.
        self.d_setGameData()
        self.d_setPlayerData(avatarId)

        # The last seat filling ends the wait early -- there is nobody left to wait for.
        if len(self.players) >= self.maxPlayers:
            self.init_game()
            return

        # Second player down: start the lobby countdown and leave the other seats open.
        if len(self.players) >= self.minPlayers and self.state == MEADOW_GAME_STATE_GROUPING:
            self.startCountdown()

    def leaveRequest(self) -> None:
        avatarId = self.air.getAvatarIdFromSender()

        if avatarId not in self.players:
            return

        wasPlaying = self.state == MEADOW_GAME_STATE_PLAY
        wasTheirTurn = self.whoseTurn == avatarId

        # Work out the successor *before* removing them -- next_player needs their
        # seat to still be in the roster to count from.
        successor = self.next_player(avatarId) if wasPlaying else 0

        self.players.remove(avatarId)

        # Their cards go back where they came from, so a long game doesn't quietly
        # starve the deck every time somebody walks away.
        for card in self.hands.pop(avatarId, []):
            self.deck.append(
                make_card(VALUE_UNDECLARED, card_suit(card))
                if card_suit(card) not in SUITS else card)
        random.shuffle(self.deck)

        # A wild *they* owed us a decision on dies with them -- but its placeholder is
        # still face-up on the pile, and an undeclared wild matches nothing: is_playable
        # lets only another wild through, so the next player could be left with no legal
        # move but "draw" for the rest of the round. Declare a colour on their behalf,
        # the same fallback forceResolveSpecial uses. No card effect and no win check
        # here -- the owner is gone and their hand went back to the deck above.
        #
        # Remembered, because it tells us where the clients are parked and so which
        # lastPlayType they can actually route below.
        abandonedWild = (self.pendingSpecial is not None
                         and self.pendingSpecial[0] == avatarId)

        if abandonedWild:
            _, played = self.pendingSpecial
            self.cancelSpecialTimeout()
            self.pendingSpecial = None
            self.pendingPowerSlot = None
            self.discard[-1] = make_card(random.choice(SUITS), card_suit(played))

        if not wasPlaying:
            self.d_setPlayers()

            # Below the minimum again while the lobby was counting down: call the
            # countdown off and go back to waiting. Whoever is still sitting there
            # keeps their seat and their launcher panel -- they're waiting for players
            # again, which is exactly the state they were in a moment ago.
            if self.state == MEADOW_GAME_STATE_INIT and len(self.players) < self.minPlayers:
                self.cancelCountdown()
            elif not self.players:
                # An empty table that isn't in play gets wiped, so no stale roster or
                # board outlives the group that made it. (This used to fire at any
                # count below minPlayers, which evicted a lone player still waiting
                # for someone to join -- now that GROUPING is a state people sit in
                # for a while, that had to go.)
                self.scheduleReset()
            return

        # Below minimum mid-round: the table can't continue.
        if len(self.players) < self.minPlayers:
            self.handleBelowMinimum()
            return

        # Still enough to play on. Roster first, then the removal notice -- the
        # client re-indexes DMG_Id from the new roster (Model.removePlayer) and the
        # handSizes[] in the setGameData that follows is already in the new order.
        self.d_setPlayers()

        # Somebody else is still mid-wild, with their colour picker or power spinner
        # open and the server waiting on the answer. Say nothing further: setPlayers on
        # its own has already done the removal everywhere -- MeadowGameBase.updateMatch
        # -> Controller.onRemovedPlayer -> Model.removePlayer marks them gone, drops
        # their card set and re-indexes every DMG_Id, none of which touches the FSM.
        #
        # A setGameData here has no safe play type. PLAYER_REMOVED drives
        # changeSuit/powerSpinner into turnStart, whose clearEventQueue() shuts the
        # picker in the player's face while we still demand a colour from them -- every
        # move they can make is then rejected (handleDiscard routes to resolveSpecial,
        # handleDraw refuses, the turn timer is ignored) until SPECIAL_RESOLVE_TIMEOUT
        # bails them out 25s later. PLAYTYPE_NONE takes changeSuit's "setGameData" edge
        # straight back to showChangeSuit, reopening the picker from the top and
        # restarting its countdown. Doing nothing costs only stale hand counts for the
        # few seconds until resolveSpecial's own setGameData lands, in the new order.
        #
        # whoseTurn sits on the wild's owner for the whole resolution
        # (handleShowSpecial leaves it there deliberately), so a wild pending that isn't
        # the leaver's means it wasn't their turn and there is no turn to hand on.
        if self.pendingSpecial is not None:
            return

        if wasTheirTurn:
            self.whoseTurn = successor

        # PLAYTYPE_PLAYER_REMOVED is not the general-purpose "someone left" signal it
        # reads as. Controller's FSM only maps "playerRemoved" out of the three states a
        # *wild* parks the table in -- changeSuit, powerSpinner, showPopupAndWait.
        # turnDisplayAndWait, where every client rests between turns, has no such
        # transition, so the update is dropped ("Undefined transition ... ignoring") and
        # the FSM never re-enters turnStart. That matters because re-entering
        # turnDisplayAndWait is the *only* thing that runs setListeners() and
        # setLocalTimer(): the successor inherits the turn with no card listeners and no
        # timer, and the board is dead for everyone.
        #
        # So pick the play type by where the clients actually are. Having just returned
        # on anyone else's pending wild, there are only two cases left. If the leaver
        # abandoned a wild, the table is still sitting in changeSuit/powerSpinner/
        # showPopupAndWait watching its show -- all three map playerRemoved, and it
        # lands them in turnStart, which clears the animation queue and falls through to
        # turnDisplayAndWait. Otherwise nothing is pending, everyone is resting in
        # turnDisplayAndWait, and PLAYTYPE_NONE -- the AI->client "nothing to animate" --
        # routes setGameData -> turnStart -> "none" -> turnDisplayAndWait, rebuilding the
        # board on the new roster.
        self.lastPlayType = PLAYTYPE_PLAYER_REMOVED if abandonedWild else PLAYTYPE_NONE
        self.lastPlayer = avatarId
        self.d_setGameData()
        self.d_setPlayerDataAll()

    # ------------------------------------------------------------------ validation

    def validatePlayer(self, avId) -> bool:
        # A client whose board outlived the server's round -- it left, the table
        # reset, the round ended -- will happily keep sending turns at a dead table.
        if self.state != MEADOW_GAME_STATE_PLAY:
            self.notify.warning(
                f"turnRequest from {avId} with no game in play (state={self.state})")
            return False

        if len(self.players) < self.minPlayers:
            self.notify.warning(
                f"turnRequest from {avId} with {len(self.players)} player(s)")
            return False

        if avId not in self.players:
            self.notify.warning(f"turnRequest from non-player {avId}")
            return False

        if avId != self.whoseTurn:
            self.notify.warning(f"turnRequest from {avId} out of turn")
            return False

        return True

    def take_from_hand(self, avId, card) -> tuple[int, int] | None:
        """Remove the played card from avId's hand and return it, or None if they don't hold it.

        Wilds are matched on suit alone. By the time a wild comes back to us its
        `value` carries the colour its owner declared (or the action the spinner
        landed on), so it no longer equals the (-1, suit) pair sitting in the hand.
        """
        hand = self.hands.get(avId)

        if not hand:
            return None

        suit = card_suit(card)

        if suit not in SUITS:
            for i, held in enumerate(hand):
                if card_suit(held) == suit:
                    return hand.pop(i)
            return None

        if card in hand:
            hand.remove(card)
            return card

        return None

    # ------------------------------------------------------------------ turn entry

    def turnRequest(self, playType, cards):
        avId = self.air.getAvatarIdFromSender()

        if not self.validatePlayer(avId):
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_PLAYER)
            return

        if playType == PLAYTYPE_DISCARD:
            self.handleDiscard(avId, cards)
        elif playType == PLAYTYPE_DRAW:
            self.handleDraw(avId)
        elif playType == PLAYTYPE_SHOW_SPECIAL:
            self.handleShowSpecial(avId, cards)
        elif playType == PLAYTYPE_NONE:
            self.handleTimeout(avId)
        else:
            self.notify.warning(f"turnRequest from {avId} with unknown playType {playType}")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)

    def handleDiscard(self, avId, cards) -> None:
        if not cards:
            self.notify.warning(f"discard from {avId} with no card")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_CARD)
            return

        # The client sends its whole _pickedCards array; the card actually being
        # played is the last one (every mutation it makes targets
        # _pickedCards[length - 1]).
        card = tuple(cards[-1])

        # A wild awaiting resolution short-circuits everything: this message is the
        # answer to a question we asked, not a fresh play.
        if self.pendingSpecial is not None:
            self.resolveSpecial(avId, card)
            return

        played = self.take_from_hand(avId, card)

        if played is None:
            self.notify.warning(f"discard from {avId} of a card they don't hold: {card}")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_CARD)
            self.d_setPlayerData(avId)
            return

        if not is_playable(card, self.topDiscard):
            self.notify.warning(
                f"discard from {avId} of unplayable {card} on {self.topDiscard}")
            # Put it back -- we already took it out of their hand.
            self.hands[avId].append(played)
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
            self.d_setPlayerData(avId)
            return

        self.d_turnResponse(avId, TURN_RESPONSE_VALID)

        # A wild played as somebody's *last* card skips the ceremony entirely:
        # dispatchDiscard force-assigns orange rather than opening a picker for a
        # hand that's already empty. So a wild can arrive here pre-declared.
        if card_suit(played) not in SUITS:
            # `value` here is the pre-declared colour, and it is client-supplied. Anything
            # that isn't a colour would land on the pile as a wild suit carrying a stray
            # value, which convertCardDataToTag renders by falling through to its "oc" +
            # "0"+value default -- i.e. a request for art like master_oc_08 that doesn't
            # exist, panicking every client at the table. Fall back to the same orange the
            # client force-assigns in dispatchDiscard.
            declared = card_value(card)
            if not is_colour(declared):
                self.notify.warning(
                    f"discard from {avId} pre-declared a non-colour {declared}; using orange")
                declared = SUIT_ORANGE
            self.discard.append(make_card(declared, card_suit(played)))
        else:
            self.discard.append(played)

        self.lastPlayer = avId
        self.lastPlayType = PLAYTYPE_DISCARD

        if not self.hands[avId]:
            self.handleWin(avId)
            return

        self.applyCardEffect(avId, self.topDiscard)

        self.d_setGameData()
        self.d_setPlayerDataAll()

    def applyCardEffect(self, avId, card) -> None:
        """Advance the turn, applying whatever the played card does on the way.

        `lastPlayer` is set to the player the card *targets*, not the player who
        played it: Controller.setEvents anchors both the draw-two animation and the
        skip notice on players[DMG.lastPlayer]. For a draw-two that's the fairy
        drawing the two cards, for a skip it's the fairy being skipped over.
        """
        value = card_value(card)

        if value == VALUE_DRAW_TWO:
            victim = self.next_player(self.whoseTurn)
            self.draw_cards(victim, 2)
            self.lastPlayer = victim
            self.advance_turn(2)
            return

        if value == VALUE_SKIP:
            self.lastPlayer = self.next_player(self.whoseTurn)
            self.advance_turn(2)
            return

        if value == VALUE_REVERSE:
            self.reverseDirection()
            return

        if value == VALUE_SELF_GO_AGAIN:
            # The spinner's "Extra Turn". whoseTurn stays put, which is also what
            # setPowerPopup's copy assumes.
            return

        if value == VALUE_ALL_PASS_ONE:
            # Named "pass one", is actually reverse -- see CrazyEightsConstants. It
            # is the same effect as a reverse card, so it goes through the same path:
            # spinning into Reverse head-to-head has to grant the extra turn a played
            # reverse card does, or the two spellings of one effect disagree.
            self.reverseDirection()
            return

        if value == VALUE_ALL_DRAW_ONE:
            for player in self.players:
                self.draw_cards(player, 1)
            self.advance_turn()
            return

        self.advance_turn()

    def handleDraw(self, avId) -> None:
        if self.pendingSpecial is not None:
            self.notify.warning(f"draw from {avId} while a wild is unresolved")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
            return

        if not self.draw_cards(avId, 1):
            # Deck and discard pile are both spent and nobody has gone out. Nothing
            # left to do but call it.
            self.handleNoCards()
            return

        self.d_turnResponse(avId, TURN_RESPONSE_VALID)

        self.lastPlayType = PLAYTYPE_DRAW
        self.lastPlayer = avId

        if DRAW_ENDS_TURN:
            self.advance_turn()

        self.d_setGameData()
        self.d_setPlayerDataAll()

    def handleTimeout(self, avId) -> None:
        """The active player's turn timer expired (Controller.onTimerComplete)."""
        if self.pendingSpecial is not None:
            # Their wild is still pending; the resolve timeout owns this table.
            return

        self.draw_cards(avId, 1)

        self.lastPlayType = PLAYTYPE_DRAW
        self.lastPlayer = avId
        self.advance_turn()

        self.d_setGameData()
        self.d_setPlayerDataAll()

    # ------------------------------------------------------------------ wilds

    def handleShowSpecial(self, avId, cards) -> None:
        """A wild was played and needs a colour (or a spin) before it resolves."""
        if not cards:
            self.notify.warning(f"showSpecial from {avId} with no card")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_CARD)
            return

        if self.pendingSpecial is not None:
            self.notify.warning(f"showSpecial from {avId} with one already pending")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
            return

        card = tuple(cards[-1])
        played = self.take_from_hand(avId, card)

        if played is None:
            self.notify.warning(f"showSpecial from {avId} of a card they don't hold: {card}")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_CARD)
            self.d_setPlayerData(avId)
            return

        suit = card_suit(played)

        if suit in SUITS:
            # SHOW_SPECIAL is only ever sent for a wild. An ordinary card arriving
            # here is a broken or hostile client.
            self.notify.warning(f"showSpecial from {avId} with ordinary card {played}")
            self.hands[avId].append(played)
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
            self.d_setPlayerData(avId)
            return

        self.d_turnResponse(avId, TURN_RESPONSE_VALID)

        self.pendingSpecial = (avId, played)
        self.lastPlayer = avId
        self.lastPlayType = PLAYTYPE_SHOW_SPECIAL

        if suit == SUIT_POWER:
            # We pick the wheel result and ship it in the same update. The client
            # branches to the spinner on topDiscard's *suit* and doesn't read the
            # value until its 3s spin timer fires, so the answer can ride along with
            # the question -- and sending it as one message avoids a second
            # setGameData driving the client FSM somewhere we don't want it.
            slot = self.forcedPowerSlot if self.forcedPowerSlot in POWER_SLOTS \
                else random.choice(POWER_SLOTS)
            self.forcedPowerSlot = None
            self.pendingPowerSlot = slot
            self.discard.append(make_card(slot, SUIT_POWER))
        else:
            self.pendingPowerSlot = None
            self.discard.append(make_card(VALUE_UNDECLARED, SUIT_CHANGE))

        # whoseTurn deliberately stays on avId -- the client shows the colour picker
        # to whoever holds the turn.
        self.d_setGameData()
        self.d_setPlayerDataAll()

        self.scheduleSpecialTimeout()

    def resolveSpecial(self, avId, card) -> None:
        """The second half of a wild: the declared colour, or the spun action."""
        owner, played = self.pendingSpecial

        if avId != owner:
            self.notify.warning(f"resolveSpecial from {avId}, wild belongs to {owner}")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_PLAYER)
            return

        value = card_value(card)
        suit = card_suit(played)

        if suit == SUIT_POWER:
            expected = POWER_SLOT_TO_ACTION.get(self.pendingPowerSlot)

            # Slot 3 is "Change Color": the client opens the colour picker after the
            # wheel settles, so what comes back is a colour rather than the action
            # id. Every other slot answers with the action itself.
            if expected == VALUE_ALL_CHANGE_SUIT:
                if not is_colour(value):
                    self.notify.warning(
                        f"power resolve from {avId} expected a colour, got {value}")
                    self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
                    return
            elif value != expected:
                # The client is telling us it landed on a slot we didn't spin.
                self.notify.warning(
                    f"power resolve from {avId} claimed {value}, "
                    f"slot {self.pendingPowerSlot} means {expected}")
                self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
                return
        elif not is_colour(value):
            self.notify.warning(f"colour resolve from {avId} with non-colour {value}")
            self.d_turnResponse(avId, TURN_RESPONSE_INVALID_MOVE)
            return

        self.cancelSpecialTimeout()
        self.pendingSpecial = None
        self.pendingPowerSlot = None

        self.d_turnResponse(avId, TURN_RESPONSE_VALID)

        # The resolved wild replaces its own placeholder on the pile. Its declared
        # colour lives in `value`; active_suit and is_playable both read it there.
        self.discard[-1] = make_card(value, suit)

        self.lastPlayer = avId
        self.lastPlayType = PLAYTYPE_DISCARD

        # Playing the wild is what emptied their hand -- the resolution is just
        # bookkeeping, but the win only lands now.
        if not self.hands.get(avId):
            self.handleWin(avId)
            return

        # A colour-only resolution (a change-colour wild, or the spinner's Change
        # Color slot) has no effect beyond the colour itself, so the turn simply
        # passes. Everything else runs its action.
        if is_colour(value):
            self.advance_turn()
        else:
            self.applyCardEffect(avId, self.topDiscard)

        self.d_setGameData()
        self.d_setPlayerDataAll()

    @property
    def specialTaskName(self) -> str:
        return f"CrazyEightsSpecial-{self.doId}"

    def scheduleSpecialTimeout(self) -> None:
        taskMgr.remove(self.specialTaskName)
        taskMgr.doMethodLater(
            SPECIAL_RESOLVE_TIMEOUT, self._specialTimeoutTask, self.specialTaskName)

    def cancelSpecialTimeout(self) -> None:
        taskMgr.remove(self.specialTaskName)

    def _specialTimeoutTask(self, task):
        self.forceResolveSpecial()
        return task.done

    def forceResolveSpecial(self) -> None:
        """Resolve a wild whose owner never answered, so the table can carry on."""
        if self.pendingSpecial is None:
            return

        owner, played = self.pendingSpecial
        suit = card_suit(played)

        if suit == SUIT_POWER and self.pendingPowerSlot is not None:
            action = POWER_SLOT_TO_ACTION.get(self.pendingPowerSlot)
            # "Change Color" needs a colour picked for them; the rest are self-contained.
            value = random.choice(SUITS) if action == VALUE_ALL_CHANGE_SUIT else action
        else:
            value = random.choice(SUITS)

        self.notify.warning(
            f"forcing wild resolution for {owner} on table {self.doId}: {value}")

        self.pendingSpecial = None
        self.pendingPowerSlot = None

        self.discard[-1] = make_card(value, suit)
        self.lastPlayer = owner
        self.lastPlayType = PLAYTYPE_DISCARD

        if not self.hands.get(owner):
            self.handleWin(owner)
            return

        if is_colour(value):
            self.advance_turn()
        else:
            self.applyCardEffect(owner, self.topDiscard)

        self.d_setGameData()
        self.d_setPlayerDataAll()

    # ------------------------------------------------------------------ endings

    def handleWin(self, avId) -> None:
        # These three sends are order-critical. Read Controller.setUpEndGameShow
        # before changing any of it:
        #
        # 1. Rewards first. The client sets winnerId from whichever Rank has
        #    rank == 0, and the winner show needs it. (Arriving late isn't fatal --
        #    setUpEndGameShow subscribes to SET_REWARDS when winnerId is still 0 --
        #    but getting there first skips that dance entirely.)
        #
        # 2. The final board, with whoseTurn == 0. That's what turnStart reads to
        #    decide the round is over, and it carries the winner's empty hand.
        #    setUpEndGameShow runs here too but does *nothing*, because its switch
        #    has an explicit `case MEADOW_GAME_STATE_PLAY: break` and the state is
        #    still PLAY.
        #
        # 3. The REWARD state, which is the send that actually produces the winner
        #    show: onGameStateUpdatedCalled fires "gameOver" for any state >= 7, and
        #    this time setUpEndGameShow sees REWARD and calls setUpWinner.
        #
        # Hoisting the state change above the setGameData looks tidier and breaks
        # it: the FSM would be sitting in gameEnd, which has no "setGameData"
        # transition. This order only ever re-enters gameEnd via "gameOver", which
        # every state (gameEnd included) maps.
        self.d_setRewards()

        self.whoseTurn = 0
        self.lastPlayType = PLAYTYPE_NONE
        self.d_setGameData()
        self.d_setPlayerDataAll()

        self.setGameState(MEADOW_GAME_STATE_REWARD, 0)
        self.d_setGameState()

        self.scheduleReset()

    def handleNoCards(self) -> None:
        """Deck and discard pile are both spent with nobody out. No winner, no reward."""
        self.cancelSpecialTimeout()

        self.setGameState(MEADOW_GAME_STATE_REWARD_NO_CARD, 0)
        self.d_setGameState()

        self.scheduleReset()

    def handleBelowMinimum(self) -> None:
        """Someone left and took the table below two players."""
        self.cancelSpecialTimeout()

        # Broadcast the shrunken roster while still in PLAY so the remaining client
        # processes the removal, then hand it the reason its game stopped.
        self.d_setPlayers()

        self.setGameState(MEADOW_GAME_STATE_REWARD_NO_PLAYER, 0)
        self.d_setGameState()

        self.scheduleReset()

    # ------------------------------------------------------------------ rewards

    def grantReward(self, avId, itemId, amount) -> None:
        avatar = self.air.doId2do.get(avId)

        if avatar is None:
            return

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemId, amount, -1):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))

    def d_setRewards(self) -> None:
        if len(self.players) < self.minPlayers:
            return

        itemId = SEASONAL_REWARD_ITEM[get_season(datetime.now(timezone.utc))]

        # Fewest cards left wins, and *everyone* is placed by what they were caught
        # holding -- not just the winner. Standard competition ranking: equal hands
        # share a place, and the next player down skips the places that tie used up
        # (0,0,2,3), which keeps rank < len(players) so the client's
        # rewardRankingMc.gotoAndStop(rank + 1) always lands on a real frame.
        #
        # The winner is the only player who can be on zero -- handleWin is the sole
        # caller of this, and it fires the moment a hand empties -- so rank 0 is
        # always theirs alone, which is what DistributedMeadowGame.setRewards reads
        # winnerId off.
        remaining = {avId: len(self.hands.get(avId, [])) for avId in self.players}

        rankForScore: dict[int, int] = {}
        for place, score in enumerate(sorted(remaining.values())):
            rankForScore.setdefault(score, place)

        payouts = REWARD_BY_PLACE[len(self.players)]

        ranks = []

        for avId in self.players:
            score = remaining[avId]
            rank = rankForScore[score]

            amount = payouts[rank]
            self.grantReward(avId, itemId, amount)
            self.creditGamePlayed(avId)

            # TODO: leaderboard/stat recording is left off deliberately, matching
            # DistributedMatchGameAI.d_setRewards. Turning it on for one meadow game
            # and not the other would make the profile "games" tab inconsistent, so
            # both should be re-enabled together.
            #
            # won = 1 if rank == 0 else 0
            # self.air.mongoInterface.recordStat(avId, "game", self.gameId, won)
            # if rank == 0:
            #     self.air.leaderBoardManager.d_addToLeaderBoard(avId, self.gameId, 1)

            # Rank struct order: (fairyId, score, Reward(itemId, amount), rank)
            ranks.append((avId, score, (itemId, amount), rank))

        for avId in self.players:
            self.sendUpdateToAvatarId(avId, "setRewards", [ranks])

    # ------------------------------------------------------------------ reset

    @property
    def resetTaskName(self) -> str:
        return f"CrazyEightsReset-{self.doId}"

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
        self.cancelSpecialTimeout()
        taskMgr.remove(self.countdownTaskName)
        super().delete()

    def resetGame(self) -> None:
        # Empty the table and return to grouping so a fresh group can sit down. The
        # client's end-game path doesn't send a leaveRequest, so the server has to
        # clear the roster itself or the seats stay occupied forever.
        self.cancelSpecialTimeout()
        taskMgr.remove(self.countdownTaskName)
        self.countdownEnds = None

        self.players = []
        self.hands = {}
        self.deck = []
        self.discard = []
        self.lastPlayType = PLAYTYPE_NONE
        self.whoseTurn = 0
        self.lastPlayer = 0
        self.direction = DIRECTION_RIGHT
        self.pendingSpecial = None
        self.pendingPowerSlot = None
        self.forcedPowerSlot = None

        self.setGameState(MEADOW_GAME_STATE_RESET, 0)
        self.d_setGameState()

        # Then back to GROUPING so the hotspot is joinable again. RESET isn't a
        # stable joinable state (the launcher reads it as "clear and close"), so it
        # has to be followed by GROUPING. Ordering GROUPING ahead of the empty
        # setPlayers keeps clients from reading the empty roster as a mid-game
        # player removal.
        self.setGameState(MEADOW_GAME_STATE_GROUPING, 0)
        self.d_setGameState()
        self.d_setPlayers()
