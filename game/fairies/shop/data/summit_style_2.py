from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

# Summit Style - OutfitId 2000 - 2999

SHOP = NPCShop(
    zone=ZoneConstants.SUMMIT_STYLE,
    shopId=2,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.DIVA_WINGS,
        position=(410, 450),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_DIVA_WINGS
    ),
    collections=[
        ShopCollection(
            collectionId=82, # Floral Collections
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=2001,
                    items = [
                        OutfitItem(itemId=2427, price=25, goldPrice=10, color1=201, color2=121, itemType="HeadItem"), # Velvet Red Hydrangea Barrette
                        OutfitItem(itemId=1000058, price=45, goldPrice=16, color1=201, color2=121, itemType="Shirt"), # Velvet Red Hydrangea Top
                        OutfitItem(itemId=1465, price=45, goldPrice=16, color1=201, color2=121, itemType="Skirt"), # Velvet Red Hydrangea Skirt
                        OutfitItem(itemId=3846, price=25, goldPrice=10, color1=201, color2=121, itemType="Shoes"), # Velvet Red Hydrangea Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2002,
                    items = [
                        OutfitItem(itemId=2284, price=25, goldPrice=10, color1=166, color2=1, itemType="HeadItem"), # Snow White Snowdrop Headband
                        OutfitItem(itemId=343, price=45, goldPrice=16, color1=166, color2=1, itemType="Shirt"), # Snow White Snowdrop Top
                        OutfitItem(itemId=629, price=15, goldPrice=6, color1=166, color2=1, itemType="Belt"), # Snow White Snowdrop Sash
                        OutfitItem(itemId=1280, price=45, goldPrice=16, color1=166, color2=1, itemType="Skirt"), # Snow White Snowdrop Skirt
                        OutfitItem(itemId=3704, price=25, goldPrice=10, color1=166, color2=1, itemType="Shoes"), # Snow White Snowdrop Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2003,
                    items = [
                        OutfitItem(itemId=2292, price=25, goldPrice=10, color1=208, color2=267, itemType="HeadItem"), # Cerulean Blue Hanami Headpiece
                        OutfitItem(itemId=377, price=45, goldPrice=16, color1=208, color2=267, itemType="Shirt"), # Cerulean Blue Hanami Top
                        OutfitItem(itemId=636, price=15, goldPrice=6, color1=209, color2=267, itemType="Belt"), # Deep Sea Blue Hanami Sash
                        OutfitItem(itemId=1300, price=45, goldPrice=16, color1=208, color2=267, itemType="Skirt"), # Cerulean Blue Hanami Long Skirt
                        OutfitItem(itemId=3717, price=25, goldPrice=16, color1=267, color2=98, itemType="Shoes"), # Celestial Blue Hanami Geta Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2004,
                    items = [
                        OutfitItem(itemId=2292, price=25, goldPrice=10, color1=81, color2=26, itemType="HeadItem"), # Crimson Red Hanami Headpiece
                        OutfitItem(itemId=377, price=45, goldPrice=16, color1=199, color2=26, itemType="Shirt"), # Cherryblossom Pink Hanami Top
                        OutfitItem(itemId=636, price=15, goldPrice=6, color1=81, color2=26, itemType="Belt"), # Crimson Red Hanami Sash
                        OutfitItem(itemId=1295, price=45, goldPrice=16, color1=199, color2=26, itemType="Skirt"), # Cherryblossom Pink Hanami Short Skirt
                        OutfitItem(itemId=3717, price=25, goldPrice=10, color1=81, color2=98, itemType="Shoes"), # Crimson Red Hanami Geta Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2005,
                    items = [
                        OutfitItem(itemId=2449, price=25, goldPrice=10, color1=267, color2=10, itemType="HeadItem"), # Celestial Blue Azalea Barrette
                        OutfitItem(itemId=1000074, price=45, goldPrice=16, color1=10, color2=267, itemType="Shirt"), # Cantaloupe Orange Azalea Top
                        OutfitItem(itemId=1481, price=45, goldPrice=16, color1=10, color2=267, itemType="Skirt"), # Cantaloupe Orange Azalea Skirt
                        OutfitItem(itemId=3866, price=25, goldPrice=10, color1=10, color2=267, itemType="Shoes"), # Cantaloupe Orange Azalea Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2006,
                    items = [
                        OutfitItem(itemId=385, price=45, goldPrice=16, color1=287, color2=166, itemType="Shirt"), # Dianthus Red Dianthus Blouse
                        OutfitItem(itemId=1305, price=45, goldPrice=16, color1=287, color2=166, itemType="Skirt"), # Dianthus Red Dianthus Skirt
                        OutfitItem(itemId=3722, price=25, goldPrice=10, color1=287, color2=166, itemType="Shoes"), # Dianthus Red Dianthus Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2007,
                    items = [
                        OutfitItem(itemId=2336, price=25, goldPrice=10, color1=186, color2=230, itemType="HeadItem"), # Honeycomb Yellow Flame Lily Barrette
                        OutfitItem(itemId=417, price=45, goldPrice=16, color1=186, color2=230, itemType="Shirt"), # Honeycomb Yellow Flame Lily Top
                        OutfitItem(itemId=1335, price=45, goldPrice=16, color1=186, color2=230, itemType="Skirt"), # Honeycomb Yellow Flame Lily Skirt
                        OutfitItem(itemId=3758, price=25, goldPrice=10, color1=186, color2=230, itemType="Shoes"), # Honeycomb Yellow Flame Lily Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2008,
                    items = [
                        OutfitItem(itemId=2348, price=25, goldPrice=10, color1=130, color2=81, itemType="HeadItem"), # Orchid Pink Chrysanthemum Beret
                        OutfitItem(itemId=477, price=45, goldPrice=16, color1=224, color2=81, itemType="Shirt"), # Ivory White Chrysanthemum Top
                        OutfitItem(itemId=640, price=15, goldPrice=6, color1=81, color2=130, itemType="Belt"), # Crimson Red Chrysanthemum Belt
                        OutfitItem(itemId=1396, price=45, goldPrice=16, color1=206, color2=81, itemType="Skirt"), # Raven Black Chrysanthemum Skirt
                        OutfitItem(itemId=3779, price=25, goldPrice=10, color1=81, color2=130, itemType="Shoes"), # Crimson Red Chrysanthemum Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2009,
                    items = [
                        OutfitItem(itemId=2356, price=25, goldPrice=10, color1=153, color2=162, itemType="HeadItem"), # Frostbunny Blue Bead Cascade Earrings
                        OutfitItem(itemId=483, price=45, goldPrice=16, color1=118, color2=153, itemType="Shirt"), # Sapphire Blue Camellia Top
                        OutfitItem(itemId=1400, price=45, goldPrice=16, color1=206, color2=118, itemType="Skirt"), # Raven Black Camellia Skirt
                        OutfitItem(itemId=3782, price=25, goldPrice=10, color1=74, color2=74, itemType="Shoes"), # Papyrus Tan Camellia Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2010,
                    items = [
                        OutfitItem(itemId=2386, price=25, goldPrice=10, color1=224, color2=153, itemType="HeadItem"), # Ivory White Snow Rose Barrettes with Frostbunny Blue Trim
                        OutfitItem(itemId=1000024, price=45, goldPrice=16, color1=224, color2=153, itemType="Shirt"), # Ivory White Snow Rose Top with Frostbunny Blue Trim
                        OutfitItem(itemId=1435, price=45, goldPrice=16, color1=153, color2=153, itemType="Skirt"), # Frostbunny Blue Snow Rose Skirt
                        OutfitItem(itemId=3815, price=25, goldPrice=10, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Snow Rose Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2011,
                    items = [
                        OutfitItem(itemId=2171, price=25, goldPrice=10, color1=211, color2=211, itemType="HeadItem"), # Gentian Purple Moth Orchid Headband
                        OutfitItem(itemId=216, price=45, goldPrice=16, color1=51, color2=15, itemType="Shirt"), # Periwinkle Blue Moth Orchid Top
                        OutfitItem(itemId=594, price=15, goldPrice=6, color1=211, color2=211, itemType="Belt"), # Gentian Purple Moth Orchid Leaf Sash
                        OutfitItem(itemId=1183, price=45, goldPrice=16, color1=51, color2=211, itemType="Skirt"), # Periwinkle Blue Moth Orchid Bottom
                        OutfitItem(itemId=3629, price=25, goldPrice=10, color1=51, color2=15, itemType="Shoes"), # Periwinkle Blue Moth Orchid Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2012,
                    items = [
                        OutfitItem(itemId=2172, price=25, goldPrice=10, color1=258, color2=125, itemType="HeadItem"), # Spearmint Green Dragon Arum Crown
                        OutfitItem(itemId=217, price=45, goldPrice=16, color1=166, color2=18, itemType="Shirt"), # Snow White Dragon Arum Top
                        OutfitItem(itemId=593, price=15, goldPrice=6, color1=258, color2=258, itemType="Belt"), # Spearmint Green Dragon Arum Sash
                        OutfitItem(itemId=1185, price=45, goldPrice=16, color1=166, color2=18, itemType="Skirt"), # Snow White Dragon Arum Skirt
                        OutfitItem(itemId=3630, price=25, goldPrice=10, color1=258, color2=125, itemType="Shoes"), # Spearmint Green Dragon Arum Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2013,
                    items = [
                        OutfitItem(itemId=2100, price=25, goldPrice=10, color1=153, color2=166, itemType="HeadItem"), # Frostbunny Blue Campanula Barrette
                        OutfitItem(itemId=108, price=45, goldPrice=16, color1=153, color2=166, itemType="Shirt"), # Frostbunny Blue Campanula Top
                        OutfitItem(itemId=1111, price=45, goldPrice=16, color1=153, color2=166, itemType="Skirt"), # Frostbunny Blue Campanula Skirt
                        OutfitItem(itemId=3578, price=25, goldPrice=10, color1=153, color2=166, itemType="Shoes"), # Frostbunny Blue Campanula Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2014,
                    items = [
                        OutfitItem(itemId=2120, price=25, goldPrice=10, color1=199, color2=121, itemType="HeadItem"), # Cherryblossom Pink Campis Barrette
                        OutfitItem(itemId=109, price=45, goldPrice=16, color1=199, color2=121, itemType="Shirt"), # Cherryblossom Pink Campis Top
                        OutfitItem(itemId=1121, price=45, goldPrice=16, color1=199, color2=121, itemType="Skirt"), # Cherryblossom Pink Campis Skirt
                        OutfitItem(itemId=3579, price=25, goldPrice=10, color1=199, color2=121, itemType="Shoes"), # Cherryblossom Pink Campis Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2015,
                    items = [
                        OutfitItem(itemId=2123, price=25, goldPrice=10, color1=152, color2=183, itemType="HeadItem"), # Pale Purple Lagerstroemia Hat
                        OutfitItem(itemId=112, price=45, goldPrice=16, color1=152, color2=183, itemType="Shirt"), # Pale Purple Lagerstroemia Top
                        OutfitItem(itemId=1124, price=45, goldPrice=16, color1=152, color2=183, itemType="Skirt"), # Pale Purple Lagerstroemia Skirt
                        OutfitItem(itemId=3582, price=25, goldPrice=10, color1=152, color2=183, itemType="Shoes"), # Pale Purple Lagerstroemia Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2016,
                    items = [
                        OutfitItem(itemId=2586, price=15, goldPrice=6, color1=138, color2=138, itemType="Necklace"), # Persimmon Orange Marigold Necklace
                        OutfitItem(itemId=333, price=45, goldPrice=16, color1=30, color2=10, itemType="Shirt"), # Pumpkin Orange Marigold Top
                        OutfitItem(itemId=1270, price=45, goldPrice=16, color1=30, color2=10, itemType="Skirt"), # Pumpkin Orange Marigold Skirt
                        OutfitItem(itemId=3695, price=25, goldPrice=10, color1=138, color2=138, itemType="Shoes"), # Persimmon Orange Marigold Shoes
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=46, # Mainland Styles
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=2017,
                    items = [
                        OutfitItem(itemId=1000031, price=45, goldPrice=16, color1=180, color2=195, itemType="Shirt"), # Seashell Blue Chic Tie-Dye Top
                        OutfitItem(itemId=1442, price=45, goldPrice=16, color1=180, color2=195, itemType="Skirt"), # Seashell Blue Chic Tie-Dye Skirt
                        OutfitItem(itemId=3822, price=25, goldPrice=10, color1=180, color2=195, itemType="Shoes"), # Seashell Blue Super Chic Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2018,
                    items = [
                        OutfitItem(itemId=1000037, price=45, goldPrice=16, color1=278, color2=110, itemType="Shirt"), # Aster Purple Fluttery Tie-Dye Top
                        OutfitItem(itemId=1445, price=45, goldPrice=16, color1=278, color2=110, itemType="Skirt"), # Aster Purple Fluttery Tie-Dye Skirt
                        OutfitItem(itemId=3822, price=25, goldPrice=10, color1=278, color2=110, itemType="Shoes"), # Aster Purple Super Chic Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2019,
                    items = [
                        OutfitItem(itemId=2423, price=25, goldPrice=10, color1=217, color2=267, itemType="HeadItem"), # Soft Gray Cute Cap
                        OutfitItem(itemId=1000057, price=45, goldPrice=16, color1=217, color2=267, itemType="Shirt"), # Soft Gray Cardie Combo Top
                        OutfitItem(itemId=1464, price=45, goldPrice=16, color1=217, color2=267, itemType="Skirt"), # Soft Gray Delightful Denim Skirt
                        OutfitItem(itemId=3844, price=25, goldPrice=10, color1=217, color2=267, itemType="Shoes"), # Soft Gray Lovely Laceups
                    ],
                ),
                ShopOutfit(
                    outfitId=2020,
                    items = [
                        OutfitItem(itemId=2634, price=15, goldPrice=6, color1=224, color2=267, itemType="Necklace"), # Ivory White Sweetheart Purse
                        OutfitItem(itemId=1000055, price=45, goldPrice=16, color1=162, color2=224, itemType="Shirt"), # Sunglow Yellow Sweetheart Top
                        OutfitItem(itemId=650, price=15, goldPrice=6, color1=267, color2=224, itemType="Belt"), # Celestial Blue Sweetheart Sash
                        OutfitItem(itemId=1463, price=45, goldPrice=16, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sweetheart Skirt
                        OutfitItem(itemId=3845, price=25, goldPrice=16, color1=162, color2=267, itemType="Shoes"), # Sunglow Yellow Sweetheart Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2021,
                    items = [
                        OutfitItem(itemId=2428, price=25, goldPrice=10, color1=135, color2=282, itemType="HeadItem"), # Boysenberry Purple Cute Cloud Earrings
                        OutfitItem(itemId=1000061, price=45, goldPrice=16, color1=5, color2=152, itemType="Shirt"), # Wysteria Purple Rainy Day Top
                        OutfitItem(itemId=1673, price=15, goldPrice=6, color1=135, color2=135, itemType="WristItem"), # Boysenberry Purple Rainbow Umbrella
                        OutfitItem(itemId=1468, price=45, goldPrice=16, color1=5, color2=152, itemType="Skirt"), # Wysteria Purple Rainy Day Skirt
                        OutfitItem(itemId=3850, price=25, goldPrice=10, color1=135, color2=282, itemType="Shoes"), # Boysenberry Purple Cozy Rain Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2022,
                    items = [
                        OutfitItem(itemId=1000052, price=45, goldPrice=16, color1=81, color2=224, itemType="Shirt"), # Crimson Red Soft Knit Sweater
                        OutfitItem(itemId=1459, price=45, goldPrice=16, color1=141, color2=81, itemType="Skirt"), # Thundercloud Gray Pleasing Pleats Skirt
                        OutfitItem(itemId=3840, price=25, goldPrice=10, color1=141, color2=224, itemType="Shoes"), # Thundercloud Gray Sweet Spring Laceups
                    ],
                ),
                ShopOutfit(
                    outfitId=2023,
                    items = [
                        OutfitItem(itemId=2636, price=15, goldPrice=6, color1=105, color2=105, itemType="Necklace"), #  Siltstone Tan Sweet Beaded Necklace
                        OutfitItem(itemId=1000063, price=45, goldPrice=16, color1=44, color2=123, itemType="Shirt"), # Plumblossom Pink Sweet Spring Hoodie
                        OutfitItem(itemId=1470, price=45, goldPrice=16, color1=126, color2=123, itemType="Skirt"), # Raindrop Blue Layered Look Skirt
                        OutfitItem(itemId=3855, price=25, goldPrice=10, color1=55, color2=224, itemType="Shoes"), # Pepper Black Cat Flats
                    ],
                ),
                ShopOutfit(
                    outfitId=2024,
                    items = [
                        OutfitItem(itemId=1000080, price=45, goldPrice=16, color1=44, color2=134, itemType="Shirt"), #  Plumblossom Pink Stylish Hoodie
                        OutfitItem(itemId=1487, price=45, goldPrice=16, color1=44, color2=134, itemType="Skirt"), # Plumblossom Pink Springy Skirt
                        OutfitItem(itemId=3871, price=25, goldPrice=10, color1=44, color2=134, itemType="Shoes"), # Plumblossom Pink Perfect Plaid Loafers
                    ],
                ),
                ShopOutfit(
                    outfitId=2025,
                    items = [
                        OutfitItem(itemId=2301, price=25, goldPrice=10, color1=11, color2=115, itemType="HeadItem"), # Marigold Yellow Folklorico Headband
                        OutfitItem(itemId=386, price=45, goldPrice=16, color1=274, color2=149, itemType="Shirt"), # Bellflower Purple Folklorico Blouse
                        OutfitItem(itemId=1306, price=45, goldPrice=16, color1=274, color2=149, itemType="Skirt"), # Bellflower Purple Folklorico Skirt
                        OutfitItem(itemId=3726, price=25, goldPrice=10, color1=11, color2=149, itemType="Shoes"), # Marigold Yellow Folklorico Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2026,
                    items = [
                        OutfitItem(itemId=1000114, price=45, goldPrice=16, color1=265, color2=17, itemType="Shirt"), # Bright Sky Blue Festive Floral Top
                        OutfitItem(itemId=1001020, price=45, goldPrice=16, color1=265, color2=17, itemType="Skirt"), # Bright Sky Blue Festive Floral Skirt
                        OutfitItem(itemId=3896, price=25, goldPrice=10, color1=17, color2=265, itemType="Shoes"), #  Tendershoot Green Pearl-Studded Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2027,
                    items = [
                        OutfitItem(itemId=1000122, price=45, goldPrice=16, color1=150, color2=18, itemType="Shirt"), # Dry Moss Green Summer Stripes Top
                        OutfitItem(itemId=1001029, price=45, goldPrice=16, color1=150, color2=18, itemType="Skirt"), #  Dry Moss Green Summer Stripes Skirt
                        OutfitItem(itemId=3904, price=25, goldPrice=10, color1=150, color2=18, itemType="Shoes"), # Dry Moss Green Summer Stripes Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2028,
                    items = [
                        OutfitItem(itemId=379, price=45, goldPrice=16, color1=189, color2=121, itemType="Shirt"), # Ladybug Red Breezy Ruffled Top
                        OutfitItem(itemId=1299, price=45, goldPrice=16, color1=121, color2=189, itemType="Skirt"), # Daisy Pink Breezy Ruffled Skirt
                        OutfitItem(itemId=3718, price=25, goldPrice=10, color1=206, color2=121, itemType="Shoes"), # Raven Black Ruffle Detail Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2029,
                    items = [
                        OutfitItem(itemId=2474, price=25, goldPrice=10, color1=84, color2=77, itemType="HeadItem"), # Copper Brown Hiking Hat
                        OutfitItem(itemId=1000108, price=45, goldPrice=16, color1=224, color2=70, itemType="Shirt"), # Ivory White Hiking Gear
                        OutfitItem(itemId=1001015, price=45, goldPrice=16, color1=209, color2=70, itemType="Skirt"), # Deep Sea Blue Hiking Shorts
                        OutfitItem(itemId=3618, price=25, goldPrice=10, color1=78, color2=84, itemType="Shoes"), # Fawn Brown Woodchucks
                    ],
                ),
                ShopOutfit(
                    outfitId=2030,
                    items = [
                        OutfitItem(itemId=145, price=45, goldPrice=16, color1=159, color2=170, itemType="Shirt"), # Tea Green Sporty Top
                        OutfitItem(itemId=1048, price=45, goldPrice=16, color1=159, color2=170, itemType="Skirt"), # Tea Green Sports Shorts
                        OutfitItem(itemId=3504, price=25, goldPrice=10, color1=170, color2=170, itemType="Shoes"), # Olive Green Striders
                    ],
                ),
                ShopOutfit(
                    outfitId=2031,
                    items = [
                        OutfitItem(itemId=2466, price=25, goldPrice=10, color1=81, color2=224, itemType="HeadItem"), # Crimson Red Adventurer's Hat
                        OutfitItem(itemId=1000112, price=45, goldPrice=16, color1=81, color2=224, itemType="Shirt"), # Crimson Red Adventurer Jacket
                        OutfitItem(itemId=1001018, price=45, goldPrice=16, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Adventurer Leggings
                        OutfitItem(itemId=3894, price=25, goldPrice=10, color1=81, color2=206, itemType="Shoes"), #  Crimson Red Adventurer's Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2032,
                    items = [
                        OutfitItem(itemId=1000116, price=45, goldPrice=16, color1=203, color2=17, itemType="Shirt"), # Shadow Green Bold Summer Vest
                        OutfitItem(itemId=1001022, price=45, goldPrice=16, color1=203, color2=17, itemType="Skirt"), # Shadow Green Bold Summer Skirt
                        OutfitItem(itemId=3898, price=25, goldPrice=10, color1=91, color2=105, itemType="Shoes"), # Coconut Brown Bold Summer Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2033,
                    items = [
                        OutfitItem(itemId=1000117, price=45, goldPrice=16, color1=166, color2=207, itemType="Shirt"), # Snow White Frills and Flounce Top
                        OutfitItem(itemId=654, price=15, goldPrice=6, color1=286, color2=123, itemType="Belt"), #  Cherry Pink Striped Summer Sash
                        OutfitItem(itemId=1001023, price=45, goldPrice=16, color1=166, color2=207, itemType="Skirt"), # Snow White Frills and Flounce Skirt
                        OutfitItem(itemId=3673, price=25, goldPrice=16, color1=286, color2=123, itemType="Shoes"), # Cherry Pink Funky Wedges
                    ],
                ),
                ShopOutfit(
                    outfitId=2034,
                    items = [
                        OutfitItem(itemId=294, price=45, goldPrice=16, color1=17, color2=165, itemType="Shirt"), #  Tendershoot Green Bow Sleeve Blouse
                        OutfitItem(itemId=1246, price=45, goldPrice=16, color1=165, color2=17, itemType="Skirt"), # Spring Breeze Green Bow Belt Skirt
                        OutfitItem(itemId=3626, price=25, goldPrice=10, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Ruffly Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=2035,
                    items = [
                        OutfitItem(itemId=96, price=45, goldPrice=16, color1=121, color2=44, itemType="Shirt"), # Daisy Pink I-Heart-Mermaids Tee
                        OutfitItem(itemId=1186, price=45, goldPrice=16, color1=121, color2=44, itemType="Skirt"), # Daisy Pink Ruffle Skirt
                        OutfitItem(itemId=3619, price=25, goldPrice=10, color1=44, color2=121, itemType="Shoes"), # Plumblossom Pink Sparkly Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=2036,
                    items = [
                        OutfitItem(itemId=2306, price=25, goldPrice=10, color1=189, color2=185, itemType="HeadItem"), # Ladybug Red Sunny Style Hat
                        OutfitItem(itemId=394, price=45, goldPrice=16, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Sunny Style Top
                        OutfitItem(itemId=1315, price=45, goldPrice=16, color1=185, color2=189, itemType="Skirt"), # Midnight Blue Sunny Style Skirt
                        OutfitItem(itemId=3734, price=25, goldPrice=10, color1=206, color2=166, itemType="Shoes"), # Raven Black Sunny Style Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2037,
                    items = [
                        OutfitItem(itemId=2084, price=25, goldPrice=10, color1=75, color2=84, itemType="HeadItem"), # Umber Brown Darling Fairy Crown
                        OutfitItem(itemId=2531, price=15, goldPrice=6, color1=84, color2=75, itemType="Necklace"), # Copper Brown Darling Fairy Necklace
                        OutfitItem(itemId=88, price=45, goldPrice=16, color1=84, color2=75, itemType="Shirt"), # Copper Brown Darling Fairy Combo Top
                        OutfitItem(itemId=1089, price=45, goldPrice=16, color1=75, color2=84, itemType="Skirt"), # Umber Brown Darling Dance Drape
                        OutfitItem(itemId=3565, price=25, goldPrice=10, color1=84, color2=75, itemType="Shoes"), # Copper Brown Darling Fairy Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2038,
                    items = [
                        OutfitItem(itemId=2208, price=25, goldPrice=10, color1=78, color2=78, itemType="HeadItem"), #  Fawn Brown Nifty Knit Hat
                        OutfitItem(itemId=320, price=45, goldPrice=16, color1=166, color2=151, itemType="Shirt"), # Snow White Carefree Sweater Top with Yellow Trim
                        OutfitItem(itemId=1259, price=45, goldPrice=16, color1=118, color2=153, itemType="Skirt"), # Sapphire Blue Casual Crops with Light Blue Trim
                        OutfitItem(itemId=3673, price=25, goldPrice=10, color1=78, color2=99, itemType="Shoes"), # Fawn Brown Funky Wedges
                    ],
                ),
                ShopOutfit(
                    outfitId=2039,
                    items = [
                        OutfitItem(itemId=2392, price=25, goldPrice=10, color1=269, color2=207, itemType="HeadItem"), # Crisp White Knit Beret
                        OutfitItem(itemId=1000025, price=45, goldPrice=16, color1=207, color2=215, itemType="Shirt"), # Diamond Blue Fluffy Puffer Top
                        OutfitItem(itemId=1436, price=45, goldPrice=16, color1=215, color2=207, itemType="Skirt"), # Pewter Gray Cozy Stripes Skirt
                        OutfitItem(itemId=3816, price=25, goldPrice=10, color1=207, color2=269, itemType="Shoes"), # Diamond Blue Fuzzy Ankle Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2040,
                    items = [
                        OutfitItem(itemId=2310, price=25, goldPrice=10, color1=275, color2=72, itemType="HeadItem"), # Shadowy Purple Knit Headwrap
                        OutfitItem(itemId=1000023, price=45, goldPrice=16, color1=275, color2=72, itemType="Shirt"), # Shadowy Purple Neat Knit Top
                        OutfitItem(itemId=1434, price=45, goldPrice=16, color1=275, color2=72, itemType="Skirt"), # Shadowy Purple Neat Knit Skirt
                        OutfitItem(itemId=3814, price=25, goldPrice=10, color1=275, color2=72, itemType="Shoes"), # Shadowy Purple Coziest Boots
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=84, # Themed Fashions
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=2041,
                    items = [
                        OutfitItem(itemId=2403, price=25, goldPrice=10, color1=18, color2=152, itemType="HeadItem"), # Waterfall Blue Northern Lights Tiara
                        OutfitItem(itemId=2629, price=15, goldPrice=6, color1=152, color2=18, itemType="Necklace"), # Pale Purple Northern Lights Necklace
                        OutfitItem(itemId=1000036, price=45, goldPrice=16, color1=18, color2=152, itemType="Shirt"), # Waterfall Blue Northern Lights Top
                        OutfitItem(itemId=1444, price=45, goldPrice=16, color1=18, color2=152, itemType="Skirt"), # Waterfall Blue Northern Lights Skirt
                        OutfitItem(itemId=3824, price=25, goldPrice=10, color1=18, color2=152, itemType="Shoes"), # Waterfall Blue Northern Lights Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2042,
                    items = [
                        OutfitItem(itemId=2285, price=25, goldPrice=10, color1=200, color2=44, itemType="HeadItem"), # Ruby Pink Sweet Baker Hat
                        OutfitItem(itemId=2591, price=15, goldPrice=6, color1=44, color2=44, itemType="Necklace"), # Plumblossom Pink Sweet Bow
                        OutfitItem(itemId=344, price=45, goldPrice=16, color1=200, color2=44, itemType="Shirt"), # Ruby Pink Sweet Puff Top
                        OutfitItem(itemId=631, price=15, goldPrice=6, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Sweet Bow Sash
                        OutfitItem(itemId=1281, price=45, goldPrice=16, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Sweet Puff Skirt
                        OutfitItem(itemId=3705, price=25, goldPrice=10, color1=200, color2=44, itemType="Shoes"), # Ruby Pink Sweet Bow Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2043,
                    items = [
                        OutfitItem(itemId=2101, price=25, goldPrice=10, color1=265, color2=45, itemType="HeadItem"), # Bright Sky Blue Straw and Blueberry Hat
                        OutfitItem(itemId=248, price=45, goldPrice=16, color1=137, color2=265, itemType="Shirt"), # Lemon Yellow Serving-Talent Blouse
                        OutfitItem(itemId=571, price=15, goldPrice=6, color1=45, color2=265, itemType="Belt"), # Strawberry Red Simple Apron with Bright Sky Blue Trim
                        OutfitItem(itemId=1208, price=45, goldPrice=16, color1=265, color2=137, itemType="Skirt"), # Bright Sky Blue Tea-Brewer Skirt
                        OutfitItem(itemId=3570, price=25, goldPrice=5, color1=265, color2=45 , itemType="Shoes"), # Bright Sky Blue Really Rainy Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2044,
                    items = [
                        OutfitItem(itemId=2438, price=25, goldPrice=10, color1=121, color2=239, itemType="HeadItem"), # Daisy Pink Carnival Chic Top Hat
                        OutfitItem(itemId=1000075, price=45, goldPrice=16, color1=121, color2=239, itemType="Shirt"), # Daisy Pink Carnival Chic Top
                        OutfitItem(itemId=1482, price=45, goldPrice=16, color1=239, color2=121, itemType="Skirt"), # Coffee Black Carnival Chic Skirt
                        OutfitItem(itemId=3867, price=25, goldPrice=10, color1=239, color2=239, itemType="Shoes"), # Coffee Black Carnival Chic Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2045,
                    items = [
                        OutfitItem(itemId=1000072, price=45, goldPrice=16, color1=111, color2=225, itemType="Shirt"), # Sparkling Yellow Siren Style Top
                        OutfitItem(itemId=1478, price=45, goldPrice=16, color1=225, color2=111, itemType="Skirt"), # Eggplant Purple Siren Style Skirt
                        OutfitItem(itemId=3863, price=25, goldPrice=10, color1=225, color2=111, itemType="Shoes"), # Eggplant Purple Siren Style Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=2046,
                    items = [
                        OutfitItem(itemId=1000113, price=45, goldPrice=16, color1=267, color2=159, itemType="Shirt"), # Celestial Blue Parrot Party Top
                        OutfitItem(itemId=1001019, price=45, goldPrice=16, color1=267, color2=159, itemType="Skirt"), # Celestial Blue Parrot Party Skirt
                        OutfitItem(itemId=3895, price=25, goldPrice=10, color1=159, color2=267, itemType="Shoes"), # Tea Green Parrot Party Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2047,
                    items = [
                        OutfitItem(itemId=1000111, price=45, goldPrice=16, color1=204, color2=205, itemType="Shirt"), # Bamboo Green Sorceress Dress Top
                        OutfitItem(itemId=1001017, price=45, goldPrice=16, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Sorceress Dress Skirt
                        OutfitItem(itemId=3893, price=25, goldPrice=10, color1=205, color2=204, itemType="Shoes"), # Myrtle Green Sorceress Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2048,
                    items = [
                        OutfitItem(itemId=2299, price=25, goldPrice=10, color1=206, color2=287, itemType="HeadItem"), # Raven Black Flaptastic Cloche
                        OutfitItem(itemId=383, price=45, goldPrice=16, color1=206, color2=216, itemType="Shirt"), # Raven Black Flaptastic Top
                        OutfitItem(itemId=1303, price=45, goldPrice=16, color1=206, color2=287, itemType="Skirt"), # Raven Black Flaptastic Skirt
                        OutfitItem(itemId=3721, price=25, goldPrice=10, color1=206, color2=287, itemType="Shoes"), # Raven Black Flaptastic Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2049,
                    items = [
                        OutfitItem(itemId=2608, price=15, goldPrice=6, color1=110, color2=110, itemType="Necklace"), # Rosy Pink Sock Hop Scarf
                        OutfitItem(itemId=399, price=45, goldPrice=16, color1=26, color2=110, itemType="Shirt"), # Raspberry Pink Sock Hop Top
                        OutfitItem(itemId=1322, price=45, goldPrice=16, color1=26, color2=110, itemType="Skirt"), # Raspberry Pink Sock Hop Skirt
                        OutfitItem(itemId=3746, price=25, goldPrice=10, color1=110, color2=26, itemType="Shoes"), # Rosy Pink Sock Hop Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2050,
                    items = [
                        OutfitItem(itemId=2111, price=25, goldPrice=10, color1=75, color2=265, itemType="HeadItem"), # Umber Brown Tiger Lily Head Piece
                        OutfitItem(itemId=117, price=45, goldPrice=16, color1=75, color2=265, itemType="Shirt"), # Umber Brown Tiger Lily Top
                        OutfitItem(itemId=1114, price=45, goldPrice=16, color1=75, color2=265, itemType="Skirt"), # Umber Brown Tassel Skirt
                        OutfitItem(itemId=3585, price=25, goldPrice=10, color1=265, color2=75, itemType="Shoes"), # Bright Sky Blue Fire Dance Moccasins
                    ],
                ),
                ShopOutfit(
                    outfitId=2051,
                    items = [
                        OutfitItem(itemId=341, price=45, goldPrice=16, color1=230, color2=8, itemType="Shirt"), # Scarlet Red Top 40 Jacket
                        OutfitItem(itemId=1619, price=15, goldPrice=6, color1=8, color2=8, itemType="WristItem"), # Watermelon Pink Sassy Glove
                        OutfitItem(itemId=1278, price=45, goldPrice=16, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Top 40 Pants
                        OutfitItem(itemId=3702, price=25, goldPrice=10, color1=224, color2=230, itemType="Shoes"), # Ivory White Top 40 Sneakers
                    ],
                ),
                ShopOutfit(
                    outfitId=2052,
                    items = [
                        OutfitItem(itemId=342, price=45, goldPrice=16, color1=239, color2=183, itemType="Shirt"), # Coffee Black Rock n' Roll Top
                        OutfitItem(itemId=628, price=15, goldPrice=6, color1=239, color2=239, itemType="Belt"), # Coffee Black Rock n' Roll Chain Belt
                        OutfitItem(itemId=1620, price=15, goldPrice=6, color1=239, color2=239, itemType="WristItem"), # Coffee Black Rock n' Roll Cuff
                        OutfitItem(itemId=1279, price=45, goldPrice=16, color1=239, color2=183, itemType="Skirt"), # Coffee Black Rock n' Roll Skirt
                        OutfitItem(itemId=3703, price=25, goldPrice=10, color1=239, color2=183, itemType="Shoes"), # Coffee Black Rock n' Roll Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2053,
                    items = [
                        OutfitItem(itemId=2280, price=25, goldPrice=10, color1=286, color2=286, itemType="HeadItem"), # Cherry Pink Far Out Funky Earrings
                        OutfitItem(itemId=339, price=25, goldPrice=16, color1=286, color2=226, itemType="Shirt"), # Cherry Pink Like, Totally! Top
                        OutfitItem(itemId=1276, price=45, goldPrice=16, color1=229, color2=226, itemType="Skirt"), # Electric Indigo Radical Tutu
                        OutfitItem(itemId=3701, price=25, goldPrice=10, color1=229, color2=226, itemType="Shoes"), # Electric Indigo Leg Warmer Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=2054,
                    items = [
                        OutfitItem(itemId=399, price=45, goldPrice=16, color1=195, color2=226, itemType="Shirt"), # Electric Blue Sock Hop Top
                        OutfitItem(itemId=1274, price=45, goldPrice=16, color1=226, color2=195, itemType="Skirt"), # Goldenrod Yellow Silly Tutu
                        OutfitItem(itemId=3699, price=25, goldPrice=10, color1=226, color2=198, itemType="Shoes"), # Goldenrod Yellow Polka-Stripe Socks
                    ],
                ),
                ShopOutfit(
                    outfitId=2055,
                    items = [
                        OutfitItem(itemId=2177, price=25, goldPrice=10, color1=70, color2=166, itemType="HeadItem"), # Tinker Blue Teatime Hat
                        OutfitItem(itemId=250, price=45, goldPrice=16, color1=70, color2=166, itemType="Shirt"), # Tinker Blue Light and Lacy Tea Top
                        OutfitItem(itemId=611, price=15, goldPrice=6, color1=166, color2=166, itemType="Belt"), # Snow White Light and Lacy Sash
                        OutfitItem(itemId=1209, price=45, goldPrice=16, color1=70, color2=166, itemType="Skirt"), # Tinker Blue Light and Lacy Tea Skirt
                        OutfitItem(itemId=3644, price=25, goldPrice=10, color1=70, color2=166, itemType="Shoes"), # Tinker Blue Light and Lacy Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=2056,
                    items = [
                        OutfitItem(itemId=2188, price=25, goldPrice=10, color1=44, color2=182, itemType="HeadItem"), # Plumblossom Pink Serving-Talent Hat with Twilight Blue Trim
                        OutfitItem(itemId=248, price=45, goldPrice=16, color1=159, color2=182, itemType="Shirt"), # Tea Green Serving-Talent Blouse with Twilight Blue Trim
                        OutfitItem(itemId=609, price=15, goldPrice=6, color1=182, color2=44, itemType="Belt"), #  Twilight Blue Serving-Talent Sash
                        OutfitItem(itemId=1207, price=45, goldPrice=16, color1=159, color2=159, itemType="Skirt"), # Tea Green Serving-Talent Skirt
                        OutfitItem(itemId=3696, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Splendid Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=2057,
                    items = [
                        OutfitItem(itemId=2176, price=25, goldPrice=10, color1=111, color2=130, itemType="HeadItem"), # Sparkling Yellow Tea-Brewer Cap
                        OutfitItem(itemId=249, price=45, goldPrice=16, color1=130, color2=111, itemType="Shirt"), # Orchid Pink Tea-Brewer Top
                        OutfitItem(itemId=610, price=15, goldPrice=6, color1=111, color2=226, itemType="Belt"), # Sparkling Yellow Tea-Brewer Apron
                        OutfitItem(itemId=1208, price=45, goldPrice=16, color1=111, color2=130, itemType="Skirt"), # Sparkling Yellow Tea-Brewer Skirt
                        OutfitItem(itemId=3696, price=25, goldPrice=10, color1=130, color2=130, itemType="Shoes"), # Orchid Pink Splendid Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=2058,
                    items = [
                        OutfitItem(itemId=2045, price=25, goldPrice=10, color1=166, color2=189, itemType="HeadItem"), # Snow White Baking Hat with Ladybug Red Trim
                        OutfitItem(itemId=93, price=45, goldPrice=16, color1=189, color2=125, itemType="Shirt"), # Ladybug Red Desert Adventure Top
                        OutfitItem(itemId=571, price=15, goldPrice=6, color1=45, color2=45, itemType="Belt"), # Strawberry Red Simple Apron
                        OutfitItem(itemId=1520, price=15, goldPrice=6, color1=45, color2=166, itemType="WristItem"), # Strawberry Red Oven Mitt with Snow White Trim
                        OutfitItem(itemId=1017, price=45, goldPrice=16, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Grass Petal Pushers
                        OutfitItem(itemId=3515, price=25, goldPrice=10, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Pea Pod Slippers
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=95, # Princess Fashion
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            outfits=[
                ShopOutfit(
                    outfitId=2059,
                    items = [
                        OutfitItem(itemId=2217, price=25, goldPrice=10, color1=162, color2=149, itemType="HeadItem"), # Sunglow Yellow Princess Headband
                        OutfitItem(itemId=297, price=45, goldPrice=16, color1=162, color2=149, itemType="Shirt"), # Sunglow Yellow Poufy Princess Top
                        OutfitItem(itemId=1247, price=45, goldPrice=16, color1=162, color2=149, itemType="Skirt"), # Sunglow Yellow Poufy Princess Skirt
                        OutfitItem(itemId=3675, price=25, goldPrice=10, color1=149, color2=149, itemType="Shoes"), # Snowflake Blue Glittering Glass Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=2060,
                    items = [
                        OutfitItem(itemId=2282, price=25, goldPrice=10, color1=206, color2=206, itemType="HeadItem"), # Raven Black Blossoming Rose Headband
                        OutfitItem(itemId=340, price=45, goldPrice=16, color1=227, color2=206, itemType="Shirt"), # Moonlight Gray Dreamy Meadow Blouse
                        OutfitItem(itemId=1277, price=45, goldPrice=16, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Dreamy Meadow Skirt
                        OutfitItem(itemId=3696, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Splendid Petal Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=2061,
                    items = [
                        OutfitItem(itemId=2397, price=25, goldPrice=10, color1=110, color2=110, itemType="HeadItem"), # Rosy Pink Lovely Blooms Crown
                        OutfitItem(itemId=1000038, price=45, goldPrice=16, color1=52, color2=110, itemType="Shirt"), # Lavender Purple Lovely Blooms Top
                        OutfitItem(itemId=1662, price=15, goldPrice=6, color1=116, color2=113, itemType="WristItem"), # Mushroom White Lovely Blooms Lantern
                        OutfitItem(itemId=1446, price=45, goldPrice=16, color1=52, color2=110, itemType="Skirt"), # Lavender Purple Lovely Blooms Skirt
                        OutfitItem(itemId=3826, price=25, goldPrice=10, color1=52, color2=110, itemType="Shoes"), # Lavender Purple Lovely Blooms Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=2062,
                    items = [
                        OutfitItem(itemId=2607, price=15, goldPrice=6, color1=69, color2=166, itemType="Necklace"), # Powder Blue Summer Breeze Necklace
                        OutfitItem(itemId=397, price=45, goldPrice=16, color1=191, color2=113, itemType="Shirt"), # Vidia Black Summer Breeze Top
                        OutfitItem(itemId=1640, price=15, goldPrice=6, color1=49, color2=166, itemType="WristItem"), # Robin Egg Blue Summer Breeze Bangles
                        OutfitItem(itemId=1319, price=45, goldPrice=16, color1=191, color2=113, itemType="Skirt"), # Vidia Black Summer Breeze Pants
                        OutfitItem(itemId=3745, price=25, goldPrice=10, color1=49, color2=166, itemType="Shoes"), # Robin Egg Blue Summer Moccassins
                    ],
                ),
                ShopOutfit(
                    outfitId=2063,
                    items = [
                        OutfitItem(itemId=2323, price=25, goldPrice=10, color1=113, color2=38, itemType="HeadItem"), # Pale Rose Red Apple Headband
                        OutfitItem(itemId=2585, price=15, goldPrice=6, color1=113, color2=118, itemType="Necklace"), # Pale Rose Red Fairy Friends Necklace
                        OutfitItem(itemId=398, price=45, goldPrice=16, color1=38, color2=118, itemType="Shirt"), # Apple Green Wishing Apple Top
                        OutfitItem(itemId=1320, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Wishing Apple Skirt
                        OutfitItem(itemId=3696, price=25, goldPrice=10, color1=38, color2=38, itemType="Shoes"), # Apple Green Splendid Petal Slippers
                    ],
                )
            ],
        ),
    ]
)