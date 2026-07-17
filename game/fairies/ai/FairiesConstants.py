from dataclasses import dataclass
from enum import Enum

# Ingredients - NEED TO BE REFACTORED BUT THEY'RE STILL DEPENDED ON TODO HACK
OAK_LEAVES = 8001
MAPLE_LEAVES = 8002
IVY = 8003
ROSE_PETALS = 8004
DAISY_PETALS = 8005
LILY_PETALS = 8006
BUTTERCUP_PETALS = 8007
SPIDER_SILK = 8008
MEADOW_GRASS = 8009
SUNFLOWER_SEEDS = 8010
ACORNS = 8011
BLUEBERRIES = 8012
DANDELION_FLUFF = 8013
RASPBERRIES = 8014
PINE_NEEDLES = 8015
SNOWFLAKES = 8016
HONEYCOMBS = 8017
TWIGS = 8018
TRUFFLES = 8019
BLUE_GEMS = 8020
YELLOW_GEMS = 8021
FEATHERS = 8022
BITS_OF_METAL = 8023

class Rarity(Enum):
    VERY_COMMON = 1
    COMMON = 2
    AVERAGE = 3
    RARE = 4
    VERY_RARE = 5

@dataclass(frozen=True)
class Ingredient:
    id: int
    rarity: Rarity

INGREDIENTS: dict[str, Ingredient] = {
    "OAK_LEAVES":       Ingredient(8001, Rarity.RARE),
    "MAPLE_LEAVES":     Ingredient(8002, Rarity.COMMON),
    "IVY":              Ingredient(8003, Rarity.VERY_RARE),
    "ROSE_PETALS":      Ingredient(8004, Rarity.RARE),
    "DAISY_PETALS":     Ingredient(8005, Rarity.COMMON),
    "LILY_PETALS":      Ingredient(8006, Rarity.VERY_RARE),
    "BUTTERCUP_PETALS": Ingredient(8007, Rarity.AVERAGE),
    "SPIDER_SILK":      Ingredient(8008, Rarity.VERY_COMMON),
    "MEADOW_GRASS":     Ingredient(8009, Rarity.AVERAGE),
    "SUNFLOWER_SEEDS":  Ingredient(8010, Rarity.VERY_COMMON),
    "ACORNS":           Ingredient(8011, Rarity.RARE),
    "BLUEBERRIES":      Ingredient(8012, Rarity.AVERAGE),
    "DANDELION_FLUFF":  Ingredient(8013, Rarity.VERY_COMMON),
    "RASPBERRIES":      Ingredient(8014, Rarity.COMMON),
    "PINE_NEEDLES":     Ingredient(8015, Rarity.AVERAGE),
    "SNOWFLAKES":       Ingredient(8016, Rarity.VERY_COMMON),
    "HONEYCOMBS":       Ingredient(8017, Rarity.AVERAGE),
    "TWIGS":            Ingredient(8018, Rarity.VERY_COMMON),
    "TRUFFLES":         Ingredient(8019, Rarity.VERY_COMMON),
    "BLUE_GEMS":        Ingredient(8020, Rarity.RARE),
    "YELLOW_GEMS":      Ingredient(8021, Rarity.AVERAGE),
    "FEATHERS":         Ingredient(8022, Rarity.COMMON),
    "BITS_OF_METAL":    Ingredient(8023, Rarity.RARE),
}

COLOR_IDS = {
    "Mint Green": 1,
    "Clover Green": 2,
    "Spruce Green": 3,
    "Bluebell Blue": 4,
    "Wysteria Purple": 5,
    "Havendish Blue": 6,
    "Salmon Pink": 7,
    "Watermelon Pink": 8,
    "Daffodil Yellow": 9,
    "Cantaloupe Orange": 10,
    "Marigold Yellow": 11,
    "Tangerine Orange": 12,
    "Coral Pink": 13,
    "Plum Purple": 14,
    "Lilac Purple": 15,
    "Camellia Pink": 16,
    "Tendershoot Green": 17,
    "Waterfall Blue": 18,
    "Sprout Green": 19,
    "Grassblade Green": 20,
    "Zucchini Green": 21,
    "Blue Jay Blue": 22,
    "Breezy Blue": 23,
    "Sky Blue": 24,
    "Peachy Orange": 25,
    "Raspberry Pink": 26,
    "Corn Cob Yellow": 27,
    "Cinnamon Brown": 28,
    "Goldfish Orange": 29,
    "Pumpkin Orange": 30,
    "Sunset Orange": 31,
    "Mulberry Purple": 32,
    "Iris Purple": 33,
    "Primrose Pink": 34,
    "Celery Green": 35,
    "Hydrangea Blue": 36,
    "Cloudy Blue": 37,
    "Apple Green": 38,
    "Springtime Green": 39,
    "Candy Blue": 40,
    "Moonshadow Blue": 41,
    "Blueberry Blue": 42,
    "Violet Purple": 43,
    "Plumblossom Pink": 44,
    "Strawberry Red": 45,
    "Bark Brown": 46,
    "Buttercup Yellow": 47,
    "Sea Green": 48,
    "Robin Egg Blue": 49,
    "Cornflower Blue": 50,
    "Periwinkle Blue": 51,
    "Lavender Purple": 52,
    "Hyacinth Pink": 53,
    "Peony Pink": 54,
    "Pepper Black": 55,
    "Bole Brown": 56,
    "Adobe Brown": 57,
    "Terracotta Brown": 58,
    "Bunny Brown": 59,
    "Tyrian Purple": 60,
    "Pale Lilac Purple": 61,
    "Bluebird Blue": 62,
    "Butterfly Blue": 63,
    "Emerald Green": 64,
    "Summer Green": 65,
    "Cactus Green": 66,
    "Chartreuse Green": 67,
    "Huckleberry Blue": 68,
    "Powder Blue": 69,
    "Tinker Blue": 70,
    "Dewdrop Blue": 71,
    "Mauve Purple": 72,
    "Grape Purple": 73,
    "Soil Brown": 74,
    "Umber Brown": 75,
    "Chocolate Brown": 76,
    "Sepia Brown": 77,
    "Fawn Brown": 78,
    "Sienna Brown": 79,
    "Pomegranate Purple": 80,
    "Crimson Red": 81,
    "Raspberry Red": 82,
    "Cherry Brown": 83,
    "Copper Brown": 84,
    "Quail Brown": 85,
    "Nutmeg Brown": 86,
    "Driftwood Brown": 87,
    "Fruitwood Brown": 88,
    "Seashore Brown": 89,
    "Custard Yellow": 90,
    "Coconut Brown": 91,
    "Hawk Brown": 92,
    "Maple Brown": 93,
    "Ochre Brown": 94,
    "Sparrow Brown": 95,
    "Almond Brown": 96,
    "Pebble Tan": 97,
    "Sandstone Tan": 98,
    "Papyrus Tan": 99,
    "Golden Tan": 100,
    "Walnut Tan": 101,
    "Beach Tan": 102,
    "Peachy Tan": 103,
    "Ginger Tan": 104,
    "Siltstone Tan": 105,
    "Butternut Tan": 106,
    "Rosy Tan": 107,
    "Creamy Tan": 108,
    "Soft Orange": 109,
    "Rosy Pink": 110,
    "Sparkling Yellow": 111,
    "Splashy Blue": 112,
    "Pale Rose Red": 113,
    "Foxtail Orange": 114,
    "Asparagus Green": 115,
    "Mushroom White": 116,
    "Amethyst Purple": 117,
    "Sapphire Blue": 118,
    "Petunia Purple": 119,
    "Fern Green": 120,
    "Daisy Pink": 121,
    "Lettuce Leaf Green": 122,
    "Squash Orange": 123,
    "Forget-Me-Not Blue": 124,
    "Pine Green": 125,
    "Raindrop Blue": 126,
    "Grasshopper Green": 127,
    "Carnation White": 128,
    "Fig Purple": 129,
    "Orchid Pink": 130,
    "Plumeria Pink": 131,
    "Bubble Blue": 132,
    "Marina Blue": 133,
    "Heather Purple": 134,
    "Boysenberry Purple": 135,
    "Peacock Blue": 136,
    "Lemon Yellow": 137,
    "Persimmon Orange": 138,
    "Seedling Green": 139,
    "Bunnynose Pink": 140,
    "Thundercloud Gray": 141,
    "Bumble Bee Yellow": 142,
    "June Bug Green": 143,
    "Petal Pink": 144,
    "Tinker Bell Green": 145,
    "Beech Brown": 146,
    "Broccoli Stem Green": 147,
    "Pots'n'Pans Purple": 148,
    "Snowflake Blue": 149,
    "Dry Moss Green": 150,
    "Peanut Yellow": 151,
    "Pale Purple": 152,
    "Frostbunny Blue": 153,
    "Beetle Brown": 154,
    "Frosty Blue": 155,
    "Friendship Pink": 156,
    "Starry White": 157,
    "Icicle Blue": 158,
    "Tea Green": 159,
    "Tender Root Tan": 160,
    "Buried Treasure Brown": 161,
    "Sunglow Yellow": 162,
    "Tundra Blue": 163,
    "Shoreline Tan": 164,
    "Spring Breeze Green": 165,
    "Snow White": 166,
    "Never Silver": 167,
    "Never Gold": 168,
    "Squirrel Gray": 169,
    "Olive Green": 170,
    "Sunrise Yellow": 171,
    "Forest Green": 172,
    "Carrot Orange": 173,
    "Rosetta Red": 174,
    "Creek Green": 175,
    "Silvermist Blue": 176,
    "Mud Brown": 177,
    "Fawn Orange": 178,
    "Iridessa Yellow": 179,
    "Seashell Blue": 180,
    "Cupcake Pink": 181,
    "Twilight Blue": 182,
    "Vidia Purple": 183,
    "Hummingbird Purple": 184,
    "Midnight Blue": 185,
    "Honeycomb Yellow": 186,
    "Maple Orange": 187,
    "Dahlia Pink": 188,
    "Ladybug Red": 189,
    "Firefly Green": 190,
    "Vidia Black": 191,
    "Royal Purple": 192,
    "Electric Green": 193,
    "Electric Pink": 194,
    "Electric Blue": 195,
    "Electric Orange": 196,
    "Electric Purple": 197,
    "Electric Yellow": 198,
    "Cherryblossom Pink": 199,
    "Ruby Pink": 200,
    "Velvet Red": 201,
    "Honeydew Green": 202,
    "Shadow Green": 203,
    "Bamboo Green": 204,
    "Myrtle Green": 205,
    "Raven Black": 206,
    "Diamond Blue": 207,
    "Cerulean Blue": 208,
    "Deep Sea Blue": 209,
    "Lotus Purple": 210,
    "Gentian Purple": 211,
    "Indigo Purple": 212,
    "Cobalt Blue": 213,
    "Smokey Gray": 214,
    "Pewter Gray": 215,
    "Slate Gray": 216,
    "Soft Gray": 217,
    "Laurel Green": 218,
    "Crystal Blue": 219,
    "Dusty Pink": 220,
    "Jade Green": 221,
    "Keylime Green": 222,
    "Teal Blue": 223,
    "Ivory White": 224,
    "Eggplant Purple": 225,
    "Goldenrod Yellow": 226,
    "Moonlight Gray": 227,
    "Duckbill Orange": 228,
    "Electric Indigo": 229,
    "Scarlet Red": 230,
    "Sunny Orange": 231,
    "Rusty Orange": 232,
    "Apricot Orange": 233,
    "Flame Orange": 234,
    "Tawny Orange": 235,
    "Dusty Brown": 236,
    "Melon Orange": 237,
    "Zesty Orange": 238,
    "Coffee Black": 239,
    "Ironwood Brown": 240,
    "Desert Brown": 241,
    "Amber Yellow": 242,
    "Harvest Yellow": 243,
    "Fairygold Yellow": 244,
    "Earthy Tan": 245,
    "Bear Brown": 246,
    "Jasmine Yellow": 247,
    "Saffron Yellow": 248,
    "Antique Yellow": 249,
    "Caramel Tan": 250,
    "Polished Brown": 251,
    "Starshine Yellow": 252,
    "Dandelion Yellow": 253,
    "Sunflower Yellow": 254,
    "Canary Yellow": 255,
    "Pear Yellow": 256,
    "Lime Green": 257,
    "Spearmint Green": 258,
    "Kiwi Green": 259,
    "Peridot Green": 260,
    "Kelly Green": 261,
    "Minty White": 262,
    "Aquamarine Green": 263,
    "Jungle Green": 264,
    "Bright Sky Blue": 265,
    "Ocean Blue": 266,
    "Celestial Blue": 267,
    "Navy Blue": 268,
    "Crisp White": 269,
    "Horizon Blue": 270,
    "True Blue": 271,
    "Charcoal Gray": 272,
    "Panther Black": 273,
    "Bellflower Purple": 274,
    "Shadowy Purple": 275,
    "Dusk Purple": 276,
    "Misty Purple": 277,
    "Aster Purple": 278,
    "Kingfisher Purple": 279,
    "Berry Purple": 280,
    "Deep Violet Purple": 281,
    "Magnolia White": 282,
    "Thistle Pink": 283,
    "Deep Magenta Purple": 284,
    "Jazzberry Red": 285,
    "Cherry Pink": 286,
    "Dianthus Red": 287,
    "Sparkle Pink": 288,
    "Pink": 498,
    "Any Color": 499,
}

ITEM_TYPES = [
    "Shirt",       # 0
    "Belt",        # 1
    "Skirt",       # 2
    "WristItem",   # 3
    "HeadItem",    # 4
    "Necklace",    # 5
    "AnkleItem",   # 6
    "Shoes",       # 7
    "Eyes",        # 8
    "Face",        # 9
    "HairFront",   # 10
    "HairBack",    # 11
    "Wings",       # 12
    "Furniture",   # 13
    "Lamp",        # 14
    "Decoration",  # 15
]

# The types the client files under storage rather than the wardrobe
# (Util.getCategory -> CATEGORY_STORAGE).
STORAGE_ITEM_TYPES = ("Furniture", "Lamp", "Decoration")

# A dye's itemId is its COLOR_IDS value plus this.
DYE_ITEM_ID_OFFSET = 14000

# An expression sets a face and its matching eye; the eye's itemId is the
# face's plus this.
FACE_TO_EYE_OFFSET = -500

# A home's itemId minus this is the fairy's homeType, so 29001-29026 are
# homeType 1-26. The client derives the same number as
# TYPE_HOME_PREVIEW_ID (58) * IDS_PER_TYPE (500).
HOME_ITEM_ID_OFFSET = 29000

def get_item_type(itemId: int) -> str:
    if itemId <= 0:
        raise ValueError(f"Invalid item_id: {itemId}")
    
    bucket = itemId // 500
    
    # Handle the extended prefix case (e.g. 1000100 -> 100)
    if bucket >= len(ITEM_TYPES):
        itemId = int(str(itemId)[1:])
        bucket = itemId // 500
    
    if bucket >= len(ITEM_TYPES):
        raise ValueError(f"Invalid item_id: {itemId}")
    
    return ITEM_TYPES[bucket]