from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

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
            items=[
                ShopItem(itemId=2427, price=25, goldPrice=10, color1=201, color2=121, itemType="HeadItem"), # Velvet Red Hydrangea Barrette
                ShopItem(itemId=1000058, price=45, goldPrice=16, color1=201, color2=121, itemType="Shirt"), # Velvet Red Hydrangea Top
                ShopItem(itemId=1465, price=45, goldPrice=16, color1=201, color2=121, itemType="Skirt"), # Velvet Red Hydrangea Skirt
                ShopItem(itemId=3846, price=25, goldPrice=10, color1=201, color2=121, itemType="Shoes"), # Velvet Red Hydrangea Heels
                ShopItem(itemId=2284, price=25, goldPrice=10, color1=166, color2=1, itemType="HeadItem"), # Snow White Snowdrop Headband
                ShopItem(itemId=343, price=45, goldPrice=16, color1=166, color2=1, itemType="Shirt"), # Snow White Snowdrop Top
                ShopItem(itemId=629, price=15, goldPrice=6, color1=166, color2=1, itemType="Belt"), # Snow White Snowdrop Sash
                ShopItem(itemId=1280, price=45, goldPrice=16, color1=166, color2=1, itemType="Skirt"), # Snow White Snowdrop Skirt
                ShopItem(itemId=3704, price=25, goldPrice=10, color1=166, color2=1, itemType="Shoes"), # Snow White Snowdrop Shoes
                ShopItem(itemId=2292, price=25, goldPrice=10, color1=208, color2=267, itemType="HeadItem"), # Cerulean Blue Hanami Headpiece
                ShopItem(itemId=377, price=45, goldPrice=16, color1=208, color2=267, itemType="Shirt"), # Cerulean Blue Hanami Top
                ShopItem(itemId=636, price=15, goldPrice=6, color1=209, color2=267, itemType="Belt"), # Deep Sea Blue Hanami Sash
                ShopItem(itemId=1300, price=45, goldPrice=16, color1=208, color2=267, itemType="Skirt"), # Cerulean Blue Hanami Long Skirt
                ShopItem(itemId=3717, price=25, goldPrice=16, color1=267, color2=98, itemType="Shoes"), # Celestial Blue Hanami Geta Shoes
                ShopItem(itemId=2292, price=25, goldPrice=10, color1=81, color2=26, itemType="HeadItem"), # Crimson Red Hanami Headpiece
                ShopItem(itemId=377, price=45, goldPrice=16, color1=199, color2=26, itemType="Shirt"), # Cherryblossom Pink Hanami Top
                ShopItem(itemId=636, price=15, goldPrice=6, color1=81, color2=26, itemType="Belt"), # Crimson Red Hanami Sash
                ShopItem(itemId=1295, price=45, goldPrice=16, color1=199, color2=26, itemType="Skirt"), # Cherryblossom Pink Hanami Short Skirt
                ShopItem(itemId=3717, price=25, goldPrice=10, color1=81, color2=98, itemType="Shoes"), # Crimson Red Hanami Geta Shoes
                ShopItem(itemId=2449, price=25, goldPrice=10, color1=267, color2=10, itemType="HeadItem"), # Celestial Blue Azalea Barrette
                ShopItem(itemId=1000074, price=45, goldPrice=16, color1=10, color2=267, itemType="Shirt"), # Cantaloupe Orange Azalea Top
                ShopItem(itemId=1481, price=45, goldPrice=16, color1=10, color2=267, itemType="Skirt"), # Cantaloupe Orange Azalea Skirt
                ShopItem(itemId=3866, price=25, goldPrice=10, color1=10, color2=267, itemType="Shoes"), # Cantaloupe Orange Azalea Sandals
                ShopItem(itemId=385, price=45, goldPrice=16, color1=287, color2=166, itemType="Shirt"), # Dianthus Red Dianthus Blouse
                ShopItem(itemId=1305, price=45, goldPrice=16, color1=287, color2=166, itemType="Skirt"), # Dianthus Red Dianthus Skirt
                ShopItem(itemId=3722, price=25, goldPrice=10, color1=287, color2=166, itemType="Shoes"), # Dianthus Red Dianthus Shoes
                ShopItem(itemId=2336, price=25, goldPrice=10, color1=186, color2=230, itemType="HeadItem"), # Honeycomb Yellow Flame Lily Barrette
                ShopItem(itemId=417, price=45, goldPrice=16, color1=186, color2=230, itemType="Shirt"), # Honeycomb Yellow Flame Lily Top
                ShopItem(itemId=1335, price=45, goldPrice=16, color1=186, color2=230, itemType="Skirt"), # Honeycomb Yellow Flame Lily Skirt
                ShopItem(itemId=3758, price=25, goldPrice=10, color1=186, color2=230, itemType="Shoes"), # Honeycomb Yellow Flame Lily Shoes
                ShopItem(itemId=2348, price=25, goldPrice=10, color1=130, color2=81, itemType="HeadItem"), # Orchid Pink Chrysanthemum Beret
                ShopItem(itemId=477, price=45, goldPrice=16, color1=224, color2=81, itemType="Shirt"), # Ivory White Chrysanthemum Top
                ShopItem(itemId=640, price=15, goldPrice=6, color1=81, color2=130, itemType="Belt"), # Crimson Red Chrysanthemum Belt
                ShopItem(itemId=1396, price=45, goldPrice=16, color1=206, color2=81, itemType="Skirt"), # Raven Black Chrysanthemum Skirt
                ShopItem(itemId=3779, price=25, goldPrice=10, color1=81, color2=130, itemType="Shoes"), # Crimson Red Chrysanthemum Shoes
                ShopItem(itemId=2356, price=25, goldPrice=10, color1=153, color2=162, itemType="HeadItem"), # Frostbunny Blue Bead Cascade Earrings
                ShopItem(itemId=483, price=45, goldPrice=16, color1=118, color2=153, itemType="Shirt"), # Sapphire Blue Camellia Top
                ShopItem(itemId=1400, price=45, goldPrice=16, color1=206, color2=118, itemType="Skirt"), # Raven Black Camellia Skirt
                ShopItem(itemId=3782, price=25, goldPrice=10, color1=74, color2=74, itemType="Shoes"), # Papyrus Tan Camellia Boots
                ShopItem(itemId=2386, price=25, goldPrice=10, color1=224, color2=153, itemType="HeadItem"), # Ivory White Snow Rose Barrettes with Frostbunny Blue Trim
                ShopItem(itemId=1000024, price=45, goldPrice=16, color1=224, color2=153, itemType="Shirt"), # Ivory White Snow Rose Top with Frostbunny Blue Trim
                ShopItem(itemId=1435, price=45, goldPrice=16, color1=153, color2=153, itemType="Skirt"), # Frostbunny Blue Snow Rose Skirt
                ShopItem(itemId=3815, price=25, goldPrice=10, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Snow Rose Heels
                ShopItem(itemId=2171, price=25, goldPrice=10, color1=211, color2=211, itemType="HeadItem"), # Gentian Purple Moth Orchid Headband
                ShopItem(itemId=216, price=45, goldPrice=16, color1=51, color2=15, itemType="Shirt"), # Periwinkle Blue Moth Orchid Top
                ShopItem(itemId=594, price=15, goldPrice=6, color1=211, color2=211, itemType="Belt"), # Gentian Purple Moth Orchid Leaf Sash
                ShopItem(itemId=1183, price=45, goldPrice=16, color1=51, color2=211, itemType="Skirt"), # Periwinkle Blue Moth Orchid Bottom
                ShopItem(itemId=3629, price=25, goldPrice=10, color1=51, color2=15, itemType="Shoes"), # Periwinkle Blue Moth Orchid Shoes
                ShopItem(itemId=2172, price=25, goldPrice=10, color1=258, color2=125, itemType="HeadItem"), # Spearmint Green Dragon Arum Crown
                ShopItem(itemId=217, price=45, goldPrice=16, color1=166, color2=18, itemType="Shirt"), # Snow White Dragon Arum Top
                ShopItem(itemId=593, price=15, goldPrice=6, color1=258, color2=258, itemType="Belt"), # Spearmint Green Dragon Arum Sash
                ShopItem(itemId=1185, price=45, goldPrice=16, color1=166, color2=18, itemType="Skirt"), # Snow White Dragon Arum Skirt
                ShopItem(itemId=3630, price=25, goldPrice=10, color1=258, color2=125, itemType="Shoes"), # Spearmint Green Dragon Arum Shoes
                ShopItem(itemId=2100, price=25, goldPrice=10, color1=153, color2=166, itemType="HeadItem"), # Frostbunny Blue Campanula Barrette
                ShopItem(itemId=108, price=45, goldPrice=16, color1=153, color2=166, itemType="Shirt"), # Frostbunny Blue Campanula Top
                ShopItem(itemId=1111, price=45, goldPrice=16, color1=153, color2=166, itemType="Skirt"), # Frostbunny Blue Campanula Skirt
                ShopItem(itemId=3578, price=25, goldPrice=10, color1=153, color2=166, itemType="Shoes"), # Frostbunny Blue Campanula Shoes
                ShopItem(itemId=2120, price=25, goldPrice=10, color1=199, color2=121, itemType="HeadItem"), # Cherryblossom Pink Campis Barrette
                ShopItem(itemId=109, price=45, goldPrice=16, color1=199, color2=121, itemType="Shirt"), # Cherryblossom Pink Campis Top
                ShopItem(itemId=1121, price=45, goldPrice=16, color1=199, color2=121, itemType="Skirt"), # Cherryblossom Pink Campis Skirt
                ShopItem(itemId=3579, price=25, goldPrice=10, color1=199, color2=121, itemType="Shoes"), # Cherryblossom Pink Campis Shoes
                ShopItem(itemId=2123, price=25, goldPrice=10, color1=152, color2=183, itemType="HeadItem"), # Pale Purple Lagerstroemia Hat
                ShopItem(itemId=112, price=45, goldPrice=16, color1=152, color2=183, itemType="Shirt"), # Pale Purple Lagerstroemia Top
                ShopItem(itemId=1124, price=45, goldPrice=16, color1=152, color2=183, itemType="Skirt"), # Pale Purple Lagerstroemia Skirt
                ShopItem(itemId=3582, price=25, goldPrice=10, color1=152, color2=183, itemType="Shoes"), # Pale Purple Lagerstroemia Shoes
                ShopItem(itemId=2586, price=15, goldPrice=6, color1=138, color2=138, itemType="Necklace"), # Persimmon Orange Marigold Necklace
                ShopItem(itemId=333, price=45, goldPrice=16, color1=30, color2=10, itemType="Shirt"), # Pumpkin Orange Marigold Top
                ShopItem(itemId=1270, price=45, goldPrice=16, color1=30, color2=10, itemType="Skirt"), # Pumpkin Orange Marigold Skirt
                ShopItem(itemId=3695, price=25, goldPrice=10, color1=138, color2=138, itemType="Shoes"), # Persimmon Orange Marigold Shoes
            ],
        ),
        ShopCollection(
            collectionId=46, # Mainland Styles
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
                ShopItem(itemId=1000031, price=45, goldPrice=16, color1=180, color2=195, itemType="Shirt"), # Seashell Blue Chic Tie-Dye Top
                ShopItem(itemId=1442, price=45, goldPrice=16, color1=180, color2=195, itemType="Skirt"), # Seashell Blue Chic Tie-Dye Skirt
                ShopItem(itemId=3822, price=25, goldPrice=10, color1=180, color2=195, itemType="Shoes"), # Seashell Blue Super Chic Sandals
                ShopItem(itemId=1000037, price=45, goldPrice=16, color1=278, color2=110, itemType="Shirt"), # Aster Purple Fluttery Tie-Dye Top
                ShopItem(itemId=1445, price=45, goldPrice=16, color1=278, color2=110, itemType="Skirt"), # Aster Purple Fluttery Tie-Dye Skirt
                ShopItem(itemId=3822, price=25, goldPrice=10, color1=278, color2=110, itemType="Shoes"), # Aster Purple Super Chic Sandals
                ShopItem(itemId=2423, price=25, goldPrice=10, color1=217, color2=267, itemType="HeadItem"), # Soft Gray Cute Cap
                ShopItem(itemId=1000057, price=45, goldPrice=16, color1=217, color2=267, itemType="Shirt"), # Soft Gray Cardie Combo Top
                ShopItem(itemId=1464, price=45, goldPrice=16, color1=217, color2=267, itemType="Skirt"), # Soft Gray Delightful Denim Skirt
                ShopItem(itemId=3844, price=25, goldPrice=10, color1=217, color2=267, itemType="Shoes"), # Soft Gray Lovely Laceups
                ShopItem(itemId=2634, price=15, goldPrice=6, color1=224, color2=267, itemType="Necklace"), # Ivory White Sweetheart Purse
                ShopItem(itemId=1000055, price=45, goldPrice=16, color1=162, color2=224, itemType="Shirt"), # Sunglow Yellow Sweetheart Top
                ShopItem(itemId=650, price=15, goldPrice=6, color1=267, color2=224, itemType="Belt"), # Celestial Blue Sweetheart Sash
                ShopItem(itemId=1463, price=45, goldPrice=16, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sweetheart Skirt
                ShopItem(itemId=3845, price=25, goldPrice=16, color1=162, color2=267, itemType="Shoes"), # Sunglow Yellow Sweetheart Sandals
                ShopItem(itemId=2428, price=25, goldPrice=10, color1=135, color2=282, itemType="HeadItem"), # Boysenberry Purple Cute Cloud Earrings
                ShopItem(itemId=1000061, price=45, goldPrice=16, color1=5, color2=152, itemType="Shirt"), # Wysteria Purple Rainy Day Top
                ShopItem(itemId=1673, price=15, goldPrice=6, color1=135, color2=135, itemType="WristItem"), # Boysenberry Purple Rainbow Umbrella
                ShopItem(itemId=1468, price=45, goldPrice=16, color1=5, color2=152, itemType="Skirt"), # Wysteria Purple Rainy Day Skirt
                ShopItem(itemId=3850, price=25, goldPrice=10, color1=135, color2=282, itemType="Shoes"), # Boysenberry Purple Cozy Rain Boots
                ShopItem(itemId=1000052, price=45, goldPrice=16, color1=81, color2=224, itemType="Shirt"), # Crimson Red Soft Knit Sweater
                ShopItem(itemId=1459, price=45, goldPrice=16, color1=141, color2=81, itemType="Skirt"), # Thundercloud Gray Pleasing Pleats Skirt
                ShopItem(itemId=3840, price=25, goldPrice=10, color1=141, color2=224, itemType="Shoes"), # Thundercloud Gray Sweet Spring Laceups
                ShopItem(itemId=2636, price=15, goldPrice=6, color1=105, color2=105, itemType="Necklace"), #  Siltstone Tan Sweet Beaded Necklace
                ShopItem(itemId=1000063, price=45, goldPrice=16, color1=44, color2=123, itemType="Shirt"), # Plumblossom Pink Sweet Spring Hoodie
                ShopItem(itemId=1470, price=45, goldPrice=16, color1=126, color2=123, itemType="Skirt"), # Raindrop Blue Layered Look Skirt
                ShopItem(itemId=3855, price=25, goldPrice=10, color1=55, color2=224, itemType="Shoes"), # Pepper Black Cat Flats
                ShopItem(itemId=1000080, price=45, goldPrice=16, color1=44, color2=134, itemType="Shirt"), #  Plumblossom Pink Stylish Hoodie
                ShopItem(itemId=1487, price=45, goldPrice=16, color1=44, color2=134, itemType="Skirt"), # Plumblossom Pink Springy Skirt
                ShopItem(itemId=3871, price=25, goldPrice=10, color1=44, color2=134, itemType="Shoes"), # Plumblossom Pink Perfect Plaid Loafers
                ShopItem(itemId=2301, price=25, goldPrice=10, color1=11, color2=115, itemType="HeadItem"), # Marigold Yellow Folklorico Headband
                ShopItem(itemId=386, price=45, goldPrice=16, color1=274, color2=149, itemType="Shirt"), # Bellflower Purple Folklorico Blouse
                ShopItem(itemId=1306, price=45, goldPrice=16, color1=274, color2=149, itemType="Skirt"), # Bellflower Purple Folklorico Skirt
                ShopItem(itemId=3726, price=25, goldPrice=10, color1=11, color2=149, itemType="Shoes"), # Marigold Yellow Folklorico Heels
                ShopItem(itemId=1000114, price=45, goldPrice=16, color1=265, color2=17, itemType="Shirt"), # Bright Sky Blue Festive Floral Top
                ShopItem(itemId=1001020, price=45, goldPrice=16, color1=265, color2=17, itemType="Skirt"), # Bright Sky Blue Festive Floral Skirt
                ShopItem(itemId=3896, price=25, goldPrice=10, color1=17, color2=265, itemType="Shoes"), #  Tendershoot Green Pearl-Studded Sandals
                ShopItem(itemId=1000122, price=45, goldPrice=16, color1=150, color2=18, itemType="Shirt"), # Dry Moss Green Summer Stripes Top
                ShopItem(itemId=1001029, price=45, goldPrice=16, color1=150, color2=18, itemType="Skirt"), #  Dry Moss Green Summer Stripes Skirt
                ShopItem(itemId=3904, price=25, goldPrice=10, color1=150, color2=18, itemType="Shoes"), # Dry Moss Green Summer Stripes Sandals
                ShopItem(itemId=379, price=45, goldPrice=16, color1=189, color2=121, itemType="Shirt"), # Ladybug Red Breezy Ruffled Top
                ShopItem(itemId=1299, price=45, goldPrice=16, color1=121, color2=189, itemType="Skirt"), # Daisy Pink Breezy Ruffled Skirt
                ShopItem(itemId=3718, price=25, goldPrice=10, color1=206, color2=121, itemType="Shoes"), # Raven Black Ruffle Detail Shoes
                ShopItem(itemId=2474, price=25, goldPrice=10, color1=84, color2=77, itemType="HeadItem"), # Copper Brown Hiking Hat
                ShopItem(itemId=1000108, price=45, goldPrice=16, color1=224, color2=70, itemType="Shirt"), # Ivory White Hiking Gear
                ShopItem(itemId=1001015, price=45, goldPrice=16, color1=209, color2=70, itemType="Skirt"), # Deep Sea Blue Hiking Shorts
                ShopItem(itemId=3618, price=25, goldPrice=10, color1=78, color2=84, itemType="Shoes"), # Fawn Brown Woodchucks
                ShopItem(itemId=145, price=45, goldPrice=16, color1=159, color2=170, itemType="Shirt"), # Tea Green Sporty Top
                ShopItem(itemId=1048, price=45, goldPrice=16, color1=159, color2=170, itemType="Skirt"), # Tea Green Sports Shorts
                ShopItem(itemId=3504, price=25, goldPrice=10, color1=170, color2=170, itemType="Shoes"), # Olive Green Striders
                ShopItem(itemId=2466, price=25, goldPrice=10, color1=81, color2=224, itemType="HeadItem"), # Crimson Red Adventurer's Hat
                ShopItem(itemId=1000112, price=45, goldPrice=16, color1=81, color2=224, itemType="Shirt"), # Crimson Red Adventurer Jacket
                ShopItem(itemId=1001018, price=45, goldPrice=16, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Adventurer Leggings
                ShopItem(itemId=3894, price=25, goldPrice=10, color1=81, color2=206, itemType="Shoes"), #  Crimson Red Adventurer's Boots
                ShopItem(itemId=1000116, price=45, goldPrice=16, color1=203, color2=17, itemType="Shirt"), # Shadow Green Bold Summer Vest
                ShopItem(itemId=1001022, price=45, goldPrice=16, color1=203, color2=17, itemType="Skirt"), # Shadow Green Bold Summer Skirt
                ShopItem(itemId=3898, price=25, goldPrice=10, color1=91, color2=105, itemType="Shoes"), # Coconut Brown Bold Summer Boots
                ShopItem(itemId=1000117, price=45, goldPrice=16, color1=166, color2=207, itemType="Shirt"), # Snow White Frills and Flounce Top
                ShopItem(itemId=654, price=15, goldPrice=6, color1=286, color2=123, itemType="Belt"), #  Cherry Pink Striped Summer Sash
                ShopItem(itemId=1001023, price=45, goldPrice=16, color1=166, color2=207, itemType="Skirt"), # Snow White Frills and Flounce Skirt
                ShopItem(itemId=3673, price=25, goldPrice=16, color1=286, color2=123, itemType="Shoes"), # Cherry Pink Funky Wedges
                ShopItem(itemId=294, price=45, goldPrice=16, color1=17, color2=165, itemType="Shirt"), #  Tendershoot Green Bow Sleeve Blouse
                ShopItem(itemId=1246, price=45, goldPrice=16, color1=165, color2=17, itemType="Skirt"), # Spring Breeze Green Bow Belt Skirt
                ShopItem(itemId=3626, price=25, goldPrice=10, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Ruffly Slippers
                ShopItem(itemId=96, price=45, goldPrice=16, color1=121, color2=44, itemType="Shirt"), # Daisy Pink I-Heart-Mermaids Tee
                ShopItem(itemId=1186, price=45, goldPrice=16, color1=121, color2=44, itemType="Skirt"), # Daisy Pink Ruffle Skirt
                ShopItem(itemId=3619, price=25, goldPrice=10, color1=44, color2=121, itemType="Shoes"), # Plumblossom Pink Sparkly Slippers
                ShopItem(itemId=2306, price=25, goldPrice=10, color1=189, color2=185, itemType="HeadItem"), # Ladybug Red Sunny Style Hat
                ShopItem(itemId=394, price=45, goldPrice=16, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Sunny Style Top
                ShopItem(itemId=1315, price=45, goldPrice=16, color1=185, color2=189, itemType="Skirt"), # Midnight Blue Sunny Style Skirt
                ShopItem(itemId=3734, price=25, goldPrice=10, color1=206, color2=166, itemType="Shoes"), # Raven Black Sunny Style Boots
                ShopItem(itemId=2084, price=25, goldPrice=10, color1=75, color2=84, itemType="HeadItem"), # Umber Brown Darling Fairy Crown
                ShopItem(itemId=2531, price=15, goldPrice=6, color1=84, color2=75, itemType="Necklace"), # Copper Brown Darling Fairy Necklace
                ShopItem(itemId=88, price=45, goldPrice=16, color1=84, color2=75, itemType="Shirt"), # Copper Brown Darling Fairy Combo Top
                ShopItem(itemId=1089, price=45, goldPrice=16, color1=75, color2=84, itemType="Skirt"), # Umber Brown Darling Dance Drape
                ShopItem(itemId=3565, price=25, goldPrice=10, color1=84, color2=75, itemType="Shoes"), # Copper Brown Darling Fairy Boots
                ShopItem(itemId=2208, price=25, goldPrice=10, color1=78, color2=78, itemType="HeadItem"), #  Fawn Brown Nifty Knit Hat
                ShopItem(itemId=320, price=45, goldPrice=16, color1=166, color2=151, itemType="Shirt"), # Snow White Carefree Sweater Top with Yellow Trim
                ShopItem(itemId=1259, price=45, goldPrice=16, color1=118, color2=153, itemType="Skirt"), # Sapphire Blue Casual Crops with Light Blue Trim
                ShopItem(itemId=3673, price=25, goldPrice=10, color1=78, color2=99, itemType="Shoes"), # Fawn Brown Funky Wedges
                ShopItem(itemId=2392, price=25, goldPrice=10, color1=269, color2=207, itemType="HeadItem"), # Crisp White Knit Beret
                ShopItem(itemId=1000025, price=45, goldPrice=16, color1=207, color2=215, itemType="Shirt"), # Diamond Blue Fluffy Puffer Top
                ShopItem(itemId=1436, price=45, goldPrice=16, color1=215, color2=207, itemType="Skirt"), # Pewter Gray Cozy Stripes Skirt
                ShopItem(itemId=3816, price=25, goldPrice=10, color1=207, color2=269, itemType="Shoes"), # Diamond Blue Fuzzy Ankle Boots
                ShopItem(itemId=2310, price=25, goldPrice=10, color1=275, color2=72, itemType="HeadItem"), # Shadowy Purple Flower Knit Headwrap
                ShopItem(itemId=1000023, price=45, goldPrice=16, color1=275, color2=72, itemType="Shirt"), # Shadowy Purple Neat Knit Top
                ShopItem(itemId=1434, price=45, goldPrice=16, color1=275, color2=72, itemType="Skirt"), # Shadowy Purple Neat Knit Skirt
                ShopItem(itemId=3814, price=25, goldPrice=10, color1=275, color2=72, itemType="Shoes"), # Shadowy Purple Coziest Boots
            ],
        ),
        ShopCollection(
            collectionId=84, # Themed Fashions
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
                ShopItem(itemId=2403, price=25, goldPrice=10, color1=18, color2=152, itemType="HeadItem"), # Waterfall Blue Northern Lights Tiara
                ShopItem(itemId=2629, price=15, goldPrice=6, color1=152, color2=18, itemType="Necklace"), # Pale Purple Northern Lights Necklace
                ShopItem(itemId=1000036, price=45, goldPrice=16, color1=18, color2=152, itemType="Shirt"), # Waterfall Blue Northern Lights Top
                ShopItem(itemId=1444, price=45, goldPrice=16, color1=18, color2=152, itemType="Skirt"), # Waterfall Blue Northern Lights Skirt
                ShopItem(itemId=3824, price=25, goldPrice=10, color1=18, color2=152, itemType="Shoes"), # Waterfall Blue Northern Lights Heels

                ShopItem(itemId=2285, price=25, goldPrice=10, color1=200, color2=44, itemType="HeadItem"), # Ruby Pink Sweet Baker Hat
                ShopItem(itemId=2591, price=15, goldPrice=6, color1=44, color2=44, itemType="Necklace"), # Plumblossom Pink Sweet Bow
                ShopItem(itemId=344, price=45, goldPrice=16, color1=200, color2=44, itemType="Shirt"), # Ruby Pink Sweet Puff Top
                ShopItem(itemId=631, price=15, goldPrice=6, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Sweet Bow Sash
                ShopItem(itemId=1281, price=45, goldPrice=16, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Sweet Puff Skirt
                ShopItem(itemId=3705, price=25, goldPrice=10, color1=200, color2=44, itemType="Shoes"), # Ruby Pink Sweet Bow Shoes

                ShopItem(itemId=2101, price=25, goldPrice=10, color1=265, color2=45, itemType="HeadItem"), # Bright Sky Blue Straw and Blueberry Hat
                ShopItem(itemId=248, price=45, goldPrice=16, color1=137, color2=265, itemType="Shirt"), # Lemon Yellow Serving-Talent Blouse
                ShopItem(itemId=571, price=15, goldPrice=6, color1=45, color2=265, itemType="Belt"), # Strawberry Red Simple Apron with Bright Sky Blue Trim
                ShopItem(itemId=1208, price=45, goldPrice=16, color1=265, color2=137, itemType="Skirt"), # Bright Sky Blue Tea-Brewer Skirt
                ShopItem(itemId=3570, price=25, goldPrice=5, color1=265, color2=45 , itemType="Shoes"), # Bright Sky Blue Really Rainy Boots

                ShopItem(itemId=2438, price=25, goldPrice=10, color1=121, color2=239, itemType="HeadItem"), # Daisy Pink Carnival Chic Top Hat
                ShopItem(itemId=1000075, price=45, goldPrice=16, color1=121, color2=239, itemType="Shirt"), # Daisy Pink Carnival Chic Top
                ShopItem(itemId=1482, price=45, goldPrice=16, color1=239, color2=121, itemType="Skirt"), # Coffee Black Carnival Chic Skirt
                ShopItem(itemId=3867, price=25, goldPrice=10, color1=239, color2=239, itemType="Shoes"), # Coffee Black Carnival Chic Boots

                ShopItem(itemId=1000072, price=45, goldPrice=16, color1=111, color2=225, itemType="Shirt"), # Sparkling Yellow Siren Style Top
                ShopItem(itemId=1478, price=45, goldPrice=16, color1=225, color2=111, itemType="Skirt"), # Eggplant Purple Siren Style Skirt
                ShopItem(itemId=3863, price=25, goldPrice=10, color1=225, color2=111, itemType="Shoes"), # Eggplant Purple Siren Style Sandals

                ShopItem(itemId=1000113, price=45, goldPrice=16, color1=267, color2=159, itemType="Shirt"), # Celestial Blue Parrot Party Top
                ShopItem(itemId=1001019, price=45, goldPrice=16, color1=267, color2=159, itemType="Skirt"), # Celestial Blue Parrot Party Skirt
                ShopItem(itemId=3895, price=25, goldPrice=10, color1=159, color2=267, itemType="Shoes"), # Tea Green Parrot Party Heels

                ShopItem(itemId=1000111, price=45, goldPrice=16, color1=204, color2=205, itemType="Shirt"), # Bamboo Green Sorceress Dress Top
                ShopItem(itemId=1001017, price=45, goldPrice=16, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Sorceress Dress Skirt
                ShopItem(itemId=3893, price=25, goldPrice=10, color1=205, color2=204, itemType="Shoes"), # Myrtle Green Sorceress Heels

                ShopItem(itemId=2299, price=25, goldPrice=10, color1=206, color2=287, itemType="HeadItem"), # Raven Black Flaptastic Cloche
                ShopItem(itemId=383, price=45, goldPrice=16, color1=206, color2=216, itemType="Shirt"), # Raven Black Flaptastic Top
                ShopItem(itemId=1303, price=45, goldPrice=16, color1=206, color2=287, itemType="Skirt"), # Raven Black Flaptastic Skirt
                ShopItem(itemId=3721, price=25, goldPrice=10, color1=206, color2=287, itemType="Shoes"), # Raven Black Flaptastic Shoes

                ShopItem(itemId=2608, price=15, goldPrice=6, color1=110, color2=110, itemType="Necklace"), # Rosy Pink Sock Hop Scarf
                ShopItem(itemId=399, price=45, goldPrice=16, color1=26, color2=110, itemType="Shirt"), # Raspberry Pink Sock Hop Top
                ShopItem(itemId=1322, price=45, goldPrice=16, color1=26, color2=110, itemType="Skirt"), # Raspberry Pink Sock Hop Skirt
                ShopItem(itemId=3746, price=25, goldPrice=10, color1=110, color2=26, itemType="Shoes"), # Rosy Pink Sock Hop Shoes

                ShopItem(itemId=2111, price=25, goldPrice=10, color1=75, color2=265, itemType="HeadItem"), # Umber Brown Tiger Lily Head Piece
                ShopItem(itemId=117, price=45, goldPrice=16, color1=75, color2=265, itemType="Shirt"), # Umber Brown Tiger Lily Top
                ShopItem(itemId=1114, price=45, goldPrice=16, color1=75, color2=265, itemType="Skirt"), # Umber Brown Tassel Skirt
                ShopItem(itemId=3585, price=25, goldPrice=10, color1=265, color2=75, itemType="Shoes"), # Bright Sky Blue Fire Dance Moccasins

                ShopItem(itemId=341, price=45, goldPrice=16, color1=230, color2=8, itemType="Shirt"), # Scarlet Red Top 40 Jacket
                ShopItem(itemId=1619, price=15, goldPrice=6, color1=8, color2=8, itemType="WristItem"), # Watermelon Pink Sassy Glove
                ShopItem(itemId=1278, price=45, goldPrice=16, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Top 40 Pants
                ShopItem(itemId=3702, price=25, goldPrice=10, color1=224, color2=230, itemType="Shoes"), # Ivory White Top 40 Sneakers

                ShopItem(itemId=342, price=45, goldPrice=16, color1=239, color2=183, itemType="Shirt"), # Coffee Black Rock n' Roll Top
                ShopItem(itemId=628, price=15, goldPrice=6, color1=239, color2=239, itemType="Belt"), # Coffee Black Rock n' Roll Chain Belt
                ShopItem(itemId=1620, price=15, goldPrice=6, color1=239, color2=239, itemType="WristItem"), # Coffee Black Rock n' Roll Cuff
                ShopItem(itemId=1279, price=45, goldPrice=16, color1=239, color2=183, itemType="Skirt"), # Coffee Black Rock n' Roll Skirt
                ShopItem(itemId=3703, price=25, goldPrice=10, color1=239, color2=183, itemType="Shoes"), # Coffee Black Rock n' Roll Boots

                ShopItem(itemId=2280, price=25, goldPrice=10, color1=286, color2=286, itemType="HeadItem"), # Cherry Pink Far Out Funky Earrings
                ShopItem(itemId=339, price=25, goldPrice=16, color1=286, color2=226, itemType="Shirt"), # Cherry Pink Like, Totally! Top
                ShopItem(itemId=1276, price=45, goldPrice=16, color1=229, color2=226, itemType="Skirt"), # Electric Indigo Radical Tutu
                ShopItem(itemId=3701, price=25, goldPrice=10, color1=229, color2=226, itemType="Shoes"), # Electric Indigo Leg Warmer Shoes

                ShopItem(itemId=399, price=45, goldPrice=16, color1=195, color2=226, itemType="Shirt"), # Electric Blue Sock Hop Top
                ShopItem(itemId=1274, price=45, goldPrice=16, color1=226, color2=195, itemType="Skirt"), # Goldenrod Yellow Silly Tutu
                ShopItem(itemId=3699, price=25, goldPrice=10, color1=226, color2=198, itemType="Shoes"), # Goldenrod Yellow Polka-Stripe Socks

                ShopItem(itemId=2177, price=25, goldPrice=10, color1=70, color2=166, itemType="HeadItem"), # Tinker Blue Teatime Hat
                ShopItem(itemId=250, price=45, goldPrice=16, color1=70, color2=166, itemType="Shirt"), # Tinker Blue Light and Lacy Tea Top
                ShopItem(itemId=611, price=15, goldPrice=6, color1=166, color2=166, itemType="Belt"), # Snow White Light and Lacy Sash
                ShopItem(itemId=1209, price=45, goldPrice=16, color1=70, color2=166, itemType="Skirt"), # Tinker Blue Light and Lacy Tea Skirt
                ShopItem(itemId=3644, price=25, goldPrice=10, color1=70, color2=166, itemType="Shoes"), # Tinker Blue Light and Lacy Boots

                ShopItem(itemId=2188, price=25, goldPrice=10, color1=44, color2=182, itemType="HeadItem"), # Plumblossom Pink Serving-Talent Hat with Twilight Blue Trim
                ShopItem(itemId=248, price=45, goldPrice=16, color1=159, color2=182, itemType="Shirt"), # Tea Green Serving-Talent Blouse with Twilight Blue Trim
                ShopItem(itemId=609, price=15, goldPrice=6, color1=182, color2=44, itemType="Belt"), #  Twilight Blue Serving-Talent Sash
                ShopItem(itemId=1207, price=45, goldPrice=16, color1=159, color2=159, itemType="Skirt"), # Tea Green Serving-Talent Skirt
                ShopItem(itemId=3696, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Petal Slippers

                ShopItem(itemId=2176, price=25, goldPrice=10, color1=111, color2=130, itemType="HeadItem"), # Sparkling Yellow Tea-Brewer Cap
                ShopItem(itemId=249, price=45, goldPrice=16, color1=130, color2=111, itemType="Shirt"), # Orchid Pink Tea-Brewer Top
                ShopItem(itemId=610, price=15, goldPrice=6, color1=111, color2=226, itemType="Belt"), # Sparkling Yellow Tea-Brewer Apron
                ShopItem(itemId=1208, price=45, goldPrice=16, color1=111, color2=130, itemType="Skirt"), # Sparkling Yellow Tea-Brewer Skirt
                ShopItem(itemId=3696, price=25, goldPrice=10, color1=130, color2=130, itemType="Shoes"), # Orchid Pink Petal Slippers

                ShopItem(itemId=2045, price=25, goldPrice=10, color1=166, color2=189, itemType="HeadItem"), # Snow White Baking Hat with Ladybug Red Trim
                ShopItem(itemId=93, price=45, goldPrice=16, color1=189, color2=125, itemType="Shirt"), # Ladybug Red Desert Adventure Top
                ShopItem(itemId=571, price=15, goldPrice=6, color1=45, color2=45, itemType="Belt"), # Strawberry Red Simple Apron
                ShopItem(itemId=1520, price=15, goldPrice=6, color1=45, color2=166, itemType="WristItem"), # Strawberry Red Oven Mitt with Snow White Trim
                ShopItem(itemId=1017, price=45, goldPrice=16, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Grass Petal Pushers
                ShopItem(itemId=3515, price=25, goldPrice=10, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Pea Pod Slippers
            ],
        ),
        ShopCollection(
            collectionId=95, # Princess Fashion
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
                ShopItem(itemId=2217, price=25, goldPrice=10, color1=162, color2=149, itemType="HeadItem"), # Sunglow Yellow Princess Headband
                ShopItem(itemId=297, price=45, goldPrice=16, color1=162, color2=149, itemType="Shirt"), # Sunglow Yellow Poufy Princess Top
                ShopItem(itemId=1247, price=45, goldPrice=16, color1=162, color2=149, itemType="Skirt"), # Sunglow Yellow Poufy Princess Skirt
                ShopItem(itemId=3675, price=25, goldPrice=10, color1=149, color2=149, itemType="Shoes"), # Snowflake Blue Glittering Glass Slippers

                ShopItem(itemId=2282, price=25, goldPrice=10, color1=206, color2=206, itemType="HeadItem"), # Raven Black Blossoming Rose Headband
                ShopItem(itemId=340, price=45, goldPrice=16, color1=227, color2=206, itemType="Shirt"), # Moonlight Gray Dreamy Meadow Blouse
                ShopItem(itemId=1277, price=45, goldPrice=16, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Dreamy Meadow Skirt
                ShopItem(itemId=3696, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Splendid Petal Slippers

                ShopItem(itemId=2397, price=25, goldPrice=10, color1=110, color2=110, itemType="HeadItem"), # Rosy Pink Lovely Blooms Crown
                ShopItem(itemId=1000038, price=45, goldPrice=16, color1=52, color2=110, itemType="Shirt"), # Lavender Purple Lovely Blooms Top
                ShopItem(itemId=1662, price=15, goldPrice=6, color1=116, color2=113, itemType="WristItem"), # Mushroom White Lovely Blooms Lantern
                ShopItem(itemId=1446, price=45, goldPrice=16, color1=52, color2=110, itemType="Skirt"), # Lavender Purple Lovely Blooms Skirt
                ShopItem(itemId=3826, price=25, goldPrice=10, color1=52, color2=110, itemType="Shoes"), # Lavender Purple Lovely Blooms Heels

                ShopItem(itemId=2607, price=15, goldPrice=6, color1=69, color2=166, itemType="Necklace"), # Powder Blue Summer Breeze Necklace
                ShopItem(itemId=397, price=45, goldPrice=16, color1=191, color2=113, itemType="Shirt"), # Vidia Black Summer Breeze Top
                ShopItem(itemId=1640, price=15, goldPrice=6, color1=49, color2=166, itemType="WristItem"), # Robin Egg Blue Summer Breeze Bangles
                ShopItem(itemId=1319, price=45, goldPrice=16, color1=191, color2=113, itemType="Skirt"), # Vidia Black Summer Breeze Pants
                ShopItem(itemId=3745, price=25, goldPrice=10, color1=49, color2=166, itemType="Shoes"), # Robin Egg Blue Summer Moccassins

                ShopItem(itemId=2323, price=25, goldPrice=10, color1=113, color2=38, itemType="HeadItem"), # Pale Rose Red Apple Headband
                ShopItem(itemId=2585, price=15, goldPrice=6, color1=113, color2=118, itemType="Necklace"), # Pale Rose Red Fairy Friends Necklace
                ShopItem(itemId=398, price=45, goldPrice=16, color1=38, color2=118, itemType="Shirt"), # Apple Green Wishing Apple Top
                ShopItem(itemId=1320, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Wishing Apple Skirt
                ShopItem(itemId=3696, price=25, goldPrice=10, color1=38, color2=38, itemType="Shoes"), # Apple Green Splendid Petal Slippers
            ],
        ),
    ]
)