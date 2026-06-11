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
# Exclusion Zones
#
# Keep-out rectangles around gateways/signs/shops. Auto-generated from
# GatewayConstants plus hand-tuned overrides in _MANUAL_EXCLUSIONS_BY_ZONE.
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


def exclusion_rect_around(
    origin_x: int,
    origin_y: int,
    padding: int = DEFAULT_SIGN_PADDING,
    sign_width: int = DEFAULT_SIGN_WIDTH,
    sign_height: int = DEFAULT_SIGN_HEIGHT,
) -> SpawnExclusionZone:
    """Build a keep-out rectangle from the upper-left corner of a sign/gateway."""
    half_w = sign_width // 2
    half_h = sign_height // 2
    center_x = origin_x + half_w
    center_y = origin_y + half_h
    return SpawnExclusionZone(
        center_x - half_w - padding,
        center_x + half_w + padding,
        center_y - half_h - padding,
        center_y + half_h + padding,
    )


def _build_gateway_exclusions(zone_id: int) -> tuple[SpawnExclusionZone, ...]:
    """Derive keep-out rectangles from GatewayConstants.GATEWAYS[zone_id] positions."""
    exclusions: list[SpawnExclusionZone] = []

    for gw in gc.GATEWAYS.get(zone_id, []):
        if gw["name"] in _MANUAL_EXCLUSION_GATEWAY_NAMES:
            continue

        x, y = gw["position"]
        sign_w, sign_h = gw.get("sign_size", (DEFAULT_SIGN_WIDTH, DEFAULT_SIGN_HEIGHT))
        padding = gw.get("padding", DEFAULT_SIGN_PADDING)
        exclusions.append(exclusion_rect_around(x, y, padding, sign_w, sign_h))

    return tuple(exclusions)


_MANUAL_EXCLUSION_GATEWAY_NAMES = frozenset({
    # Spring
    "9017", "9302",  # Cherry Blossom Heights
    "9170", "9009", "9011",  # Springtime Orchard
    "9025", "9021", "9303",  # Dewdrop Vale
    "9286", "9205",  # Neverberry Thicket
    # Summer
    "9216", "9299",  # Palm Tree Cove
    "9146", "9147",  # Sunflower Gully
    "9278",  # Neverfruit Grove
    # Autumn
    "9023", "9228", "9024",  # Acorn Summit
    "9210", "9145",  # Cottonpuff Field
    "9154", "9012", "9301",  # Maple Tree Hill
    "9015",  # Pumpkin Patch
    # Winter
    "9246", "9144", "9126",  # Snowcap Glade
    "9125", "9280",  # Evergreen Overlook
    "9124", "9269",  # Chilly Falls
    # Havendish Square
    "9282", "9214", "9267", "9179", "9188", "9180", "9206", "9028",
})

_MANUAL_EXCLUSIONS_BY_ZONE: dict[int, tuple[SpawnExclusionZone, ...]] = {
    # --- Spring ---
    zc.CHERRYBLOSSOM_HEIGHTS: (
        _sign(1345, 570),  # 9017 Daisy's Dyes
        _sign(880, 815, margin_top=145, margin_bottom=145, margin_left=95),  # 9302 Troop Butterfly
    ),
    zc.SPRINGTIME_ORCHARD: (
        exclusion_footprint(-10, 420, 130, 120, margin_top=30, margin_right=30, margin_bottom=30, margin_left=20),  # 9170 Havendish sign
        _sign(1460, 853, margin_right=70),  # 9009 Firefly Light Up
        _sign(390, 765, margin_right=145),  # 9011 Bobbin's Tailoring
    ),
    zc.DEWDROP_VALE: (
        _sign(920, 1210),  # 9025 Silvermist's Grotto
        _sign(544, 810),  # 9021 Garden Supply (shop entrance, not gateway coord)
        _sign(483, 330, margin_top=70, margin_bottom=70),  # 9303 Troop Otter
    ),
    zc.NEVERBERRY_THICKET: (
        _sign(1183, 324, margin_bottom=70, margin_left=145),  # 9286 Harmony's Sweet Shop
        _sign(1596, 595, margin_top=70, margin_right=70, margin_bottom=70, margin_left=70),  # 9205 Elixa's Hospital
    ),
    # --- Summer ---
    zc.PALM_TREE_COVE: (
        _sign(1707, 602, margin_top=95, margin_left=95),  # 9216 Butterfly Painter
        _sign(406, 571, margin_right=545, margin_bottom=295),  # 9299 Prism's Pixie Spa
    ),
    zc.SUNFLOWER_GULLY: (
        _sign(285, 1030, margin_left=15),  # 9146 Iridessa's Glade
        _sign(508, 756, margin_top=245, margin_right=245),  # 9147 Phoebe's Party Favors
    ),
    zc.NEVERFRUIT_GROVE: (
        exclusion_footprint(380, 130, 150, 170, margin_top=75, margin_right=375, margin_bottom=100, margin_left=25),  # 9278 Pixie Post Office
    ),
    # --- Autumn ---
    zc.ACORN_SUMMIT: (
        _sign(964, 452, margin_top=70, margin_right=220, margin_bottom=95, margin_left=70),  # 9023 Summit Style
        _sign(1017, 185, margin_right=95, margin_bottom=70),  # 9228 Vidia's Daily Spin
        _sign(460, 52, margin_right=95, margin_bottom=95),  # 9024 Fairy Fireworks
    ),
    zc.COTTONPUFF_FIELD: (
        _sign(646, 433, margin_top=-5, margin_right=145, margin_bottom=145, margin_left=145),  # 9210 Coal's Clothiers
        _sign(672, 745),  # 9145 Tinker Toss
    ),
    zc.MAPLE_TREE_HILL: (
        _sign(482, 940, margin_top=145, margin_right=15, margin_bottom=95, margin_left=245),  # 9154 Copper's Tinkering
        _sign(738, 1318, margin_top=95, margin_bottom=95, margin_left=95),  # 9012 Mendy's Tailoring
        _sign(575, 280, margin_top=95, margin_right=70, margin_bottom=70, margin_left=70),  # 9301 Troop Rabbit
    ),
    zc.PUMPKIN_PATCH: (
        _sign(980, 670, margin_right=95),  # 9015 Harvest Hustle
    ),
    # --- Winter ---
    zc.SNOWCAP_GLADE: (
        _sign(239, 124),  # 9246 Pinecone Pop
        _sign(1830, 550, margin_right=70),  # 9144 Snowy Lullaby
        _sign(1509, 215, margin_top=145, margin_bottom=20, margin_left=220),  # 9126 Gale's Outfitters
    ),
    zc.EVERGREEN_OVERLOOK: (
        _sign(645, 1500, margin_top=70, margin_left=95),  # 9125 Snowflake Sweep
        _sign(908, 1057, margin_top=120, margin_left=120),  # 9280 Kit's Place
    ),
    zc.CHILLY_FALLS: (
        _sign(960, 831, margin_left=345),  # 9124 Ember's Essentials
        _sign(1001, 1096, margin_bottom=195, margin_left=270),  # 9269 Gem Juggle
    ),
    # --- Havendish Square ---
    zc.HAVENDISH_SQUARE: (
        exclusion_footprint(40, 223, 220, 200, margin_top=5, margin_right=40, margin_bottom=50, margin_left=10),  # 9282 Queen's Boutique
        exclusion_footprint(250, 300, 310, 280, margin_top=5, margin_right=55, margin_bottom=60, margin_left=20),  # 9214 Cassie's Costume Shop
        exclusion_footprint(200, 860, 240, 360, margin_top=20, margin_right=35, margin_bottom=25, margin_left=90),  # 9267 Pixie Dust Mill
        exclusion_footprint(940, 460, 420, 420, margin_top=80, margin_right=90, margin_bottom=90, margin_left=110),  # 9179 Fairy Tale Theater
        exclusion_footprint(1170, 300, 250, 350, margin_top=90, margin_right=80, margin_bottom=80, margin_left=100),  # 9188 Ballroom
        exclusion_rect(1870, 2140, 300, 610),  # 9180 Tearoom
        exclusion_footprint(1600, 900, 120, 130, margin_top=40, margin_right=35, margin_bottom=15, margin_left=35),  # 9206 Pixie Postings
        exclusion_footprint(1960, 720, 110, 120, margin_top=35, margin_right=35, margin_bottom=35, margin_left=35),  # 9028 Springtime Orchard sign
    ),
}

ZONE_EXCLUSIONS: dict[int, tuple[SpawnExclusionZone, ...]] = {
    zone_id: _MANUAL_EXCLUSIONS_BY_ZONE.get(zone_id, ()) + _build_gateway_exclusions(zone_id)
    for zone_id in ZONE_MAP_BOUNDS
}


# =============================================================================
# Pool Builder
#
# Assembles ActiveSpawnPool configs consumed by IngredientSpawnMgrAI at startup.
# =============================================================================

# TEMP — per-zone acorn density test (zone_id -> stack count). Clear when done tuning.
SPAWN_DENSITY_TEST_ZONES: dict[int, int] = {}


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

    for zone_id, stack_count in SPAWN_DENSITY_TEST_ZONES.items():
        bounds = ZONE_MAP_BOUNDS.get(zone_id)
        if bounds is None:
            continue

        notify.warning(
            "SPAWN_DENSITY_TEST_ZONES: spawning %d acorns in zone %d"
            % (stack_count, zone_id)
        )
        pools.append(
            ActiveSpawnPool(
                zone_id=zone_id,
                item_id=fc.ACORNS,
                display_name="Acorn",
                rarity=Rarity.MOST_COMMON,
                bounds=bounds,
                max_stacks=stack_count,
                respawn_min_sec=9999,
                respawn_max_sec=9999,
                exclusions=ZONE_EXCLUSIONS.get(zone_id, ()),
            )
        )

    return pools
