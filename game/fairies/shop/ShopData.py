from game.fairies.ai import ZoneConstants
from game.fairies.ai import FairiesConstants
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

TEST_SHOP_DATA = ShopCollection(collectionId=1, currencyId=1, items=[ShopItem(itemId=77515, price=100, goldPrice=100)])

# Note that shopId 1 is locked to the Garden Shop despite shopId 7000 *also* being the Garden Shop

SHOPS = [
    NPCShop(
        zone=ZoneConstants.BELLAS_BAUBLES,
        shopId=0,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.BELLA_ROSE,
            position=(420, 420),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BELLA_ROSE
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.SUMMIT_STYLE,
        shopId=2,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.DIVA_WINGS,
            position=(410, 450),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_DIVA_WINGS
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.GALES_OUTFITTERS,
        shopId=3,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.GALE,
            position=(434, 429),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_GALE
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.CASSIES_COSTUME_SHOP,
        shopId=4,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.CASSIE,
            position=(500, 350),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_CASSIE
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.COALS_CLOTHIERS,
        shopId=5,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.COAL,
            position=(420, 420),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_COAL,
            gender=2
        ),
        collections=[
            ShopCollection(
                collectionId=83, # Mainland Styles
                items=[
                    ShopItem(itemId=484, price=30, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Varsity Jacket
                    ShopItem(itemId=1651, price=10, goldPrice=2, color1=78, color2=78, itemType="WristItem") # Fawn Brown Football
                ],
            ),
        ]
    ),

    NPCShop(
        zone=ZoneConstants.ZEPHYRS_ZOOM_ROOM,
        shopId=7,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.ZEPHYR,
            position=(408, 452),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_ZEPHYR
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.PIXIE_POST_OFFICE,
        shopId=8,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.SPRING,
            position=(500, 350),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_SPRING
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.QUEENS_BOUTIQUE,
        shopId=9,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.ERICA,
            position=(417, 455),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_ERICA
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.EMBERS_ESSENTIALS,
        shopId=1002,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.EMBER,
            position=(433, 432),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_EMBER
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.TREETOP_HOUSEWARES,
        shopId=1002,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.TRINKET,
            position=(425, 444),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_TRINKET
        ),
        collections=[
            TEST_SHOP_DATA
        ]
    ),

    NPCShop(
        zone=ZoneConstants.DAISYS_DYES,
        shopId=2000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.DAISY,
            position=(390, 434),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_DAISY
        ),
        # Dye Bottle Item IDs are 14000 + Color ID in colorAssets.xml
        collections=[
            ShopCollection(
                collectionId=2003, # Seasonal Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14034, price=10, goldPrice=2), # Primrose Pink
                    ShopItem(itemId=14231, price=10, goldPrice=2), # Sunny Orange
                    ShopItem(itemId=14255, price=10, goldPrice=2), # Canary Yellow
                    ShopItem(itemId=14259, price=10, goldPrice=2), # Kiwi Green
                    ShopItem(itemId=14069, price=10, goldPrice=2), # Powder Blue
                    ShopItem(itemId=14208, price=10, goldPrice=2), # Cerulean Blue
                    ShopItem(itemId=14274, price=10, goldPrice=2), # Bellflower Purple
                    ShopItem(itemId=14285, price=10, goldPrice=2), # Jazzberry Red
                ],
            ),
            ShopCollection(
                collectionId=2020, # Red & Purple Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 57
                    ShopItem(itemId=14110, price=5, goldPrice=1), # Rosy Pink
                    ShopItem(itemId=14121, price=5, goldPrice=1), # Daisy Pink
                    ShopItem(itemId=14016, price=5, goldPrice=1), # Camellia Pink
                    ShopItem(itemId=14194, price=5, goldPrice=1), # Electric Pink
                    ShopItem(itemId=14008, price=5, goldPrice=1), # Watermelon Pink
                    ShopItem(itemId=14013, price=5, goldPrice=1), # Coral Pink
                    ShopItem(itemId=14026, price=5, goldPrice=1), # Raspberry Pink
                    ShopItem(itemId=14286, price=5, goldPrice=1), # Cherry Pink
                    ShopItem(itemId=14113, price=5, goldPrice=1), # Pale Rose Red
                    ShopItem(itemId=14045, price=5, goldPrice=1), # Strawberry Red
                    ShopItem(itemId=14082, price=5, goldPrice=1), # Raspberry Red
                    ShopItem(itemId=14230, price=5, goldPrice=1), # Scarlet Red
                    ShopItem(itemId=14201, price=5, goldPrice=1), # Velvet Red
                    ShopItem(itemId=14044, price=5, goldPrice=1), # Plumblossom Pink
                    ShopItem(itemId=14045, price=5, goldPrice=1), # Hyacinth Pink
                    ShopItem(itemId=14081, price=5, goldPrice=1), # Crimson Red
                    ShopItem(itemId=14130, price=5, goldPrice=1), # Orchid Pink
                    ShopItem(itemId=14140, price=5, goldPrice=1), # Bunnynose Pink
                    ShopItem(itemId=14144, price=5, goldPrice=1), # Petal Pink
                    ShopItem(itemId=14156, price=5, goldPrice=1), # Friendship Pink
                    ShopItem(itemId=14181, price=5, goldPrice=1), # Cupcake Pink
                    ShopItem(itemId=14174, price=5, goldPrice=1), # Rosetta Red
                    ShopItem(itemId=14189, price=5, goldPrice=1), # Ladybug Red
                    ShopItem(itemId=14199, price=5, goldPrice=1), # Cherryblossom Pink
                    ShopItem(itemId=14200, price=5, goldPrice=1), # Ruby Pink
                    ShopItem(itemId=14220, price=5, goldPrice=1), # Dusty Pink
                    ShopItem(itemId=14283, price=5, goldPrice=1), # Thistle Pink
                    ShopItem(itemId=14287, price=5, goldPrice=1), # Dianthus Red
                    ShopItem(itemId=14005, price=5, goldPrice=1), # Wysteria Purple
                    ShopItem(itemId=14014, price=5, goldPrice=1), # Plum Purple
                    ShopItem(itemId=14073, price=5, goldPrice=1), # Grape Purple
                    ShopItem(itemId=14061, price=5, goldPrice=1), # Pale Lilac Purple
                    ShopItem(itemId=14072, price=5, goldPrice=1), # Mauve Purple
                    ShopItem(itemId=14135, price=5, goldPrice=1), # Boysenberry Purple
                    ShopItem(itemId=14183, price=5, goldPrice=1), # Vidia Purple
                    ShopItem(itemId=14184, price=5, goldPrice=1), # Hummingbird Purple
                    ShopItem(itemId=14210, price=5, goldPrice=1), # Lotus Purple
                    ShopItem(itemId=14211, price=5, goldPrice=1), # Gentian Purple
                    ShopItem(itemId=14212, price=5, goldPrice=1), # Indigo Purple
                    ShopItem(itemId=14225, price=5, goldPrice=1), # Eggplant Purple
                    ShopItem(itemId=14229, price=5, goldPrice=1), # Electric Indigo
                    ShopItem(itemId=14276, price=5, goldPrice=1), # Dusk Purple
                    ShopItem(itemId=14129, price=5, goldPrice=1), # Fig Purple
                    ShopItem(itemId=14134, price=5, goldPrice=1), # Heather Purple
                    ShopItem(itemId=14278, price=5, goldPrice=1), # Aster Purple
                    ShopItem(itemId=14277, price=5, goldPrice=1), # Misty Purple
                    ShopItem(itemId=14117, price=5, goldPrice=1), # Amethyst Purple
                    ShopItem(itemId=14033, price=5, goldPrice=1), # Iris Purple
                    ShopItem(itemId=14197, price=5, goldPrice=1), # Electric Purple
                    ShopItem(itemId=14032, price=5, goldPrice=1), # Mulberry Purple
                    ShopItem(itemId=14275, price=5, goldPrice=1), # Shadowy Purple
                    ShopItem(itemId=14152, price=5, goldPrice=1), # Pale Purple
                    ShopItem(itemId=14192, price=5, goldPrice=1), # Royal Purple
                    ShopItem(itemId=14279, price=5, goldPrice=1), # Kingfisher Purple
                    ShopItem(itemId=14135, price=5, goldPrice=1), # Berry Purple
                    ShopItem(itemId=14281, price=5, goldPrice=1), # Deep Violet Purple
                    ShopItem(itemId=14284, price=5, goldPrice=1), # Deep Magenta Purple
                ],
            ),
            ShopCollection(
                collectionId=2001, # Orange & Yellow Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 43
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                ],
            ),
            ShopCollection(
                collectionId=2008, # Blue & Green Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 85
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                    ShopItem(itemId=0, price=5, goldPrice=1), #
                ],
            ),
            ShopCollection(
                collectionId=2009, # Brown & Neutral Dyes
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[ # 47
                    ShopItem(itemId=14087, price=5, goldPrice=1), # Driftwood Brown
                    ShopItem(itemId=14083, price=5, goldPrice=1), # Cherry Brown
                    ShopItem(itemId=14079, price=5, goldPrice=1), # Sienna Brown
                    ShopItem(itemId=14075, price=5, goldPrice=1), # Umber Brown
                    ShopItem(itemId=14236, price=5, goldPrice=1), # Dusty Brown
                    ShopItem(itemId=14078, price=5, goldPrice=1), # Fawn Brown
                    ShopItem(itemId=14056, price=5, goldPrice=1), # Bole Brown
                    ShopItem(itemId=14076, price=5, goldPrice=1), # Chocolate Brown
                    ShopItem(itemId=14089, price=5, goldPrice=1), # Seashore Brown
                    ShopItem(itemId=14085, price=5, goldPrice=1), # Quail Brown
                    ShopItem(itemId=14246, price=5, goldPrice=1), # Bear Brown
                    ShopItem(itemId=14240, price=5, goldPrice=1), # Ironwood Brown
                    ShopItem(itemId=14161, price=5, goldPrice=1), # Buried Treasure Brown
                    ShopItem(itemId=14088, price=5, goldPrice=1), # Fruitwood Brown
                    ShopItem(itemId=14084, price=5, goldPrice=1), # Copper Brown
                    ShopItem(itemId=14074, price=5, goldPrice=1), # Soil Brown
                    ShopItem(itemId=14075, price=5, goldPrice=1), # Desert Brown
                    ShopItem(itemId=14154, price=5, goldPrice=1), # Beetle Brown
                    ShopItem(itemId=14046, price=5, goldPrice=1), # Bark Brown
                    ShopItem(itemId=14077, price=5, goldPrice=1), # Sepia Brown
                    ShopItem(itemId=14250, price=5, goldPrice=1), # Caramel Tan
                    ShopItem(itemId=14146, price=5, goldPrice=1), # Beech Brown
                    ShopItem(itemId=14245, price=5, goldPrice=1), # Earthy Tan
                    ShopItem(itemId=14251, price=5, goldPrice=1), # Polished Brown
                    ShopItem(itemId=14177, price=5, goldPrice=1), # Mud Brown
                    ShopItem(itemId=14166, price=5, goldPrice=1), # Snow White
                    ShopItem(itemId=14262, price=5, goldPrice=1), # Minty White
                    ShopItem(itemId=14269, price=5, goldPrice=1), # Crisp White
                    ShopItem(itemId=14282, price=5, goldPrice=1), # Magnolia White
                    ShopItem(itemId=14224, price=5, goldPrice=1), # Ivory White
                    ShopItem(itemId=14157, price=5, goldPrice=1), # Starry White
                    ShopItem(itemId=14116, price=5, goldPrice=1), # Mushroom White
                    ShopItem(itemId=14128, price=5, goldPrice=1), # Carnation White
                    ShopItem(itemId=14227, price=5, goldPrice=1), # Moonlight Gray
                    ShopItem(itemId=14169, price=5, goldPrice=1), # Squirrel Gray
                    ShopItem(itemId=14214, price=5, goldPrice=1), # Smokey Gray
                    ShopItem(itemId=14272, price=5, goldPrice=1), # Charcoal Gray
                    ShopItem(itemId=14239, price=5, goldPrice=1), # Coffee Black
                    ShopItem(itemId=14206, price=5, goldPrice=1), # Raven Black
                    ShopItem(itemId=14217, price=5, goldPrice=1), # Soft Gray
                    ShopItem(itemId=14215, price=5, goldPrice=1), # Pewter Gray
                    ShopItem(itemId=14141, price=5, goldPrice=1), # Thundercloud Gray
                    ShopItem(itemId=14273, price=5, goldPrice=1), # Panther Black
                    ShopItem(itemId=14167, price=5, goldPrice=1), # Never Silver
                    ShopItem(itemId=14216, price=5, goldPrice=1), # Slate Gray
                    ShopItem(itemId=14191, price=5, goldPrice=1), # Vidia Black
                    ShopItem(itemId=14055, price=5, goldPrice=1), # Pepper Black
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.PHOEBES_PARTY_FAVORS,
        shopId=3000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.PHOEBE,
            position=(352, 810),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_PHOEBE
        ),
        collections=[
            TEST_SHOP_DATA
        ],
    ),

    NPCShop(
        zone=ZoneConstants.SCHELLYS_HAIR_SALON,
        shopId=4000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.SCHELLY,
            position=(290, 470),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_SCHELLY
        ),
        collections=[
            ShopCollection(
                collectionId=4001, # Classic Hair Fronts (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5001, price=10, goldPrice=2), # Simple Style
                    ShopItem(itemId=5002, price=10, goldPrice=2), # Parted Bangs
                    ShopItem(itemId=5003, price=10, goldPrice=2), # Center Swoops
                    ShopItem(itemId=5004, price=10, goldPrice=2), # Sweepy Side Part
                    ShopItem(itemId=5005, price=10, goldPrice=2), # Wind-Swept Bangs
                    ShopItem(itemId=5006, price=10, goldPrice=2), # Sleek and Styled
                    ShopItem(itemId=5007, price=10, goldPrice=2), # Parted Pomp
                    ShopItem(itemId=5008, price=10, goldPrice=2), # Blunt Cut
                    ShopItem(itemId=5009, price=10, goldPrice=2), # Swoopy Side Part
                    ShopItem(itemId=5010, price=10, goldPrice=2), # Angled Bangs
                    ShopItem(itemId=5011, price=10, goldPrice=2), # Pulled Back -- Wavy
                    ShopItem(itemId=5012, price=10, goldPrice=2), # Pulled Back -- Glamorous
                    ShopItem(itemId=5013, price=10, goldPrice=2), # Pulled Back
                    ShopItem(itemId=5014, price=10, goldPrice=2), # Pulled Back -- Wispy
                    ShopItem(itemId=5015, price=10, goldPrice=2), # Sweeping Bangs
                    ShopItem(itemId=5016, price=10, goldPrice=2), # Shy Style
                    ShopItem(itemId=5017, price=10, goldPrice=2), # Tousled Layers
                    ShopItem(itemId=5018, price=10, goldPrice=2), # Tousled Top
                    ShopItem(itemId=5019, price=10, goldPrice=2), # Long Strand Front
                ],
            ),
            ShopCollection(
                collectionId=4003, # Classic Hair Backs (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5521, price=10, goldPrice=2), # No Back
                    ShopItem(itemId=5501, price=10, goldPrice=2), # Classic Back
                    ShopItem(itemId=5502, price=10, goldPrice=2), # Pixie Braids
                    ShopItem(itemId=5503, price=10, goldPrice=2), # Short Tresses
                    ShopItem(itemId=5504, price=10, goldPrice=2), # Fluffy Short
                    ShopItem(itemId=5505, price=10, goldPrice=2), # Styled Short
                    ShopItem(itemId=5506, price=10, goldPrice=2), # Super Long Braid
                    ShopItem(itemId=5507, price=10, goldPrice=2), # Berry Bouffant
                    ShopItem(itemId=5508, price=10, goldPrice=2), # Pixie Pom Pom
                    ShopItem(itemId=5509, price=10, goldPrice=2), # Big Hair
                    ShopItem(itemId=5510, price=10, goldPrice=2), # Long Tresses
                    ShopItem(itemId=5511, price=10, goldPrice=2), # Styled Long Strands
                    ShopItem(itemId=5512, price=10, goldPrice=2), # Fairy Braids
                    ShopItem(itemId=5513, price=10, goldPrice=2), # Long Tapered Tresses
                    ShopItem(itemId=5514, price=10, goldPrice=2), # Long Braids
                    ShopItem(itemId=5515, price=10, goldPrice=2), # Long and Straight
                    ShopItem(itemId=5516, price=10, goldPrice=2), # Short and Teased
                    ShopItem(itemId=5517, price=10, goldPrice=2), # Long Flowing Locks
                    ShopItem(itemId=5518, price=10, goldPrice=2), # Pixie Pin Curls
                    ShopItem(itemId=5519, price=10, goldPrice=2), # Wind-Swept Bun
                    ShopItem(itemId=5520, price=10, goldPrice=2), # Thick Ponytails
                    ShopItem(itemId=5522, price=10, goldPrice=2), # Puff Ball Back
                ],
            ),
            ShopCollection(
                collectionId=4004, # Stylish Hair Fronts (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5118, price=10, goldPrice=2), # Plaited Side Part Front
                    ShopItem(itemId=5119, price=10, goldPrice=2), # Sideswept Barrette Front
                    ShopItem(itemId=5121, price=10, goldPrice=2), # Curly Pompadour Front
                    ShopItem(itemId=5122, price=10, goldPrice=2), # Short Waves Front
                    ShopItem(itemId=5123, price=10, goldPrice=2), # Fashion Bob Front
                    ShopItem(itemId=5120, price=10, goldPrice=2), # Beautiful Bangs
                    ShopItem(itemId=5124, price=10, goldPrice=2), # Periwinkle's Hair Front
                    ShopItem(itemId=5125, price=10, goldPrice=2), # Spike's Hair Front
                    ShopItem(itemId=5126, price=10, goldPrice=2), # Long and Curly Front
                    ShopItem(itemId=5027, price=10, goldPrice=2), # Pixie Bangs
                    ShopItem(itemId=5113, price=10, goldPrice=2), # Original Pixie Bangs
                    ShopItem(itemId=5028, price=10, goldPrice=2), # Pixie Pigtails
                    ShopItem(itemId=5115, price=10, goldPrice=2), # Original Pixie Pigtails
                    ShopItem(itemId=5029, price=10, goldPrice=2), # Star Strands Front
                    ShopItem(itemId=5114, price=10, goldPrice=2), # Original Star Strands Front
                    ShopItem(itemId=5030, price=10, goldPrice=2), # Side Swept Bangs
                    ShopItem(itemId=5116, price=10, goldPrice=2), # Original Side Swept Bangs
                    ShopItem(itemId=5032, price=10, goldPrice=2), # Fairy Mary Hair
                    ShopItem(itemId=5075, price=10, goldPrice=2), # Cool Waves
                    ShopItem(itemId=5077, price=10, goldPrice=2), # Classic Pulled Back
                    ShopItem(itemId=5094, price=10, goldPrice=2), # Flowy Pigtails
                    ShopItem(itemId=5081, price=10, goldPrice=2), # Sweet and Stylish Bun
                    ShopItem(itemId=5080, price=10, goldPrice=2), # Puffy Bangs
                    ShopItem(itemId=5093, price=10, goldPrice=2), # Long and Flowing Tieback
                    ShopItem(itemId=5084, price=10, goldPrice=2), # Sleek Part
                    ShopItem(itemId=5107, price=10, goldPrice=2), # Royal Heart Braids
                    ShopItem(itemId=5102, price=10, goldPrice=2), # Lovely Layers
                    ShopItem(itemId=5076, price=10, goldPrice=2), # Fairy Fishtails
                    ShopItem(itemId=5108, price=10, goldPrice=2), # Will 'O Whisp Bangs
                    ShopItem(itemId=5101, price=10, goldPrice=2), # Long Swept Bangs
                    ShopItem(itemId=5089, price=10, goldPrice=2), # Braided Tieback
                    ShopItem(itemId=5098, price=10, goldPrice=2), # Short Twists
                    ShopItem(itemId=5092, price=10, goldPrice=2), # Long and Flitterific Locks
                    ShopItem(itemId=5082, price=10, goldPrice=2), # Stylish Ringlets
                    ShopItem(itemId=5033, price=10, goldPrice=2), # Side-Part Swirly Bob
                    ShopItem(itemId=5034, price=10, goldPrice=2), # Front Swept Bangs
                    ShopItem(itemId=5035, price=10, goldPrice=2), # Totally Tousled Bangs
                    ShopItem(itemId=5036, price=10, goldPrice=2), # Soft Tousled Bangs
                    ShopItem(itemId=5037, price=10, goldPrice=2), # Tight Wave Crop
                    ShopItem(itemId=5062, price=10, goldPrice=2), # Perfect Bob
                    ShopItem(itemId=5064, price=10, goldPrice=2), # Swift and Swooshy Locks
                    ShopItem(itemId=5063, price=10, goldPrice=2), # Long Angled Bangs
                    ShopItem(itemId=5066, price=10, goldPrice=2), # Braid Over Bangs
                    ShopItem(itemId=5078, price=10, goldPrice=2), # Mouse-Ear Buns
                    ShopItem(itemId=5099, price=10, goldPrice=2), # Pulled Back Twists
                    ShopItem(itemId=5090, price=10, goldPrice=2), # Inverted Bob
                    ShopItem(itemId=5087, price=10, goldPrice=2), # Rock and Roll Bangs
                    ShopItem(itemId=5086, price=10, goldPrice=2), # Double Roll Bangs
                    ShopItem(itemId=5100, price=10, goldPrice=2), # Triple Braid Bob
                    ShopItem(itemId=5079, price=10, goldPrice=2), # Topsy-Turvy Short
                    ShopItem(itemId=5105, price=10, goldPrice=2), # Twisty Locks
                    ShopItem(itemId=5088, price=10, goldPrice=2), # Bowtie Bob
                    ShopItem(itemId=5097, price=10, goldPrice=2), # Long and Curly Twisties
                ],
            ),
            ShopCollection(
                collectionId=4005, # Stylish Hair Backs (Fairies)
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=5521, price=10, goldPrice=2), # No Back
                    ShopItem(itemId=5602, price=10, goldPrice=2), # Sideswept Barrette Back
                    ShopItem(itemId=5603, price=10, goldPrice=2), # Plaited Side Part Back
                    ShopItem(itemId=5605, price=10, goldPrice=2), # Curly Pompadour Back
                    ShopItem(itemId=5606, price=10, goldPrice=2), # Pom Pom Pigtails
                    ShopItem(itemId=5604, price=10, goldPrice=2), # Beautiful Bangs Back
                    ShopItem(itemId=5607, price=10, goldPrice=2), # Periwinkle's Hair Back
                    ShopItem(itemId=5601, price=10, goldPrice=2), # Spike's Hair Back
                    ShopItem(itemId=5608, price=10, goldPrice=2), # Long and Curly Back
                    ShopItem(itemId=5532, price=10, goldPrice=2), # Sweet Bun
                    ShopItem(itemId=5533, price=10, goldPrice=2), # Girly Curlies
                    ShopItem(itemId=5534, price=10, goldPrice=2), # Pixie Ponytails Back
                    ShopItem(itemId=5535, price=10, goldPrice=2), # Star Strands Back
                    ShopItem(itemId=5599, price=10, goldPrice=2), # Original Star Strands Back
                    ShopItem(itemId=5536, price=10, goldPrice=2), # Pixie Bob Back
                    ShopItem(itemId=5537, price=10, goldPrice=2), # Long Pony
                    ShopItem(itemId=5598, price=10, goldPrice=2), # Original Long Pony
                    ShopItem(itemId=5569, price=10, goldPrice=2), # Cool Waves Back
                    ShopItem(itemId=5570, price=10, goldPrice=2), # Braided-Bun
                    ShopItem(itemId=5574, price=10, goldPrice=2), # Swept Up Hair Back
                    ShopItem(itemId=5573, price=10, goldPrice=2), # Puffy Pigtails
                    ShopItem(itemId=5576, price=10, goldPrice=2), # Twin Buns
                    ShopItem(itemId=5591, price=10, goldPrice=2), # Lovely Layers Back
                    ShopItem(itemId=5593, price=10, goldPrice=2), # Whale of a Fishtail
                    ShopItem(itemId=5582, price=10, goldPrice=2), # High Flowing Ponytail
                    ShopItem(itemId=5584, price=10, goldPrice=2), # Long and Flowing Hair
                    ShopItem(itemId=5590, price=10, goldPrice=2), # Swept Up
                    ShopItem(itemId=5581, price=10, goldPrice=2), # Bunny Tail Bun
                    ShopItem(itemId=5572, price=10, goldPrice=2), # Long Braided Back
                    ShopItem(itemId=5588, price=10, goldPrice=2), # Short Twists Back
                    ShopItem(itemId=5583, price=10, goldPrice=2), # Long and Flitterific Locks Back
                    ShopItem(itemId=5575, price=10, goldPrice=2), # Stylish Ringlets Back
                    ShopItem(itemId=5538, price=10, goldPrice=2), # Swirly Glamour Mane
                    ShopItem(itemId=5539, price=10, goldPrice=2), # Swept-Up Bun
                    ShopItem(itemId=5540, price=10, goldPrice=2), # Totally Rounded Bob
                    ShopItem(itemId=5541, price=10, goldPrice=2), # Soft Layered Locks
                    ShopItem(itemId=5563, price=10, goldPrice=2), # Perfect Bob Back
                    ShopItem(itemId=5565, price=10, goldPrice=2), # Swift and Swooshy Back
                    ShopItem(itemId=5564, price=10, goldPrice=2), # Angled Bang Back
                    ShopItem(itemId=5566, price=10, goldPrice=2), # Braid and Bun
                    ShopItem(itemId=5571, price=10, goldPrice=2), # Draping Locks
                    ShopItem(itemId=5580, price=10, goldPrice=2), # Super Long Ponytail
                    ShopItem(itemId=5589, price=10, goldPrice=2), # Pulled Back Twists Back
                    ShopItem(itemId=5579, price=10, goldPrice=2), # Wavy Silky Tresses
                    ShopItem(itemId=5578, price=10, goldPrice=2), # Rolled and Wavy Back
                    ShopItem(itemId=5587, price=10, goldPrice=2), # Long and Curly Twisties Back
                ],
            )
        ],
    ),

    NPCShop(
        zone=ZoneConstants.BECKS_ANIMAL_NURSERY,
        shopId=5000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.BECK,
            position=(387, 440),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BECK
        ),
        collections=[
            TEST_SHOP_DATA
        ],
    ),

    NPCShop(
        zone=ZoneConstants.NEVILLES_NEW_HOMES,
        shopId=6000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.NEVILLE,
            position=(785, 458),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_NEVILLE,
            gender=2
        ),
        collections=[
            TEST_SHOP_DATA
        ],
    ),

    NPCShop(
        zone=ZoneConstants.GARDEN_SUPPLY,
        shopId=7000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.BROOK,
            position=(418, 453),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BROOK
        ),
        collections=[
            ShopCollection(
                collectionId=119, # Basic Seeds
                items=[
                    ShopItem(itemId=89002, goldPrice=1), # Dulcie's Cookie Seeds
                    ShopItem(itemId=89017, goldPrice=1), # Dulcie's Truffle Seeds
                    ShopItem(itemId=89001, goldPrice=1), # Colorful Sweet Seeds
                    ShopItem(itemId=89023, goldPrice=1), # Rainbow Sweet Seeds
                    ShopItem(itemId=89018, goldPrice=1), # Sweet Trails Seeds
                    ShopItem(itemId=89031, goldPrice=1), # Summer Sweets Seeds
                ],
            ),
            ShopCollection(
                collectionId=118, # Special Edition Seeds
                items=[
                    ShopItem(itemId=89009, goldPrice=1), # Garden Premier Seeds
                    ShopItem(itemId=89022, goldPrice=1), # Autumn Breeze Seeds
                    ShopItem(itemId=89021, goldPrice=1), # Winter Wardrobe Seeds
                    ShopItem(itemId=89030, goldPrice=1), # Spring Style Seeds
                    ShopItem(itemId=89038, goldPrice=1), # Summer Chic Seeds
                ],
            ),
            ShopCollection(
                collectionId=132, # Summer 2012 Seeds
                items=[
                    ShopItem(itemId=89004, goldPrice=1), # Fancy Flower Seeds
                    ShopItem(itemId=89000, goldPrice=1), # Rainbow Dye Seeds
                    ShopItem(itemId=89006, goldPrice=1), # Teatime Seeds
                    ShopItem(itemId=89008, goldPrice=1), # Little Gardener Seeds
                    ShopItem(itemId=89005, goldPrice=1), # To-Fly-For Top Seeds
                    ShopItem(itemId=89007, goldPrice=1), # Skirt or Slacks Seeds
                    ShopItem(itemId=89003, goldPrice=1), # Stylish Shoe Seeds
                ],
            ),
            ShopCollection(
                collectionId=131, # Fall 2012 Seeds
                items=[
                    ShopItem(itemId=89014, goldPrice=1), # Autumn Masquerade Dye Seeds
                    ShopItem(itemId=89019, goldPrice=1), # Autumn Harvest Seeds
                ],
            ),
            ShopCollection(
                collectionId=130, # Winter 2012 Seeds
                items=[
                    ShopItem(itemId=89012, goldPrice=1), # Chilly Plants Seeds
                    ShopItem(itemId=89013, goldPrice=1), # Winter Wonderland Dye Seeds
                    ShopItem(itemId=89016, goldPrice=1), # Tink's Decorating Seeds
                    ShopItem(itemId=89010, goldPrice=1), # Festive Ornament Seeds
                    ShopItem(itemId=89011, goldPrice=1), # Flitterific Tops Seeds
                    ShopItem(itemId=89015, goldPrice=1), # Flitterific Skirt or Slacks Seeds
                    ShopItem(itemId=89020, goldPrice=1), # Flitterific Shoe Seeds
                ],
            ),
            ShopCollection(
                collectionId=129, # Spring 2013 Seeds
                items=[
                    ShopItem(itemId=89029, goldPrice=1), # Springtime Flower Seeds
                    ShopItem(itemId=89028, goldPrice=1), # Never Dove Egg Dye Seeds
                    ShopItem(itemId=89027, goldPrice=1), # Clover Comfort Seeds
                    ShopItem(itemId=89024, goldPrice=1), # Springtime Top Seeds
                    ShopItem(itemId=89025, goldPrice=1), # Springtime Skirt or Slacks Seeds
                    ShopItem(itemId=89026, goldPrice=1), # Springtime Shoe Seeds
                ],
            ),
            ShopCollection(
                collectionId=120, # Summer 2013 Seeds
                items=[
                    ShopItem(itemId=89033, goldPrice=1), # Sprightly Sprouts Seeds
                    ShopItem(itemId=89032, goldPrice=1), # Midsummer Dye Seeds
                    ShopItem(itemId=89035, goldPrice=1), # Blooming Benches Seeds
                    ShopItem(itemId=89036, goldPrice=1), # Tropical Tops Seeds
                    ShopItem(itemId=89037, goldPrice=1), # Sunny Skirt or Slacks Seeds
                    ShopItem(itemId=89034, goldPrice=1), # Summertime Shoes Seeds
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.HARMONYS_SWEET_SHOP,
        shopId=8000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.HARMONY,
            position=(417, 455),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_HARMONY,
        ),
        collections=[
            ShopCollection(
                collectionId=146, # Scrumptious Cookies
                items=[
                    ShopItem(itemId=22502, goldPrice=1), # Sunflower Cookie
                    ShopItem(itemId=22503, goldPrice=1), # Honey Cookie
                    ShopItem(itemId=22504, goldPrice=1), # Raspberry Cookie
                    ShopItem(itemId=22505, goldPrice=1), # Blueberry Cookie
                    ShopItem(itemId=22506, goldPrice=1), # Honey Maple Cookie
                    ShopItem(itemId=22507, goldPrice=1), # Truffle Cookie
                    ShopItem(itemId=22508, goldPrice=1), # Honey Truffle Cookie
                    ShopItem(itemId=22509, goldPrice=1), # Raspberry Truffle Cookie
                    ShopItem(itemId=22510, goldPrice=1), # Blueberry Truffle Cookie
                    ShopItem(itemId=22532, goldPrice=1), # Sunflower Double Truffle Cookie
                    ShopItem(itemId=22533, goldPrice=1), # Honey Double Truffle Cookie
                    ShopItem(itemId=22534, goldPrice=1), # Raspberry Double Truffle Cookie
                    ShopItem(itemId=22535, goldPrice=1), # Blueberry Double Truffle Cookie
                    ShopItem(itemId=22542, goldPrice=1), # Honey Maple Double Truffle Cookie
                ],
            ),
            ShopCollection(
                collectionId=61, # Delectable Cupcakes
                items=[
                    ShopItem(itemId=22551, goldPrice=1), # Sunflower Cupcake
                    ShopItem(itemId=22552, goldPrice=1), # Honey Cupcake
                    ShopItem(itemId=22553, goldPrice=1), # Raspberry Cupcake
                ],
            ),
            ShopCollection(
                collectionId=147, # Color Changing Silly Sweets
                items=[
                    ShopItem(itemId=22520, goldPrice=1), # Red
                    ShopItem(itemId=22521, goldPrice=1), # Orange
                    ShopItem(itemId=22522, goldPrice=1), # Yellow
                    ShopItem(itemId=22518, goldPrice=1), # Green
                    ShopItem(itemId=22516, goldPrice=1), # Blue
                    ShopItem(itemId=22519, goldPrice=1), # Purple
                    ShopItem(itemId=22514, goldPrice=1), # Pink
                    ShopItem(itemId=22515, goldPrice=1), # White
                    ShopItem(itemId=22517, goldPrice=1), # Gray
                    ShopItem(itemId=22523, goldPrice=1), # Cool Rainbow
                    ShopItem(itemId=22524, goldPrice=1), # Bright Rainbow
                    ShopItem(itemId=22525, goldPrice=1), # Invisible
                ],
            ),
            ShopCollection(
                collectionId=38, # Aura Silly Sweets
                items=[
                    ShopItem(itemId=22527, goldPrice=1), # Rainbow Glow
                    ShopItem(itemId=22526, goldPrice=1), # Bubble
                    ShopItem(itemId=22543, goldPrice=1), # Bubble Trail
                    ShopItem(itemId=22530, goldPrice=1), # Tornado
                    ShopItem(itemId=22528, goldPrice=1), # Dizzy
                    ShopItem(itemId=22529, goldPrice=1), # Bright Idea
                    ShopItem(itemId=22539, goldPrice=1), # Puffy Cloud
                    ShopItem(itemId=22536, goldPrice=1), # Fairy Cupcake
                    ShopItem(itemId=22537, goldPrice=1), # Fireworks
                    ShopItem(itemId=22538, goldPrice=1), # Snowglobe
                    ShopItem(itemId=22540, goldPrice=1), # Ice Cube
                    ShopItem(itemId=22541, goldPrice=1), # Snowman
                    ShopItem(itemId=22544, goldPrice=1), # Flower Trail
                    ShopItem(itemId=22545, goldPrice=1), # Snowflake Trail
                    ShopItem(itemId=22546, goldPrice=1), # Raining Cloud
                    ShopItem(itemId=22547, goldPrice=1), # Snowing Cloud
                    ShopItem(itemId=22548, goldPrice=1), # Shrinking
                    ShopItem(itemId=22549, goldPrice=1), # Growing
                    ShopItem(itemId=22550, goldPrice=1), # Flip-Flop
                ],
            ),
            ShopCollection(
                collectionId=21, # Wing Changing Silly Sweets
                items=[
                    ShopItem(itemId=22571, goldPrice=1), # Sparkly Wings
                    ShopItem(itemId=22572, goldPrice=1), # Pepper Black Wings
                    ShopItem(itemId=22573, goldPrice=1), # Bluejay Blue Wings
                    ShopItem(itemId=22574, goldPrice=1), # Electric Blue Wings
                    ShopItem(itemId=22575, goldPrice=1), # Friendship Pink Wings
                    ShopItem(itemId=22576, goldPrice=1), # Electric Pink Wings
                    ShopItem(itemId=22577, goldPrice=1), # Electric Orange Wings
                    ShopItem(itemId=22578, goldPrice=1), # Electric Purple Wings
                    ShopItem(itemId=22579, goldPrice=1), # Lemon Yellow Wings
                    ShopItem(itemId=22580, goldPrice=1), # Rosetta Red Wings
                    ShopItem(itemId=22581, goldPrice=1), # Electric Green Wings
                ],
            ),
        ],
    ),

    NPCShop(
        zone=ZoneConstants.SPIKES_SWEETS,
        shopId=8001,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.SPIKE,
            position=(417, 355),
            famousFairyId=45,
        ),
        collections=[
            TEST_SHOP_DATA
        ],
    ),


    NPCShop(
        zone=ZoneConstants.PRISMS_PIXIE_SPA,
        shopId=9000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.PRISM,
            position=(290, 460),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_PRISM,
        ),
        collections=[
            ShopCollection(
                collectionId=4017, # Wings
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=6001, price=25, goldPrice=5),
                    ShopItem(itemId=6002, price=25, goldPrice=5),
                    ShopItem(itemId=6003, price=25, goldPrice=5),
                    ShopItem(itemId=6004, price=25, goldPrice=5),
                    ShopItem(itemId=6005, price=25, goldPrice=5),
                    ShopItem(itemId=6006, price=25, goldPrice=5),
                ],
            ),
            ShopCollection(
                collectionId=4018,
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=4501, price=10, goldPrice=2),
                    ShopItem(itemId=4502, price=10, goldPrice=2),
                    ShopItem(itemId=4503, price=10, goldPrice=2),
                    ShopItem(itemId=4504, price=10, goldPrice=2),
                    ShopItem(itemId=4505, price=10, goldPrice=2),
                    ShopItem(itemId=4506, price=10, goldPrice=2),
                    ShopItem(itemId=4507, price=10, goldPrice=2),
                    ShopItem(itemId=4508, price=10, goldPrice=2),
                    ShopItem(itemId=4509, price=10, goldPrice=2),
                    ShopItem(itemId=4510, price=10, goldPrice=2),
                    ShopItem(itemId=4511, price=10, goldPrice=2),
                    ShopItem(itemId=4512, price=10, goldPrice=2),
                    ShopItem(itemId=4513, price=10, goldPrice=2),
                    ShopItem(itemId=4514, price=10, goldPrice=2),
                    ShopItem(itemId=4515, price=10, goldPrice=2),
                    ShopItem(itemId=4516, price=10, goldPrice=2),
                    ShopItem(itemId=4517, price=10, goldPrice=2),
                    ShopItem(itemId=4518, price=10, goldPrice=2),
                    ShopItem(itemId=4519, price=10, goldPrice=2),
                    ShopItem(itemId=4520, price=10, goldPrice=2),
                    ShopItem(itemId=4521, price=10, goldPrice=2),
                    ShopItem(itemId=4522, price=10, goldPrice=2),
                    ShopItem(itemId=4523, price=10, goldPrice=2),
                ],
            ),
            ShopCollection(
                collectionId=4019,
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14091, price=5, goldPrice=1),
                    ShopItem(itemId=14092, price=5, goldPrice=1),
                    ShopItem(itemId=14093, price=5, goldPrice=1),
                    ShopItem(itemId=14094, price=5, goldPrice=1),
                    ShopItem(itemId=14095, price=5, goldPrice=1),
                    ShopItem(itemId=14096, price=5, goldPrice=1),
                    ShopItem(itemId=14097, price=5, goldPrice=1),
                    ShopItem(itemId=14098, price=5, goldPrice=1),
                    ShopItem(itemId=14099, price=5, goldPrice=1),
                    ShopItem(itemId=14100, price=5, goldPrice=1),
                    ShopItem(itemId=14101, price=5, goldPrice=1),
                    ShopItem(itemId=14102, price=5, goldPrice=1),
                    ShopItem(itemId=14103, price=5, goldPrice=1),
                    ShopItem(itemId=14104, price=5, goldPrice=1),
                    ShopItem(itemId=14105, price=5, goldPrice=1),
                    ShopItem(itemId=14106, price=5, goldPrice=1),
                    ShopItem(itemId=14107, price=5, goldPrice=1),
                    ShopItem(itemId=14108, price=5, goldPrice=1),
                    ShopItem(itemId=14028, price=5, goldPrice=1),
                    ShopItem(itemId=14057, price=5, goldPrice=1),
                    ShopItem(itemId=14160, price=5, goldPrice=1),
                    ShopItem(itemId=14007, price=5, goldPrice=1),
                ],
            ),
            ShopCollection(
                collectionId=4020,
                currencyId=FairiesConstants.DAISY_PETALS,
                items=[
                    ShopItem(itemId=14055, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14056, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14057, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14058, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14059, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14060, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14061, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14062, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14063, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14064, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14065, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14066, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14067, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14068, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14069, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14070, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14071, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14072, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14136, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14221, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14172, price=5, goldPrice=1, specialType=4),
                    ShopItem(itemId=14032, price=5, goldPrice=1, specialType=4),
                ],
            )
        ],
    ),

]

SHOPS_BY_ZONE = {shop.zone: shop for shop in SHOPS}

for shop in SHOPS:
    shop.collectionsById = {collection.collectionId: collection for collection in shop.collections}

def getShopByZone(zone: int) -> dict:
    return SHOPS_BY_ZONE.get(zone, {})

def getShopItemByIndex(shop: NPCShop, collectionId: int, itemIndex: int) -> ShopItem | None:
    collection = shop.collectionsById.get(collectionId)

    if not collection:
        return None

    if 0 <= itemIndex < len(collection.items):
        return collection.items[itemIndex]

    return None
