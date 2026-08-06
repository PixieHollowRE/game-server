"""
Magic words that change the fairy who typed them.

Level, experience, hair, item colours, which house they live in, and Vidia's
daily spin.
"""

from game.fairies.housing.HomeItems import clearPlacedHomeItems
from game.fairies.magicwords.registry import command

# Slot indices into FairyDNA, in the order set-hair takes them. The client's
# character creator picks a back and a front hairpiece plus one colour for both
# (CAFSceneBody's hairback/hairfront selectors and its single hairPicker), and
# these are the DNA fields those three land in.
DNA_HAIR_BACK = 4
DNA_HAIR_FRONT = 5
DNA_HAIR_COLOR = 9


@command("set-level", "set-level <level>")
def setLevel(ctx) -> str:
    level = ctx.intArg(0)

    # setLevel is `db`, so the broadcast persists through the DBSS bridge.
    ctx.avatar.b_setLevel(level)

    return f"level set to {level}"


@command("set-experience-points", "set-experience-points <points>")
def setExperiencePoints(ctx) -> str:
    points = ctx.intArg(0)

    ctx.avatar.b_setExperiencePoints(points)
    
    # This is a live poke at the pixie dust meter and the level-up
    # panel, nothing more right now -- it is gone at the next login.
    return f"experience set to {points} (not persisted -- session only)"


@command("set-hair", "set-hair <hairBack> <hairFront> <hairColor>")
def setHair(ctx) -> str:
    hairBack = ctx.intArg(0)
    hairFront = ctx.intArg(1)
    hairColor = ctx.intArg(2)

    dna = list(ctx.avatar.getFairyDNA())
    dna[DNA_HAIR_BACK] = hairBack
    dna[DNA_HAIR_FRONT] = hairFront
    dna[DNA_HAIR_COLOR] = hairColor

    ctx.avatar.b_setFairyDNA(tuple(dna))
    ctx.avatar.redrawFairy()

    return f"hair set to back={hairBack} front={hairFront} colour={hairColor}"


@command("dye-item", "dye-item <invId> <color1> <color2>")
def dyeItem(ctx) -> str:
    invId = ctx.intArg(0)
    color1 = ctx.intArg(1)
    color2 = ctx.intArg(2)

    # -1 in either slot means "leave this one alone", matching the shop's
    # setRequestDyeItem. The client's dye-item always sends both, but a GM
    # recolouring one half of an item shouldn't have to restate the other.
    fields = {}

    if color1 != -1:
        fields["avatar.items.$.color1"] = color1

    if color2 != -1:
        fields["avatar.items.$.color2"] = color2

    if not fields:
        ctx.fail("nothing to dye -- both colours were -1")

    result = ctx.air.mongoInterface.mongodb.fairies.update_one(
        {"_id": ctx.avatar.doId, "avatar.items.inv_id": invId},
        {"$set": fields},
    )

    if result.matched_count == 0:
        ctx.fail(f"no item with invId {invId}")

    # Only an equipped item has anything to redraw; a wardrobe entry just shows
    # its new colours the next time the panel reads it.
    ctx.avatar.d_refreshEquippedItem(invId)

    return f"dyed item {invId} to {color1}/{color2}"


@command("set-home-type-id", "set-home-type-id <homeTypeId>")
def setHomeTypeId(ctx) -> str:
    homeType = ctx.intArg(0)

    # Same two steps the shop's purchaseHomeType takes: empty the old house out
    # (placed furniture is laid out against the old floorplan and has nowhere to
    # go in the new one) and persist by hand, because b_setHomeType only reaches
    # the client and _defaultHomeType reads the database on the next login.
    if ctx.avatar.getHomeType() != homeType:
        clearPlacedHomeItems(ctx.air, ctx.avatar.doId)

    ctx.air.mongoInterface.updateField(
        "fairies", "homeType", ctx.avatar.doId, homeType
    )
    ctx.avatar.b_setHomeType(homeType)

    return f"home type set to {homeType} (placed items returned to storage)"


@command("tryon", "tryon <itemIndex> <collectionId>")
def tryOn(ctx) -> str:
    from game.fairies.fairy.npc.DistributedFairyShopkeeperNPCAI import (
        DistributedFairyShopkeeperNPCAI,
    )

    itemIndex = ctx.intArg(0)
    collectionId = ctx.intArg(1)

    # setTriedOnItems is a field on the shopkeeper, so there has to be one in
    # the room -- the client's try-on mirror is part of the shop panel.
    shopkeeper = next(
        (do for do in ctx.air.doId2do.values()
         if isinstance(do, DistributedFairyShopkeeperNPCAI) and do.zoneId == ctx.avatar.zoneId),
        None,
    )

    if shopkeeper is None:
        ctx.fail("no shopkeeper in this zone -- stand in a shop first")

    shopkeeper.sendUpdateToAvatarId(
        ctx.avatar.doId, "setTriedOnItems",
        [[(ctx.avatar.doId, [(itemIndex, collectionId)])]],
    )

    return f"trying on item {itemIndex} from collection {collectionId}"


@command("daily-chance", "daily-chance")
def dailyChance(ctx) -> str:
    # Clear today's spin first so the command always spins, rather than doing
    # nothing on the second use of the day -- testing the wheel is the whole
    # point of asking for it from a console.
    ctx.air.mongoInterface.updateField(
        "fairies", "dailyChanceLastSpin", ctx.avatar.doId, None
    )

    # excludeMask 0: the client normally works out whether there is wardrobe or
    # storage room and passes it in. Zero means "no restrictions", so a GM can
    # win anything on the wheel.
    ctx.avatar.doDailyChance(0)

    return "spun the daily chance wheel"


@command("set-daily-chance", "set-daily-chance <0|1>")
def setDailyChance(ctx) -> str:
    played = ctx.intArg(0)

    if played:
        ctx.avatar.recordDailyChanceSpin()
        return "daily chance marked as played for today"

    ctx.air.mongoInterface.updateField(
        "fairies", "dailyChanceLastSpin", ctx.avatar.doId, None
    )
    ctx.avatar.b_setDailyChancePlayed(0)

    return "daily chance reset -- the wheel is available again"
