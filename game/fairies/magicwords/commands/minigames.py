"""
Magic words for the Tearoom's two multiplayer table games -- Two For Tea (the
memory game) and Crazy Cakes (Crazy Eights).

All of these need the game instance the GM is actually sitting at. The tables
aren't indexed anywhere, so they are found by scanning doId2do for whichever
instance has the caller on its roster.
"""

from game.fairies.magicwords.registry import command
from game.fairies.minigame.DistributedMatchGameAI import (
    DistributedMatchGameAI,
    MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS,
    MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS,
    MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2,
    MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN,
    MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE,
)
from game.fairies.minigame.DistributedCrazyEightsAI import DistributedCrazyEightsAI
from game.fairies.minigame.CrazyEightsConstants import (
    SUIT_CHANGE,
    SUIT_POWER,
    VALUE_DRAW_TWO,
    VALUE_POWER_0,
    VALUE_POWER_1,
    VALUE_POWER_2,
    VALUE_POWER_3,
    VALUE_REVERSE,
    VALUE_SKIP,
    card_suit,
    card_value,
)

# The four pixie-power wheel slots, named after the copy the client prints for
# each (powerSpinnerChoice1..4 in meadowgameCrazyEight.xml) rather than after the
# misleading constant names -- "reverse" really is slot 2's ALL_PASS_ONE.
POWER_SLOTS_BY_NAME = {
    "extraturn": VALUE_POWER_0,
    "reverse": VALUE_POWER_1,
    "changecolor": VALUE_POWER_2,
    "drawone": VALUE_POWER_3,
}

SUIT_NAMES = {101: "orange", 102: "blue", 103: "purple", 104: "yellow",
              SUIT_CHANGE: "change", SUIT_POWER: "power"}

VALUE_NAMES = {VALUE_DRAW_TWO: "draw2", VALUE_REVERSE: "rev", VALUE_SKIP: "skip"}

# The four results the power spinner wheel can actually land on. REVEAL and
# LOSETURN exist in the client's enum but are not wheel slots -- sending either
# leaves stuck cards or a desynced turn -- so they are not offered here either.
SPIN_RESULTS = {
    "bonus": MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS,
    "bonus2": MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BONUS_X2,
    "badnews": MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_BADNEWS,
    "shuffle": MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_SHUFFLE,
    "golden": MEADOW_GAME_MEMORY_PLAYTYPE_SPIN_GOLDEN,
}


@command("reveal-match-cards", "reveal-match-cards")
def revealMatchCards(ctx) -> str:
    game = _matchGameFor(ctx)

    game.d_revealBoard()

    return "revealed the board (until the next move redraws it)"


@command("match-spin-result", "match-spin-result <bonus|bonus2|badnews|shuffle|golden>")
def matchSpinResult(ctx) -> str:
    game = _matchGameFor(ctx)
    token = ctx.arg(0).lower()

    if token in SPIN_RESULTS:
        result = SPIN_RESULTS[token]
    elif token.isdigit() and int(token) in SPIN_RESULTS.values():
        result = int(token)
    else:
        ctx.fail(f"unknown spin result {token!r} -- usage: {ctx.usage}")

    game.forcedSpinResult = result

    return f"next power spinner match will land on {token}"


@command("c8-spin-result", "c8-spin-result <extraturn|reverse|changecolor|drawone>")
def crazyEightsSpinResult(ctx) -> str:
    game = _crazyEightsFor(ctx)
    token = ctx.arg(0).lower()

    if token in POWER_SLOTS_BY_NAME:
        slot = POWER_SLOTS_BY_NAME[token]
    elif token.isdigit() and int(token) in POWER_SLOTS_BY_NAME.values():
        slot = int(token)
    else:
        ctx.fail(f"unknown spin result {token!r} -- usage: {ctx.usage}")

    game.forcedPowerSlot = slot

    return f"next pixie power card will land on {token} (slot {slot})"


@command("c8-hand", "c8-hand")
def crazyEightsHand(ctx) -> str:
    game = _crazyEightsFor(ctx)

    hand = game.hands.get(ctx.avatar.doId, [])

    if not hand:
        return "your hand is empty"

    return (f"top discard {_cardName(game.topDiscard)} | "
            f"{len(hand)} cards: " + ", ".join(_cardName(c) for c in hand))


@command("c8-deal", "c8-deal <count>")
def crazyEightsDeal(ctx) -> str:
    """Resize your own hand, to reach an end state without playing a whole round."""
    game = _crazyEightsFor(ctx)

    # One card is the floor: emptying the hand outright would skip the win path
    # entirely, which is usually the thing being tested.
    count = max(1, min(ctx.intArg(0), 20))
    avId = ctx.avatar.doId
    hand = game.hands.setdefault(avId, [])

    while len(hand) > count:
        game.deck.append(hand.pop())

    if len(hand) < count:
        game.draw_cards(avId, count - len(hand))

    game.d_setGameData()
    game.d_setPlayerData(avId)

    return f"your hand is now {len(hand)} card(s)"


def _cardName(card) -> str:
    value, suit = card_value(card), card_suit(card)
    return f"{SUIT_NAMES.get(suit, suit)}-{VALUE_NAMES.get(value, value)}"


def _matchGameFor(ctx):
    return _tableFor(ctx, DistributedMatchGameAI, "Two For Tea")


def _crazyEightsFor(ctx):
    return _tableFor(ctx, DistributedCrazyEightsAI, "Crazy Cakes")


def _tableFor(ctx, gameClass, label):
    game = next(
        (do for do in ctx.air.doId2do.values()
         if isinstance(do, gameClass) and ctx.avatar.doId in do.players),
        None,
    )

    if game is None:
        ctx.fail(f"you are not sitting at a {label} table")

    return game
