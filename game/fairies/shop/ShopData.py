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
            TEST_SHOP_DATA
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
        zone=ZoneConstants.DAISYS_DYES,
        shopId=2000,
        shopkeeper=Shopkeeper(
            name=FamousFairyData.DAISY,
            position=(390, 434),
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_DAISY
        ),
        collections=[
            TEST_SHOP_DATA
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
            TEST_SHOP_DATA
        ],
    ),

    NPCShop( # BECK IS FACING THE WRONG WAY - HOW DO I FLIP HER???
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
            position=(500, 350), # NOT PLACED
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
            position=(500, 350), # NOT PLACED
            famousFairyId=FamousFairyData.FAMOUS_FAIRY_BROOK
        ),
        collections=[
            TEST_SHOP_DATA
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
