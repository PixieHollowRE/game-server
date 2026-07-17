from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.ZEPHYRS_ZOOM_ROOM,
    shopId=7,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.ZEPHYR,
        position=(408, 452),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_ZEPHYR
    ),
    collections=[
        ShopCollection(
            collectionId=1, # Rapid Racer - Fairies
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=2219, price=10, goldPrice=4, color1=191, color2=72, itemType="HeadItem"), # Vidia Black Racing Goggles
                ShopItem(itemId=302, price=18, goldPrice=7, color1=129, color2=72, itemType="Shirt"), # Fig Purple Rapid Racer Top
                ShopItem(itemId=1264, price=18, goldPrice=7, color1=129, color2=72, itemType="Skirt"), # Fig Purple Rapid Racer Knickers
                ShopItem(itemId=3678, price=13, goldPrice=5, color1=72, color2=191, itemType="Shoes"), # Mauve Purple Riding Boots

                ShopItem(itemId=2219, price=10, goldPrice=4, color1=55, color2=48, itemType="HeadItem"), # Pepper Black Racing Goggles
                ShopItem(itemId=302, price=18, goldPrice=7, color1=48, color2=41, itemType="Shirt"), # Sea Green Rapid Racer Top
                ShopItem(itemId=1264, price=18, goldPrice=7, color1=41, color2=48, itemType="Skirt"), # Moonshadow Blue Rapid Racer Knickers
                ShopItem(itemId=3678, price=13, goldPrice=5, color1=55, color2=48, itemType="Shoes"), # Sea Green Riding Boots
            ],
        ),
        ShopCollection(
            collectionId=42, # Rapid Racer - Sparrows
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=2225, price=10, goldPrice=4, color1=55, color2=48, itemType="HeadItem"), # Pepper Black Racing Goggles
                ShopItem(itemId=306, price=18, goldPrice=7, color1=48, color2=41, itemType="Shirt"), # Sea Green Rapid Racer Top
                ShopItem(itemId=1255, price=18, goldPrice=7, color1=41, color2=48, itemType="Skirt"), # Moonshadow Blue Rapid Racer Knickers
                ShopItem(itemId=3681, price=13, goldPrice=5, color1=55, color2=48, itemType="Shoes"), # Pepper Black Riding Boots with Sea Green Trim

                ShopItem(itemId=2225, price=10, goldPrice=4, color1=191, color2=189, itemType="HeadItem"), # Vidia Black Racing Goggles
                ShopItem(itemId=306, price=18, goldPrice=7, color1=189, color2=113, itemType="Shirt"), # Ladybug Red Rapid Racer Top
                ShopItem(itemId=1255, price=18, goldPrice=7, color1=191, color2=189, itemType="Skirt"), # Vidia Black Rapid Racer Knickers
                ShopItem(itemId=3681, price=13, goldPrice=5, color1=75, color2=189, itemType="Shoes"), # Umber Brown Riding Boots
            ],
        ),
        ShopCollection(
            collectionId=69, # Super Speedster - Fairies
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=323, price=18, goldPrice=5, color1=8, color2=81, itemType="Shirt"), # Watermelon Pink Super Speedster Jacket
                ShopItem(itemId=1263, price=18, goldPrice=7, color1=8, color2=81, itemType="Skirt"), # Watermelon Pink Super Speedster Pants
                ShopItem(itemId=3685, price=13, goldPrice=5, color1=81, color2=8, itemType="Shoes"), # Crimson Red Finish Line Shoes

                ShopItem(itemId=323, price=18, goldPrice=7, color1=151, color2=111, itemType="Shirt"), # Peanut Yellow Super Speedster Jacket
                ShopItem(itemId=1263, price=18, goldPrice=7, color1=151, color2=111, itemType="Skirt"), # Peanut Yellow Super Speedster Pants
                ShopItem(itemId=3685, price=13, goldPrice=5, color1=151, color2=111, itemType="Shoes"), # Peanut Yellow Finish Line Shoes
            ],
        ),
        ShopCollection(
            collectionId=70, # Super Speedster - Sparrow
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=318, price=18, goldPrice=7, color1=74, color2=92, itemType="Shirt"), # Soil Brown Super Speedster Jacket
                ShopItem(itemId=1257, price=18, goldPrice=7, color1=74, color2=92, itemType="Skirt"), # Soil Brown Super Speedster Pants
                ShopItem(itemId=3686, price=13, goldPrice=5, color1=74, color2=92, itemType="Shoes"), # Soil Brown Finish Line Shoes

                ShopItem(itemId=318, price=18, goldPrice=7, color1=172, color2=125, itemType="Shirt"), # Forest Green Super Speedster Jacket
                ShopItem(itemId=1257, price=18, goldPrice=7, color1=125, color2=172, itemType="Skirt"), # Pine Green Super Speedster Pants
                ShopItem(itemId=3686, price=13, goldPrice=5, color1=125, color2=172, itemType="Shoes"), # Pine Green Finish Line Shoes
            ],
        ),
        ShopCollection(
            collectionId=71, # Fast Flash Racer - Fairies
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=322, price=18, goldPrice=7, color1=130, color2=181, itemType="Shirt"), # Orchid Pink Fast Flash Racing Top
                ShopItem(itemId=1260, price=18, goldPrice=7, color1=130, color2=181, itemType="Skirt"), # Orchid Pink Fast Flash Racing Pants
                ShopItem(itemId=3685, price=13, goldPrice=5, color1=181, color2=130, itemType="Shoes"), # Cupcake Pink Finish Line Shoes

                ShopItem(itemId=322, price=18, goldPrice=7, color1=24, color2=185, itemType="Shirt"), # Sky Blue Fast Flash Racing Top
                ShopItem(itemId=1260, price=18, goldPrice=7, color1=24, color2=185, itemType="Skirt"), # Sky Blue Fast Flash Racing Pants
                ShopItem(itemId=3685, price=13, goldPrice=5, color1=185, color2=24, itemType="Shoes"), # Midnight Blue Finish Line Shoes
            ],
        ),
        ShopCollection(
            collectionId=72, # Fast Flash Racer - Sparrow
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=319, price=18, goldPrice=7, color1=24, color2=185, itemType="Shirt"), # Sky Blue Fast Flash Racing Top
                ShopItem(itemId=1258, price=18, goldPrice=7, color1=185, color2=24, itemType="Skirt"), # Midnight Blue Fast Flash Racing Pants
                ShopItem(itemId=3686, price=13, goldPrice=5, color1=185, color2=24, itemType="Shoes"), # Midnight Blue Finish Line Shoes

                ShopItem(itemId=319, price=18, goldPrice=7, color1=12, color2=138, itemType="Shirt"), # Tangerine Orange Fast Flash Racing Top
                ShopItem(itemId=1258, price=18, goldPrice=7, color1=138, color2=12, itemType="Skirt"), # Persimmon Orange Fast Flash Racing Pants
                ShopItem(itemId=3686, price=13, goldPrice=5, color1=138, color2=12, itemType="Shoes"), # Persimmon Orange Finish Line Shoes
            ],
        ),
        ShopCollection(
            collectionId=18, # Riding Helmets
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=2223, price=8, goldPrice=3, color1=105, color2=92, itemType="HeadItem"), # Siltstone Tan Walnut Shell Helmet
                ShopItem(itemId=2223, price=8, goldPrice=3, color1=61, color2=55, itemType="HeadItem"), # Pale Lilac Purple Walnut Shell Helmet
                ShopItem(itemId=2220, price=13, goldPrice=5, color1=52, color2=129, itemType="HeadItem"), # Lavender Purple Rapid Racer Helmet
                ShopItem(itemId=2220, price=13, goldPrice=5, color1=48, color2=41, itemType="HeadItem"), # Sea Green Rapid Racer Helmet
                ShopItem(itemId=2242, price=13, goldPrice=5, color1=130, color2=181, itemType="HeadItem"), # Orchid Pink Vintage Racer Helmet
                ShopItem(itemId=2242, price=13, goldPrice=5, color1=24, color2=185, itemType="HeadItem"), # Sky Blue Vintage Racer Helmet

                # Sparrows \/
                ShopItem(itemId=2229, price=8, goldPrice=3, color1=105, color2=92, itemType="HeadItem"), # Siltstone Tan Walnut Shell Helmet
                ShopItem(itemId=2229, price=8, goldPrice=3, color1=61, color2=55, itemType="HeadItem"), # Pale Lilac Purple Walnut Shell Helmet
                ShopItem(itemId=2226, price=13, goldPrice=5, color1=48, color2=41, itemType="HeadItem"), # Sea Green Rapid Racer Helmet
                ShopItem(itemId=2226, price=13, goldPrice=5, color1=113, color2=189, itemType="HeadItem"), # Pale Rose Red Rapid Racer Helmet
                ShopItem(itemId=2244, price=13, goldPrice=5, color1=24, color2=185, itemType="HeadItem"), # Sky Blue Vintage Racer Helmet
                ShopItem(itemId=2244, price=13, goldPrice=5, color1=12, color2=138, itemType="HeadItem"), # Tangerine Orange Vintage Racer Helmet

                # Both \/
                ShopItem(itemId=2243, price=13, goldPrice=5, color1=81, color2=8, itemType="HeadItem"), # Crimson Red Dustkicker Helmet
                ShopItem(itemId=2243, price=13, goldPrice=5, color1=151, color2=111, itemType="HeadItem"), # Peanut Yellow Dustkicker Helmet
                ShopItem(itemId=2243, price=13, goldPrice=5, color1=172, color2=172, itemType="HeadItem"), # Forest Green Dustkicker Helmet
                ShopItem(itemId=2243, price=13, goldPrice=5, color1=74, color2=74, itemType="HeadItem"), # Soil Brown Dustkicker Helmet
            ],
        ),
    ],
)