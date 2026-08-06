"""
A giveaway is the free seasonal item left lying in a meadow that every fairy may
pick up exactly once, ever -- unlike an ingredient stack, it never respawns and
it is not consumed by being collected. It just stops being eligible for the
fairy who took it.

Every giveaway carries both:

  giveaway_id    15000-15499 (client TYPE_GIVEAWAY_ID). Picks the *art* standing
                 in the meadow and the name on its tooltip. The client resolves
                 it against giveaways.xml for the name and cacheableMedia.xml
                 for the asset ("<asset id="15122_item" swf="..."/>"), so a
                 giveaway_id with no entry in both will fail to load and the
                 spawnable is silently dropped client-side.

  reward_item_id The thing that actually lands in the inventory, in the normal
                 item id space. This is what the client size-checks against the
                 wardrobe/storage/pouch limits before it will let the fairy
                 click, and what the AI routes on when it pays out. A badge is
                 a legal reward: badge ids live in the same id space (buckets
                 19-23), which is how the original hung a badge off a giveaway.

Collection is remembered per fairy in `giveawaysCollected` on the fairy document
-- a plain list of giveaway_id (see GiveawayReward). Reusing a giveaway_id for a
different reward later would therefore hand nothing to everyone who already
collected the old one; mint a new id instead.
"""

from __future__ import annotations

from dataclasses import dataclass

from game.fairies.ai import ZoneConstants as zc


@dataclass(frozen=True)
class GiveawayDef:
    """One giveaway: what it looks like and what it pays out."""

    giveaway_id: int
    display_name: str
    reward_item_id: int

    event_id: int = 0
    holiday_bit: int = 0
    item_event_id: int = 0

    members_only: bool = False

    # The colours the reward is dyed when it lands in the fairy's inventory,
    # as color_id from colorAssets.xml. A colourable item stored with 0 comes
    # out grey ("This Color Does Not Exist"), so anything the fairy wears or
    # puts in a room wants real values here; badges and pouch items ignore them.
    # There is no way to read an item's palette off the XML in this repo, so
    # like the reward pairing itself these are picked by hand.
    reward_color1: int = 0
    reward_color2: int = 0

    # Not the same thing as reward_color1/2. This tints the *art standing in
    # the meadow*, and it does it by changing which asset the client asks for:
    # MeadowSpawnableRequest.createUniqueMultiColorID glues these onto the end
    # of the giveaway id, so [1, 2] on giveaway 15122 makes the client look up
    # asset 122001002 instead of 122. Set it only when a multi-colour asset for
    # that exact combination really exists, or nothing loads. Almost always
    # empty.
    color_ids: tuple[int, ...] = ()


@dataclass(frozen=True)
class GiveawayPlacement:
    """One giveaway standing in one meadow at one spot."""

    giveaway_id: int
    zone_id: int
    x: int
    y: int
    enabled: bool = True


# ── the giveaways ────────────────────────────────────────────────────────── #

GIVEAWAY_DEFS: dict[int, GiveawayDef] = {
    definition.giveaway_id: definition
    for definition in (
        GiveawayDef(15122, "Lucky Fish", 11243, event_id=20120802), # event_id being set to this number removes the pinwheel!
        GiveawayDef(15010, "Lucky Goldie", 11099, event_id=20120802), # event_id being set to this number removes the pinwheel!
        GiveawayDef(15084, "Camp Sign Up", 11234),

        GiveawayDef(15235, "Rubber Ducky Tube", 655,
                    reward_color1=228,   # Duckbill Orange
                    reward_color2=226),  # Goldenrod Yellow
    )
}

PLACEMENTS: tuple[GiveawayPlacement, ...] = (
    GiveawayPlacement(15122, zc.SUNFLOWER_GULLY, 85, 1500),
    GiveawayPlacement(15010, zc.HAVENDISH_SQUARE, 1220, 1430),
    GiveawayPlacement(15084, zc.HAVENDISH_SQUARE, 1295, 1007),
    GiveawayPlacement(15235, zc.THE_BALLROOM, 740, 725),
)


def get_giveaway(giveaway_id: int) -> GiveawayDef | None:
    return GIVEAWAY_DEFS.get(giveaway_id)
