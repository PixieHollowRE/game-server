from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

# Gale's Outfitters - OutfitId 3000 - 3999

SHOP = NPCShop(
    zone=ZoneConstants.GALES_OUTFITTERS,
    shopId=3,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.GALE,
        position=(434, 429),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_GALE
    ),
    collections=[
        ShopCollection(
            collectionId=41, # Gale's Favorites
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                    ShopItem(itemId=2037, price=10, goldPrice=3, color1=47, color2=47, itemType="HeadItem"), # Buttercup Yellow Gadgety Goggles
                    ShopItem(itemId=2003, price=10, goldPrice=3, color1=184, color2=184, itemType="HeadItem"), # Hummingbird Purple Grass Bow
                    ShopItem(itemId=40, price=17, goldPrice=5, color1=4, color2=128, itemType="Shirt"), # Bluebell Blue Down Feather Sweater
                    ShopItem(itemId=1047, price=17, goldPrice=5, color1=27, color2=157, itemType="Skirt"), # Corn Cob Yellow Sleepy Time Capris
                    ShopItem(itemId=3532, price=10, goldPrice=3, color1=163, color2=262, itemType="Shoes"), # Tundra Blue Bear Slippers
            ],
        ),
        ShopCollection(
            collectionId=78, # Pixie Party Dresses
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=3001,
                    items = [
                        OutfitItem(itemId=1000129, price=40, goldPrice=13, color1=221, color2= 1, itemType="Shirt"), # Jade Green Tink's Pixie Party Top
                        OutfitItem(itemId=1001038, price=40, goldPrice=13, color1=221, color2= 1, itemType="Skirt"), # Jade Green Tink's Pixie Party Skirt
                        OutfitItem(itemId=3578, price=33, goldPrice=11, color1=221, color2= 1, itemType="Shoes"), # Jade Green Campanula Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3002,
                    items = [
                        OutfitItem(itemId=1000126, price=40, goldPrice=13, color1=40, color2=207, itemType="Shirt"), # Candy Blue Peri's Pixie Party Top
                        OutfitItem(itemId=1001035, price=40, goldPrice=13, color1=40, color2=207, itemType="Skirt"), # Candy Blue Peri's Pixie Party Skirt
                        OutfitItem(itemId=3578, price=33, goldPrice=11, color1=40, color2=207, itemType="Shoes"), # Candy Blue Campanula Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3003,
                    items = [
                        OutfitItem(itemId=1000124, price=40, goldPrice=13, color1=178, color2=10, itemType="Shirt"), # Fawn Orange Fawn's Pixie Party Top
                        OutfitItem(itemId=1001032, price=40, goldPrice=13, color1=178, color2=10, itemType="Skirt"), # Fawn Orange Fawn's Pixie Party Skirt
                        OutfitItem(itemId=3768, price=33, goldPrice=11, color1=178, color2=10, itemType="Shoes"), # Fawn Orange Autumn Leaf Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3004,
                    items = [
                        OutfitItem(itemId=1000127, price=40, goldPrice=13, color1=286, color2=286, itemType="Shirt"), # Cherry Pink Rosetta's Pixie Party Top
                        OutfitItem(itemId=1001036, price=40, goldPrice=13, color1=286, color2=286, itemType="Skirt"), # Cherry Pink Rosetta's Pixie Party Skirt
                        OutfitItem(itemId=3578, price=33, goldPrice=11, color1=286, color2=286, itemType="Shoes"), # Cherry Pink Campanula Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3005,
                    items = [
                        OutfitItem(itemId=1000128, price=40, goldPrice=13, color1=208, color2=126, itemType="Shirt"), # Cerulean Blue Sil's Pixie Party Top
                        OutfitItem(itemId=1001037, price=40, goldPrice=13, color1=208, color2=126, itemType="Skirt"), # Cerulean Blue Sil's Pixie Party Skirt
                        OutfitItem(itemId=3578, price=33, goldPrice=11, color1=208, color2=126, itemType="Shoes"), # Cerulean Blue Campanula Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3006,
                    items = [
                        OutfitItem(itemId=1000125, price=40, goldPrice=13, color1=228, color2=248, itemType="Shirt"), # Duckbill Orange Dessa's Pixie Party Top
                        OutfitItem(itemId=1001033, price=40, goldPrice=13, color1=228, color2=248, itemType="Skirt"), # Duckbill Orange Dessa's Pixie Party Skirt
                        OutfitItem(itemId=3578, price=33, goldPrice=11, color1=248, color2=248, itemType="Shoes"), # Saffron Yellow Campanula Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3007,
                    items = [
                        OutfitItem(itemId=1000130, price=40, goldPrice=13, color1=225, color2=131, itemType="Shirt"), # Eggplant Purple Vidia's Pixie Party Top
                        OutfitItem(itemId=1001039, price=40, goldPrice=13, color1=225, color2=131, itemType="Skirt"), # Eggplant Purple Vidia's Pixie Party Skirt
                        OutfitItem(itemId=3578, price=33, goldPrice=11, color1=225, color2=131, itemType="Shoes"), # Eggplant Purple Campanula Shoes
                    ],
                )
            ],
        ),  
        ShopCollection(
            collectionId=97, # Famous Fairy Collection
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=3008,
                    items = [
                        OutfitItem(itemId=185, price=40, goldPrice=16, color1=145, color2=145, itemType="Shirt"), # Tinker Bell Green Tink's Summer Top
                        OutfitItem(itemId=1167, price=40, goldPrice=16, color1=145, color2=145, itemType="Skirt"), # Tinker Bell Green Tink's Summer Skirt
                        OutfitItem(itemId=3568, price=25, goldPrice=10, color1=145, color2=224, itemType="Shoes"), # Tinker Bell Green Tie Dye Sandals with White Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3009,
                    items = [
                        OutfitItem(itemId=168, price=40, goldPrice=16, color1=174, color2=174, itemType="Shirt"), # Rosetta Red Rosetta's Summer Top
                        OutfitItem(itemId=1154, price=40, goldPrice=16, color1=174, color2=174, itemType="Skirt"), # Rosetta Red Rosetta's Summer Skirt
                        OutfitItem(itemId=3626, price=25, goldPrice=10, color1=174, color2=174, itemType="Shoes"), # Rosetta Red Ruffly Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3010,
                    items = [
                        OutfitItem(itemId=184, price=40, goldPrice=16, color1=176, color2=27, itemType="Shirt"), # Silvermist Blue Sil's Summer Top
                        OutfitItem(itemId=1166, price=40, goldPrice=16, color1=176, color2=27, itemType="Skirt"), # Silvermist Blue Sil's Summer Skirt
                        OutfitItem(itemId=3608, price=25, goldPrice=10, color1=176, color2=27, itemType="Shoes"), # Silvermist Blue Strappy Sandal
                    ],
                ),
                ShopOutfit(
                    outfitId=3011,
                    items = [
                        OutfitItem(itemId=182, price=40, goldPrice=16, color1=178, color2=123, itemType="Shirt"), # Fawn Orange Fawn's Summer Tank
                        OutfitItem(itemId=1164, price=40, goldPrice=16, color1=178, color2=123, itemType="Skirt"), # Fawn Orange Fawn's Summer Skirt
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=178, color2=123, itemType="Shoes"), # Fawn Orange Sparkle Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3012,
                    items = [
                        OutfitItem(itemId=183, price=40, goldPrice=16, color1=226, color2=29, itemType="Shirt"), # Goldenrod Yellow Dessa's Summer Tank
                        OutfitItem(itemId=1165, price=40, goldPrice=16, color1=226, color2=29, itemType="Skirt"), # Goldenrod Yellow Dessa's Summer Skirt
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=226, color2=29, itemType="Shoes"), # Goldenrod Yellow Sparkle Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3013,
                    items = [
                        OutfitItem(itemId=2077, price=25, goldPrice=10, color1=145, color2=224, itemType="HeadItem"), # Tinker Bell Green Adventure Bonnet with White Trim
                        OutfitItem(itemId=2533, price=15, goldPrice=6, color1=145, color2=145, itemType="Necklace"), # Tinker Bell Green Ruffle Neck Wrap
                        OutfitItem(itemId=80, price=40, goldPrice=16, color1=35, color2=35, itemType="Shirt"), # Celery Green Tink's Travel Top
                        OutfitItem(itemId=542, price=15, goldPrice=6, color1=86, color2=86, itemType="Belt"), # Nutmeg Brown Grass-braided Belt
                        OutfitItem(itemId=1082, price=40, goldPrice=16, color1=145, color2=1, itemType="Skirt"), # Tinker Bell Green Tink's Travel Skirt
                        OutfitItem(itemId=3562, price=25, goldPrice=10, color1=145, color2=145, itemType="Shoes"), # Tinker Bell Green Puffie Toe Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3014,
                    items = [
                        OutfitItem(itemId=85, price=40, goldPrice=16, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Fluffy Ruff Top
                        OutfitItem(itemId=1086, price=40, goldPrice=16, color1=174, color2=121, itemType="Skirt"), # Rosetta Red Bellflower Skirt
                        OutfitItem(itemId=3564, price=25, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red Slim Leaf Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3015,
                    items = [
                        OutfitItem(itemId=84, price=40, goldPrice=16, color1=126, color2=269, itemType="Shirt"), # Raindrop Blue Waterfall Top
                        OutfitItem(itemId=1087, price=40, goldPrice=16, color1=126, color2=269, itemType="Skirt"), # Raindrop Blue Waterfall Wrap
                        OutfitItem(itemId=3537, price=25, goldPrice=10, color1=126, color2=269, itemType="Shoes"), # Raindrop Blue Iris Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3016,
                    items = [
                        OutfitItem(itemId=82, price=40, goldPrice=16, color1=84, color2=178, itemType="Shirt"), # Copper Brown Feather Fun Top
                        OutfitItem(itemId=543, price=15, goldPrice=6, color1=86, color2=86, itemType="Belt"), # Nutmeg Brown Fawn Adventure Belt
                        OutfitItem(itemId=1084, price=40, goldPrice=16, color1=84, color2=178, itemType="Skirt"), # Copper Brown Critter Comfort Skirt
                        OutfitItem(itemId=3514, price=25, goldPrice=10, color1=178, color2=178, itemType="Shoes"), # Fawn Orange Ivy Ankle Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3017,
                    items = [
                        OutfitItem(itemId=2042, price=25, goldPrice=10, color1=231, color2=226, itemType="HeadItem"), # Sunny Orange Athletic Headband
                        OutfitItem(itemId=83, price=40, goldPrice=16, color1=226, color2=231, itemType="Shirt"), # Goldenrod Yellow Light Bright Top
                        OutfitItem(itemId=1085, price=40, goldPrice=16, color1=226, color2=231, itemType="Skirt"), # Goldenrod Yellow Light Bright Skirt
                        OutfitItem(itemId=3511, price=25, goldPrice=10, color1=226, color2=231, itemType="Shoes"), # Goldenrod Yellow Sparkle Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3018,
                    items = [
                        OutfitItem(itemId=1000009, price=40, goldPrice=16, color1=145, color2=224, itemType="Shirt"), # Tinker Bell Green Tink's Frosty Top
                        OutfitItem(itemId=1423, price=40, goldPrice=16, color1=145, color2=224, itemType="Skirt"), # Tinker Bell Green Tink's Frosty Skirt
                        OutfitItem(itemId=3798, price=25, goldPrice=10, color1=145, color2=224, itemType="Shoes"), # Tinker Bell Green Tink's Frosty Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3019,
                    items = [
                        OutfitItem(itemId=1000008, price=40, goldPrice=16, color1=149, color2=166, itemType="Shirt"), # Snowflake Blue Periwinkle's Frosty Top
                        OutfitItem(itemId=1422, price=40, goldPrice=16, color1=149, color2=166, itemType="Skirt"), # Snowflake Blue Periwinkle's Frosty Skirt
                        OutfitItem(itemId=3797, price=25, goldPrice=10, color1=149, color2=166, itemType="Shoes"), # Snowflake Blue Periwinkle's Frosty Flats
                    ],
                ),
                ShopOutfit(
                    outfitId=3020,
                    items = [
                        OutfitItem(itemId=2371, price=25, goldPrice=10, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Rosetta's Headwrap
                        OutfitItem(itemId=1000004, price=40, goldPrice=16, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Rosetta's Winter Top
                        OutfitItem(itemId=1658, price=15, goldPrice=6, color1=84, color2=166, itemType="WristItem"), # Copper Brown Cottonpuff Clutch
                        OutfitItem(itemId=1419, price=40, goldPrice=16, color1=224, color2=174, itemType="Skirt"), # Ivory White Rosetta's Winter Skirt
                        OutfitItem(itemId=3564, price=25, goldPrice=10, color1=174, color2=217, itemType="Shoes"), # Rosetta Red Slim Leaf Shoes with Gray Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3021,
                    items = [
                        OutfitItem(itemId=2372, price=25, goldPrice=10, color1=224, color2=224, itemType="HeadItem"), # Ivory White Sil's Winter Hat
                        OutfitItem(itemId=1000005, price=40, goldPrice=16, color1=126, color2=224, itemType="Shirt"), # Raindrop Blue Sil's Winter Top
                        OutfitItem(itemId=1420, price=40, goldPrice=16, color1=135, color2=126, itemType="Skirt"), # Boysenberry Purple Sil's Winter Skirt
                        OutfitItem(itemId=3564, price=25, goldPrice=10, color1=126, color2=135, itemType="Shoes"), # Raindrop Blue Slim Leaf Shoes with Boysenberry Purple Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3022,
                    items = [
                        OutfitItem(itemId=1000001, price=40, goldPrice=16, color1=238, color2=123, itemType="Shirt"), #  Zesty Orange Fawn's Winter Top
                        OutfitItem(itemId=1417, price=40, goldPrice=16, color1=79, color2=238, itemType="Skirt"), # Sienna Brown Fawn's Winter Skirt with Zesty Orange Trim
                        OutfitItem(itemId=3802, price=25, goldPrice=10, color1=238, color2=224, itemType="Shoes"), # Zesty Orange Fawn's Winter Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3023,
                    items = [
                        OutfitItem(itemId=2370, price=25, goldPrice=10, color1=84, color2=224, itemType="HeadItem"), # Copper Brown Iridessa's Earmuffs
                        OutfitItem(itemId=1000003, price=40, goldPrice=16, color1=84, color2=171, itemType="Shirt"), # Copper Brown Iridessa's Winter Top
                        OutfitItem(itemId=1418, price=40, goldPrice=16, color1=171, color2=84, itemType="Skirt"), # Sunrise Yellow Iridessa's Winter Skirt
                        OutfitItem(itemId=3795, price=25, goldPrice=10, color1=84, color2=224, itemType="Shoes"), # Copper Brown Iridessa's Winter Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3024,
                    items = [
                        OutfitItem(itemId=2373, price=25, goldPrice=10, color1=135, color2=5, itemType="HeadItem"), # Boysenberry Purple Vidia's Headwrap
                        OutfitItem(itemId=1000006, price=40, goldPrice=16, color1=5, color2=135, itemType="Shirt"), # Wysteria Purple Vidia's Winter Top
                        OutfitItem(itemId=1424, price=40, goldPrice=16, color1=5, color2=135, itemType="Skirt"), # Wysteria Purple Vidia's Winter Skirt
                        OutfitItem(itemId=3799, price=25, goldPrice=10, color1=135, color2=5, itemType="Shoes"), # Boysenberry Purple Vidia's Winter Boots
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=79, # Floral Collections
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=3025,
                    items = [
                        OutfitItem(itemId=2140, price=25, goldPrice=10, color1=10, color2=30, itemType="HeadItem"), # Cantaloupe Orange Citrus Barrette
                        OutfitItem(itemId=158, price=45, goldPrice=5, color1=10, color2=30, itemType="Shirt"), # Cantaloupe Orange Citrus Layer Top
                        OutfitItem(itemId=1144, price=45, goldPrice=5, color1=10, color2=30, itemType="Skirt"), # Cantaloupe Orange Citrus Peel Wrap
                        OutfitItem(itemId=3603, price=25, goldPrice=10, color1=30, color2=10, itemType="Shoes"), # Pumpkin Orange Citrus Peel Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=3026,
                    items = [
                        OutfitItem(itemId=2139, price=25, goldPrice=10, color1=18, color2=27, itemType="HeadItem"), # Waterfall Blue Strawberry Barrette with Yellow Trim
                        OutfitItem(itemId=159, price=45, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Strawberry Top
                        OutfitItem(itemId=569, price=15, goldPrice=1, color1=139, color2=18, itemType="Belt"), # Seedling Green Strawberry Sash with Waterfall Blue Trim
                        OutfitItem(itemId=1142, price=45, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Strawberry Skirt
                        OutfitItem(itemId=3602, price=25, goldPrice=10, color1=139, color2=45, itemType="Shoes"), # Seedling Green Strawberry Low Heels with Strawberry Red Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3027,
                    items = [
                        OutfitItem(itemId=2058, price=25, goldPrice=10, color1=17, color2=0, itemType="HeadItem"), # Tendershoot Green Clover Headband
                        OutfitItem(itemId=59, price=45, goldPrice=5, color1=2, color2=17, itemType="Shirt"), # Clover Green Clover Top with Tendershoot Green Trim
                        OutfitItem(itemId=1064, price=45, goldPrice=5, color1=2, color2=17, itemType="Skirt"), # Clover Green Clover Skirt with Tendershoot Green Trim
                        OutfitItem(itemId=3546, price=25, goldPrice=10, color1=2, color2=17, itemType="Shoes"), # Clover Green Clover Slippers with Tendershoot Green Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3028,
                    items = [
                        OutfitItem(itemId=2067, price=25, goldPrice=10, color1=195, color2=209, itemType="HeadItem"), # Electric Blue Helenium Headband with Deep Sea Blue Trim
                        OutfitItem(itemId=68, price=45, goldPrice=5, color1=209, color2=195, itemType="Shirt"), # Deep Sea Blue Helenium Top
                        OutfitItem(itemId=1073, price=45, goldPrice=5, color1=209, color2=195, itemType="Skirt"), # Deep Sea Blue Helenium Skirt
                        OutfitItem(itemId=3555, price=25, goldPrice=10, color1=209, color2=195, itemType="Shoes"), # Deep Sea Blue Helenium Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3029,
                    items = [
                        OutfitItem(itemId=155, price=45, goldPrice=5, color1=152, color2=129, itemType="Shirt"), # Pale Purple Plumeria Top with Dark Purple Trim
                        OutfitItem(itemId=568, price=15, goldPrice=1, color1=69, color2=69, itemType="Belt"), # Powder Blue Plumeria Garland
                        OutfitItem(itemId=1140, price=45, goldPrice=5, color1=152, color2=129, itemType="Skirt"), # Pale Purple Plumeria Sarong with Dark Purple Trim
                        OutfitItem(itemId=3608, price=25, goldPrice=10, color1=69, color2=69, itemType="Shoes"), # Powder Blue Strappy Sandal
                    ],
                ),
                ShopOutfit(
                    outfitId=3030,
                    items = [
                        OutfitItem(itemId=2047, price=25, goldPrice=3, color1=265, color2=258, itemType="HeadItem"), # Bright Sky Blue Lantana Headband
                        OutfitItem(itemId=48, price=45, goldPrice=5, color1=265, color2=258, itemType="Shirt"), # Bright Sky Blue Lantana Top
                        OutfitItem(itemId=1053, price=45, goldPrice=5, color1=265, color2=258, itemType="Skirt"), # Bright Sky Blue Lantana Skirt
                        OutfitItem(itemId=3535, price=25, goldPrice=10, color1=258, color2=258, itemType="Shoes"), # Spearmint Green Lantana Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3031,
                    items = [
                        OutfitItem(itemId=2057, price=25, goldPrice=10, color1=230, color2=121, itemType="HeadItem"), # Scarlet Red Ginkgo Headband
                        OutfitItem(itemId=58, price=45, goldPrice=5, color1=230, color2=121, itemType="Shirt"), # Scarlet Red Ginkgo Top
                        OutfitItem(itemId=1063, price=45, goldPrice=5, color1=230, color2=121, itemType="Skirt"), # Scarlet Red Ginkgo Skirt
                        OutfitItem(itemId=3545, price=25, goldPrice=10, color1=121, color2=121, itemType="Shoes"), # Daisy Pink Ginkgo Slippers 
                    ],
                ),
                ShopOutfit(
                    outfitId=3032,
                    items = [
                        OutfitItem(itemId=2060, price=25, goldPrice=10, color1=152, color2=73, itemType="HeadItem"), # Pale Purple Lemon Balm Headband with Grape Purple Trim
                        OutfitItem(itemId=61, price=45, goldPrice=5, color1=152, color2=73, itemType="Shirt"), # Pale Purple Lemon Balm Top with Grape Purple Trim
                        OutfitItem(itemId=1066, price=45, goldPrice=5, color1=73, color2=152, itemType="Skirt"), # Grape Purple Lemon Balm Skirt
                        OutfitItem(itemId=3548, price=25, goldPrice=10, color1=73, color2=152, itemType="Shoes"), # Grape Purple Lemon Balm Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3033,
                    items = [
                        OutfitItem(itemId=2052, price=25, goldPrice=10, color1=226, color2=208, itemType="HeadItem"), # Goldenrod Yellow Saffron Headband
                        OutfitItem(itemId=53, price=45, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Saffron Top
                        OutfitItem(itemId=1058, price=45, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Saffron Skirt
                        OutfitItem(itemId=3540, price=25, goldPrice=10, color1=226, color2=226, itemType="Shoes"), # Goldenrod Yellow Saffron Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3034,
                    items = [
                        OutfitItem(itemId=2061, price=25, goldPrice=10, color1=45, color2=139, itemType="HeadItem"), # Strawberry Red Poinsettia Headband with Seedling Green Trim
                        OutfitItem(itemId=62, price=45, goldPrice=5, color1=139, color2=45, itemType="Shirt"), # Seedling Green Poinsettia Top
                        OutfitItem(itemId=1067, price=45, goldPrice=5, color1=139, color2=45, itemType="Skirt"), # Seedling Green Poinsettia Skirt
                        OutfitItem(itemId=3549, price=25, goldPrice=10, color1=139, color2=45, itemType="Shoes"), # Seedling Green Poinsettia Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3035,
                    items = [
                        OutfitItem(itemId=2051, price=25, goldPrice=10, color1=18, color2=18, itemType="HeadItem"), # Waterfall Blue White Rose Headband
                        OutfitItem(itemId=52, price=45, goldPrice=5, color1=166, color2=18, itemType="Shirt"), # Snow White White Rose Top
                        OutfitItem(itemId=1057, price=45, goldPrice=5, color1=166, color2=18, itemType="Skirt"), # Snow White White Rose Skirt
                        OutfitItem(itemId=3539, price=25, goldPrice=10, color1=18, color2=18, itemType="Shoes"), # Waterfall Blue White Rose Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3036,
                    items = [
                        OutfitItem(itemId=2054, price=25, goldPrice=10, color1=287, color2=121, itemType="HeadItem"), # Dianthus Red Cosmos Headband
                        OutfitItem(itemId=55, price=45, goldPrice=5, color1=287, color2=121, itemType="Shirt"), # Dianthus Red Cosmos Top
                        OutfitItem(itemId=1060, price=45, goldPrice=5, color1=287, color2=287, itemType="Skirt"), # Dianthus Red Cosmos Skirt
                        OutfitItem(itemId=3542, price=25, goldPrice=10, color1=287, color2=121, itemType="Shoes"), # Dianthus Red Cosmos Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3037,
                    items = [
                        OutfitItem(itemId=2049, price=25, goldPrice=10, color1=136, color2=125, itemType="HeadItem"), # Peacock Blue Iris Headband
                        OutfitItem(itemId=50, price=45, goldPrice=5, color1=136, color2=136, itemType="Shirt"), # Peacock Blue Iris Top
                        OutfitItem(itemId=1055, price=45, goldPrice=5, color1=136, color2=136, itemType="Skirt"), # Peacock Blue Iris Skirt
                        OutfitItem(itemId=3537, price=25, goldPrice=10, color1=136, color2=136, itemType="Shoes"), # Peacock Blue Iris Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3038,
                    items = [
                        OutfitItem(itemId=2046, price=25, goldPrice=10, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Nerine Headband
                        OutfitItem(itemId=47, price=45, goldPrice=5, color1=277, color2=144, itemType="Shirt"), # Misty Purple Nerine Top
                        OutfitItem(itemId=1052, price=45, goldPrice=5, color1=277, color2=144, itemType="Skirt"), # Misty Purple Nerine Skirt
                        OutfitItem(itemId=3534, price=25, goldPrice=10, color1=277, color2=144, itemType="Shoes"), # Misty Purple Nerine Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3039,
                    items = [
                        OutfitItem(itemId=2065, price=25, goldPrice=10, color1=223, color2=223, itemType="HeadItem"), # Teal Blue Euphorbia Headband
                        OutfitItem(itemId=66, price=45, goldPrice=5, color1=68, color2=223, itemType="Shirt"), # Huckleberry Blue Euphorbia Top
                        OutfitItem(itemId=1071, price=45, goldPrice=5, color1=223, color2=68, itemType="Skirt"), # Teal Blue Euphorbia Skirt
                        OutfitItem(itemId=3553, price=25, goldPrice=10, color1=223, color2=68, itemType="Shoes"), # Teal Blue Euphorbia Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3040,
                    items = [
                        OutfitItem(itemId=2053, price=25, goldPrice=10, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Dahlia Headband
                        OutfitItem(itemId=54, price=45, goldPrice=5, color1=267, color2=166, itemType="Shirt"), # Celestial Blue Dahlia Top
                        OutfitItem(itemId=1059, price=45, goldPrice=5, color1=267, color2=166, itemType="Skirt"), # Celestial Blue Dahlia Skirt
                        OutfitItem(itemId=3541, price=25, goldPrice=10, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Dahlia Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3041,
                    items = [
                        OutfitItem(itemId=2059, price=25, goldPrice=10, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Geranium Headband
                        OutfitItem(itemId=60, price=45, goldPrice=5, color1=44, color2=130, itemType="Shirt"), # Plumblossom Pink Geranium Top
                        OutfitItem(itemId=1065, price=45, goldPrice=5, color1=44, color2=130, itemType="Skirt"), # Plumblossom Pink Geranium Skirt
                        OutfitItem(itemId=3547, price=25, goldPrice=10, color1=44, color2=130, itemType="Shoes"), # Plumblossom Pink Geranium Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3042,
                    items = [
                        OutfitItem(itemId=2048, price=25, goldPrice=10, color1=258, color2=264, itemType="HeadItem"), # Spearmint Green Bougainvillea Headband
                        OutfitItem(itemId=49, price=45, goldPrice=5, color1=264, color2=258, itemType="Shirt"), # Jungle Green Bougainvillea Top
                        OutfitItem(itemId=1054, price=45, goldPrice=5, color1=264, color2=258, itemType="Skirt"), # Jungle Green Bougainvillea Skirt
                        OutfitItem(itemId=3536, price=25, goldPrice=10, color1=264, color2=258, itemType="Shoes"), # Jungle Green Bougainvillea Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3043,
                    items = [
                        OutfitItem(itemId=2056, price=25, goldPrice=10, color1=51, color2=55, itemType="HeadItem"), # Periwinkle Blue Aster Headband
                        OutfitItem(itemId=57, price=45, goldPrice=5, color1=51, color2=55, itemType="Shirt"), #  Periwinkle Blue Aster Top
                        OutfitItem(itemId=1062, price=45, goldPrice=5, color1=51, color2=55, itemType="Skirt"), # Periwinkle Blue Aster Skirt
                        OutfitItem(itemId=3544, price=25, goldPrice=10, color1=51, color2=55, itemType="Shoes"), # Periwinkle Blue Aster Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3044,
                    items = [
                        OutfitItem(itemId=2121, price=25, goldPrice=10, color1=27, color2=26, itemType="HeadItem"), # Corn Cob Yellow Commelina Band
                        OutfitItem(itemId=110, price=45, goldPrice=5, color1=27, color2=26, itemType="Shirt"), # Corn Cob Yellow Commelina Top
                        OutfitItem(itemId=1122, price=45, goldPrice=5, color1=27, color2=26, itemType="Skirt"), #  Corn Cob Yellow Commelina Skirt
                        OutfitItem(itemId=3580, price=25, goldPrice=10, color1=27, color2=27, itemType="Shoes"), #  Corn Cob Yellow Commelina Shoes
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=28, # Animal-Inspired Fashions
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=3045,
                    items = [
                        OutfitItem(itemId=2073, price=25, goldPrice=10, color1=206, color2=142, itemType="HeadItem"), # Raven Black Buzzy Bee Mask
                        OutfitItem(itemId=76, price=45, goldPrice=16, color1=206, color2=142, itemType="Shirt"), # Raven Black Buzzy Bee Striped Wrap
                        OutfitItem(itemId=1003, price=45, goldPrice=16, color1=142, color2=142, itemType="Skirt"), # Bumble Bee Yellow Leafy Bubble Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=142, color2=142, itemType="Shoes"), # Bumble Bee Yellow Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3046,
                    items = [
                        OutfitItem(itemId=2071, price=25, goldPrice=10, color1=44, color2=257, itemType="HeadItem"), # Plumblossom Pink Little Light Antennae
                        OutfitItem(itemId=91, price=45, goldPrice=16, color1=44, color2=44, itemType="Shirt"), # Plumblossom Pink Little Light Top
                        OutfitItem(itemId=1091, price=45, goldPrice=16, color1=44, color2=257, itemType="Skirt"), #  Plumblossom Pink Little Light Mini
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), #  Plumblossom Pink Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3047,
                    items = [
                        OutfitItem(itemId=2071, price=25, goldPrice=10, color1=206, color2=189, itemType="HeadItem"), # Raven Black Little Light Antennae
                        OutfitItem(itemId=172, price=45, goldPrice=16, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tank
                        OutfitItem(itemId=1156, price=45, goldPrice=16, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3048,
                    items = [
                        OutfitItem(itemId=2151, price=25, goldPrice=10, color1=1, color2=1, itemType="HeadItem"), # Mint Green Dragonfly Mask
                        OutfitItem(itemId=186, price=45, goldPrice=16, color1=1, color2=1, itemType="Shirt"), # Mint Green Dragonfly Top
                        OutfitItem(itemId=1168, price=45, goldPrice=16, color1=1, color2=1, itemType="Skirt"), # Mint Green Dragonfly Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=1, color2=1, itemType="Shoes"), # Mint Green Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3049,
                    items = [
                        OutfitItem(itemId=2150, price=25, goldPrice=10, color1=267, color2=186, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
                        OutfitItem(itemId=187, price=45, goldPrice=16, color1=267, color2=186, itemType="Shirt"), # Celestial Blue Hummingbird Top
                        OutfitItem(itemId=1169, price=45, goldPrice=16, color1=267, color2=186, itemType="Skirt"), # Celestial Blue Hummingbird Skirt
                        OutfitItem(itemId=3501, price=25, goldPrice=10, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3050,
                    items = [
                        OutfitItem(itemId=2033, price=25, goldPrice=10, color1=175, color2=159, itemType="HeadItem"), # Creek Green Firefly Spotlight Barrette
                        OutfitItem(itemId=2524, price=15, goldPrice=6, color1=175, color2=159, itemType="Necklace"), # Creek Green Firefly Glow Choker
                        OutfitItem(itemId=29, price=45, goldPrice=16, color1=175, color2=159, itemType="Shirt"), # Creek Green Orchid Firefly Wrap
                        OutfitItem(itemId=1032, price=45, goldPrice=16, color1=175, color2=159, itemType="Skirt"), # Creek Green Slit Satin Firefly Skirt
                        OutfitItem(itemId=3519, price=25, goldPrice=10, color1=175, color2=159, itemType="Shoes"), # Creek Green Firefly Glow Toes Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3051,
                    items = [
                        OutfitItem(itemId=90, price=45, goldPrice=16, color1=63, color2=166, itemType="Shirt"), # Butterfly Blue Fanciful Flutter Top with White Trim
                        OutfitItem(itemId=548, price=15, goldPrice=1, color1=63, color2=166, itemType="Belt"), # Butterfly Blue Fanciful Flutter Sash with White Trim
                        OutfitItem(itemId=1090, price=45, goldPrice=16, color1=63, color2=166, itemType="Skirt"), # Butterfly Blue Fanciful Flutter Gown with White Trim
                        OutfitItem(itemId=3559, price=25, goldPrice=10, color1=63, color2=166, itemType="Shoes"), # Butterfly Blue Fanciful Flutter Flats with White Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3052,
                    items = [
                        OutfitItem(itemId=376, price=45, goldPrice=16, color1=189, color2=206, itemType="Shirt"), # Ladybug Red Morpho Butterfly Top with Raven Black Trim
                        OutfitItem(itemId=635, price=15, goldPrice=1, color1=189, color2=189, itemType="Belt"), # Ladybug Red Morpho Butterfly Sash
                        OutfitItem(itemId=1294, price=45, goldPrice=16, color1=30, color2=206, itemType="Skirt"), # Pumpkin Orange Morpho Butterfly Skirt with Raven Black Trim
                        OutfitItem(itemId=3716, price=25, goldPrice=10, color1=206, color2=189, itemType="Shoes"), # Raven Black Morpho Butterfly Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3053,
                    items = [
                        OutfitItem(itemId=2367, price=25, goldPrice=10, color1=216, color2=216, itemType="HeadItem"), # Slate Gray Raven Mask
                        OutfitItem(itemId=499, price=45, goldPrice=16, color1=206, color2=216, itemType="Shirt"), # Raven Black Raven Costume Top with Slate Gray Trim
                        OutfitItem(itemId=1415, price=45, goldPrice=16, color1=206, color2=216, itemType="Skirt"), # Raven Black Raven Skirt with Slate Gray Trim
                        OutfitItem(itemId=3794, price=25, goldPrice=10, color1=206, color2=216, itemType="Shoes"), # Raven Black Raven Heels with Slate Gray Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3054,
                    items = [
                        OutfitItem(itemId=2347, price=25, goldPrice=10, color1=224, color2=224, itemType="HeadItem"), # Ivory White Fox Mask
                        OutfitItem(itemId=1000011, price=45, goldPrice=16, color1=224, color2=224, itemType="Shirt"), # Ivory White Fox Top
                        OutfitItem(itemId=1395, price=45, goldPrice=16, color1=224, color2=224, itemType="Skirt"), # Ivory White Fox Skirt
                        OutfitItem(itemId=3801, price=25, goldPrice=10, color1=224, color2=224, itemType="Shoes"), # Ivory White Furry Critter Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3055,
                    items = [
                        OutfitItem(itemId=2360, price=25, goldPrice=10, color1=206, color2=169, itemType="HeadItem"), # Raven Black Raccoon Mask
                        OutfitItem(itemId=481, price=45, goldPrice=16, color1=169, color2=206, itemType="Shirt"), # Squirrel Gray Raccoon Top
                        OutfitItem(itemId=1398, price=45, goldPrice=16, color1=169, color2=206, itemType="Skirt"), # Squirrel Gray Raccoon Skirt
                        OutfitItem(itemId=3801, price=25, goldPrice=10, color1=206, color2=169, itemType="Shoes"), # Raven Black Furry Critter Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=3056,
                    items = [
                        OutfitItem(itemId=2440, price=25, goldPrice=10, color1=212, color2=194, itemType="HeadItem"), # Indigo Purple Songbird Headband
                        OutfitItem(itemId=1000078, price=45, goldPrice=16, color1=194, color2=212, itemType="Shirt"), # Electric Pink Songbird Top
                        OutfitItem(itemId=1484, price=45, goldPrice=16, color1=212, color2=194, itemType="Skirt"), # Indigo Purple Songbird Skirt
                        OutfitItem(itemId=3869, price=25, goldPrice=10, color1=212, color2=194, itemType="Shoes"), # Indigo Purple Songbird Heels
                    ],
                )
            ],
        ),   
        ShopCollection(
            collectionId=40, # Casual and Sporty Wear
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=3057,
                    items = [
                        OutfitItem(itemId=303, price=45, goldPrice=16, color1=166, color2=286, itemType="Shirt"), # Snow White Snowbound Ski Jacket with Cherry Pink Trim
                        OutfitItem(itemId=1253, price=45, goldPrice=16, color1=166, color2=286, itemType="Skirt"), # Snow White Warm Ski Pants with Cherry Pink Trim
                        OutfitItem(itemId=3682, price=25, goldPrice=10, color1=105, color2=286, itemType="Shoes"), # Siltstone Tan Swift Skis with Cherry Pink Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3058,
                    items = [
                        OutfitItem(itemId=197, price=45, goldPrice=16, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Rainbow Tee
                        OutfitItem(itemId=588, price=15, goldPrice=6, color1=141, color2=141, itemType="Belt"), # Thundercloud Gray Studded Belt
                        OutfitItem(itemId=1143, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Denim Flyers
                        OutfitItem(itemId=3849, price=25, goldPrice=10, color1=224, color2=224, itemType="Shoes"), # Ivory White Rainbow Sneakers
                    ],
                ),
                ShopOutfit(
                    outfitId=3059,
                    items = [
                        OutfitItem(itemId=145, price=45, goldPrice=16, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Sporty Top
                        OutfitItem(itemId=1048, price=45, goldPrice=16, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sports Shorts
                        OutfitItem(itemId=3504, price=25, goldPrice=10, color1=162, color2=162, itemType="Shoes"), # Sunglow Yellow Striders
                    ],
                ),
                ShopOutfit(
                    outfitId=3060,
                    items = [
                        OutfitItem(itemId=214, price=45, goldPrice=16, color1=121, color2=282, itemType="Shirt"), # Daisy Pink Pretty Plaid Top
                        OutfitItem(itemId=1187, price=45, goldPrice=16, color1=121, color2=121, itemType="Skirt"), # Daisy Pink Stitched Leaf Skirt
                        OutfitItem(itemId=3620, price=25, goldPrice=10, color1=121, color2=121, itemType="Shoes"), # Daisy Pink Pretty Plaid Flats
                    ],
                ),
                ShopOutfit(
                    outfitId=3061,
                    items = [
                        OutfitItem(itemId=283, price=45, goldPrice=16, color1=211, color2=5, itemType="Shirt"), # Gentian Purple Sporty Tankini
                        OutfitItem(itemId=1233, price=45, goldPrice=16, color1=211, color2=5, itemType="Skirt"), # Gentian Purple Sporty Swim Skirt
                        OutfitItem(itemId=3757, price=25, goldPrice=10, color1=211, color2=5, itemType="Shoes"), # Gentian Purple Summer Splash Shoes with Wysteria Purple Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=3062,
                    items = [
                        OutfitItem(itemId=2335, price=25, goldPrice=10, color1=267, color2=166, itemType="HeadItem"), # Celestial Blue Summer Splash Hat
                        OutfitItem(itemId=415, price=45, goldPrice=16, color1=267, color2=166, itemType="Shirt"), # Celestial Blue Summer Splash Top
                        OutfitItem(itemId=1334, price=45, goldPrice=16, color1=267, color2=166, itemType="Skirt"), # Celestial Blue Summer Splash Skirt
                        OutfitItem(itemId=3757, price=25, goldPrice=10, color1=166, color2=267, itemType="Shoes"), # Snow White Summer Splash Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=3063,
                    items = [
                        OutfitItem(itemId=2043, price=25, goldPrice=10, color1=175, color2=175, itemType="HeadItem"), # Creek Green Sunny Days Hat
                        OutfitItem(itemId=45, price=45, goldPrice=16, color1=17, color2=175, itemType="Shirt"), # Tendershoot Green Sunshine Top
                        OutfitItem(itemId=1050, price=45, goldPrice=16, color1=35, color2=175, itemType="Skirt"), # Celery Green Sunshine Skirt
                        OutfitItem(itemId=3610, price=25, goldPrice=10, color1=17, color2=175, itemType="Shoes"), # Tendershoot Green Fresh Petal Pumps
                    ],
                ),
                ShopOutfit(
                    outfitId=3064,
                    items = [
                        OutfitItem(itemId=46, price=45, goldPrice=16, color1=278, color2=135, itemType="Shirt"), # Aster Purple Tropical Top
                        OutfitItem(itemId=539, price=15, goldPrice=6, color1=135, color2=135, itemType="Belt"), # Boysenberry Purple Tropical Belt
                        OutfitItem(itemId=1051, price=45, goldPrice=16, color1=278, color2=135, itemType="Skirt"), # Aster Purple Tropical Sarong
                        OutfitItem(itemId=3568, price=25, goldPrice=10, color1=135, color2=278, itemType="Shoes"), # Boysenberry Purple Tie Dye Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=3065,
                    items = [
                        OutfitItem(itemId=28, price=45, goldPrice=16, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Bubble Button Top
                        OutfitItem(itemId=532, price=15, goldPrice=6, color1=69, color2=208, itemType="Belt"), # Powder Blue Triple Bubble Belt
                        OutfitItem(itemId=1010, price=45, goldPrice=16, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Lily Pad Bubble Skirt
                        OutfitItem(itemId=3520, price=25, goldPrice=10, color1=208, color2=208, itemType="Shoes"), # Cerulean Blue Bubble Top Slippers
                    ],
                )
            ],
        ),    
        ShopCollection(
            collectionId=9, # Berry
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=3085, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=2009, price=20, goldPrice=8, color1=42, color2=51, itemType="HeadItem"), # Blueberry Blue Rose Bloom Barrettes
                        OutfitItem(itemId=480, price=35, goldPrice=13, color1=42, color2=51, itemType="Shirt"), # Blueberry Blue Sleek and Stylish Top
                        OutfitItem(itemId=653, price=10, goldPrice=5, color1=42, color2=42, itemType="Belt"), # Blueberry Blue Spring Rose Sash
                        OutfitItem(itemId=1377, price=35, goldPrice=13, color1=42, color2=51, itemType="Skirt"), # Blueberry Blue Sweet Stripey Skirt
                        OutfitItem(itemId=3778, price=20, goldPrice=8, color1=42, color2=51, itemType="Shoes"), # Blueberry Blue Colorblock Wedges
                ],
            ),
                ShopOutfit(
                    outfitId=3086, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=1000073, price=35, goldPrice=13, color1=199, color2=26, itemType="Shirt"), # Cherryblossom Pink Spring Rose Top
                        OutfitItem(itemId=653, price=10, goldPrice=5, color1=26, color2=26, itemType="Belt"), # Raspberry Pink Spring Rose Sash
                        OutfitItem(itemId=1077, price=35, goldPrice=13, color1=130, color2=26, itemType="Skirt"), # Orchid Pink Teeny Tiny Tutu
                        OutfitItem(itemId=3845, price=15, goldPrice=8, color1=199, color2=26, itemType="Shoes"), # Cherryblossom Pink Spring Rose Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=3087, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=13, price=35, goldPrice=13, color1=272, color2=47, itemType="Shirt"), # Charcoal Gray Maple Leaf Wrap
                        OutfitItem(itemId=1392, price=35, goldPrice=13, color1=272, color2=47, itemType="Skirt"), # Charcoal Gray Pixie Diamond Skirt
                        OutfitItem(itemId=3518, price=15, goldPrice=8, color1=272, color2=47, itemType="Shoes"), # Charcoal Gray Lavender Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=3088, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=331, price=35, goldPrice=13, color1=189, color2=272, itemType="Shirt"), # Ladybug Red Gentian Top
                        OutfitItem(itemId=1268, price=35, goldPrice=13, color1=189, color2=272, itemType="Skirt"), # Ladybug Red Gentian Skirt
                        OutfitItem(itemId=3691, price=15, goldPrice=8, color1=189, color2=272, itemType="Shoes"), # Ladybug Red Gentian Shoes
                    ],
                ),
            ]
        )
    ]
)