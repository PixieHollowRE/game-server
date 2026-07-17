from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import NamedTuple
import game.fairies.ai.FairiesConstants as fc

FREE_ACORNS = 1
MEMBER_ACORNS = 3

# ────────────────────────────────── EXCLUDE MASK ──────────────────────────────────── #
# Bits the client packs into requestDailyChance, from MMOConstants in mmo.swf.
# The two badge bits are ignored -- the client has none for Mr. Twitches, who was
# added later, so earned badges are read from the fairy instead. See
# DistributedFairyPlayerAI._dailyChanceExcludedBadges.
EXCLUDE_VIDIA_LUCK_BADGE = 1
EXCLUDE_SOUR_PLUM_BADGE = 2
EXCLUDE_WARDROBE = 4
EXCLUDE_STORAGE = 8

# ─────────────────────────────────────── ENUMS ────────────────────────────────────── #
# An IntEnum because these values arrive as plain ints on FairyDNA.gender, which
# is what the client packs (FairiesConstants.GENDER_FEMALE/GENDER_MALE in
# framework.swf). A plain Enum would compare unequal to those ints and quietly
# filter every gendered item out of the pool.
class Gender(IntEnum):
    FAIRY = 1
    SPARROW = 2

class Category(Enum):
    WARDROBE = "wardrobe"
    HOME = "home"
    INGREDIENT = "ingredient"
    BADGE = "badge"
    DYE = "dye"
    COOKIE = "cookie"

# ────────────────────────────────────── WEIGHTS ───────────────────────────────────── #
DEFAULT_WEIGHT_BY_RARITY = {
    fc.Rarity.VERY_COMMON: 250, # Currently Unused - just here to mimic the full fc.Rarity Table
    fc.Rarity.COMMON: 100,
    fc.Rarity.AVERAGE: 40,
    fc.Rarity.RARE: 10,
    fc.Rarity.VERY_RARE: 1,
}

DEFAULT_RARITY_BY_CATEGORY: dict[Category, fc.Rarity] = {
    Category.INGREDIENT:  fc.Rarity.COMMON,
    Category.DYE:         fc.Rarity.AVERAGE,
    Category.COOKIE:      fc.Rarity.AVERAGE,
    Category.HOME:        fc.Rarity.RARE,
    Category.WARDROBE:    fc.Rarity.RARE,
}

# ──────────────────────────────────── POOL CONSTS ─────────────────────────────────── #
SPIN_INGREDIENTS = [ing.id for ing in fc.INGREDIENTS.values()]

# Based on the ingredient's rarity (not it's rarity in the pool),
# determines how many to award the player.
INGR_RARITY_TO_PRIZE_AMOUNT = {
    fc.Rarity.VERY_COMMON: 15,
    fc.Rarity.COMMON: 10,
    fc.Rarity.AVERAGE: 8,
    fc.Rarity.RARE: 5,
    fc.Rarity.VERY_RARE: 5,
}

COOKIE_RARITY_TO_PRIZE_AMOUNT = {
    fc.Rarity.VERY_COMMON: 6,
    fc.Rarity.COMMON: 4,
    fc.Rarity.AVERAGE: 3,
    fc.Rarity.RARE: 2,
    fc.Rarity.VERY_RARE: 1,
}

SPIN_DYES = [
    14183, # Vidia Purple
    14052, # Lavender Purple
    14043, # Violet Purple
    14129, # Fig Purple
    # - NEW - 
    14073, # Grape Purple
    14275, # Shadowy Purple
    14276, # Dusk Purple
    14055, # Pepper Black
    14191, # Vidia Black
    14206, # Raven Black
    14273, # Panther Black
]

class SpinBadge(NamedTuple):
    id: int
    rarity: fc.Rarity

SPIN_BADGE_IDS = {
    "BADGE_SOUR_PLUM": SpinBadge(10903, fc.Rarity.AVERAGE),
    "BADGE_LUCKY_PURPLE_FEATHERS": SpinBadge(10902, fc.Rarity.RARE),
    "BADGE_SNEAKY_MR_TWITCHES": SpinBadge(11130, fc.Rarity.VERY_RARE),
}

SPIN_BADGE_ID_SET = {badge.id for badge in SPIN_BADGE_IDS.values()}

# What the Rocks/Rock and Roll/Rock Star badges count ("awarded for winning
# #GOAL# rocks in Vidia's Daily Spin"). Only the River Rock below is treated as
# one; the Jack-O-Lantern Rock in SPIN_HOME_ITEMS is a holiday item that happens
# to be rock-shaped. Add it here if it should count too.
SPIN_ROCK_ITEM_IDS = {7665}

SPIN_WARDROBE_FAIRIES = [ # TODO: These all only have one color, will have to do secondaries
    {"itemId": 2136, "c1": 141, "c2": 183},
    {"itemId": 181,  "c1": 183, "c2": 183}, 
    {"itemId": 576,  "c1": 60,  "c2": 60},
    {"itemId": 1163, "c1": 183, "c2": 183},
    {"itemId": 3614, "c1": 183, "c2": 183},
    {"itemId": 2166, "c1": 191, "c2": 183},
    {"itemId": 210,  "c1": 191, "c2": 183},
    {"itemId": 1178, "c1": 191, "c2": 183},
    {"itemId": 2166, "c1": 191, "c2": 46},
    {"itemId": 210,  "c1": 191, "c2": 46},
    {"itemId": 1178, "c1": 191, "c2": 46},
    {"itemId": 2216, "c1": 55,  "c2": 141}, 
    {"itemId": 2209, "c1": 141, "c2": 141},
    {"itemId": 2216, "c1": 55,  "c2": 259},
    {"itemId": 2209, "c1": 55,  "c2": 121},
    {"itemId": 2209, "c1": 55,  "c2": 54},
    {"itemId": 2209, "c1": 141, "c2": 110},
    {"itemId": 1657, "c1": 162, "c2": 162},
    {"itemId": 1656, "c1": 162, "c2": 162},
]

SPIN_WARDROBE_SPARROWS = [ # TODO: These all only have one color, will have to do secondaries
    {"itemId": 2136, "c1": 141, "c2": 183},
    {"itemId": 174,  "c1": 183, "c2": 183},
    {"itemId": 573,  "c1": 60,  "c2": 60},
    {"itemId": 1158, "c1": 183, "c2": 183},
    {"itemId": 3611, "c1": 183, "c2": 183},
    {"itemId": 2167, "c1": 191, "c2": 183},
    {"itemId": 211,  "c1": 191, "c2": 183},
    {"itemId": 1179, "c1": 191, "c2": 183},
    {"itemId": 2167, "c1": 191, "c2": 46},
    {"itemId": 211,  "c1": 191, "c2": 46},
    {"itemId": 1179, "c1": 191, "c2": 46},
    {"itemId": 2228, "c1": 55,  "c2": 55},
    {"itemId": 2215, "c1": 141, "c2": 141},
    {"itemId": 2228, "c1": 55,  "c2": 259},
    {"itemId": 2215, "c1": 55,  "c2": 55},
    {"itemId": 2304, "c1": 55,  "c2": 54},
    {"itemId": 2215, "c1": 141, "c2": 110},
    {"itemId": 1654, "c1": 162, "c2": 162},
    {"itemId": 1655, "c1": 162, "c2": 162},
]

SPIN_HOME_ITEMS = [
    {"itemId": 6655, "c1": 33,  "c2": 33},
    {"itemId": 6654, "c1": 183, "c2": 183},
    {"itemId": 6734, "c1": 46,  "c2": 46},
    {"itemId": 6735, "c1": 116, "c2": 116},
    {"itemId": 6734, "c1": 116, "c2": 116},
    {"itemId": 7028, "c1": 46,  "c2": 46},
    {"itemId": 7640, "c1": 46,  "c2": 46},
    {"itemId": 7616, "c1": 129, "c2": 129},
    {"itemId": 7639, "c1": 17,  "c2": 17},
    {"itemId": 7641, "c1": 60,  "c2": 60},
    {"itemId": 7598, "c1": 183, "c2": 183},
    {"itemId": 7668, "c1": 183, "c2": 183},
    {"itemId": 7667, "c1": 183, "c2": 183},
    {"itemId": 7728, "c1": 30,  "c2": 30},
    {"itemId": 7738, "c1": 13,  "c2": 13},
    {"itemId": 7734, "c1": 191, "c2": 191},
    {"itemId": 7785, "c1": 186, "c2": 186},
    # - ROCKS -
    # "rarity" overrides the category default (RARE) for the draw. The rocks are
    # the one home item with badges counting them, and at RARE the numbers those
    # badges ask for don't arrive: six variants at weight 10 is 1.6% of the pool,
    # or one rock every ~20 member spins, putting Rock Star's 50 about 2.8 years
    # out -- against 100 spins for Flitterific Daily Spin Challenger next to it
    # on the same page. COMMON is what makes the page finish together: a rock
    # every ~2.4 spins, so the 5/20/50 tiers land at roughly 12/49/121 spins.
    {"itemId": 7665, "c1": 37,  "c2": 37,  "rarity": fc.Rarity.COMMON},
    {"itemId": 7665, "c1": 150, "c2": 150, "rarity": fc.Rarity.COMMON},
    {"itemId": 7665, "c1": 116, "c2": 116, "rarity": fc.Rarity.COMMON},
    {"itemId": 7665, "c1": 61,  "c2": 61,  "rarity": fc.Rarity.COMMON},
    {"itemId": 7665, "c1": 110, "c2": 110, "rarity": fc.Rarity.COMMON},
    {"itemId": 7665, "c1": 109, "c2": 109, "rarity": fc.Rarity.COMMON},
]

SPIN_COOKIES = [
    {"itemId": 22501, "rarity": fc.Rarity.VERY_COMMON}, # Acorn Cookie (10)
    {"itemId": 22502, "rarity": fc.Rarity.VERY_COMMON}, # Sunflower Cookie (20)
    {"itemId": 22503, "rarity": fc.Rarity.VERY_COMMON}, # Honey Cookie (30)
    {"itemId": 22504, "rarity": fc.Rarity.COMMON}, # Raspberry (40)
    {"itemId": 22505, "rarity": fc.Rarity.COMMON}, # Blueberry (50)
    {"itemId": 22506, "rarity": fc.Rarity.COMMON}, # Honey Maple (60)
    {"itemId": 22507, "rarity": fc.Rarity.AVERAGE}, # Truffle (70)
    {"itemId": 22508, "rarity": fc.Rarity.AVERAGE}, # Honey Truffle (80)
    {"itemId": 22509, "rarity": fc.Rarity.AVERAGE}, # Raspberry Truffle (90)
    {"itemId": 22510, "rarity": fc.Rarity.AVERAGE}, # Blueberry Truffle (100)
    {"itemId": 22532, "rarity": fc.Rarity.RARE}, # Sunflower Double Truffle (120)
    {"itemId": 22533, "rarity": fc.Rarity.RARE}, # Honey Double Truffle (150)
    {"itemId": 22534, "rarity": fc.Rarity.RARE}, # Raspberry Double Truffle (180)
    {"itemId": 22535, "rarity": fc.Rarity.RARE}, # Blueberry Double Truffle (210)
    {"itemId": 22542, "rarity": fc.Rarity.VERY_RARE}, # Honey Maple Double Truffle (240)
]


