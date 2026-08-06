"""
Magic words that put items into a fairy's inventory.

The get- forms give to whoever typed the command; the give- forms name a fairy
last, because fairy names have spaces in them and anything after the fixed
arguments has to be the name.
"""

from game.fairies.fairy.ItemGrant import STORAGE, WARDROBE, grant_item
from game.fairies.magicwords.registry import MagicWordError, command


@command("get-home-item", "get-home-item <itemId> [color1] [color2]")
def getHomeItem(ctx) -> str:
    itemId, color1, color2 = _readItemArgs(ctx, len(ctx.args))

    return _grant(ctx, ctx.avatar.doId, itemId, color1, color2, STORAGE, "storage")


@command("give-home-item", "give-home-item <itemId> [color1] [color2] <fairy>")
def giveHomeItem(ctx) -> str:
    return _grantToTarget(ctx, STORAGE, "storage")


@command("get-wardrobe-item", "get-wardrobe-item <itemId> [color1] [color2]")
def getWardrobeItem(ctx) -> str:
    itemId, color1, color2 = _readItemArgs(ctx, len(ctx.args))

    return _grant(ctx, ctx.avatar.doId, itemId, color1, color2, WARDROBE, "wardrobe")


@command("give-wardrobe-item", "give-wardrobe-item <itemId> [color1] [color2] <fairy>")
def giveWardrobeItem(ctx) -> str:
    return _grantToTarget(ctx, WARDROBE, "wardrobe")


def _readItemArgs(ctx, upTo: int) -> tuple[int, int, int]:
    """itemId plus the two optional colours, reading no further than `upTo`."""
    itemId = ctx.intArg(0)
    color1 = ctx.optIntArg(1, 0) if upTo > 1 else 0
    color2 = ctx.optIntArg(2, 0) if upTo > 2 else 0

    return itemId, color1, color2


def _grant(ctx, avatarId: int, itemId: int, color1: int, color2: int, where, label: str) -> str:
    try:
        invId = grant_item(ctx.air, avatarId, itemId, color1, color2, where)
    except ValueError as e:
        # get_item_type refuses an id it can't bucket into an item type.
        raise MagicWordError(str(e)) from e

    if not invId:
        ctx.fail(f"could not add item {itemId} to fairy {avatarId}")

    return f"gave {label} item {itemId} to {avatarId} as invId {invId}"


def _grantToTarget(ctx, where, label: str) -> str:
    nameStart = _targetStart(ctx)
    itemId, color1, color2 = _readItemArgs(ctx, min(nameStart, 3))
    targetId = ctx.targetId(nameStart)

    return _grant(ctx, targetId, itemId, color1, color2, where, label)


def _targetStart(ctx) -> int:
    """
    Where the fairy the command names begins.

    The optional numbers in the middle make this ambiguous from the front, so
    read from the back instead: a fairy name is a run of non-numeric words
    ("Rosetta Sparkle Dust") and everything before it is arguments. When there
    is no such run the fairy was named by doId, which is the last word.
    """
    args = ctx.args
    start = len(args)

    while start > 1 and not _isInt(args[start - 1]):
        start -= 1

    if start == len(args):
        start = len(args) - 1

    if start < 1:
        ctx.fail(f"no fairy named -- usage: {ctx.usage}")

    return start


def _isInt(token: str) -> bool:
    try:
        int(token)
    except ValueError:
        return False

    return True


@command("get-pouch-item", "get-pouch-item <itemId> [amount]")
def getPouchItem(ctx) -> str:
    itemId = ctx.intArg(0)
    amount = ctx.optIntArg(1, 1)

    # The feedback flavour also fires the client's pickup sparkle and resyncs
    # the pouch, which is what the fairy would see picking one up in a meadow.
    if not ctx.air.inventoryManager.addIngredientsToPouchWithPickupFeedback(
        ctx.avatar.doId, itemId, amount
    ):
        ctx.fail(f"could not add {amount}x{itemId} to the pouch")

    return f"gave {amount}x pouch item {itemId}"


@command("give-pouch-item", "give-pouch-item <itemId> [amount] <fairy>")
def givePouchItem(ctx) -> str:
    itemId = ctx.intArg(0)
    nameStart = _targetStart(ctx)
    amount = ctx.optIntArg(1, 1) if nameStart > 1 else 1
    targetId = ctx.targetId(nameStart)

    if not ctx.air.inventoryManager.addIngredientsToPouch(targetId, itemId, amount, -1):
        ctx.fail(f"could not add {amount}x{itemId} to fairy {targetId}'s pouch")

    # Only a fairy on this district has a live pouch to refresh; anyone else
    # reads the new amount out of the database on their next login.
    target = ctx.air.doId2do.get(targetId)

    if target is not None:
        target.d_syncPouchAfterChanges()

    return f"gave {amount}x pouch item {itemId} to {targetId}"


@command("add-crafting-points", "add-crafting-points <recipeId> <points>")
def addCraftingPoints(ctx) -> str:
    return _addRecipePoints(ctx)


# The client's `add-tailoring-points` actually sends "add-crafting-points" (see
# LiveMod), so this only ever fires if something speaks to the manager directly.
# Registered anyway so the two names behave the same.
@command("add-tailoring-points", "add-tailoring-points <recipeId> <points>")
def addTailoringPoints(ctx) -> str:
    return _addRecipePoints(ctx)


def _addRecipePoints(ctx) -> str:
    recipeId = ctx.intArg(0)
    points = ctx.intArg(1)

    # Same shape a finished craft records (DistributedCraftingMinigameAI), so
    # the recipe card's craft count, best quality and running total all move.
    # The client updates its own copy of the card from LiveMod, so this is only
    # about what survives the session.
    ctx.air.mongoInterface.recordStat(ctx.avatar.doId, "recipe", recipeId, points)

    return f"recorded {points} point(s) on recipe {recipeId}"
