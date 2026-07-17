from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

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
            items=[
                ShopItem(itemId=1000129, price=40, goldPrice=13, color1=221, color2= 1, itemType="Shirt"), # Jade Green Tink's Pixie Party Top
                ShopItem(itemId=1001038, price=40, goldPrice=13, color1=221, color2= 1, itemType="Skirt"), # Jade Green Tink's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=221, color2= 1, itemType="Shoes"), # Jade Green Campanula Shoes

                ShopItem(itemId=1000126, price=40, goldPrice=13, color1=40, color2=207, itemType="Shirt"), # Candy Blue Peri's Pixie Party Top
                ShopItem(itemId=1001035, price=40, goldPrice=13, color1=40, color2=207, itemType="Skirt"), # Candy Blue Peri's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=40, color2=207, itemType="Shoes"), # Candy Blue Campanula Shoes

                ShopItem(itemId=1000124, price=40, goldPrice=13, color1=178, color2=10, itemType="Shirt"), # Fawn Orange Fawn's Pixie Party Top
                ShopItem(itemId=1001032, price=40, goldPrice=13, color1=178, color2=10, itemType="Skirt"), # Fawn Orange Fawn's Pixie Party Skirt
                ShopItem(itemId=3768, price=33, goldPrice=11, color1=178, color2=10, itemType="Shoes"), # Fawn Orange Autumn Leaf Boots

                ShopItem(itemId=1000127, price=40, goldPrice=13, color1=286, color2=286, itemType="Shirt"), # Cherry Pink Rosetta's Pixie Party Top
                ShopItem(itemId=1001036, price=40, goldPrice=13, color1=286, color2=286, itemType="Skirt"), # Cherry Pink Rosetta's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=286, color2=286, itemType="Shoes"), # Cherry Pink Campanula Shoes

                ShopItem(itemId=1000128, price=40, goldPrice=13, color1=208, color2=126, itemType="Shirt"), # Cerulean Blue Sil's Pixie Party Top
                ShopItem(itemId=1001037, price=40, goldPrice=13, color1=208, color2=126, itemType="Skirt"), # Cerulean Blue Sil's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=208, color2=126, itemType="Shoes"), # Cerulean Blue Campanula Shoes

                ShopItem(itemId=1000125, price=40, goldPrice=13, color1=228, color2=248, itemType="Shirt"), # Duckbill Orange Dessa's Pixie Party Top
                ShopItem(itemId=1001033, price=40, goldPrice=13, color1=228, color2=248, itemType="Skirt"), # Duckbill Orange Dessa's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=248, color2=248, itemType="Shoes"), # Saffron Yellow Campanula Shoes

                ShopItem(itemId=1000130, price=40, goldPrice=13, color1=225, color2=131, itemType="Shirt"), # Eggplant Purple Vidia's Pixie Party Top
                ShopItem(itemId=1001039, price=40, goldPrice=13, color1=225, color2=131, itemType="Skirt"), # Eggplant Purple Vidia's Pixie Party Skirt
                ShopItem(itemId=3578, price=33, goldPrice=11, color1=225, color2=131, itemType="Shoes"), # Eggplant Purple Campanula Shoes
            ],
        ),  
        ShopCollection(
            collectionId=97, # Famous Fairy Collection
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=185, price=40, goldPrice=16, color1=145, color2=145, itemType="Shirt"), # Tinker Bell Green Tink's Summer Top
                ShopItem(itemId=1167, price=40, goldPrice=16, color1=145, color2=145, itemType="Skirt"), # Tinker Bell Green Tink's Summer Skirt
                ShopItem(itemId=3568, price=25, goldPrice=10, color1=145, color2=224, itemType="Shoes"), # Tinker Bell Green Tie Dye Sandals with White Trim

                ShopItem(itemId=168, price=40, goldPrice=16, color1=174, color2=174, itemType="Shirt"), # Rosetta Red Rosetta's Summer Top
                ShopItem(itemId=1154, price=40, goldPrice=16, color1=174, color2=174, itemType="Skirt"), # Rosetta Red Rosetta's Summer Skirt
                ShopItem(itemId=3626, price=25, goldPrice=10, color1=174, color2=174, itemType="Shoes"), # Rosetta Red Ruffly Slippers

                ShopItem(itemId=184, price=40, goldPrice=16, color1=176, color2=27, itemType="Shirt"), # Silvermist Blue Sil's Summer Top
                ShopItem(itemId=1166, price=40, goldPrice=16, color1=176, color2=27, itemType="Skirt"), # Silvermist Blue Sil's Summer Skirt
                ShopItem(itemId=3608, price=25, goldPrice=10, color1=176, color2=27, itemType="Shoes"), # Silvermist Blue Strappy Sandal

                ShopItem(itemId=182, price=40, goldPrice=16, color1=178, color2=123, itemType="Shirt"), # Fawn Orange Fawn's Summer Tank
                ShopItem(itemId=1164, price=40, goldPrice=16, color1=178, color2=123, itemType="Skirt"), # Fawn Orange Fawn's Summer Skirt
                ShopItem(itemId=3511, price=25, goldPrice=10, color1=178, color2=123, itemType="Shoes"), # Fawn Orange Sparkle Slippers

                ShopItem(itemId=183, price=40, goldPrice=16, color1=226, color2=29, itemType="Shirt"), # Goldenrod Yellow Dessa's Summer Tank
                ShopItem(itemId=1165, price=40, goldPrice=16, color1=226, color2=29, itemType="Skirt"), # Goldenrod Yellow Dessa's Summer Skirt
                ShopItem(itemId=3511, price=25, goldPrice=10, color1=226, color2=29, itemType="Shoes"), # Goldenrod Yellow Sparkle Slippers

                ShopItem(itemId=2077, price=25, goldPrice=10, color1=145, color2=224, itemType="HeadItem"), # Tinker Bell Green Adventure Bonnet with White Trim
                ShopItem(itemId=2533, price=15, goldPrice=6, color1=145, color2=145, itemType="Necklace"), # Tinker Bell Green Ruffle Neck Wrap
                ShopItem(itemId=80, price=40, goldPrice=16, color1=35, color2=35, itemType="Shirt"), # Celery Green Tink's Travel Top
                ShopItem(itemId=542, price=15, goldPrice=6, color1=86, color2=86, itemType="Belt"), # Nutmeg Brown Grass-braided Belt
                ShopItem(itemId=1082, price=40, goldPrice=16, color1=145, color2=1, itemType="Skirt"), # Tinker Bell Green Tink's Travel Skirt
                ShopItem(itemId=3562, price=25, goldPrice=10, color1=145, color2=145, itemType="Shoes"), # Tinker Bell Green Puffie Toe Boots

                ShopItem(itemId=85, price=40, goldPrice=16, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Fluffy Ruff Top
                ShopItem(itemId=1086, price=40, goldPrice=16, color1=174, color2=121, itemType="Skirt"), # Rosetta Red Bellflower Skirt
                ShopItem(itemId=3564, price=25, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red Slim Leaf Shoes

                ShopItem(itemId=84, price=40, goldPrice=16, color1=126, color2=269, itemType="Shirt"), # Raindrop Blue Waterfall Top
                ShopItem(itemId=1087, price=40, goldPrice=16, color1=126, color2=269, itemType="Skirt"), # Raindrop Blue Waterfall Wrap
                ShopItem(itemId=3537, price=25, goldPrice=10, color1=126, color2=269, itemType="Shoes"), # Raindrop Blue Iris Boots

                ShopItem(itemId=82, price=40, goldPrice=16, color1=84, color2=178, itemType="Shirt"), # Copper Brown Feather Fun Top
                ShopItem(itemId=543, price=15, goldPrice=6, color1=86, color2=86, itemType="Belt"), # Nutmeg Brown Fawn Adventure Belt
                ShopItem(itemId=1084, price=40, goldPrice=16, color1=84, color2=178, itemType="Skirt"), # Copper Brown Critter Comfort Skirt
                ShopItem(itemId=3514, price=25, goldPrice=10, color1=178, color2=178, itemType="Shoes"), # Fawn Orange Ivy Ankle Boots

                ShopItem(itemId=2042, price=25, goldPrice=10, color1=231, color2=226, itemType="HeadItem"), # Sunny Orange Athletic Headband
                ShopItem(itemId=83, price=40, goldPrice=16, color1=226, color2=231, itemType="Shirt"), # Goldenrod Yellow Light Bright Top
                ShopItem(itemId=1085, price=40, goldPrice=16, color1=226, color2=231, itemType="Skirt"), # Goldenrod Yellow Light Bright Skirt
                ShopItem(itemId=3511, price=25, goldPrice=10, color1=226, color2=231, itemType="Shoes"), # Goldenrod Yellow Sparkle Slippers

                ShopItem(itemId=1000009, price=40, goldPrice=16, color1=145, color2=224, itemType="Shirt"), # Tinker Bell Green Tink's Frosty Top
                ShopItem(itemId=1423, price=40, goldPrice=16, color1=145, color2=224, itemType="Skirt"), # Tinker Bell Green Tink's Frosty Skirt
                ShopItem(itemId=3798, price=25, goldPrice=10, color1=145, color2=224, itemType="Shoes"), # Tinker Bell Green Tink's Frosty Boots

                ShopItem(itemId=1000008, price=40, goldPrice=16, color1=149, color2=166, itemType="Shirt"), # Snowflake Blue Periwinkle's Frosty Top
                ShopItem(itemId=1422, price=40, goldPrice=16, color1=149, color2=166, itemType="Skirt"), # Snowflake Blue Periwinkle's Frosty Skirt
                ShopItem(itemId=3797, price=25, goldPrice=10, color1=149, color2=166, itemType="Shoes"), # Snowflake Blue Periwinkle's Frosty Flats

                ShopItem(itemId=2371, price=25, goldPrice=10, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Rosetta's Headwrap
                ShopItem(itemId=1000004, price=40, goldPrice=16, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Rosetta's Winter Top
                ShopItem(itemId=1658, price=15, goldPrice=6, color1=84, color2=166, itemType="WristItem"), # Copper Brown Cottonpuff Clutch
                ShopItem(itemId=1419, price=40, goldPrice=16, color1=224, color2=174, itemType="Skirt"), # Ivory White Rosetta's Winter Skirt
                ShopItem(itemId=3564, price=25, goldPrice=10, color1=174, color2=217, itemType="Shoes"), # Rosetta Red Slim Leaf Shoes with Gray Trim

                ShopItem(itemId=2372, price=25, goldPrice=10, color1=224, color2=224, itemType="HeadItem"), # Ivory White Sil's Winter Hat
                ShopItem(itemId=1000005, price=40, goldPrice=16, color1=126, color2=224, itemType="Shirt"), # Raindrop Blue Sil's Winter Top
                ShopItem(itemId=1420, price=40, goldPrice=16, color1=135, color2=126, itemType="Skirt"), # Boysenberry Purple Sil's Winter Skirt
                ShopItem(itemId=3564, price=25, goldPrice=10, color1=126, color2=135, itemType="Shoes"), # Raindrop Blue Slim Leaf Shoes with Boysenberry Purple Trim

                ShopItem(itemId=1000001, price=40, goldPrice=16, color1=238, color2=123, itemType="Shirt"), #  Zesty Orange Fawn's Winter Top
                ShopItem(itemId=1417, price=40, goldPrice=16, color1=79, color2=238, itemType="Skirt"), # Sienna Brown Fawn's Winter Skirt with Zesty Orange Trim
                ShopItem(itemId=3802, price=25, goldPrice=10, color1=238, color2=224, itemType="Shoes"), # Zesty Orange Fawn's Winter Boots

                ShopItem(itemId=2370, price=25, goldPrice=10, color1=84, color2=224, itemType="HeadItem"), # Copper Brown Iridessa's Earmuffs
                ShopItem(itemId=1000003, price=40, goldPrice=16, color1=84, color2=171, itemType="Shirt"), # Copper Brown Iridessa's Winter Top
                ShopItem(itemId=1418, price=40, goldPrice=16, color1=171, color2=84, itemType="Skirt"), # Sunrise Yellow Iridessa's Winter Skirt
                ShopItem(itemId=3795, price=25, goldPrice=10, color1=84, color2=224, itemType="Shoes"), # Copper Brown Iridessa's Winter Boots

                ShopItem(itemId=2373, price=25, goldPrice=10, color1=135, color2=5, itemType="HeadItem"), # Boysenberry Purple Vidia's Headwrap
                ShopItem(itemId=1000006, price=40, goldPrice=16, color1=5, color2=135, itemType="Shirt"), # Wysteria Purple Vidia's Winter Top
                ShopItem(itemId=1424, price=40, goldPrice=16, color1=5, color2=135, itemType="Skirt"), # Wysteria Purple Vidia's Winter Skirt
                ShopItem(itemId=3799, price=25, goldPrice=10, color1=135, color2=5, itemType="Shoes"), # Boysenberry Purple Vidia's Winter Boots

            ],
        ),
        ShopCollection(
            collectionId=79, # Floral Collections
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=2140, price=25, goldPrice=10, color1=10, color2=30, itemType="HeadItem"), # Cantaloupe Orange Citrus Barrette
                ShopItem(itemId=158, price=45, goldPrice=5, color1=10, color2=30, itemType="Shirt"), # Cantaloupe Orange Citrus Layer Top
                ShopItem(itemId=1144, price=45, goldPrice=5, color1=10, color2=30, itemType="Skirt"), # Cantaloupe Orange Citrus Peel Wrap
                ShopItem(itemId=3603, price=25, goldPrice=10, color1=30, color2=10, itemType="Shoes"), # Pumpkin Orange Citrus Peel Heels

                ShopItem(itemId=2139, price=25, goldPrice=10, color1=18, color2=27, itemType="HeadItem"), # Waterfall Blue Strawberry Barrette with Yellow Trim
                ShopItem(itemId=159, price=45, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Strawberry Top
                ShopItem(itemId=569, price=15, goldPrice=1, color1=139, color2=18, itemType="Belt"), # Seedling Green Strawberry Sash with Waterfall Blue Trim
                ShopItem(itemId=1142, price=45, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Strawberry Skirt
                ShopItem(itemId=3602, price=25, goldPrice=10, color1=139, color2=45, itemType="Shoes"), # Seedling Green Strawberry Low Heels with Strawberry Red Trim

                ShopItem(itemId=2058, price=25, goldPrice=10, color1=17, color2=0, itemType="HeadItem"), # Tendershoot Green Clover Headband
                ShopItem(itemId=59, price=45, goldPrice=5, color1=2, color2=17, itemType="Shirt"), # Clover Green Clover Top with Tendershoot Green Trim
                ShopItem(itemId=1064, price=45, goldPrice=5, color1=2, color2=17, itemType="Skirt"), # Clover Green Clover Skirt with Tendershoot Green Trim
                ShopItem(itemId=3546, price=25, goldPrice=10, color1=2, color2=17, itemType="Shoes"), # Clover Green Clover Slippers with Tendershoot Green Trim

                ShopItem(itemId=2067, price=25, goldPrice=10, color1=195, color2=209, itemType="HeadItem"), # Electric Blue Helenium Headband with Deep Sea Blue Trim
                ShopItem(itemId=68, price=45, goldPrice=5, color1=209, color2=195, itemType="Shirt"), # Deep Sea Blue Helenium Top
                ShopItem(itemId=1073, price=45, goldPrice=5, color1=209, color2=195, itemType="Skirt"), # Deep Sea Blue Helenium Skirt
                ShopItem(itemId=3555, price=25, goldPrice=10, color1=209, color2=195, itemType="Shoes"), # Deep Sea Blue Helenium Boots

                ShopItem(itemId=155, price=45, goldPrice=5, color1=152, color2=129, itemType="Shirt"), # Pale Purple Plumeria Top with Dark Purple Trim
                ShopItem(itemId=568, price=15, goldPrice=1, color1=69, color2=69, itemType="Belt"), # Powder Blue Plumeria Garland
                ShopItem(itemId=1140, price=45, goldPrice=5, color1=152, color2=129, itemType="Skirt"), # Pale Purple Plumeria Sarong with Dark Purple Trim
                ShopItem(itemId=3608, price=25, goldPrice=10, color1=69, color2=69, itemType="Shoes"), # Powder Blue Strappy Sandal

                ShopItem(itemId=2047, price=25, goldPrice=3, color1=265, color2=258, itemType="HeadItem"), # Bright Sky Blue Lantana Headband
                ShopItem(itemId=48, price=45, goldPrice=5, color1=265, color2=258, itemType="Shirt"), # Bright Sky Blue Lantana Top
                ShopItem(itemId=1053, price=45, goldPrice=5, color1=265, color2=258, itemType="Skirt"), # Bright Sky Blue Lantana Skirt
                ShopItem(itemId=3535, price=25, goldPrice=10, color1=258, color2=258, itemType="Shoes"), # Spearmint Green Lantana Slippers

                ShopItem(itemId=2057, price=25, goldPrice=10, color1=230, color2=121, itemType="HeadItem"), # Scarlet Red Ginkgo Headband
                ShopItem(itemId=58, price=45, goldPrice=5, color1=230, color2=121, itemType="Shirt"), # Scarlet Red Ginkgo Top
                ShopItem(itemId=1063, price=45, goldPrice=5, color1=230, color2=121, itemType="Skirt"), # Scarlet Red Ginkgo Skirt
                ShopItem(itemId=3545, price=25, goldPrice=10, color1=121, color2=121, itemType="Shoes"), # Daisy Pink Ginkgo Slippers 

                ShopItem(itemId=2060, price=25, goldPrice=10, color1=152, color2=73, itemType="HeadItem"), # Pale Purple Lemon Balm Headband with Grape Purple Trim
                ShopItem(itemId=61, price=45, goldPrice=5, color1=152, color2=73, itemType="Shirt"), # Pale Purple Lemon Balm Top with Grape Purple Trim
                ShopItem(itemId=1066, price=45, goldPrice=5, color1=73, color2=152, itemType="Skirt"), # Grape Purple Lemon Balm Skirt
                ShopItem(itemId=3548, price=25, goldPrice=10, color1=73, color2=152, itemType="Shoes"), # Grape Purple Lemon Balm Boots

                ShopItem(itemId=2052, price=25, goldPrice=10, color1=226, color2=208, itemType="HeadItem"), # Goldenrod Yellow Saffron Headband
                ShopItem(itemId=53, price=45, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Saffron Top
                ShopItem(itemId=1058, price=45, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Saffron Skirt
                ShopItem(itemId=3540, price=25, goldPrice=10, color1=226, color2=226, itemType="Shoes"), # Goldenrod Yellow Saffron Slippers

                ShopItem(itemId=2061, price=25, goldPrice=10, color1=45, color2=139, itemType="HeadItem"), # Strawberry Red Poinsettia Headband with Seedling Green Trim
                ShopItem(itemId=62, price=45, goldPrice=5, color1=139, color2=45, itemType="Shirt"), # Seedling Green Poinsettia Top
                ShopItem(itemId=1067, price=45, goldPrice=5, color1=139, color2=45, itemType="Skirt"), # Seedling Green Poinsettia Skirt
                ShopItem(itemId=3549, price=25, goldPrice=10, color1=139, color2=45, itemType="Shoes"), # Seedling Green Poinsettia Boots

                ShopItem(itemId=2051, price=25, goldPrice=10, color1=18, color2=18, itemType="HeadItem"), # Waterfall Blue White Rose Headband
                ShopItem(itemId=52, price=45, goldPrice=5, color1=166, color2=18, itemType="Shirt"), # Snow White White Rose Top
                ShopItem(itemId=1057, price=45, goldPrice=5, color1=166, color2=18, itemType="Skirt"), # Snow White White Rose Skirt
                ShopItem(itemId=3539, price=25, goldPrice=10, color1=18, color2=18, itemType="Shoes"), # Waterfall Blue White Rose Slippers

                ShopItem(itemId=2054, price=25, goldPrice=10, color1=287, color2=121, itemType="HeadItem"), # Dianthus Red Cosmos Headband
                ShopItem(itemId=55, price=45, goldPrice=5, color1=287, color2=121, itemType="Shirt"), # Dianthus Red Cosmos Top
                ShopItem(itemId=1060, price=45, goldPrice=5, color1=287, color2=287, itemType="Skirt"), # Dianthus Red Cosmos Skirt
                ShopItem(itemId=3542, price=25, goldPrice=10, color1=287, color2=121, itemType="Shoes"), # Dianthus Red Cosmos Boots

                ShopItem(itemId=2049, price=25, goldPrice=10, color1=136, color2=125, itemType="HeadItem"), # Peacock Blue Iris Headband
                ShopItem(itemId=50, price=45, goldPrice=5, color1=136, color2=136, itemType="Shirt"), # Peacock Blue Iris Top
                ShopItem(itemId=1055, price=45, goldPrice=5, color1=136, color2=136, itemType="Skirt"), # Peacock Blue Iris Skirt
                ShopItem(itemId=3537, price=25, goldPrice=10, color1=136, color2=136, itemType="Shoes"), # Peacock Blue Iris Boots

                ShopItem(itemId=2046, price=25, goldPrice=10, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Nerine Headband
                ShopItem(itemId=47, price=45, goldPrice=5, color1=277, color2=144, itemType="Shirt"), # Misty Purple Nerine Top
                ShopItem(itemId=1052, price=45, goldPrice=5, color1=277, color2=144, itemType="Skirt"), # Misty Purple Nerine Skirt
                ShopItem(itemId=3534, price=25, goldPrice=10, color1=277, color2=144, itemType="Shoes"), # Misty Purple Nerine Boots

                ShopItem(itemId=2065, price=25, goldPrice=10, color1=223, color2=223, itemType="HeadItem"), # Teal Blue Euphorbia Headband
                ShopItem(itemId=66, price=45, goldPrice=5, color1=68, color2=223, itemType="Shirt"), # Huckleberry Blue Euphorbia Top
                ShopItem(itemId=1071, price=45, goldPrice=5, color1=223, color2=68, itemType="Skirt"), # Teal Blue Euphorbia Skirt
                ShopItem(itemId=3553, price=25, goldPrice=10, color1=223, color2=68, itemType="Shoes"), # Teal Blue Euphorbia Boots

                ShopItem(itemId=2053, price=25, goldPrice=10, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Dahlia Headband
                ShopItem(itemId=54, price=45, goldPrice=5, color1=267, color2=166, itemType="Shirt"), # Celestial Blue Dahlia Top
                ShopItem(itemId=1059, price=45, goldPrice=5, color1=267, color2=166, itemType="Skirt"), # Celestial Blue Dahlia Skirt
                ShopItem(itemId=3541, price=25, goldPrice=10, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Dahlia Slippers

                ShopItem(itemId=2059, price=25, goldPrice=10, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Geranium Headband
                ShopItem(itemId=60, price=45, goldPrice=5, color1=44, color2=130, itemType="Shirt"), # Plumblossom Pink Geranium Top
                ShopItem(itemId=1065, price=45, goldPrice=5, color1=44, color2=130, itemType="Skirt"), # Plumblossom Pink Geranium Skirt
                ShopItem(itemId=3547, price=25, goldPrice=10, color1=44, color2=130, itemType="Shoes"), # Plumblossom Pink Geranium Slippers

                ShopItem(itemId=2048, price=25, goldPrice=10, color1=258, color2=264, itemType="HeadItem"), # Spearmint Green Bougainvillea Headband
                ShopItem(itemId=49, price=45, goldPrice=5, color1=264, color2=258, itemType="Shirt"), # Jungle Green Bougainvillea Top
                ShopItem(itemId=1054, price=45, goldPrice=5, color1=264, color2=258, itemType="Skirt"), # Jungle Green Bougainvillea Skirt
                ShopItem(itemId=3536, price=25, goldPrice=10, color1=264, color2=258, itemType="Shoes"), # Jungle Green Bougainvillea Slippers

                ShopItem(itemId=2056, price=25, goldPrice=10, color1=51, color2=55, itemType="HeadItem"), # Periwinkle Blue Aster Headband
                ShopItem(itemId=57, price=45, goldPrice=5, color1=51, color2=55, itemType="Shirt"), #  Periwinkle Blue Aster Top
                ShopItem(itemId=1062, price=45, goldPrice=5, color1=51, color2=55, itemType="Skirt"), # Periwinkle Blue Aster Skirt
                ShopItem(itemId=3544, price=25, goldPrice=10, color1=51, color2=55, itemType="Shoes"), # Periwinkle Blue Aster Boots

                ShopItem(itemId=2121, price=25, goldPrice=10, color1=27, color2=26, itemType="HeadItem"), # Corn Cob Yellow Commelina Band
                ShopItem(itemId=110, price=45, goldPrice=5, color1=27, color2=26, itemType="Shirt"), # Corn Cob Yellow Commelina Top
                ShopItem(itemId=1122, price=45, goldPrice=5, color1=27, color2=26, itemType="Skirt"), #  Corn Cob Yellow Commelina Skirt
                ShopItem(itemId=3580, price=25, goldPrice=10, color1=27, color2=27, itemType="Shoes"), #  Corn Cob Yellow Commelina Shoes
            ],    
        ),
        ShopCollection(
            collectionId=28, # Animal-Inspired Fashions
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=2073, price=25, goldPrice=10, color1=206, color2=142, itemType="HeadItem"), # Raven Black Buzzy Bee Mask
                ShopItem(itemId=76, price=45, goldPrice=16, color1=206, color2=142, itemType="Shirt"), # Raven Black Buzzy Bee Striped Wrap
                ShopItem(itemId=1003, price=45, goldPrice=16, color1=142, color2=142, itemType="Skirt"), # Bumble Bee Yellow Leafy Bubble Skirt
                ShopItem(itemId=3501, price=25, goldPrice=10, color1=142, color2=142, itemType="Shoes"), # Bumble Bee Yellow Petal Slippers

                ShopItem(itemId=2071, price=25, goldPrice=10, color1=44, color2=257, itemType="HeadItem"), # Plumblossom Pink Little Light Antennae
                ShopItem(itemId=91, price=45, goldPrice=16, color1=44, color2=44, itemType="Shirt"), # Plumblossom Pink Little Light Top
                ShopItem(itemId=1091, price=45, goldPrice=16, color1=44, color2=257, itemType="Skirt"), #  Plumblossom Pink Little Light Mini
                ShopItem(itemId=3501, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), #  Plumblossom Pink Petal Slippers

                ShopItem(itemId=2071, price=25, goldPrice=10, color1=206, color2=189, itemType="HeadItem"), # Raven Black Little Light Antennae
                ShopItem(itemId=172, price=45, goldPrice=16, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tank
                ShopItem(itemId=1156, price=45, goldPrice=16, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Skirt
                ShopItem(itemId=3501, price=25, goldPrice=10, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Petal Slippers

                ShopItem(itemId=2151, price=25, goldPrice=10, color1=1, color2=1, itemType="HeadItem"), # Mint Green Dragonfly Mask
                ShopItem(itemId=186, price=45, goldPrice=16, color1=1, color2=1, itemType="Shirt"), # Mint Green Dragonfly Top
                ShopItem(itemId=1168, price=45, goldPrice=16, color1=1, color2=1, itemType="Skirt"), # Mint Green Dragonfly Skirt
                ShopItem(itemId=3501, price=25, goldPrice=10, color1=1, color2=1, itemType="Shoes"), # Mint Green Petal Slippers

                ShopItem(itemId=2150, price=25, goldPrice=10, color1=267, color2=186, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
                ShopItem(itemId=187, price=45, goldPrice=16, color1=267, color2=186, itemType="Shirt"), # Celestial Blue Hummingbird Top
                ShopItem(itemId=1169, price=45, goldPrice=16, color1=267, color2=186, itemType="Skirt"), # Celestial Blue Hummingbird Skirt
                ShopItem(itemId=3501, price=25, goldPrice=10, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Petal Slippers

                ShopItem(itemId=2033, price=25, goldPrice=10, color1=175, color2=159, itemType="HeadItem"), # Creek Green Firefly Spotlight Barrette
                ShopItem(itemId=2524, price=15, goldPrice=6, color1=175, color2=159, itemType="Necklace"), # Creek Green Firefly Glow Choker
                ShopItem(itemId=29, price=45, goldPrice=16, color1=175, color2=159, itemType="Shirt"), # Creek Green Orchid Firefly Wrap
                ShopItem(itemId=1032, price=45, goldPrice=16, color1=175, color2=159, itemType="Skirt"), # Creek Green Slit Satin Firefly Skirt
                ShopItem(itemId=3519, price=25, goldPrice=10, color1=175, color2=159, itemType="Shoes"), # Creek Green Firefly Glow Toes Slippers

                ShopItem(itemId=90, price=45, goldPrice=16, color1=63, color2=166, itemType="Shirt"), # Butterfly Blue Fanciful Flutter Top with White Trim
                ShopItem(itemId=548, price=15, goldPrice=1, color1=63, color2=166, itemType="Belt"), # Butterfly Blue Fanciful Flutter Sash with White Trim
                ShopItem(itemId=1090, price=45, goldPrice=16, color1=63, color2=166, itemType="Skirt"), # Butterfly Blue Fanciful Flutter Gown with White Trim
                ShopItem(itemId=3559, price=25, goldPrice=10, color1=63, color2=166, itemType="Shoes"), # Butterfly Blue Fanciful Flutter Flats with White Trim

                ShopItem(itemId=376, price=45, goldPrice=16, color1=189, color2=206, itemType="Shirt"), # Ladybug Red Morpho Butterfly Top with Raven Black Trim
                ShopItem(itemId=635, price=15, goldPrice=1, color1=189, color2=189, itemType="Belt"), # Ladybug Red Morpho Butterfly Sash
                ShopItem(itemId=1294, price=45, goldPrice=16, color1=30, color2=206, itemType="Skirt"), # Pumpkin Orange Morpho Butterfly Skirt with Raven Black Trim
                ShopItem(itemId=3716, price=25, goldPrice=10, color1=206, color2=189, itemType="Shoes"), # Raven Black Morpho Butterfly Shoes

                ShopItem(itemId=2367, price=25, goldPrice=10, color1=216, color2=216, itemType="HeadItem"), # Slate Gray Raven Mask
                ShopItem(itemId=499, price=45, goldPrice=16, color1=206, color2=216, itemType="Shirt"), # Raven Black Raven Costume Top with Slate Gray Trim
                ShopItem(itemId=1415, price=45, goldPrice=16, color1=206, color2=216, itemType="Skirt"), # Raven Black Raven Skirt with Slate Gray Trim
                ShopItem(itemId=3794, price=25, goldPrice=10, color1=206, color2=216, itemType="Shoes"), # Raven Black Raven Heels with Slate Gray Trim

                ShopItem(itemId=2347, price=25, goldPrice=10, color1=224, color2=224, itemType="HeadItem"), # Ivory White Fox Mask
                ShopItem(itemId=1000011, price=45, goldPrice=16, color1=224, color2=224, itemType="Shirt"), # Ivory White Fox Top
                ShopItem(itemId=1395, price=45, goldPrice=16, color1=224, color2=224, itemType="Skirt"), # Ivory White Fox Skirt
                ShopItem(itemId=3801, price=25, goldPrice=10, color1=224, color2=224, itemType="Shoes"), # Ivory White Furry Critter Boots

                ShopItem(itemId=2360, price=25, goldPrice=10, color1=206, color2=169, itemType="HeadItem"), # Raven Black Raccoon Mask
                ShopItem(itemId=481, price=45, goldPrice=16, color1=169, color2=206, itemType="Shirt"), # Squirrel Gray Raccoon Top
                ShopItem(itemId=1398, price=45, goldPrice=16, color1=169, color2=206, itemType="Skirt"), # Squirrel Gray Raccoon Skirt
                ShopItem(itemId=3801, price=25, goldPrice=10, color1=206, color2=169, itemType="Shoes"), # Raven Black Furry Critter Boots

                ShopItem(itemId=2440, price=25, goldPrice=10, color1=212, color2=194, itemType="HeadItem"), # Indigo Purple Songbird Headband
                ShopItem(itemId=1000078, price=45, goldPrice=16, color1=194, color2=212, itemType="Shirt"), # Electric Pink Songbird Top
                ShopItem(itemId=1484, price=45, goldPrice=16, color1=212, color2=194, itemType="Skirt"), # Indigo Purple Songbird Skirt
                ShopItem(itemId=3869, price=25, goldPrice=10, color1=212, color2=194, itemType="Shoes"), # Indigo Purple Songbird Heels
            ],
        ),   
        ShopCollection(
            collectionId=40, # Casual and Sporty Wear
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=303, price=45, goldPrice=16, color1=166, color2=286, itemType="Shirt"), # Snow White Snowbound Ski Jacket with Cherry Pink Trim
                ShopItem(itemId=1253, price=45, goldPrice=16, color1=166, color2=286, itemType="Skirt"), # Snow White Warm Ski Pants with Cherry Pink Trim
                ShopItem(itemId=3682, price=25, goldPrice=10, color1=105, color2=286, itemType="Shoes"), # Siltstone Tan Swift Skis with Cherry Pink Trim

                ShopItem(itemId=197, price=45, goldPrice=16, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Rainbow Tee
                ShopItem(itemId=588, price=15, goldPrice=6, color1=141, color2=141, itemType="Belt"), # Thundercloud Gray Studded Belt
                ShopItem(itemId=1143, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Denim Flyers
                ShopItem(itemId=3849, price=25, goldPrice=10, color1=224, color2=224, itemType="Shoes"), # Ivory White Rainbow Sneakers

                ShopItem(itemId=145, price=45, goldPrice=16, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Sporty Top
                ShopItem(itemId=1048, price=45, goldPrice=16, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sports Shorts
                ShopItem(itemId=3504, price=25, goldPrice=10, color1=162, color2=162, itemType="Shoes"), # Sunglow Yellow Striders

                ShopItem(itemId=214, price=45, goldPrice=16, color1=121, color2=282, itemType="Shirt"), # Daisy Pink Pretty Plaid Top
                ShopItem(itemId=1187, price=45, goldPrice=16, color1=121, color2=121, itemType="Skirt"), # Daisy Pink Stitched Leaf Skirt
                ShopItem(itemId=3620, price=25, goldPrice=10, color1=121, color2=121, itemType="Shoes"), # Daisy Pink Pretty Plaid Flats

                ShopItem(itemId=283, price=45, goldPrice=16, color1=211, color2=5, itemType="Shirt"), # Gentian Purple Sporty Tankini
                ShopItem(itemId=1233, price=45, goldPrice=16, color1=211, color2=5, itemType="Skirt"), # Gentian Purple Sporty Swim Skirt
                ShopItem(itemId=3757, price=25, goldPrice=10, color1=211, color2=5, itemType="Shoes"), # Gentian Purple Summer Splash Shoes with Wysteria Purple Trim

                ShopItem(itemId=2335, price=25, goldPrice=10, color1=267, color2=166, itemType="HeadItem"), # Celestial Blue Summer Splash Hat
                ShopItem(itemId=415, price=45, goldPrice=16, color1=267, color2=166, itemType="Shirt"), # Celestial Blue Summer Splash Top
                ShopItem(itemId=1334, price=45, goldPrice=16, color1=267, color2=166, itemType="Skirt"), # Celestial Blue Summer Splash Skirt
                ShopItem(itemId=3757, price=25, goldPrice=10, color1=166, color2=267, itemType="Shoes"), # Snow White Summer Splash Shoes

                ShopItem(itemId=2043, price=25, goldPrice=10, color1=175, color2=175, itemType="HeadItem"), # Creek Green Sunny Days Hat
                ShopItem(itemId=45, price=45, goldPrice=16, color1=17, color2=175, itemType="Shirt"), # Tendershoot Green Sunshine Top
                ShopItem(itemId=1050, price=45, goldPrice=16, color1=35, color2=175, itemType="Skirt"), # Celery Green Sunshine Skirt
                ShopItem(itemId=3610, price=25, goldPrice=10, color1=17, color2=175, itemType="Shoes"), # Tendershoot Green Fresh Petal Pumps

                ShopItem(itemId=46, price=45, goldPrice=16, color1=278, color2=135, itemType="Shirt"), # Aster Purple Tropical Top
                ShopItem(itemId=539, price=15, goldPrice=6, color1=135, color2=135, itemType="Belt"), # Boysenberry Purple Tropical Belt
                ShopItem(itemId=1051, price=45, goldPrice=16, color1=278, color2=135, itemType="Skirt"), # Aster Purple Tropical Sarong
                ShopItem(itemId=3568, price=25, goldPrice=10, color1=135, color2=278, itemType="Shoes"), # Boysenberry Purple Tie Dye Sandals

                ShopItem(itemId=28, price=45, goldPrice=16, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Bubble Button Top
                ShopItem(itemId=532, price=15, goldPrice=6, color1=69, color2=208, itemType="Belt"), # Powder Blue Triple Bubble Belt
                ShopItem(itemId=1010, price=45, goldPrice=16, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Lily Pad Bubble Skirt
                ShopItem(itemId=3520, price=25, goldPrice=10, color1=208, color2=208, itemType="Shoes"), # Cerulean Blue Bubble Top Slippers
            ],    
        ),    
        ShopCollection(
            collectionId=9, # Berry
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=2005, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=2009, price=20, goldPrice=8, color1=42, color2=51, itemType="HeadItem"), 
                        OutfitItem(itemId=480, price=35, goldPrice=13, color1=42, color2=51, itemType="Shirt"),
                        OutfitItem(itemId=653, price=10, goldPrice=5, color1=42, color2=42, itemType="Belt"),
                        OutfitItem(itemId=1377, price=35, goldPrice=13, color1=42, color2=51, itemType="Skirt"),
                        OutfitItem(itemId=3778, price=20, goldPrice=8, color1=42, color2=51, itemType="Shoes"),
                ],
            ),
                ShopOutfit(
                    outfitId=2006, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=1000073, price=35, goldPrice=13, color1=199, color2=26, itemType="Shirt"),
                        OutfitItem(itemId=653, price=10, goldPrice=5, color1=26, color2=26, itemType="Belt"),
                        OutfitItem(itemId=1077, price=35, goldPrice=13, color1=130, color2=26, itemType="Skirt"),
                        OutfitItem(itemId=3845, price=15, goldPrice=8, color1=199, color2=26, itemType="Shoes"),
                    ],
                ),
            ],
        ),
    ]
)