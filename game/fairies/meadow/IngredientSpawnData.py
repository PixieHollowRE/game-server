from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import NamedTuple

from direct.directnotify import DirectNotifyGlobal
from game.fairies.ai import FairiesConstants as fc
from game.fairies.ai import ZoneConstants as zc
from game.fairies.gateway import GatewayConstants as gc

notify = DirectNotifyGlobal.directNotify.newCategory("IngredientSpawnData")


# =============================================================================
# Types
# =============================================================================

class SpawnBounds(NamedTuple):
    x_min: int
    x_max: int
    y_min: int
    y_max: int


SpawnExclusionZone = SpawnBounds


class Rarity(Enum):
    MOST_COMMON = auto()
    COMMON = auto()
    AVERAGE = auto()
    RARE = auto()
    VERY_RARE = auto()


@dataclass(frozen=True)
class RaritySpawnSettings:
    max_stacks: int
    respawn_min_sec: int
    respawn_max_sec: int


@dataclass(frozen=True)
class IngredientSpawnDef:
    item_id: int
    display_name: str
    rarity: Rarity
    zones: tuple[int, ...]
    enabled: bool = True


@dataclass(frozen=True)
class ActiveSpawnPool:
    zone_id: int
    item_id: int
    display_name: str
    rarity: Rarity
    bounds: SpawnBounds
    max_stacks: int
    respawn_min_sec: int
    respawn_max_sec: int
    exclusions: tuple[SpawnExclusionZone, ...] = ()


# =============================================================================
# Meadow Groups
#
# Reusable zone ID tuples referenced by INGREDIENT_SPAWNS.
# =============================================================================

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


# =============================================================================
# Ingredients
#
# Master catalog — item ID, display name, rarity, and eligible meadow zones.
# =============================================================================

INGREDIENT_SPAWNS: tuple[IngredientSpawnDef, ...] = (
    IngredientSpawnDef(fc.ACORNS, "Acorn", Rarity.RARE, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.BLUEBERRIES, "Blueberries", Rarity.AVERAGE, AUTUMN_MEADOWS),
    IngredientSpawnDef(fc.BUTTERCUP_PETALS, "Buttercup Petals", Rarity.AVERAGE, SPRING_MEADOWS),
    IngredientSpawnDef(fc.DAISY_PETALS, "Daisy Petals", Rarity.COMMON, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.DANDELION_FLUFF, "Dandelion Fluff", Rarity.MOST_COMMON, AUTUMN_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.HONEYCOMBS, "Honeycombs", Rarity.AVERAGE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.IVY, "Ivy Leaves", Rarity.VERY_RARE, AUTUMN_MEADOWS + WINTER_MEADOWS),
    IngredientSpawnDef(fc.LILY_PETALS, "Lily Petals", Rarity.VERY_RARE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.MAPLE_LEAVES, "Maple Leaf", Rarity.COMMON, AUTUMN_MEADOWS),
    IngredientSpawnDef(fc.MEADOW_GRASS, "Meadow Grass", Rarity.AVERAGE, SPRING_MEADOWS + SUMMER_MEADOWS),
    IngredientSpawnDef(fc.OAK_LEAVES, "Oak Leaves", Rarity.RARE, AUTUMN_MEADOWS + (zc.SNOWCAP_GLADE,)),
    IngredientSpawnDef(fc.PINE_NEEDLES, "Pine Needles", Rarity.AVERAGE, WINTER_MEADOWS + (zc.ACORN_SUMMIT,)),
    IngredientSpawnDef(fc.RASPBERRIES, "Raspberries", Rarity.COMMON, SPRING_MEADOWS + (zc.NEVERFRUIT_GROVE,)),
    IngredientSpawnDef(fc.ROSE_PETALS, "Rose Petals", Rarity.RARE, SPRING_MEADOWS),
    IngredientSpawnDef(fc.SNOWFLAKES, "Snowflakes", Rarity.MOST_COMMON, WINTER_MEADOWS),
    IngredientSpawnDef(fc.SPIDER_SILK, "Spider Silk", Rarity.MOST_COMMON, SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.SUNFLOWER_SEEDS, "Sunflower Seeds", Rarity.MOST_COMMON, SPRING_MEADOWS + SUMMER_MEADOWS + HAVENDISH_SQUARE),
    IngredientSpawnDef(fc.TWIGS, "Twigs", Rarity.MOST_COMMON, AUTUMN_MEADOWS + WINTER_MEADOWS),
)

# Disabled — enable when zones exist in ZoneConstants + ZONE_MAP_BOUNDS.
FUTURE_INGREDIENT_SPAWNS: tuple[IngredientSpawnDef, ...] = (
    IngredientSpawnDef(fc.TRUFFLES, "Truffles", Rarity.MOST_COMMON, (), enabled=False),
    IngredientSpawnDef(fc.FEATHERS, "Feathers", Rarity.COMMON, (), enabled=False),
    IngredientSpawnDef(fc.YELLOW_GEMS, "Yellow Gems", Rarity.AVERAGE, (), enabled=False),
    IngredientSpawnDef(fc.BLUE_GEMS, "Blue Gems", Rarity.AVERAGE, (), enabled=False),
    IngredientSpawnDef(fc.BITS_OF_METAL, "Bits of Metal", Rarity.RARE, (), enabled=False),
)


# =============================================================================
# Spawn Density
#
# Stack count and respawn seconds per rarity tier (applied to every ingredient).
#
#   Tier         | Stacks/zone | Respawn
#   Most Common  | 7           | 2 min
#   Common       | 5           | 2 min
#   Average      | 3           | 3 min
#   Rare         | 2           | 3 min
#   Very Rare    | 1           | 4 min
# =============================================================================

RARITY_SPAWN_SETTINGS: dict[Rarity, RaritySpawnSettings] = {
    Rarity.MOST_COMMON: RaritySpawnSettings(max_stacks=7, respawn_min_sec=120, respawn_max_sec=120),
    Rarity.COMMON: RaritySpawnSettings(max_stacks=5, respawn_min_sec=120, respawn_max_sec=120),
    Rarity.AVERAGE: RaritySpawnSettings(max_stacks=3, respawn_min_sec=180, respawn_max_sec=180),
    Rarity.RARE: RaritySpawnSettings(max_stacks=2, respawn_min_sec=180, respawn_max_sec=180),
    Rarity.VERY_RARE: RaritySpawnSettings(max_stacks=1, respawn_min_sec=240, respawn_max_sec=240),
}


# =============================================================================
# Zone Map Bounds
#
# Per-meadow spawn rectangle (from config.xml ground layer minus edge margin).
# =============================================================================

SPAWN_EDGE_MARGIN = 100


def _map_bounds(width: int, height: int, margin: int = SPAWN_EDGE_MARGIN) -> SpawnBounds:
    return SpawnBounds(margin, width - margin, margin, height - margin)


ZONE_MAP_BOUNDS: dict[int, SpawnBounds] = {
    # Spring
    zc.CHERRYBLOSSOM_HEIGHTS: _map_bounds(1907, 1131),
    zc.SPRINGTIME_ORCHARD: _map_bounds(1922, 1130),
    zc.DEWDROP_VALE: _map_bounds(1402, 1589),
    zc.NEVERBERRY_THICKET: _map_bounds(2021, 1190),
    zc.TREETOP_BEND: _map_bounds(1711, 1489),
    # Summer
    zc.PALM_TREE_COVE: _map_bounds(1960, 1204),
    zc.SUNFLOWER_GULLY: _map_bounds(1115, 1603),
    zc.NEVERFRUIT_GROVE: _map_bounds(1464, 1000),
    # Autumn
    zc.ACORN_SUMMIT: _map_bounds(1896, 1115),
    zc.COTTONPUFF_FIELD: _map_bounds(1895, 1307),
    zc.MAPLE_TREE_HILL: _map_bounds(1269, 1827),
    zc.PUMPKIN_PATCH: _map_bounds(1733, 1019),
    # Winter
    zc.EVERGREEN_OVERLOOK: _map_bounds(1271, 1827),
    zc.SNOWCAP_GLADE: _map_bounds(2548, 1011),
    zc.CHILLY_FALLS: _map_bounds(1255, 1781),
    # Havendish
    zc.HAVENDISH_SQUARE: _map_bounds(2166, 1509),
}


def zone_map_bounds(zone_id: int) -> SpawnBounds:
    return ZONE_MAP_BOUNDS[zone_id]


# =============================================================================
# Spawn Exclusions
#
# Keep-out rectangles around gateways, games, and shops. Gateways in
# _TUNED_EXCLUSIONS were hand-tuned during the acorn density pass; every other
# gateway in the meadow gets a default sign footprint at its GatewayConstants
# position.
# =============================================================================

DEFAULT_SIGN_WIDTH = 96
DEFAULT_SIGN_HEIGHT = 100
DEFAULT_SIGN_PADDING = 45


def exclusion_rect(x_min: int, x_max: int, y_min: int, y_max: int) -> SpawnExclusionZone:
    return SpawnExclusionZone(x_min, x_max, y_min, y_max)


def exclusion_footprint(
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
    """Keep-out from upper-left anchor + clickable footprint (asymmetric margins allowed)."""
    return exclusion_rect(
        origin_x - margin_left,
        origin_x + width + margin_right,
        origin_y - margin_top,
        origin_y + height + margin_bottom,
    )


def _sign(
    origin_x: int,
    origin_y: int,
    *,
    margin_top: int = DEFAULT_SIGN_PADDING,
    margin_right: int = DEFAULT_SIGN_PADDING,
    margin_bottom: int = DEFAULT_SIGN_PADDING,
    margin_left: int = DEFAULT_SIGN_PADDING,
) -> SpawnExclusionZone:
    """Standard gateway/sign keep-out (96x100 + padding)."""
    return exclusion_footprint(
        origin_x,
        origin_y,
        DEFAULT_SIGN_WIDTH,
        DEFAULT_SIGN_HEIGHT,
        margin_top=margin_top,
        margin_right=margin_right,
        margin_bottom=margin_bottom,
        margin_left=margin_left,
    )


# Hand-tuned keep-outs keyed by gateway ID (see GatewayConstants.GATEWAYS).
_TUNED_EXCLUSIONS: dict[int, dict[str, SpawnExclusionZone]] = {
    # --- Spring ---
    zc.CHERRYBLOSSOM_HEIGHTS: {
        "9014": _sign(385, 100, margin_right=85, margin_bottom=110, margin_left=245),  # Petal Pick-Up
        "9149": _sign(90, 555, margin_right=85, margin_bottom=245),  # Rosetta's Garden
        "9017": _sign(1345, 570, margin_top=195, margin_right=70, margin_left=195),  # Daisy's Dyes
        "9302": _sign(880, 815, margin_top=195, margin_right=95, margin_bottom=195, margin_left=145),  # Troop Butterfly Hideout
    },
    zc.SPRINGTIME_ORCHARD: {
        "9170": exclusion_footprint(-10, 420, 130, 120, margin_top=30, margin_right=30, margin_bottom=30, margin_left=20),  # Havendish sign
        "9009": _sign(1460, 853, margin_top=70, margin_right=145, margin_bottom=95),  # Firefly Light Up
        "9011": _sign(390, 765, margin_right=195, margin_bottom=195),  # Bobbin's Tailoring
        "9203": _sign(402, 338, margin_top=85, margin_right=85, margin_bottom=165, margin_left=195),  # Beck's Animal Nursery
    },
    zc.DEWDROP_VALE: {
        "9025": _sign(920, 1210, margin_top=70, margin_left=85),  # Silvermist's Grotto
        "9021": _sign(544, 810, margin_top=195, margin_bottom=85, margin_left=235),  # Garden Supply
        "9303": _sign(483, 330, margin_top=160, margin_right=95, margin_bottom=120, margin_left=135),  # Troop Otter Hideout
        "9010": _sign(100, 1190, margin_right=195, margin_bottom=195),  # Bubble Bounce
        "9053": _sign(1125, 910, margin_right=75),  # Neverberry Thicket sign
        "9031": _sign(98, 410, margin_right=70, margin_bottom=69),  # Springtime Orchard sign
    },
    zc.NEVERBERRY_THICKET: {
        "9286": _sign(1183, 324, margin_top=120, margin_right=70, margin_bottom=70, margin_left=220),  # Harmony's Sweet Shop
        "9205": _sign(1596, 595, margin_top=120, margin_right=70, margin_bottom=125, margin_left=120),  # Elixa's Hospital
        "9013": _sign(1750, 705, margin_right=145, margin_bottom=195, margin_left=70),  # Water Web
        "9155": _sign(850, 710, margin_right=145, margin_bottom=120, margin_left=70),  # Dulcie's Baking
    },
    zc.TREETOP_BEND: {
        "9019": exclusion_footprint(341, 1067, 96, 100, margin_top=95, margin_right=245, margin_bottom=145, margin_left=95),  # Bella's Baubles
        "9187": exclusion_footprint(1365, 985, 96, 100, margin_top=70, margin_right=155, margin_bottom=310, margin_left=70),  # Seed Sorting
        "9020": exclusion_footprint(1019, 648, 96, 100, margin_top=120, margin_right=195, margin_bottom=195, margin_left=170),  # Treetop Housewares
        "9224": exclusion_footprint(422, 238, 96, 100, margin_top=45, margin_right=445, margin_bottom=195, margin_left=45),  # Neville's New Homes
    },
    # --- Summer ---
    zc.PALM_TREE_COVE: {
        "9216": _sign(1707, 602, margin_top=145, margin_bottom=195, margin_left=150),  # Butterfly Painter
        "9299": _sign(406, 571, margin_top=145, margin_right=545, margin_bottom=295),  # Prism's Pixie Spa
        "9148": _sign(406, 571, margin_top=145, margin_right=545, margin_bottom=295),  # Schelly's Hair Salon
        "9045": _sign(1630, 233),  # Dewdrop Vale sign
        "9159": _sign(205, 215),  # Neverfruit Grove sign
        "9247": _sign(1450, 795, margin_right=120, margin_bottom=270),  # Mermaid Grotto
    },
    zc.SUNFLOWER_GULLY: {
        "9146": _sign(285, 1030, margin_top=75, margin_right=105, margin_bottom=75, margin_left=15),  # Iridessa's Glade
        "9147": _sign(508, 756, margin_top=245, margin_right=245, margin_bottom=95),  # Phoebe's Party Favors
        "9079": _sign(220, 1437, margin_top=55, margin_right=75),  # Cottonpuff Field sign
        "9272": exclusion_rect(800, 1150, 850, 1250),  # Sunbeam Bend game area
        "9305": _sign(905, 640, margin_top=115, margin_right=95, margin_bottom=95, margin_left=95),  # Troop Glowworm Hideout
    },
    zc.NEVERFRUIT_GROVE: {
        "9278": exclusion_footprint(380, 130, 150, 170, margin_top=75, margin_right=375, margin_bottom=100, margin_left=25),  # Pixie Post Office
        "9209": _sign(1202, 462, margin_top=95, margin_right=95, margin_bottom=195),  # First Flight
    },
    # --- Autumn ---
    zc.ACORN_SUMMIT: {
        "9023": _sign(964, 452, margin_top=90, margin_right=270, margin_bottom=125, margin_left=70),  # Summit Style
        "9228": _sign(1017, 185, margin_right=125, margin_bottom=70, margin_left=75),  # Vidia's Daily Spin
        "9024": _sign(460, 52, margin_right=135, margin_bottom=125, margin_left=145),  # Fairy Fireworks
    },
    zc.COTTONPUFF_FIELD: {
        "9210": _sign(646, 433, margin_top=-5, margin_right=145, margin_bottom=145, margin_left=145),  # Coal's Clothiers
        "9145": _sign(672, 745, margin_right=145, margin_bottom=195, margin_left=65),  # Tinker Toss
        "9026": _sign(1715, 765, margin_top=95, margin_right=95, margin_bottom=95, margin_left=95),  # Tinker's Nook
        "9304": _sign(330, 815, margin_top=145, margin_right=145, margin_bottom=145, margin_left=145),  # Troop Turtle Hideout
    },
    zc.MAPLE_TREE_HILL: {
        "9154": _sign(482, 940, margin_top=145, margin_right=15, margin_bottom=135, margin_left=285),  # Copper's Tinkering
        "9012": _sign(738, 1318, margin_top=95, margin_bottom=145, margin_left=145),  # Mendy's Tailoring
        "9301": _sign(575, 280, margin_top=175, margin_right=120, margin_bottom=120, margin_left=120),  # Troop Rabbit Hideout
        "9027": _sign(342, 1740, margin_top=145, margin_left=145),  # Fawn's Hideout
        "9028": _sign(1075, 445),  # Springtime Orchard sign
    },
    zc.PUMPKIN_PATCH: {
        "9015": _sign(980, 670, margin_top=95, margin_right=245, margin_bottom=145, margin_left=95),  # Harvest Hustle
    },
    # --- Winter ---
    zc.SNOWCAP_GLADE: {
        "9246": _sign(239, 124, margin_top=95, margin_right=125, margin_bottom=195, margin_left=145),  # Pinecone Pop
        "9144": _sign(1830, 550, margin_right=270, margin_bottom=145, margin_left=85),  # Snowy Lullaby
        "9126": _sign(1509, 215, margin_top=145, margin_bottom=20, margin_left=220),  # Gale's Outfitters
        "9075": _sign(201, 632, margin_right=65, margin_bottom=65),  # Acorn Summit sign
    },
    zc.EVERGREEN_OVERLOOK: {
        "9125": _sign(645, 1500, margin_top=120, margin_right=65, margin_bottom=165, margin_left=175),  # Snowflake Sweep
        "9280": _sign(908, 1057, margin_top=120, margin_left=120),  # Kit's Place
        "9291": _sign(720, 320, margin_top=195, margin_bottom=95, margin_left=125),  # Frosted Forest sign
    },
    zc.CHILLY_FALLS: {
        "9124": _sign(960, 831, margin_left=345),  # Ember's Essentials
        "9269": _sign(1001, 1096, margin_bottom=195, margin_left=270),  # Gem Juggle
    },
    # --- Havendish Square ---
    zc.HAVENDISH_SQUARE: {
        "9282": exclusion_footprint(40, 223, 220, 200, margin_top=5, margin_right=40, margin_bottom=50, margin_left=10),  # Queen's Boutique
        "9214": exclusion_footprint(250, 300, 310, 280, margin_top=5, margin_right=105, margin_bottom=60, margin_left=20),  # Cassie's Costume Shop
        "9267": exclusion_footprint(200, 860, 240, 360, margin_top=20, margin_right=35, margin_bottom=25, margin_left=90),  # Pixie Dust Mill
        "9179": exclusion_footprint(940, 460, 420, 420, margin_top=80, margin_right=90, margin_bottom=90, margin_left=110),  # Fairy Tale Theater
        "9188": exclusion_footprint(1170, 300, 250, 350, margin_top=90, margin_right=80, margin_bottom=80, margin_left=100),  # Ballroom
        "9180": exclusion_rect(1870, 2140, 300, 610),  # Tearoom
        "9206": _sign(1635, 949, margin_top=145, margin_right=95, margin_left=195),  # Pixie Postings
        "9028": exclusion_footprint(1960, 760, 110, 120, margin_top=35, margin_right=35, margin_bottom=35, margin_left=35),  # Springtime Orchard sign
    },
}


def _build_zone_exclusions(zone_id: int) -> tuple[SpawnExclusionZone, ...]:
    """One keep-out per meadow gateway: tuned box if present, else default sign footprint."""
    tuned = _TUNED_EXCLUSIONS.get(zone_id, {})
    exclusions: list[SpawnExclusionZone] = []

    for gw in gc.GATEWAYS.get(zone_id, ()):
        gw_id = gw["name"]
        if gw_id in tuned:
            exclusions.append(tuned[gw_id])
            continue

        x, y = gw["position"]
        exclusions.append(_sign(x, y))

    return tuple(exclusions)


ZONE_EXCLUSIONS: dict[int, tuple[SpawnExclusionZone, ...]] = {
    zone_id: _build_zone_exclusions(zone_id)
    for zone_id in ZONE_MAP_BOUNDS
}


# =============================================================================
# Pool Builder
# =============================================================================

# Dev-only — {zone_id: (item_id, stack_count)} replaces all normal spawns in that zone.
SPAWN_DENSITY_TEST_ZONES: dict[int, tuple[int, int]] = {}


def _display_name_for_item(item_id: int) -> str:
    for ingredient in INGREDIENT_SPAWNS + FUTURE_INGREDIENT_SPAWNS:
        if ingredient.item_id == item_id:
            return ingredient.display_name
    return "Ingredient"


def _validate_zone_map_bounds() -> None:
    """Raise if any enabled ingredient references a zone missing from ZONE_MAP_BOUNDS."""
    missing: set[int] = set()

    for ingredient in INGREDIENT_SPAWNS:
        if not ingredient.enabled:
            continue

        for zone_id in ingredient.zones:
            if zone_id not in ZONE_MAP_BOUNDS:
                missing.add(zone_id)

    if missing:
        raise ValueError(
            "Missing ZONE_MAP_BOUNDS for zone IDs: %s"
            % ", ".join(str(z) for z in sorted(missing))
        )


def build_active_spawn_pools() -> list[ActiveSpawnPool]:
    """Build runtime spawn configs for every enabled (zone, ingredient) pair."""
    _validate_zone_map_bounds()

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
                    max_stacks=settings.max_stacks,
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
        display_name = _display_name_for_item(item_id)

        notify.warning(
            "SPAWN_DENSITY_TEST_ZONES: spawning %d %s (item %d) in zone %d"
            % (stack_count, display_name, item_id, zone_id)
        )
        pools.append(
            ActiveSpawnPool(
                zone_id=zone_id,
                item_id=item_id,
                display_name=display_name,
                rarity=Rarity.MOST_COMMON,
                bounds=bounds,
                max_stacks=stack_count,
                respawn_min_sec=9999,
                respawn_max_sec=9999,
                exclusions=ZONE_EXCLUSIONS.get(zone_id, ()),
            )
        )

    return pools
