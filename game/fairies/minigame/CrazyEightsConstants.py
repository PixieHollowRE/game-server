"""
Protocol constants for Crazy Cakes (gameId 13070), the Tearoom's Crazy Eights game.

Every value here mirrors one in the client's MMOConstants (mmo.swf) -- the client is
already shipped and complete, so these are fixed by it, not chosen by us. Where a
constant's *name* is misleading the comment says so; the names are kept identical to
the client's anyway so the two can be diffed by eye.

A card on the wire is the `Card` struct from fairy.dc:

    struct Card { int8 value; int8 suit; };

which crosses the Python boundary as a plain ``(value, suit)`` tuple -- value FIRST.
(The nested Rank/Reward structs in DistributedMatchGameAI.d_setRewards already work
this way.) Inverting the pair doesn't raise, it just renders as garbage card art, so
prefer the make_card/card_value/card_suit helpers below over raw indexing.
"""

# --- Suits -------------------------------------------------------------------
# The four real colours. These are the `suit` field of an ordinary card.
SUIT_ORANGE = 101
SUIT_BLUE = 102
SUIT_PURPLE = 103
SUIT_YELLOW = 104

SUITS = (SUIT_ORANGE, SUIT_BLUE, SUIT_PURPLE, SUIT_YELLOW)

# Two pseudo-suits mark the wild cards. They are never a "colour" -- a wild has no
# colour until its owner declares one.
#
# NOTE: meadowgameCrazyEight.xml labels these backwards (<suit8>power card</suit8>,
# <suit4>change color</suit4>). The XML copy is a mislabelled tooltip; the constants
# below are what drives behaviour (Controller.turnStart branches on suit == 8 for the
# colour picker and suit == 4 for the spinner). Follow these, not the copy.
SUIT_CHANGE = 8   # "Change Color" wild  -> art master_crazy_08
SUIT_POWER = 4    # "Pixie Power" wild   -> art master_crd

WILD_SUITS = (SUIT_CHANGE, SUIT_POWER)

# --- Values ------------------------------------------------------------------
# Number cards run 1..9 -- NOT 1..10, and NOT including 8. CrazyEight.convertCardDataToTag
# builds the art symbol for an unrecognised value as "0" + value, so a 10 would ask for
# the nonexistent symbol master_oc_010. Nine is the ceiling the art imposes.
#
# Eight is the hole in the middle: it's the game's namesake wild, so the colour suits
# have no 8 face. Messenger.as enumerates the per-suit art and goes ..._06, _07, _09 --
# there is no master_oc_08/bc_08/pc_08/yc_08 symbol in the library. Dealing one panics
# the container with "Variable master_pc_08 is not defined". An 8 is only ever
# (VALUE_UNDECLARED, SUIT_CHANGE), which renders as master_crazy_08.
MIN_NUMBER_VALUE = 1
MAX_NUMBER_VALUE = 9
WILD_NUMBER_VALUE = 8   # not dealt as a colour card -- see SUIT_CHANGE
NUMBER_VALUES = tuple(
    value
    for value in range(MIN_NUMBER_VALUE, MAX_NUMBER_VALUE + 1)
    if value != WILD_NUMBER_VALUE
)

VALUE_DRAW_TWO = 11
VALUE_REVERSE = 12
VALUE_SKIP = 13

# A colour card with no number on it. We never deal one: the client synthesises it
# when rendering a resolved wild (convertCardDataToTag swaps suit = value; value =
# BASE once it sees a colour id sitting in `value`).
VALUE_BASE = 14

ACTION_VALUES = (VALUE_DRAW_TWO, VALUE_REVERSE, VALUE_SKIP)

# An unplayed wild carries value -1. convertCardDataToTag keys the face-up wild art
# off exactly this (`suit == SUIT_CHANGE && value == -1` -> master_crazy_08).
VALUE_UNDECLARED = -1

# --- Resolved pixie-power actions --------------------------------------------
# What a power card becomes once the wheel has been spun and the client has told us
# which slot it landed on.
#
# NOTE: ALL_PASS_ONE is *reverse direction*, despite the name. The client's copy for
# it is <action23>Reverse</action23> / "#PLAYER# has reversed the direction!". Nobody
# passes anything.
VALUE_ALL_DRAW_ONE = 21
VALUE_SELF_GO_AGAIN = 22
VALUE_ALL_PASS_ONE = 23     # reverse
VALUE_ALL_CHANGE_SUIT = 24

POWER_ACTION_VALUES = (
    VALUE_ALL_DRAW_ONE,
    VALUE_SELF_GO_AGAIN,
    VALUE_ALL_PASS_ONE,
    VALUE_ALL_CHANGE_SUIT,
)

# The top discard reading as one of these means "an action card that hasn't been
# resolved yet", which the client treats as making *every* card playable
# (Model.getValidCardSets). Mirrored in is_playable() below.
UNRESOLVED_ACTION_VALUES = (
    VALUE_ALL_DRAW_ONE,
    VALUE_SELF_GO_AGAIN,
    VALUE_ALL_PASS_ONE,
)

# --- Power spinner slots -----------------------------------------------------
# The AI picks the wheel result and sends it as topDiscard.value; the client does
# onPick(value - POWER_OFFSET + 1) to land the pointer on wheel frame 1..4.
POWER_OFFSET = 50
VALUE_POWER_0 = 50
VALUE_POWER_1 = 51
VALUE_POWER_2 = 52
VALUE_POWER_3 = 53

POWER_SLOTS = (VALUE_POWER_0, VALUE_POWER_1, VALUE_POWER_2, VALUE_POWER_3)

# Which action each wheel slot resolves to. The active player's client performs this
# same translation (Controller.onClosePowerSpinner) and sends the right-hand value
# back to us as a DISCARD -- so this table is also what we validate that reply
# against. Without the check a modified client just picks its own power-up.
POWER_SLOT_TO_ACTION = {
    VALUE_POWER_0: VALUE_SELF_GO_AGAIN,     # wheel 1 "Extra Turn"
    VALUE_POWER_1: VALUE_ALL_PASS_ONE,      # wheel 2 "Reverse"
    VALUE_POWER_2: VALUE_ALL_CHANGE_SUIT,   # wheel 3 "Change Color"
    VALUE_POWER_3: VALUE_ALL_DRAW_ONE,      # wheel 4 "All Players Draw 1 Card"
}

# --- Play types (the int8 in setGameData / turnRequest) ----------------------
PLAYTYPE_NONE = 0           # client->AI: turn timer expired. AI->client: nothing to animate
PLAYTYPE_DISCARD = 1
PLAYTYPE_DRAW = 2
PLAYTYPE_REWARD = 4         # AI->client only; suppresses the client's SET_GAMEDATA dispatch
PLAYTYPE_SHOW_SPECIAL = 5   # a wild was played and is awaiting its colour/spin
PLAYTYPE_PLAYER_REMOVED = 6

# --- Direction ---------------------------------------------------------------
DIRECTION_RIGHT = 1
DIRECTION_LEFT = 2

# --- turnResponse codes ------------------------------------------------------
# DistributedCrazyEights.turnResponse only logs these -- the client takes no
# corrective action whatsoever. They're diagnostics. Real recovery from a rejected
# move is re-broadcasting authoritative setGameData + setPlayerData.
TURN_RESPONSE_VALID = 0
TURN_RESPONSE_INVALID_PLAYER = 1
TURN_RESPONSE_INVALID_CARD = 2
TURN_RESPONSE_INVALID_MOVE = 3

# --- Table / deck configuration ---------------------------------------------
GAME_ID = 13070

MIN_PLAYERS = 2
MAX_PLAYERS = 4

# Seconds the table sits in INIT with its seats still open once the second player sits
# down, so a third and fourth can join before the deal. This is the number that rides in
# setGameState's timeOutSecs and drives the launcher's "Game will begin in:" clock, so
# the server's task and the client's display must both key off it.
#
# 10 to match MeadowGameLauncher.GAME_LAUNCH_DELAY, the client's own fallback. Note the
# launcher only draws the countdown when maxPlayers > 2 (a two-seat table shows "Waiting
# for one more player..." instead and starts on the second join), which is exactly why
# Two For Tea needs none of this.
LOBBY_COUNTDOWN = 10

STARTING_HAND_SIZE = 7

# 4 suits x (1..7 + 9 + draw two + reverse + skip) = 44, plus the wilds = 52.
# The wild counts are ours to tune; nothing in the client depends on them.
CHANGE_WILD_COUNT = 4
POWER_WILD_COUNT = 4


def make_card(value, suit):
    """Build the (value, suit) pair the Card struct expects. Value comes first."""
    return (int(value), int(suit))


def card_value(card):
    return card[0]


def card_suit(card):
    return card[1]


def is_wild(card):
    return card_suit(card) in WILD_SUITS


def is_colour(value):
    """Is this `value` field actually carrying a declared colour?

    After a wild resolves, its chosen colour rides in the card's *value*, not its
    suit (the client does exactly this in onChangeSuitToBlue and friends). So a
    value in 101..104 means "wild, declared as this colour".
    """
    return value in SUITS


def build_deck():
    """The full 56-card deck, unshuffled and in a stable order."""
    deck = []

    for suit in SUITS:
        for value in NUMBER_VALUES:
            deck.append(make_card(value, suit))
        for value in ACTION_VALUES:
            deck.append(make_card(value, suit))

    deck.extend([make_card(VALUE_UNDECLARED, SUIT_CHANGE)] * CHANGE_WILD_COUNT)
    deck.extend([make_card(VALUE_UNDECLARED, SUIT_POWER)] * POWER_WILD_COUNT)

    return deck


def active_suit(top_discard):
    """The colour a play must currently match, or None if the top card has no colour.

    An ordinary card's colour is its suit. A *resolved* wild's colour is parked in
    its value instead, which is why this can't just read card_suit().
    """
    value, suit = top_discard

    if is_colour(value):
        return value

    if suit in SUITS:
        return suit

    return None


def is_playable(card, top_discard):
    """Mirror of the client's Model.getValidCardSets rule.

    This MUST agree with the client exactly. If the server is stricter the client
    offers cards it will then reject; if the server is looser a hacked client gets
    away with an illegal play that everyone else's board can't render.
    """
    value, suit = card
    top_value, top_suit = top_discard

    # Wilds are always playable.
    if suit in WILD_SUITS:
        return True

    # An action card sitting unresolved on the discard pile opens the board up.
    if top_value in UNRESOLVED_ACTION_VALUES:
        return True

    if suit == top_suit or value == top_value:
        return True

    # `suit == top_value` catches the resolved-wild case: the declared colour is in
    # the top card's value field.
    if suit == top_value:
        return True

    return False
