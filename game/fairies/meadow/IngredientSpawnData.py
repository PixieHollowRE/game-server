from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import NamedTuple

from direct.directnotify import DirectNotifyGlobal
from game.fairies.ai import FairiesConstants as fc
from game.fairies.ai import ZoneConstants as zc
from game.fairies.gateway import GatewayConstants as gc

notify = DirectNotifyGlobal.directNotify.newCategory("IngredientSpawnData")

# Rewrite by Saturn and Em - Multiplayer Bunches by Jessi

class SpawnBounds(NamedTuple):
    x_min: int
    x_max: int
    y_min: int
    y_max: int

SpawnExclusionZone = SpawnBounds

class Rarity(Enum):
    VERY_COMMON = auto()
    COMMON = auto()
    AVERAGE = auto()
    RARE = auto()
    VERY_RARE = auto()

@dataclass(frozen=True)
class RaritySpawnSettings:
    spawn_limit: int
    respawn_min_sec: int
    respawn_max_sec: int

@dataclass(frozen=True)
class IngredientSpawnDef:
    item_id: int
    display_name: str
    rarity: Rarity
    zones: tuple[int, ...]
    enabled: bool = True

# An ingredient eligible to appear as a bunch, and where. No rarity: bunch
# density is a per-zone budget (MP_BUNCHES_PER_ZONE), not a per-ingredient one.
@dataclass(frozen=True)
class MPBunchSpawnDef:
    item_id: int
    display_name: str
    zones: tuple[int, ...]
    enabled: bool = True

class SpawnItem(NamedTuple):
    item_id: int
    display_name: str

@dataclass(frozen=True)
class ActiveSpawnPool:
    zone_id: int
    item_id: int
    display_name: str
    rarity: Rarity | None
    bounds: SpawnBounds
    spawn_limit: int
    respawn_min_sec: int
    respawn_max_sec: int
    exclusions: tuple[SpawnExclusionZone, ...] = ()
    items: tuple[SpawnItem, ...] = ()  # bunch pools only; spawn() draws one per stack
    multiplayer: bool = False

# Meadows
AUTUMN_MEADOWS = (
    zc.ACORN_SUMMIT,
    zc.MAPLE_TREE_HILL,
    zc.COTTONPUFF_FIELD,
    zc.PUMPKIN_PATCH,
)

SPRING_MEADOWS = (
    zc.SPRINGTIME_ORCHARD,
    zc.TREETOP_BEND,
    zc.NEVERBERRY_THICKET,
    zc.CHERRYBLOSSOM_HEIGHTS,
    zc.DEWDROP_VALE,
)

WINTER_MEADOWS = (
    zc.CHILLY_FALLS,
    zc.EVERGREEN_OVERLOOK,
    zc.SNOWCAP_GLADE,
)

SUMMER_MEADOWS = (
    zc.PALM_TREE_COVE,
    zc.NEVERFRUIT_GROVE,
    zc.SUNFLOWER_GULLY,
)

HAVENDISH_SQUARE = (zc.HAVENDISH_SQUARE,)

# Ingredient spawn zones
INGREDIENT_SPAWNS: tuple[IngredientSpawnDef, ...] = (
    # Very Common
    IngredientSpawnDef(fc.TWIGS, "Twigs", Rarity.VERY_COMMON, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.SNOWFLAKES, "Snowflakes", Rarity.VERY_COMMON, WINTER_MEADOWS),
    IngredientSpawnDef(fc.DANDELION_FLUFF, "Dandelion Fluff", Rarity.VERY_COMMON, AUTUMN_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.SPIDER_SILK, "Spider Silk", Rarity.VERY_COMMON, SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.SUNFLOWER_SEEDS, "Sunflower Seeds", Rarity.VERY_COMMON, SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    # Common
    IngredientSpawnDef(fc.MAPLE_LEAVES, "Maple Leaf", Rarity.COMMON, AUTUMN_MEADOWS),
    IngredientSpawnDef(fc.RASPBERRIES, "Raspberries", Rarity.COMMON, SPRING_MEADOWS + (zc.NEVERFRUIT_GROVE,)),
    IngredientSpawnDef(fc.DAISY_PETALS, "Daisy Petals", Rarity.COMMON, SPRING_MEADOWS + SUMMER_MEADOWS),
    # Average
    IngredientSpawnDef(fc.BLUEBERRIES, "Blueberries", Rarity.AVERAGE, AUTUMN_MEADOWS),
    IngredientSpawnDef(fc.BUTTERCUP_PETALS, "Buttercup Petals", Rarity.AVERAGE, SPRING_MEADOWS),
    IngredientSpawnDef(fc.HONEYCOMBS, "Honeycombs", Rarity.AVERAGE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.MEADOW_GRASS, "Meadow Grass", Rarity.AVERAGE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.PINE_NEEDLES, "Pine Needles", Rarity.AVERAGE, WINTER_MEADOWS + (zc.ACORN_SUMMIT,)),
    # Rare
    IngredientSpawnDef(fc.ACORNS, "Acorn", Rarity.RARE, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.OAK_LEAVES, "Oak Leaves", Rarity.RARE, AUTUMN_MEADOWS + (zc.SNOWCAP_GLADE,)),
    IngredientSpawnDef(fc.ROSE_PETALS, "Rose Petals", Rarity.RARE, SPRING_MEADOWS),
    # Very Rare
    IngredientSpawnDef(fc.IVY, "Ivy Leaves", Rarity.VERY_RARE, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.LILY_PETALS, "Lily Petals", Rarity.VERY_RARE, SPRING_MEADOWS + SUMMER_MEADOWS),
)

# for Wilderness
FUTURE_INGREDIENT_SPAWNS: tuple[IngredientSpawnDef, ...] = (
    IngredientSpawnDef(fc.TRUFFLES, "Truffles", Rarity.VERY_COMMON, (), enabled=False),
    IngredientSpawnDef(fc.FEATHERS, "Feathers", Rarity.COMMON, (), enabled=False),
    IngredientSpawnDef(fc.YELLOW_GEMS, "Yellow Gems", Rarity.AVERAGE, (), enabled=False),
    IngredientSpawnDef(fc.BLUE_GEMS, "Blue Gems", Rarity.AVERAGE, (), enabled=False),
    IngredientSpawnDef(fc.BITS_OF_METAL, "Bits of Metal", Rarity.RARE, (), enabled=False),
)

# Multiplayer bunches — DistributedMultiplayerSpawnStackAI instead of a plain
# stack. First fairy to click starts a shared countdown; everyone who joins
# before it expires is paid out, multiplied by how many joined (capped at 5).
#
# item_id is the ordinary ingredient — the client remaps it to bunch art via
# <spawnableIdRemaps> in spawnableAssets.xml, so an ingredient can only appear
# here if it has a remap entry (see BUNCH_ASSET_IDS below). Zones mirror each
# ingredient's entry in INGREDIENT_SPAWNS — keep them in sync.

# Kill switch — False stops all bunch pools without touching the table below.
MP_BUNCHES_ENABLED = True

# Bunches a zone keeps up at once, drawn at random from the ingredients that
# zone grows. One pool per zone, not one per ingredient, so adding a row below
# widens variety without adding bunches.
MP_BUNCHES_PER_ZONE = 2

# Jittered so a collected bunch doesn't reappear on a predictable beat.
MP_BUNCH_RESPAWN_MIN_SEC = 300
MP_BUNCH_RESPAWN_MAX_SEC = 480

MP_BUNCH_SPAWNS: tuple[MPBunchSpawnDef, ...] = (
    MPBunchSpawnDef(fc.ACORNS, "Acorn Bunch", AUTUMN_MEADOWS + WINTER_MEADOWS),
    MPBunchSpawnDef(fc.BLUEBERRIES, "Blueberry Bunch", AUTUMN_MEADOWS),
    MPBunchSpawnDef(fc.BUTTERCUP_PETALS, "Buttercup Bunch", SPRING_MEADOWS),
    MPBunchSpawnDef(fc.DAISY_PETALS, "Daisy Bunch", SPRING_MEADOWS + SUMMER_MEADOWS),
    MPBunchSpawnDef(fc.DANDELION_FLUFF, "Dandelion Fluff Bunch", AUTUMN_MEADOWS + HAVENDISH_SQUARE),
    MPBunchSpawnDef(fc.HONEYCOMBS, "Honeycomb Bunch", SPRING_MEADOWS + SUMMER_MEADOWS),
    MPBunchSpawnDef(fc.IVY, "Ivy Bunch", AUTUMN_MEADOWS + WINTER_MEADOWS),
    MPBunchSpawnDef(fc.LILY_PETALS, "Lily Bunch", SPRING_MEADOWS + SUMMER_MEADOWS),
    MPBunchSpawnDef(fc.MAPLE_LEAVES, "Maple Leaf Bunch", AUTUMN_MEADOWS),
    MPBunchSpawnDef(fc.MEADOW_GRASS, "Meadow Grass Bunch", SPRING_MEADOWS + SUMMER_MEADOWS),
    MPBunchSpawnDef(fc.OAK_LEAVES, "Oak Leaf Bunch", AUTUMN_MEADOWS + (zc.SNOWCAP_GLADE,)),
    MPBunchSpawnDef(fc.PINE_NEEDLES, "Pine Needle Bunch", WINTER_MEADOWS + (zc.ACORN_SUMMIT,)),
    MPBunchSpawnDef(fc.RASPBERRIES, "Raspberry Bunch", SPRING_MEADOWS + (zc.NEVERFRUIT_GROVE,)),
    MPBunchSpawnDef(fc.ROSE_PETALS, "Rose Bunch", SPRING_MEADOWS),
    MPBunchSpawnDef(fc.SNOWFLAKES, "Snowflake Bunch", WINTER_MEADOWS),
    MPBunchSpawnDef(fc.SPIDER_SILK, "Spider Silk Bunch", SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    MPBunchSpawnDef(fc.SUNFLOWER_SEEDS, "Sunflower Seed Bunch", SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    MPBunchSpawnDef(fc.TWIGS, "Twig Bunch", AUTUMN_MEADOWS + WINTER_MEADOWS),
)

# Mirrors <spawnableIdRemaps> in spawnableAssets.xml: ingredient -> bunch asset
# the client swaps in. A bunch whose ingredient is absent here renders as
# nothing, so bunchAssetErrorHandler() refuses to let it spawn. Truffles,
# Feathers and Bits of Metal are deliberately absent — no bunch art.
BUNCH_ASSET_IDS: dict[int, int] = {
    fc.OAK_LEAVES: 8039,
    fc.MAPLE_LEAVES: 8030,
    fc.IVY: 8040,
    fc.ROSE_PETALS: 8041,
    fc.DAISY_PETALS: 8026,
    fc.LILY_PETALS: 8037,
    fc.BUTTERCUP_PETALS: 8025,
    fc.SPIDER_SILK: 8034,
    fc.MEADOW_GRASS: 8028,
    fc.SUNFLOWER_SEEDS: 8035,
    fc.ACORNS: 8038,
    fc.BLUEBERRIES: 8024,
    fc.DANDELION_FLUFF: 8027,
    fc.RASPBERRIES: 8032,
    fc.PINE_NEEDLES: 8031,
    fc.SNOWFLAKES: 8033,
    fc.HONEYCOMBS: 8029,
    fc.TWIGS: 8036,
    fc.BLUE_GEMS: 8042,
    fc.YELLOW_GEMS: 8043,
}

# Spawn times
RARITY_SPAWN_SETTINGS: dict[Rarity, RaritySpawnSettings] = {
    Rarity.VERY_COMMON: RaritySpawnSettings(spawn_limit=7, respawn_min_sec=120, respawn_max_sec=120),
    Rarity.COMMON: RaritySpawnSettings(spawn_limit=5, respawn_min_sec=120, respawn_max_sec=120),
    Rarity.AVERAGE: RaritySpawnSettings(spawn_limit=3, respawn_min_sec=180, respawn_max_sec=180),
    Rarity.RARE: RaritySpawnSettings(spawn_limit=2, respawn_min_sec=180, respawn_max_sec=180),
    Rarity.VERY_RARE: RaritySpawnSettings(spawn_limit=1, respawn_min_sec=240, respawn_max_sec=240),
}

# Spawn areas
SPAWN_EDGE_MARGIN = 100

def mapArea(width: int, height: int, margin: int = SPAWN_EDGE_MARGIN) -> SpawnBounds:
    return SpawnBounds(margin, width - margin, margin, height - margin)

ZONE_MAP_BOUNDS: dict[int, SpawnBounds] = {
    # Spring
    zc.CHERRYBLOSSOM_HEIGHTS: mapArea(1907, 1131),
    zc.SPRINGTIME_ORCHARD: mapArea(1922, 1130),
    zc.DEWDROP_VALE: mapArea(1402, 1589),
    zc.NEVERBERRY_THICKET: mapArea(2021, 1190),
    zc.TREETOP_BEND: mapArea(1711, 1489),
    # Summer
    zc.PALM_TREE_COVE: mapArea(1960, 1204),
    zc.SUNFLOWER_GULLY: mapArea(1115, 1603),
    zc.NEVERFRUIT_GROVE: mapArea(1464, 1000),
    # Autumn
    zc.ACORN_SUMMIT: mapArea(1896, 1115),
    zc.COTTONPUFF_FIELD: mapArea(1895, 1307),
    zc.MAPLE_TREE_HILL: mapArea(1269, 1827),
    zc.PUMPKIN_PATCH: mapArea(1733, 1019),
    # Winter
    zc.EVERGREEN_OVERLOOK: mapArea(1271, 1827),
    zc.SNOWCAP_GLADE: mapArea(2548, 1011),
    zc.CHILLY_FALLS: mapArea(1255, 1781),
    # Havendish
    zc.HAVENDISH_SQUARE: mapArea(2166, 1509),
}

def zoneMapArea(zone_id: int) -> SpawnBounds:
    return ZONE_MAP_BOUNDS[zone_id]

# Control where items spawn

DEFAULT_SIGN_WIDTH = 96
DEFAULT_SIGN_HEIGHT = 100
DEFAULT_SIGN_PADDING = 45

def ingredientBlocker(x_min: int, x_max: int, y_min: int, y_max: int) -> SpawnExclusionZone:
    return SpawnExclusionZone(x_min, x_max, y_min, y_max)

def blockOrigin(
    origin_x: int,
    origin_y: int,
    width: int,
    height: int,
    *,
    margin_top: int = 30,
    margin_right: int = 30,
    margin_bottom: int = 30,
    margin_left: int = 30,
) -> SpawnExclusionZone:
    return ingredientBlocker(
        origin_x - margin_left,
        origin_x + width + margin_right,
        origin_y - margin_top,
        origin_y + height + margin_bottom,
    )

def sign(
    origin_x: int,
    origin_y: int,
    *,
    margin_top: int = DEFAULT_SIGN_PADDING,
    margin_right: int = DEFAULT_SIGN_PADDING,
    margin_bottom: int = DEFAULT_SIGN_PADDING,
    margin_left: int = DEFAULT_SIGN_PADDING,
) -> SpawnExclusionZone:
    return blockOrigin(
        origin_x,
        origin_y,
        DEFAULT_SIGN_WIDTH,
        DEFAULT_SIGN_HEIGHT,
        margin_top=margin_top,
        margin_right=margin_right,
        margin_bottom=margin_bottom,
        margin_left=margin_left,
    )

SPAWN_BLOCK: dict[int, dict[str, SpawnExclusionZone]] = {
    # --- Spring ---
    zc.CHERRYBLOSSOM_HEIGHTS: {
        "9014": sign(385, 100, margin_right=85, margin_bottom=110, margin_left=245),  # Petal Pick-Up
        "9149": sign(90, 555, margin_right=85, margin_bottom=245),  # Rosetta's Garden
        "9017": sign(1345, 570, margin_top=195, margin_right=70, margin_left=195),  # Daisy's Dyes
        "9302": sign(880, 815, margin_top=195, margin_right=95, margin_bottom=195, margin_left=145),  # Troop Butterfly Hideout
    },
    zc.SPRINGTIME_ORCHARD: {
        "9170": blockOrigin(-10, 420, 130, 120, margin_top=30, margin_right=30, margin_bottom=30, margin_left=20),  # Havendish sign
        "9009": sign(1460, 853, margin_top=70, margin_right=145, margin_bottom=95),  # Firefly Light Up
        "9011": sign(390, 765, margin_right=195, margin_bottom=195),  # Bobbin's Tailoring
        "9203": sign(402, 338, margin_top=85, margin_right=85, margin_bottom=165, margin_left=195),  # Beck's Animal Nursery
    },
    zc.DEWDROP_VALE: {
        "9025": sign(920, 1210, margin_top=70, margin_left=85),  # Silvermist's Grotto
        "9021": sign(544, 810, margin_top=195, margin_bottom=85, margin_left=235),  # Garden Supply
        "9303": sign(483, 330, margin_top=160, margin_right=95, margin_bottom=120, margin_left=135),  # Troop Otter Hideout
        "9010": sign(100, 1190, margin_right=195, margin_bottom=195),  # Bubble Bounce
        "9053": sign(1125, 910, margin_right=75),  # Neverberry Thicket sign
        "9031": sign(98, 410, margin_right=70, margin_bottom=69),  # Springtime Orchard sign
    },
    zc.NEVERBERRY_THICKET: {
        "9286": sign(1183, 324, margin_top=120, margin_right=70, margin_bottom=70, margin_left=220),  # Harmony's Sweet Shop
        "9205": sign(1596, 595, margin_top=120, margin_right=70, margin_bottom=125, margin_left=120),  # Elixa's Hospital
        "9013": sign(1750, 705, margin_right=145, margin_bottom=195, margin_left=70),  # Water Web
        "9155": sign(850, 710, margin_right=145, margin_bottom=120, margin_left=70),  # Dulcie's Baking
    },
    zc.TREETOP_BEND: {
        "9019": blockOrigin(341, 1067, 96, 100, margin_top=95, margin_right=245, margin_bottom=145, margin_left=95),  # Bella's Baubles
        "9187": blockOrigin(1365, 985, 96, 100, margin_top=70, margin_right=155, margin_bottom=310, margin_left=70),  # Seed Sorting
        "9020": blockOrigin(1019, 648, 96, 100, margin_top=120, margin_right=195, margin_bottom=195, margin_left=170),  # Treetop Housewares
        "9224": blockOrigin(422, 238, 96, 100, margin_top=45, margin_right=445, margin_bottom=195, margin_left=45),  # Neville's New Homes
    },
    # --- Summer ---
    zc.PALM_TREE_COVE: {
        "9216": sign(1707, 602, margin_top=145, margin_bottom=195, margin_left=150),  # Butterfly Painter
        "9299": sign(406, 571, margin_top=145, margin_right=545, margin_bottom=295),  # Prism's Pixie Spa
        "9148": sign(406, 571, margin_top=145, margin_right=545, margin_bottom=295),  # Schelly's Hair Salon
        "9045": sign(1630, 233),  # Dewdrop Vale sign
        "9159": sign(205, 215),  # Neverfruit Grove sign
        "9247": sign(1450, 795, margin_right=120, margin_bottom=270),  # Mermaid Grotto
    },
    zc.SUNFLOWER_GULLY: {
        "9146": sign(285, 1030, margin_top=75, margin_right=105, margin_bottom=75, margin_left=15),  # Iridessa's Glade
        "9147": sign(508, 756, margin_top=245, margin_right=245, margin_bottom=95),  # Phoebe's Party Favors
        "9079": sign(220, 1437, margin_top=55, margin_right=75),  # Cottonpuff Field sign
        "9272": ingredientBlocker(800, 1150, 850, 1250),  # Sunbeam Bend game area
        "9305": sign(905, 640, margin_top=115, margin_right=95, margin_bottom=95, margin_left=95),  # Troop Glowworm Hideout
    },
    zc.NEVERFRUIT_GROVE: {
        "9278": blockOrigin(380, 130, 150, 170, margin_top=75, margin_right=375, margin_bottom=100, margin_left=25),  # Pixie Post Office
        "9209": sign(1202, 462, margin_top=95, margin_right=95, margin_bottom=195),  # First Flight
    },
    # --- Autumn ---
    zc.ACORN_SUMMIT: {
        "9023": sign(964, 452, margin_top=90, margin_right=270, margin_bottom=125, margin_left=70),  # Summit Style
        "9228": sign(1017, 185, margin_right=125, margin_bottom=70, margin_left=75),  # Vidia's Daily Spin
        "9024": sign(460, 52, margin_right=135, margin_bottom=125, margin_left=145),  # Fairy Fireworks
    },
    zc.COTTONPUFF_FIELD: {
        "9210": sign(646, 433, margin_top=-5, margin_right=145, margin_bottom=145, margin_left=145),  # Coal's Clothiers
        "9145": sign(672, 745, margin_right=145, margin_bottom=195, margin_left=65),  # Tinker Toss
        "9026": sign(1715, 765, margin_top=95, margin_right=95, margin_bottom=95, margin_left=95),  # Tinker's Nook
        "9304": sign(330, 815, margin_top=145, margin_right=145, margin_bottom=145, margin_left=145),  # Troop Turtle Hideout
    },
    zc.MAPLE_TREE_HILL: {
        "9154": sign(482, 940, margin_top=145, margin_right=15, margin_bottom=135, margin_left=285),  # Copper's Tinkering
        "9012": sign(738, 1318, margin_top=95, margin_bottom=145, margin_left=145),  # Mendy's Tailoring
        "9301": sign(575, 280, margin_top=175, margin_right=120, margin_bottom=120, margin_left=120),  # Troop Rabbit Hideout
        "9027": sign(342, 1740, margin_top=145, margin_left=145),  # Fawn's Hideout
        "9028": sign(1075, 445),  # Springtime Orchard sign
    },
    zc.PUMPKIN_PATCH: {
        "9015": sign(980, 670, margin_top=95, margin_right=245, margin_bottom=145, margin_left=95),  # Harvest Hustle
    },
    # --- Winter ---
    zc.SNOWCAP_GLADE: {
        "9246": sign(239, 124, margin_top=95, margin_right=125, margin_bottom=195, margin_left=145),  # Pinecone Pop
        "9144": sign(1830, 550, margin_right=270, margin_bottom=145, margin_left=85),  # Snowy Lullaby
        "9126": sign(1509, 215, margin_top=145, margin_bottom=20, margin_left=220),  # Gale's Outfitters
        "9075": sign(201, 632, margin_right=65, margin_bottom=65),  # Acorn Summit sign
    },
    zc.EVERGREEN_OVERLOOK: {
        "9125": sign(645, 1500, margin_top=120, margin_right=65, margin_bottom=165, margin_left=175),  # Snowflake Sweep
        "9280": sign(908, 1057, margin_top=120, margin_left=120),  # Kit's Place
        "9291": sign(720, 320, margin_top=195, margin_bottom=95, margin_left=125),  # Frosted Forest sign
    },
    zc.CHILLY_FALLS: {
        "9124": sign(960, 831, margin_left=345),  # Ember's Essentials
        "9269": sign(1001, 1096, margin_bottom=195, margin_left=270),  # Gem Juggle
    },
    # --- Havendish Square ---
    zc.HAVENDISH_SQUARE: {
        "9282": blockOrigin(40, 223, 220, 200, margin_top=5, margin_right=40, margin_bottom=50, margin_left=10),  # Queen's Boutique
        "9214": blockOrigin(250, 300, 310, 280, margin_top=5, margin_right=105, margin_bottom=60, margin_left=20),  # Cassie's Costume Shop
        "9267": blockOrigin(200, 860, 240, 360, margin_top=20, margin_right=35, margin_bottom=25, margin_left=90),  # Pixie Dust Mill
        "9179": blockOrigin(940, 460, 420, 420, margin_top=80, margin_right=90, margin_bottom=90, margin_left=110),  # Fairy Tale Theater
        "9188": blockOrigin(1170, 300, 250, 350, margin_top=90, margin_right=80, margin_bottom=80, margin_left=100),  # Ballroom
        "9180": ingredientBlocker(1870, 2140, 300, 610),  # Tearoom
        "9206": sign(1635, 949, margin_top=145, margin_right=95, margin_left=195),  # Pixie Postings
        "9028": blockOrigin(1960, 760, 110, 120, margin_top=35, margin_right=35, margin_bottom=35, margin_left=35),  # Springtime Orchard sign
    },
}

def makeIngredientBlocker(zone_id: int) -> tuple[SpawnExclusionZone, ...]:
    tuned = SPAWN_BLOCK.get(zone_id, {})
    exclusions: list[SpawnExclusionZone] = []

    for gw in gc.GATEWAYS.get(zone_id, ()):
        gw_id = gw["name"]
        if gw_id in tuned:
            exclusions.append(tuned[gw_id])
            continue

        x, y = gw["position"]
        exclusions.append(sign(x, y))

    return tuple(exclusions)

ZONE_EXCLUSIONS: dict[int, tuple[SpawnExclusionZone, ...]] = {
    zone_id: makeIngredientBlocker(zone_id)
    for zone_id in ZONE_MAP_BOUNDS
}

# Ingredient pools
SPAWN_DENSITY_TEST_ZONES: dict[int, tuple[int, int]] = {}

def ingredientName(item_id: int) -> str:
    for ingredient in INGREDIENT_SPAWNS + FUTURE_INGREDIENT_SPAWNS:
        if ingredient.item_id == item_id:
            return ingredient.display_name
    return "Ingredient"

def ingredientErrorHandler() -> None:
    missing: set[int] = set()

    for spawn_def in INGREDIENT_SPAWNS + MP_BUNCH_SPAWNS:
        if not spawn_def.enabled:
            continue

        for zone_id in spawn_def.zones:
            if zone_id not in ZONE_MAP_BOUNDS:
                missing.add(zone_id)

    if missing:
        raise ValueError(
            "Missing ZONE_MAP_BOUNDS for zone IDs: %s"
            % ", ".join(str(z) for z in sorted(missing))
        )

def bunchAssetErrorHandler() -> None:
    unrenderable = sorted(
        bunch.item_id
        for bunch in MP_BUNCH_SPAWNS
        if bunch.enabled and bunch.item_id not in BUNCH_ASSET_IDS
    )

    if unrenderable:
        raise ValueError(
            "MP_BUNCH_SPAWNS item IDs have no bunch asset to remap to: %s"
            % ", ".join(str(i) for i in unrenderable)
        )

def makeIngredientSpawn() -> list[ActiveSpawnPool]:
    ingredientErrorHandler()
    bunchAssetErrorHandler()

    pools: list[ActiveSpawnPool] = []

    for ingredient in INGREDIENT_SPAWNS:
        if not ingredient.enabled:
            continue

        settings = RARITY_SPAWN_SETTINGS[ingredient.rarity]

        for zone_id in ingredient.zones:
            if zone_id in SPAWN_DENSITY_TEST_ZONES:
                continue

            bounds = ZONE_MAP_BOUNDS.get(zone_id)
            if bounds is None:
                continue

            pools.append(
                ActiveSpawnPool(
                    zone_id=zone_id,
                    item_id=ingredient.item_id,
                    display_name=ingredient.display_name,
                    rarity=ingredient.rarity,
                    bounds=bounds,
                    spawn_limit=settings.spawn_limit,
                    respawn_min_sec=settings.respawn_min_sec,
                    respawn_max_sec=settings.respawn_max_sec,
                    exclusions=ZONE_EXCLUSIONS.get(zone_id, ()),
                )
            )

    for zone_id, test_config in SPAWN_DENSITY_TEST_ZONES.items():
        bounds = ZONE_MAP_BOUNDS.get(zone_id)
        if bounds is None:
            continue

        item_id, stack_count = test_config
        display_name = ingredientName(item_id)

        notify.warning(
            "SPAWN_DENSITY_TEST_ZONES: spawning %d %s (item %d) in zone %d"
            % (stack_count, display_name, item_id, zone_id)
        )
        pools.append(
            ActiveSpawnPool(
                zone_id=zone_id,
                item_id=item_id,
                display_name=display_name,
                rarity=Rarity.VERY_COMMON,
                bounds=bounds,
                spawn_limit=stack_count,
                respawn_min_sec=9999,
                respawn_max_sec=9999,
                exclusions=ZONE_EXCLUSIONS.get(zone_id, ()),
            )
        )

    return pools

# Bunch pools — one per zone, holding every bunch that zone grows. Each pool
# keeps MP_BUNCHES_PER_ZONE bunches up and draws its ingredient at random from
# candidates on respawn, so a collected bunch comes back as a fresh roll.
def makeBunchSpawn() -> list[ActiveSpawnPool]:
    candidates: dict[int, list[SpawnItem]] = {}

    for bunch in MP_BUNCH_SPAWNS:
        if not bunch.enabled:
            continue

        for zone_id in bunch.zones:
            if zone_id in SPAWN_DENSITY_TEST_ZONES:
                continue

            if zone_id not in ZONE_MAP_BOUNDS:
                continue

            candidates.setdefault(zone_id, []).append(
                SpawnItem(bunch.item_id, bunch.display_name)
            )

    return [
        ActiveSpawnPool(
            zone_id=zone_id,
            item_id=0,
            display_name="Bunch",
            rarity=None,
            bounds=ZONE_MAP_BOUNDS[zone_id],
            spawn_limit=MP_BUNCHES_PER_ZONE,
            respawn_min_sec=MP_BUNCH_RESPAWN_MIN_SEC,
            respawn_max_sec=MP_BUNCH_RESPAWN_MAX_SEC,
            exclusions=ZONE_EXCLUSIONS.get(zone_id, ()),
            items=tuple(items),
            multiplayer=True,
        )
        for zone_id, items in sorted(candidates.items())
    ]
