from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.BECKS_ANIMAL_NURSERY,
    shopId=5000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.BECK,
        position=(387, 440),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_BECK
    ),
    collections=[
        ShopCollection(
            collectionId=5001, # Fireflies
            currencyId=INGREDIENTS["HONEYCOMBS"].id,
            items=[
                ShopItem(itemId=73000, price=80, goldPrice=25, color1=17, color2=60, itemType="Firefly"), # Tendershoot Green Firefly
                ShopItem(itemId=73000, price=80, goldPrice=25, color1=11, color2=60, itemType="Firefly"), # Marigold Yellow Firefly	
                ShopItem(itemId=73000, price=80, goldPrice=25, color1=64, color2=60, itemType="Firefly"), # Emerald Green Firefly
                ShopItem(itemId=73000, price=80, goldPrice=25, color1=54, color2=130, itemType="Firefly"), # Peony Pink Firefly
                ShopItem(itemId=73000, price=80, goldPrice=25, color1=32, color2=149, itemType="Firefly"), # Mulberry Purple Firefly	
                ShopItem(itemId=73000, price=80, goldPrice=25, color1=142, color2=72, itemType="Firefly"), # Bumble Bee Yellow Firefly 
            ]
        ),
        ShopCollection(
            collectionId=5002, # Ladybugs
            currencyId=INGREDIENTS["BUTTERCUP_PETALS"].id,
            items=[
                ShopItem(itemId=73001, price=100, goldPrice=30, color1=45, color2=55, itemType="Ladybug"), # Strawberry Red Ladybug	
                ShopItem(itemId=73001, price=100, goldPrice=30, color1=142, color2=55, itemType="Ladybug"), # Bumble Bee Yellow Ladybug
                ShopItem(itemId=73001, price=100, goldPrice=30, color1=124, color2=55, itemType="Ladybug"), # Forget-Me-Not Blue Ladybug
                ShopItem(itemId=73001, price=100, goldPrice=30, color1=65, color2=118, itemType="Ladybug"), # Summer Green Ladybug
                ShopItem(itemId=73001, price=100, goldPrice=30, color1=11, color2=125, itemType="Ladybug"), # Marigold Yellow Ladybug
                ShopItem(itemId=73001, price=100, goldPrice=30, color1=8, color2=139, itemType="Ladybug"), # Watermelon Pink Ladybug

            ]
        ),   
        ShopCollection(
            collectionId=5003, # Baby Hummingbirds
            currencyId=INGREDIENTS["BLUEBERRIES"].id,
            items=[
                ShopItem(itemId=73002, price=110, goldPrice=35, color1=82, color2=128, itemType="Hummingbird"), # Raspberry Red Hummingbird
                ShopItem(itemId=73002, price=110, goldPrice=35, color1=64, color2=128, itemType="Hummingbird"), # Emerald Green Hummingbird
                ShopItem(itemId=73002, price=110, goldPrice=35, color1=50, color2=128, itemType="Hummingbird"), # Cornflower Blue Hummingbird
                ShopItem(itemId=73002, price=110, goldPrice=35, color1=50, color2=151, itemType="Hummingbird"), # Cornflower Blue Hummingbird with Yellow Trim
                ShopItem(itemId=73002, price=110, goldPrice=35, color1=34, color2=111, itemType="Hummingbird"), # Primrose Pink Hummingbird
                ShopItem(itemId=73002, price=110, goldPrice=35, color1=72, color2=153, itemType="Hummingbird"), # Mauve Purple Hummingbird
            ]
        ),
        ShopCollection(
            collectionId=5004, # Dragonflies
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            items=[
                ShopItem(itemId=73003, price=50, goldPrice=20, color1=81, color2=141, itemType="Dragonfly"), # Crimson Red Dragonfly
                ShopItem(itemId=73003, price=50, goldPrice=20, color1=137, color2=141, itemType="Dragonfly"), # Lemon Yellow Dragonfly
                ShopItem(itemId=73003, price=50, goldPrice=20, color1=145, color2=141, itemType="Dragonfly"), # Tinker Bell Green Dragonfly
                ShopItem(itemId=73003, price=50, goldPrice=20, color1=144, color2=32, itemType="Dragonfly"), # Petal Pink Dragonfly
                ShopItem(itemId=73003, price=50, goldPrice=20, color1=128, color2=41, itemType="Dragonfly"), # Carnation White Dragonfly	
                ShopItem(itemId=73003, price=50, goldPrice=20, color1=133, color2=48, itemType="Dragonfly"), # Marina Blue Dragonfly

            ]
        ),
        ShopCollection(
            collectionId=5005, # Bees
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=73004, price=55, goldPrice=23, color1=142, color2=73, itemType="Bee"), # Bumble Bee Yellow Bee
                ShopItem(itemId=73004, price=55, goldPrice=23, color1=10, color2=82, itemType="Bee"), # Cantaloupe Orange Bee
                ShopItem(itemId=73004, price=55, goldPrice=23, color1=28, color2=56, itemType="Bee"), # Cinnamon Brown Bee
                ShopItem(itemId=73004, price=55, goldPrice=23, color1=159, color2=40, itemType="Bee"), # Tea Green Bee
                ShopItem(itemId=73004, price=55, goldPrice=23, color1=156, color2=73, itemType="Bee"), # Friendship Pink Bee
                ShopItem(itemId=73004, price=55, goldPrice=23, color1=6, color2=118, itemType="Bee"), # Havendish Blue Bee


            ]
        ),
        ShopCollection(
            collectionId=5007, # Butterflies
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=73006, price=120, goldPrice=60, color1=82, color2=189, itemType="Butterfly"), # Raspberry Red Butterfly
                ShopItem(itemId=73006, price=120, goldPrice=60, color1=288, color2=200, itemType="Butterfly"), # Sparkle Pink Butterfly
                ShopItem(itemId=73006, price=120, goldPrice=60, color1=11, color2=228, itemType="Butterfly"), # Marigold Yellow Butterfly	
                ShopItem(itemId=73006, price=120, goldPrice=60, color1=143, color2=261, itemType="Butterfly"), # June Bug Green Butterfly
                ShopItem(itemId=73006, price=120, goldPrice=60, color1=50, color2=185, itemType="Butterfly"), # Cornflower Blue Butterfly
                ShopItem(itemId=73006, price=120, goldPrice=60, color1=278, color2=279, itemType="Butterfly"), # Aster Purple Butterfly
            ],
        ),
    ],
)