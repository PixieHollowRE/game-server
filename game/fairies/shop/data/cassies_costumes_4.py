from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

# Cassie's - OutfitId 4000 - 4999

SHOP = NPCShop(
    zone=ZoneConstants.CASSIES_COSTUME_SHOP,
    shopId=4,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.CASSIE,
        position=(500, 350),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_CASSIE
    ),
    collections=[
        ShopCollection(
            collectionId=4031, # ToT Baskets
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=1583, price=30, goldPrice=3, color1=228, color2=125, itemType="WristItem"), # Duckbill Orange Trick or Treat Basket
                ShopItem(itemId=1583, price=30, goldPrice=3, color1=216, color2=206, itemType="WristItem"), # Slate Gray Trick or Treat Basket
                ShopItem(itemId=1583, price=30, goldPrice=3, color1=193, color2=197, itemType="WristItem"), # Electric Green Trick or Treat Basket
                ShopItem(itemId=1583, price=30, goldPrice=3, color1=194, color2=195, itemType="WristItem"), # Electric Pink Trick or Treat Basket
                ShopItem(itemId=1583, price=30, goldPrice=3, color1=30, color2=55, itemType="WristItem"), # Pumpkin Orange Trick or Treat Basket
            ],
        ),   
        ShopCollection(
            collectionId=28, # Animal-Inspired Fashions
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            outfits=[
                ShopOutfit(
                    outfitId=4001,
                    items = [
                        OutfitItem(itemId=2073, price=25, goldPrice=10, color1=206, color2=142, itemType="HeadItem"), # Raven Black Buzzy Bee Mask
                        OutfitItem(itemId=76, price=45, goldPrice=16, color1=206, color2=142, itemType="Shirt"), # Raven Black Buzzy Bee Striped Wrap
                        OutfitItem(itemId=1003, price=45, goldPrice=16, color1=142, color2=0, itemType="Skirt"), # Bumble Bee Yellow Leafy Bubble Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=142, color2=0, itemType="Shoes"), # Bumble Bee Yellow Petal Slippers
                    ],
                ),

                ShopOutfit(
                    outfitId=4002,
                    items = [
                        OutfitItem(itemId=2071, price=25, goldPrice=10, color1=44, color2=257, itemType="HeadItem"), # Plumblossom Pink Little Light Antennae
                        OutfitItem(itemId=91, price=45, goldPrice=16, color1=44, color2=44, itemType="Shirt"), # Plumblossom Pink Little Light Top
                        OutfitItem(itemId=1091, price=45, goldPrice=16, color1=44, color2=257, itemType="Skirt"), #  Plumblossom Pink Little Light Mini
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=44, color2=0, itemType="Shoes"), #  Plumblossom Pink Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=4003,
                    items = [
                        OutfitItem(itemId=2071, price=25, goldPrice=10, color1=206, color2=189, itemType="HeadItem"), # Raven Black Little Light Antennae
                        OutfitItem(itemId=172, price=45, goldPrice=16, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tank
                        OutfitItem(itemId=1156, price=45, goldPrice=16, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=189, color2=0, itemType="Shoes"), # Ladybug Red Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=4004,
                    items = [
                        OutfitItem(itemId=2151, price=25, goldPrice=10, color1=193, color2=175, itemType="HeadItem"), # Mint Green Dragonfly Mask
                        OutfitItem(itemId=186, price=45, goldPrice=16, color1=175, color2=193, itemType="Shirt"), # Mint Green Dragonfly Top
                        OutfitItem(itemId=1168, price=45, goldPrice=16, color1=175, color2=193, itemType="Skirt"), # Mint Green Dragonfly Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=175, color2=0, itemType="Shoes"), # Creek Green Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=4005,
                    items = [
                        OutfitItem(itemId=2150, price=25, goldPrice=10, color1=267, color2=186, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
                        OutfitItem(itemId=187, price=45, goldPrice=16, color1=267, color2=186, itemType="Shirt"), # Celestial Blue Hummingbird Top
                        OutfitItem(itemId=1169, price=45, goldPrice=16, color1=267, color2=186, itemType="Skirt"), # Celestial Blue Hummingbird Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=267, color2=0, itemType="Shoes"), # Celestial Blue Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=4006,
                    items = [
                        OutfitItem(itemId=2033, price=25, goldPrice=10, color1=175, color2=159, itemType="HeadItem"), # Creek Green Firefly Spotlight Barrette
                        OutfitItem(itemId=2524, price=15, goldPrice=6, color1=175, color2=159, itemType="Necklace"), # Creek Green Firefly Glow Choker
                        OutfitItem(itemId=29, price=45, goldPrice=16, color1=175, color2=159, itemType="Shirt"), # Creek Green Orchid Firefly Wrap
                        OutfitItem(itemId=1032, price=45, goldPrice=16, color1=175, color2=159, itemType="Skirt"), # Creek Green Slit Satin Firefly Skirt
                        OutfitItem(itemId=3519, price=25, goldPrice=10, color1=175, color2=159, itemType="Shoes"), # Creek Green Firefly Glow Toes Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=4007,
                    items = [
                        OutfitItem(itemId=90, price=45, goldPrice=16, color1=63, color2=166, itemType="Shirt"), # Butterfly Blue Fanciful Flutter Top with White Trim
                        OutfitItem(itemId=548, price=15, goldPrice=1, color1=63, color2=166, itemType="Belt"), # Butterfly Blue Fanciful Flutter Sash with White Trim
                        OutfitItem(itemId=1090, price=45, goldPrice=16, color1=63, color2=166, itemType="Skirt"), # Butterfly Blue Fanciful Flutter Gown with White Trim
                        OutfitItem(itemId=3559, price=25, goldPrice=10, color1=63, color2=166, itemType="Shoes"), # Butterfly Blue Fanciful Flutter Flats with White Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4008,
                    items = [
                        OutfitItem(itemId=376, price=45, goldPrice=16, color1=189, color2=206, itemType="Shirt"), # Ladybug Red Morpho Butterfly Top with Raven Black Trim
                        OutfitItem(itemId=635, price=15, goldPrice=1, color1=189, color2=206, itemType="Belt"), # Ladybug Red Morpho Butterfly Sash
                        OutfitItem(itemId=1294, price=45, goldPrice=16, color1=30, color2=206, itemType="Skirt"), # Pumpkin Orange Morpho Butterfly Skirt with Raven Black Trim
                        OutfitItem(itemId=3716, price=25, goldPrice=10, color1=206, color2=189, itemType="Shoes"), # Raven Black Morpho Butterfly Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=4009,
                    items = [
                        OutfitItem(itemId=2367, price=25, goldPrice=10, color1=216, color2=206, itemType="HeadItem"), # Slate Gray Raven Mask
                        OutfitItem(itemId=499, price=45, goldPrice=16, color1=206, color2=216, itemType="Shirt"), # Raven Black Raven Costume Top with Slate Gray Trim
                        OutfitItem(itemId=1415, price=45, goldPrice=16, color1=206, color2=216, itemType="Skirt"), # Raven Black Raven Skirt with Slate Gray Trim
                        OutfitItem(itemId=3794, price=25, goldPrice=10, color1=206, color2=216, itemType="Shoes"), # Raven Black Raven Heels with Slate Gray Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4010,
                    items = [
                        OutfitItem(itemId=2347, price=25, goldPrice=10, color1=224, color2=128, itemType="HeadItem"), # Ivory White Fox Mask
                        OutfitItem(itemId=1000011, price=45, goldPrice=16, color1=224, color2=128, itemType="Shirt"), # Ivory White Fox Top
                        OutfitItem(itemId=1395, price=45, goldPrice=16, color1=224, color2=128, itemType="Skirt"), # Ivory White Fox Skirt
                        OutfitItem(itemId=3801, price=25, goldPrice=10, color1=224, color2=128, itemType="Shoes"), # Ivory White Furry Critter Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=4011,
                    items = [
                        OutfitItem(itemId=2360, price=25, goldPrice=10, color1=206, color2=169, itemType="HeadItem"), # Raven Black Raccoon Mask
                        OutfitItem(itemId=481, price=45, goldPrice=16, color1=169, color2=206, itemType="Shirt"), # Squirrel Gray Raccoon Top
                        OutfitItem(itemId=1398, price=45, goldPrice=16, color1=169, color2=206, itemType="Skirt"), # Squirrel Gray Raccoon Skirt
                        OutfitItem(itemId=3801, price=25, goldPrice=10, color1=206, color2=169, itemType="Shoes"), # Raven Black Furry Critter Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=4012,
                    items = [
                        OutfitItem(itemId=2440, price=25, goldPrice=10, color1=212, color2=194, itemType="HeadItem"), # Indigo Purple Songbird Headband
                        OutfitItem(itemId=1000078, price=45, goldPrice=16, color1=194, color2=212, itemType="Shirt"), # Electric Pink Songbird Top
                        OutfitItem(itemId=1484, price=45, goldPrice=16, color1=212, color2=194, itemType="Skirt"), # Indigo Purple Songbird Skirt
                        OutfitItem(itemId=3869, price=25, goldPrice=10, color1=212, color2=194, itemType="Shoes"), # Indigo Purple Songbird Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=4013,
                    items = [ # lobster f
                        OutfitItem(itemId=2286, price=25, goldPrice=10, color1=45, color2=25, itemType="HeadItem"),
                        OutfitItem(itemId=347, price=45, goldPrice=16, color1=45, color2=25, itemType="Shirt"),
                        OutfitItem(itemId=1293, price=45, goldPrice=16, color1=45, color2=25, itemType="Skirt"), 
                    ]
                ),
                ShopOutfit(
                    outfitId=4014,
                    items = [ # lobster m
                        OutfitItem(itemId=2288, price=25, goldPrice=10, color1=45, color2=25, itemType="HeadItem"),
                        OutfitItem(itemId=360, price=45, goldPrice=16, color1=45, color2=25, itemType="Shirt"),
                        OutfitItem(itemId=1290, price=45, goldPrice=16, color1=45, color2=25, itemType="Skirt"), 
                    ]
                )
            ],
        ),  

        ShopCollection(
            collectionId=133, # Mermaid Friends Forever
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            outfits=[
                ShopOutfit(
                    outfitId=4021,
                    items = [
                        OutfitItem(itemId=2083, price=25, goldPrice=10, color1=30, color2=86, itemType="HeadItem"), # Coral Pink Mer-Made Crown
                        OutfitItem(itemId=86, price=45, goldPrice=16, color1=13, color2=107, itemType="Shirt"), # Coral Pink Mer-Made Top
                        OutfitItem(itemId=1180, price=45, goldPrice=16, color1=65, color2=21, itemType="Skirt"), # Summer Green Long Mermaid Skirt
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=13, color2=0, itemType="Shoes"), # Coral Pink Sparkle Slippers
                        OutfitItem(itemId=1088, price=45, goldPrice=16, color1=65, color2=21, itemType="Skirt"), # Summer Green Mer-Made Lagoon Drape
                        OutfitItem(itemId=3520, price=25, goldPrice=10, color1=13, color2=0, itemType="Shoes"), # Coral Pink Bubble Top Slippers
                    ], 
                ),
                ShopOutfit(
                    outfitId=4022,
                    items = [
                        OutfitItem(itemId=2083, price=25, goldPrice=10, color1=11, color2=40, itemType="HeadItem"), # Marigold Yellow Mer-Made Crown
                        OutfitItem(itemId=86, price=45, goldPrice=16, color1=11, color2=40, itemType="Shirt"), # Marigold Yellow Mer-Made Top
                        OutfitItem(itemId=1180, price=45, goldPrice=16, color1=40, color2=266, itemType="Skirt"), # Candy Blue Long Mermaid Skirt
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=11, color2=0, itemType="Shoes"), # Marigold Yellow Sparkle Slippers
                        OutfitItem(itemId=1088, price=45, goldPrice=16, color1=40, color2=266, itemType="Skirt"), # Candy Blue Mer-Made Lagoon Drape
                        OutfitItem(itemId=3520, price=25, goldPrice=10, color1=11, color2=0, itemType="Shoes"), # Coral Pink Bubble Top Slippers
                    ], 
                ),
                ShopOutfit(
                    outfitId=4023,
                    items = [
                        OutfitItem(itemId=2075, price=25, goldPrice=10, color1=43, color2=55, itemType="HeadItem"),
                        OutfitItem(itemId=78, price=45, goldPrice=16, color1=43, color2=0, itemType="Shirt"),
                        OutfitItem(itemId=1180, price=45, goldPrice=16, color1=55, color2=43, itemType="Skirt"), 
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=43, color2=0, itemType="Shoes"),
                        OutfitItem(itemId=1081, price=45, goldPrice=16, color1=55, color2=43, itemType="Skirt"),
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=43, color2=0, itemType="Shoes"), 
                    ], 
                ),
                ShopOutfit(
                    outfitId=4024,
                    items = [
                        OutfitItem(itemId=2075, price=25, goldPrice=10, color1=166, color2=156, itemType="HeadItem"),
                        OutfitItem(itemId=78, price=45, goldPrice=16, color1=156, color2=0, itemType="Shirt"),
                        OutfitItem(itemId=1180, price=45, goldPrice=16, color1=166, color2=156, itemType="Skirt"), 
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=156, color2=0, itemType="Shoes"),
                        OutfitItem(itemId=1081, price=45, goldPrice=16, color1=156, color2=166, itemType="Skirt"),
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=156, color2=0, itemType="Shoes"), 
                    ], 
                ),
                ShopOutfit(
                    outfitId=4025,
                    items = [
                        OutfitItem(itemId=2637, price=25, goldPrice=10, color1=282, color2=168, itemType="Necklace"),
                        OutfitItem(itemId=1000086, price=45, goldPrice=16, color1=191, color2=135, itemType="Shirt"),
                        OutfitItem(itemId=1493, price=45, goldPrice=16, color1=191, color2=135, itemType="Skirt"), 
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=135, color2=0, itemType="Shoes"),
                    ], 
                ),
            ]
        ),

        ShopCollection(
            collectionId=58, # Animal Friend Costumes (Sparrows)
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            outfits=[
                ShopOutfit(
                    outfitId=4015,
                    items = [
                        OutfitItem(itemId=230, price=45, goldPrice=16, color1=142, color2=206, itemType="Shirt"), # Bumble Bee Yellow Buzzy Bee Top
                        OutfitItem(itemId=1170, price=45, goldPrice=16, color1=206, color2=206, itemType="Skirt"), # Raven Black Pocket Pants
                        OutfitItem(itemId=3577, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Ivy Lace Work Boots
                    ], 
                ),
                ShopOutfit(
                    outfitId=4016,
                    items = [
                        OutfitItem(itemId=175, price=45, goldPrice=16, color1=44, color2=190, itemType="Shirt"), # Plumblossom Pink Firefly Wrap
                        OutfitItem(itemId=1195, price=45, goldPrice=16, color1=190, color2=190, itemType="Skirt"), # Firefly Green Dry Leaf Shorts
                        OutfitItem(itemId=3577, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Ivy Lace Work Boots
                    ], 
                ),
                ShopOutfit(
                    outfitId=4017,
                    items = [
                        OutfitItem(itemId=177, price=45, goldPrice=16, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tee
                        OutfitItem(itemId=1175, price=45, goldPrice=16, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Shorts
                        OutfitItem(itemId=3577, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Ivy Lace Work Boots
                    ], 
                ),
                ShopOutfit(
                    outfitId=4018,
                    items = [
                        OutfitItem(itemId=2149, price=25, goldPrice=10, color1=193, color2=175, itemType="HeadItem"), # Electric Green Dragonfly Mask
                        OutfitItem(itemId=178, price=45, goldPrice=16, color1=175, color2=175, itemType="Shirt"), # Creek Green Dragonfly Top 
                        OutfitItem(itemId=1173, price=45, goldPrice=16, color1=175, color2=193, itemType="Skirt"), # Creek Green Dragonfly Trousers
                        OutfitItem(itemId=3577, price=25, goldPrice=10, color1=175, color2=175, itemType="Shoes"), # Creek Green Ivy Lace Work Boots
                    ], 
                ),
                ShopOutfit(
                    outfitId=4019,
                    items = [
                        OutfitItem(itemId=2153, price=25, goldPrice=10, color1=267, color2=27, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
                        OutfitItem(itemId=190, price=45, goldPrice=16, color1=267, color2=27, itemType="Shirt"), # Celestial Blue Hummingbird Top 
                        OutfitItem(itemId=1174, price=45, goldPrice=16, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Hummingbird Trousers
                        OutfitItem(itemId=3577, price=25, goldPrice=10, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Ivy Lace Work Boots
                    ], 
                ),
                ShopOutfit(
                    outfitId=4020,
                    items = [
                        OutfitItem(itemId=2362, price=25, goldPrice=10, color1=224, color2=128, itemType="HeadItem"), # Ivory White Fox Mask
                        OutfitItem(itemId=497, price=45, goldPrice=16, color1=224, color2=128, itemType="Shirt"), # Ivory White Fox Top
                        OutfitItem(itemId=1413, price=45, goldPrice=16, color1=224, color2=128, itemType="Skirt"), # Ivory White Fox Trousers
                        OutfitItem(itemId=3793, price=25, goldPrice=10, color1=224, color2=128, itemType="Shoes"), # Ivory White Fox Boots
                    ],
                ),
            ]
        ),

        
    ],
)