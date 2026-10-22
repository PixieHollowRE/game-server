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

    # Several giveaways may share one art id (the trick-or-treat pumpkins all use
    # 15128), so the once-only record needs its own number; 0 means giveaway_id
    claim_id: int = 0

    # Collectable only through TrickOrTreat; a click on the stack is refused
    phrase_only: bool = False

    event_id: int = 0
    holiday_bit: int = 0
    item_event_id: int = 0

    members_only: bool = False

    # Reward dye as colorAssets color_id; 0 on a colorable item comes out gray
    reward_color1: int = 0
    reward_color2: int = 0

    # Pouch rewards only; wardrobe and storage grants are always one item
    reward_amount: int = 1

    # Tints the meadow art, not the reward: the client appends these to the id
    # (createUniqueMultiColorID), so only set a combination whose asset exists
    color_ids: tuple[int, ...] = ()

    @property
    def key(self) -> int:
        """What this giveaway is recorded under in `giveawaysCollected`."""
        return self.claim_id or self.giveaway_id


@dataclass(frozen=True)
class GiveawayPlacement:
    """One giveaway standing in one meadow at one spot."""

    # GiveawayDef.key, not necessarily its art id
    key: int
    zone_id: int
    x: int
    y: int
    enabled: bool = True


# ── the giveaways ────────────────────────────────────────────────────────── #

# The 2012 Animal Masquerade pumpkins. All twelve draw 15128's tiny marker art,
# and each is told apart by its reward, which is also what the pumpkin hotspot's
# eligibleGiveAwayId names. Rewards and colors are from the wiki; where it names
# one color the second repeats it, unless the shop sells the item in that color.
PUMPKIN_ART_ID = 15128
PUMPKIN_EVENT_ID = 20120802  # removes the pinwheel backdrop, like the two fish

PUMPKIN_ORANGE = 30
ELECTRIC_ORANGE = 196
VIDIA_BLACK = 191


def _pumpkin(reward_item_id: int, display_name: str, **fields) -> GiveawayDef:
    return GiveawayDef(
        PUMPKIN_ART_ID, display_name, reward_item_id,
        claim_id=reward_item_id, phrase_only=True, event_id=PUMPKIN_EVENT_ID,
        **fields,
    )


GIVEAWAY_DEFS: dict[int, GiveawayDef] = {
    definition.key: definition
    for definition in (
        #GiveawayDef(15122, "Lucky Fish", 11243, event_id=20120802), # event_id being set to this number removes the pinwheel!
        #GiveawayDef(15010, "Lucky Goldie", 11099, event_id=20120802), # event_id being set to this number removes the pinwheel!
        #GiveawayDef(15084, "Camp Sign Up", 11234),

        #GiveawayDef(15235, "Rubber Ducky Tube", 655,
        #            reward_color1=228,   # Duckbill Orange
        #            reward_color2=226),  # Goldenrod Yellow
        GiveawayDef(15191, "Candy Corn Silly Sweet", 22570),

        _pumpkin(89014, "Autumn Masquerade Dye Seeds"),
        _pumpkin(2227, "Jack o' Lantern Headpiece",
                 reward_color1=ELECTRIC_ORANGE, reward_color2=ELECTRIC_ORANGE),
        _pumpkin(22543, "Bubble Trail Silly Sweet", reward_amount=3),
        _pumpkin(7830, "Jack O'Lantern Stand",
                 reward_color1=PUMPKIN_ORANGE, reward_color2=239),  # Coffee Black trim
        _pumpkin(2237, "Spider Web Veil Hat",
                 reward_color1=VIDIA_BLACK, reward_color2=VIDIA_BLACK),
        _pumpkin(22548, "Shrinking Silly Sweet", reward_amount=3),
        _pumpkin(89022, "Autumn Breeze Seeds"),
        _pumpkin(7828, "Silly Scarecrow",
                 reward_color1=PUMPKIN_ORANGE, reward_color2=PUMPKIN_ORANGE),
        _pumpkin(7045, "Spider Web Lantern",
                 reward_color1=VIDIA_BLACK, reward_color2=VIDIA_BLACK),
        _pumpkin(7044, "Gourd Lights",
                 reward_color1=PUMPKIN_ORANGE, reward_color2=35),  # Celery Green trim
        _pumpkin(22551, "Sunflower Cupcake", reward_amount=3),
        _pumpkin(22549, "Growing Silly Sweet", reward_amount=3),
    )
}

# Pumpkin x,y: center of its body (see TrickOrTreat.PUMPKIN_BODIES), not the hotspot corner
PLACEMENTS: tuple[GiveawayPlacement, ...] = (
    #GiveawayPlacement(15122, zc.SUNFLOWER_GULLY, 85, 1500),
    #GiveawayPlacement(15010, zc.HAVENDISH_SQUARE, 1220, 1430),
    #GiveawayPlacement(15084, zc.HAVENDISH_SQUARE, 1295, 1007),
    #GiveawayPlacement(15235, zc.THE_BALLROOM, 740, 725),

    GiveawayPlacement(15191, zc.THE_BALLROOM, 575, 655),
    GiveawayPlacement(89014, zc.CHERRYBLOSSOM_HEIGHTS, 1047, 758),
    GiveawayPlacement(2227, zc.SPRINGTIME_ORCHARD, 1000, 850),
    GiveawayPlacement(22543, zc.DEWDROP_VALE, 448, 1288),
    GiveawayPlacement(7830, zc.NEVERBERRY_THICKET, 1075, 920),
    GiveawayPlacement(2237, zc.TREETOP_BEND, 863, 1258),
    GiveawayPlacement(22548, zc.ACORN_SUMMIT, 586, 778),
    GiveawayPlacement(89022, zc.PUMPKIN_PATCH, 692, 542),
    GiveawayPlacement(7828, zc.EVERGREEN_OVERLOOK, 227, 1223),
    GiveawayPlacement(7045, zc.SNOWCAP_GLADE, 1948, 379),
    GiveawayPlacement(7044, zc.CHILLY_FALLS, 416, 510),
    GiveawayPlacement(22551, zc.PALM_TREE_COVE, 1403, 882),
    GiveawayPlacement(22549, zc.NEVERFRUIT_GROVE, 869, 600),
)


def get_giveaway(giveaway_id: int) -> GiveawayDef | None:
    return GIVEAWAY_DEFS.get(giveaway_id)
