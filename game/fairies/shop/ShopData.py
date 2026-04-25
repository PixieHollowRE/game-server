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
            ShopCollection(
                collectionId=82, # Floral Collections
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2427, price=15, goldPrice=3, color1=201, color2=201, itemType="HeadItem"), # Velvet Red Hydrangea Barrette
                    ShopItem(itemId=1000058, price=25, goldPrice=5, color1=201, color2=201, itemType="Shirt"), # Velvet Red Hydrangea Top
                    ShopItem(itemId=1465, price=25, goldPrice=5, color1=201, color2=201, itemType="Skirt"), # Velvet Red Hydrangea Skirt
                    ShopItem(itemId=3846, price=15, goldPrice=3, color1=201, color2=201, itemType="Shoes"), # Velvet Red Hydrangea Heels
                    ShopItem(itemId=2284, price=15, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Snowdrop Headband
                    ShopItem(itemId=343, price=25, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Snowdrop Top
                    ShopItem(itemId=629, price=5, goldPrice=1, color1=166, color2=166, itemType="Belt"), # Snow White Snowdrop Sash
                    ShopItem(itemId=1280, price=25, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Snowdrop Skirt
                    ShopItem(itemId=3704, price=15, goldPrice=3, color1=166, color2=166, itemType="Shoes"), # Snow White Snowdrop Shoes
                    ShopItem(itemId=2292, price=15, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Hanami Headpiece
                    ShopItem(itemId=377, price=25, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Hanami Top
                    ShopItem(itemId=636, price=5, goldPrice=1, color1=29, color2=29, itemType="Belt"), # Deep Sea Blue Hanami Sash
                    ShopItem(itemId=1300, price=25, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Hanami Long Skirt
                    ShopItem(itemId=3717, price=15, goldPrice=5, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Hanami Geta Shoes
                    ShopItem(itemId=2292, price=15, goldPrice=3, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Hanami Headpiece
                    ShopItem(itemId=377, price=25, goldPrice=5, color1=199, color2=199, itemType="Shirt"), # Cherryblossom Pink Hanami Top
                    ShopItem(itemId=636, price=5, goldPrice=1, color1=81, color2=81, itemType="Belt"), # Crimson Red Hanami Sash
                    ShopItem(itemId=1295, price=25, goldPrice=5, color1=199, color2=199, itemType="Skirt"), # Cherryblossom Pink Hanami Short Skirt
                    ShopItem(itemId=3717, price=15, goldPrice=3, color1=81, color2=81, itemType="Shoes"), # Crimson Red Hanami Geta Shoes
                    ShopItem(itemId=2449, price=15, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Azalea Barrette
                    ShopItem(itemId=1000074, price=25, goldPrice=5, color1=10, color2=10, itemType="Shirt"), # Cantaloupe Orange Azalea Top
                    ShopItem(itemId=1481, price=25, goldPrice=5, color1=10, color2=10, itemType="Skirt"), # Cantaloupe Orange Azalea Skirt
                    ShopItem(itemId=3866, price=15, goldPrice=3, color1=10, color2=10, itemType="Shoes"), # Cantaloupe Orange Azalea Sandals
                    ShopItem(itemId=385, price=25, goldPrice=5, color1=287, color2=287, itemType="Shirt"), # Dianthus Red Dianthus Blouse
                    ShopItem(itemId=1305, price=25, goldPrice=5, color1=287, color2=287, itemType="Skirt"), # Dianthus Red Dianthus Skirt
                    ShopItem(itemId=3722, price=15, goldPrice=3, color1=287, color2=287, itemType="Shoes"), # Dianthus Red Dianthus Shoes
                    ShopItem(itemId=2336, price=15, goldPrice=3, color1=186, color2=186, itemType="HeadItem"), # Honeycomb Yellow Flame Lily Barrette
                    ShopItem(itemId=417, price=25, goldPrice=5, color1=186, color2=186, itemType="Shirt"), # Honeycomb Yellow Flame Lily Top
                    ShopItem(itemId=1335, price=25, goldPrice=5, color1=186, color2=186, itemType="Skirt"), # Honeycomb Yellow Flame Lily Skirt
                    ShopItem(itemId=3758, price=15, goldPrice=3, color1=186, color2=186, itemType="Shoes"), # Honeycomb Yellow Flame Lily Shoes
                    ShopItem(itemId=2348, price=15, goldPrice=3, color1=130, color2=130, itemType="HeadItem"), # Orchid Pink Chrysanthemum Beret
                    ShopItem(itemId=477, price=25, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Chrysanthemum Top
                    ShopItem(itemId=640, price=5, goldPrice=1, color1=81, color2=81, itemType="Belt"), # Crimson Red Chrysanthemum Belt
                    ShopItem(itemId=1396, price=25, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Chrysanthemum Skirt
                    ShopItem(itemId=3779, price=15, goldPrice=3, color1=81, color2=81, itemType="Shoes"), # Crimson Red Chrysanthemum Shoes
                    ShopItem(itemId=2356, price=15, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Bead Cascade Earrings
                    ShopItem(itemId=483, price=25, goldPrice=5, color1=118, color2=118, itemType="Shirt"), # Sapphire Blue Camellia Top
                    ShopItem(itemId=1400, price=25, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Camellia Skirt
                    ShopItem(itemId=3782, price=15, goldPrice=3, color1=99, color2=99, itemType="Shoes"), # Papyrus Tan Camellia Boots
                    ShopItem(itemId=2386, price=15, goldPrice=3, color1=224, color2=153, itemType="HeadItem"), # Ivory White Snow Rose Barrettes with Frostbunny Blue Trim
                    ShopItem(itemId=1000024, price=25, goldPrice=5, color1=224, color2=153, itemType="Shirt"), # Ivory White Snow Rose Top with Frostbunny Blue Trim
                    ShopItem(itemId=1435, price=25, goldPrice=5, color1=153, color2=153, itemType="Skirt"), # Frostbunny Blue Snow Rose Skirt
                    ShopItem(itemId=3815, price=15, goldPrice=3, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Snow Rose Heels
                    ShopItem(itemId=2171, price=15, goldPrice=3, color1=211, color2=211, itemType="HeadItem"), # Gentian Purple Moth Orchid Headband
                    ShopItem(itemId=216, price=25, goldPrice=5, color1=51, color2=51, itemType="Shirt"), # Periwinkle Blue Moth Orchid Top
                    ShopItem(itemId=594, price=5, goldPrice=1, color1=211, color2=211, itemType="Belt"), # Gentian Purple Moth Orchid Leaf Sash
                    ShopItem(itemId=1183, price=25, goldPrice=5, color1=51, color2=51, itemType="Skirt"), # Periwinkle Blue Moth Orchid Bottom
                    ShopItem(itemId=3629, price=15, goldPrice=3, color1=51, color2=51, itemType="Shoes"), # Periwinkle Blue Moth Orchid Shoes
                    ShopItem(itemId=2172, price=15, goldPrice=3, color1=258, color2=258, itemType="HeadItem"), # Spearmint Green Dragon Arum Crown
                    ShopItem(itemId=217, price=25, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Dragon Arum Top
                    ShopItem(itemId=593, price=5, goldPrice=1, color1=258, color2=258, itemType="Belt"), # Spearmint Green Dragon Arum Sash
                    ShopItem(itemId=1185, price=15, goldPrice=3, color1=166, color2=166, itemType="Skirt"), # Snow White Dragon Arum Skirt
                    ShopItem(itemId=3630, price=15, goldPrice=3, color1=258, color2=258, itemType="Shoes"), # Spearmint Green Dragon Arum Shoes
                    ShopItem(itemId=2100, price=15, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Campanula Barrette
                    ShopItem(itemId=108, price=25, goldPrice=5, color1=153, color2=153, itemType="Shirt"), # Frostbunny Blue Campanula Top
                    ShopItem(itemId=1111, price=25, goldPrice=5, color1=153, color2=153, itemType="Skirt"), # Frostbunny Blue Campanula Skirt
                    ShopItem(itemId=3578, price=15, goldPrice=3, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Campanula Shoes
                    ShopItem(itemId=2120, price=15, goldPrice=3, color1=199, color2=199, itemType="HeadItem"), # Cherryblossom Pink Campis Barrette
                    ShopItem(itemId=109, price=25, goldPrice=5, color1=199, color2=199, itemType="Shirt"), # Cherryblossom Pink Campis Top
                    ShopItem(itemId=1121, price=25, goldPrice=5, color1=199, color2=199, itemType="Skirt"), # Cherryblossom Pink Campis Skirt
                    ShopItem(itemId=3579, price=15, goldPrice=3, color1=199, color2=199, itemType="Shoes"), # Cherryblossom Pink Campis Shoes
                    ShopItem(itemId=2123, price=15, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Lagerstroemia Hat
                    ShopItem(itemId=112, price=25, goldPrice=5, color1=152, color2=152, itemType="Shirt"), # Pale Purple Lagerstroemia Top
                    ShopItem(itemId=1124, price=25, goldPrice=5, color1=152, color2=152, itemType="Skirt"), # Pale Purple Lagerstroemia Skirt
                    ShopItem(itemId=3582, price=15, goldPrice=3, color1=152, color2=152, itemType="Shoes"), # Pale Purple Lagerstroemia Shoes
                    ShopItem(itemId=2586, price=5, goldPrice=1, color1=138, color2=138, itemType="Necklace"), # Persimmon Orange Marigold Necklace
                    ShopItem(itemId=333, price=25, goldPrice=5, color1=30, color2=30, itemType="Shirt"), # Pumpkin Orange Marigold Top
                    ShopItem(itemId=1270, price=25, goldPrice=5, color1=30, color2=30, itemType="Skirt"), # Pumpkin Orange Marigold Skirt
                    ShopItem(itemId=3695, price=15, goldPrice=3, color1=138, color2=0, itemType="Shoes"), # Persimmon Orange Marigold Shoes
                ],
            ),
            ShopCollection(
                collectionId=46, # Mainland Styles
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=1000031, price=25, goldPrice=5, color1=180, color2=180, itemType="Shirt"), # Seashell Blue Chic Tie-Dye Top
                    ShopItem(itemId=1442, price=25, goldPrice=5, color1=180, color2=180, itemType="Skirt"), # Seashell Blue Chic Tie-Dye Skirt
                    ShopItem(itemId=3822, price=15, goldPrice=3, color1=180, color2=180, itemType="Shoes"), # Seashell Blue Super Chic Sandals
                    ShopItem(itemId=1000037, price=25, goldPrice=5, color1=278, color2=278, itemType="Shirt"), # Aster Purple Fluttery Tie-Dye Top
                    ShopItem(itemId=1445, price=25, goldPrice=5, color1=278, color2=278, itemType="Skirt"), # Aster Purple Fluttery Tie-Dye Skirt
                    ShopItem(itemId=3822, price=15, goldPrice=3, color1=278, color2=278, itemType="Shoes"), # Aster Purple Super Chic Sandals
                    ShopItem(itemId=2423, price=15, goldPrice=3, color1=217, color2=217, itemType="HeadItem"), # Soft Gray Cute Cap
                    ShopItem(itemId=1000057, price=25, goldPrice=5, color1=217, color2=217, itemType="Shirt"), # Soft Gray Cardie Combo Top
                    ShopItem(itemId=1464, price=25, goldPrice=5, color1=217, color2=217, itemType="Skirt"), # Soft Gray Delightful Denim Skirt
                    ShopItem(itemId=3844, price=15, goldPrice=3, color1=217, color2=217, itemType="Shoes"), # Soft Gray Lovely Laceups
                    ShopItem(itemId=2634, price=5, goldPrice=1, color1=224, color2=224, itemType="Necklace"), # Ivory White Sweetheart Purse
                    ShopItem(itemId=1000055, price=25, goldPrice=5, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Sweetheart Top
                    ShopItem(itemId=650, price=5, goldPrice=1, color1=267, color2=267, itemType="Belt"), # Celestial Blue Sweetheart Sash
                    ShopItem(itemId=1463, price=25, goldPrice=5, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Sweetheart Skirt
                    ShopItem(itemId=3845, price=15, goldPrice=5, color1=162, color2=162, itemType="Shoes"), # Sunglow Yellow Sweetheart Sandals
                    ShopItem(itemId=2428, price=15, goldPrice=3, color1=135, color2=135, itemType="HeadItem"), # Boysenberry Purple Cute Cloud Earrings
                    ShopItem(itemId=1000061, price=25, goldPrice=5, color1=5, color2=5, itemType="Shirt"), # Wysteria Purple Rainy Day Top
                    ShopItem(itemId=1673, price=5, goldPrice=1, color1=135, color2=135, itemType="WristItem"), # Boysenberry Purple Rainbow Umbrella
                    ShopItem(itemId=1468, price=25, goldPrice=5, color1=5, color2=5, itemType="Skirt"), # Wysteria Purple Rainy Day Skirt
                    ShopItem(itemId=3850, price=15, goldPrice=3, color1=135, color2=135, itemType="Shoes"), # Boysenberry Purple Cozy Rain Boots
                    ShopItem(itemId=1000052, price=25, goldPrice=5, color1=81, color2=81, itemType="Shirt"), # Crimson Red Soft Knit Sweater
                    ShopItem(itemId=1459, price=25, goldPrice=5, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Pleasing Pleats Skirt
                    ShopItem(itemId=3840, price=15, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Sweet Spring Laceups
                    ShopItem(itemId=2636, price=5, goldPrice=1, color1=105, color2=105, itemType="Necklace"), #  Siltstone Tan Sweet Beaded Necklace
                    ShopItem(itemId=1000063, price=25, goldPrice=5, color1=44, color2=44, itemType="Shirt"), # Plumblossom Pink Sweet Spring Hoodie
                    ShopItem(itemId=1470, price=25, goldPrice=5, color1=126, color2=126, itemType="Skirt"), # Raindrop Blue Layered Look Skirt
                    ShopItem(itemId=3855, price=15, goldPrice=3, color1=55, color2=55, itemType="Shoes"), # Pepper Black Cat Flats
                    ShopItem(itemId=1000080, price=25, goldPrice=5, color1=44, color2=44, itemType="Shirt"), #  Plumblossom Pink Stylish Hoodie
                    ShopItem(itemId=1487, price=25, goldPrice=5, color1=44, color2=44, itemType="Skirt"), # Plumblossom Pink Springy Skirt
                    ShopItem(itemId=3871, price=15, goldPrice=3, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Perfect Plaid Loafers
                    ShopItem(itemId=2301, price=15, goldPrice=3, color1=11, color2=11, itemType="HeadItem"), # Marigold Yellow Folklorico Headband
                    ShopItem(itemId=386, price=25, goldPrice=5, color1=274, color2=274, itemType="Shirt"), # Bellflower Purple Folklorico Blouse
                    ShopItem(itemId=1306, price=25, goldPrice=5, color1=274, color2=274, itemType="Skirt"), # Bellflower Purple Folklorico Skirt
                    ShopItem(itemId=3726, price=15, goldPrice=3, color1=11, color2=11, itemType="Shoes"), # Marigold Yellow Folklorico Heels
                    ShopItem(itemId=1000114, price=25, goldPrice=5, color1=265, color2=265, itemType="Shirt"), # Bright Sky Blue Festive Floral Top
                    ShopItem(itemId=1001020, price=25, goldPrice=5, color1=265, color2=265, itemType="Skirt"), # Bright Sky Blue Festive Floral Skirt
                    ShopItem(itemId=3896, price=15, goldPrice=3, color1=17, color2=17, itemType="Shoes"), #  Tendershoot Green Pearl-Studded Sandals
                    ShopItem(itemId=1000122, price=25, goldPrice=5, color1=150, color2=150, itemType="Shirt"), # Dry Moss Green Summer Stripes Top
                    ShopItem(itemId=1001029, price=25, goldPrice=5, color1=150, color2=150, itemType="Skirt"), #  Dry Moss Green Summer Stripes Skirt
                    ShopItem(itemId=3904, price=15, goldPrice=3, color1=150, color2=150, itemType="Shoes"), # Dry Moss Green Summer Stripes Sandals
                    ShopItem(itemId=379, price=25, goldPrice=5, color1=189, color2=189, itemType="Shirt"), # Ladybug Red Breezy Ruffled Top
                    ShopItem(itemId=1299, price=25, goldPrice=5, color1=121, color2=121, itemType="Skirt"), # Daisy Pink Breezy Ruffled Skirt
                    ShopItem(itemId=3718, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Ruffle Detail Shoes
                    ShopItem(itemId=2474, price=15, goldPrice=3, color1=84, color2=84, itemType="HeadItem"), # Copper Brown Hiking Hat
                    ShopItem(itemId=1000108, price=25, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Hiking Gear
                    ShopItem(itemId=1001015, price=25, goldPrice=5, color1=29, color2=29, itemType="Skirt"), # Deep Sea Blue Hiking Shorts
                    ShopItem(itemId=3618, price=15, goldPrice=3, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Woodchucks
                    ShopItem(itemId=145, price=25, goldPrice=5, color1=159, color2=159, itemType="Shirt"), # Tea Green Sporty Top
                    ShopItem(itemId=1048, price=25, goldPrice=5, color1=159, color2=159, itemType="Skirt"), # Tea Green Sports Shorts
                    ShopItem(itemId=3504, price=15, goldPrice=3, color1=170, color2=170, itemType="Shoes"), # Olive Green Striders
                    ShopItem(itemId=2466, price=15, goldPrice=3, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Adventurer's Hat
                    ShopItem(itemId=1000112, price=25, goldPrice=5, color1=81, color2=81, itemType="Shirt"), # Crimson Red Adventurer Jacket
                    ShopItem(itemId=1001018, price=25, goldPrice=5, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Adventurer Leggings
                    ShopItem(itemId=3894, price=15, goldPrice=3, color1=81, color2=81, itemType="Shoes"), #  Crimson Red Adventurer's Boots
                    ShopItem(itemId=1000116, price=25, goldPrice=5, color1=203, color2=203, itemType="Shirt"), # Shadow Green Bold Summer Vest
                    ShopItem(itemId=1001022, price=25, goldPrice=5, color1=203, color2=203, itemType="Skirt"), # Shadow Green Bold Summer Skirt
                    ShopItem(itemId=3898, price=15, goldPrice=3, color1=91, color2=91, itemType="Shoes"), # Coconut Brown Bold Summer Boots
                    ShopItem(itemId=1000117, price=25, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Frills and Flounce Top
                    ShopItem(itemId=654, price=5, goldPrice=1, color1=286, color2=286, itemType="Belt"), #  Cherry Pink Striped Summer Sash
                    ShopItem(itemId=1001023, price=25, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Frills and Flounce Skirt
                    ShopItem(itemId=3673, price=15, goldPrice=5, color1=286, color2=286, itemType="Shoes"), # Cherry Pink Funky Wedges
                    ShopItem(itemId=294, price=25, goldPrice=5, color1=17, color2=17, itemType="Shirt"), #  Tendershoot Green Bow Sleeve Blouse
                    ShopItem(itemId=1338, price=25, goldPrice=5, color1=165, color2=165, itemType="Skirt"), # Spring Breeze Green Bow Belt Skirt
                    ShopItem(itemId=3626, price=15, goldPrice=3, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Ruffly Slippers
                    ShopItem(itemId=96, price=25, goldPrice=5, color1=121, color2=121, itemType="Shirt"), # Daisy Pink I-Heart-Mermaids Tee
                    ShopItem(itemId=1186, price=25, goldPrice=5, color1=121, color2=121, itemType="Skirt"), # Daisy Pink Ruffle Skirt
                    ShopItem(itemId=3619, price=15, goldPrice=3, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Sparkly Slippers
                    ShopItem(itemId=2306, price=15, goldPrice=3, color1=189, color2=189, itemType="HeadItem"), # Ladybug Red Sunny Style Hat
                    ShopItem(itemId=394, price=25, goldPrice=5, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Sunny Style Top
                    ShopItem(itemId=1315, price=25, goldPrice=5, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Sunny Style Skirt
                    ShopItem(itemId=3734, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Sunny Style Boots
                    ShopItem(itemId=2084, price=15, goldPrice=3, color1=75, color2=75, itemType="HeadItem"), # Umber Brown Darling Fairy Crown
                    ShopItem(itemId=2531, price=5, goldPrice=1, color1=84, color2=84, itemType="Necklace"), # Copper Brown Darling Fairy Necklace
                    ShopItem(itemId=88, price=25, goldPrice=5, color1=84, color2=84, itemType="Shirt"), # Copper Brown Darling Fairy Combo Top
                    ShopItem(itemId=1089, price=25, goldPrice=5, color1=75, color2=75, itemType="Skirt"), # Umber Brown Darling Dance Drape
                    ShopItem(itemId=3565, price=15, goldPrice=3, color1=84, color2=84, itemType="Shoes"), # Copper Brown Darling Fairy Boots
                    ShopItem(itemId=2208, price=15, goldPrice=3, color1=78, color2=78, itemType="HeadItem"), #  Fawn Brown Nifty Knit Hat
                    ShopItem(itemId=320, price=25, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Carefree Sweater Top with Yellow Trim
                    ShopItem(itemId=1259, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Casual Crops with Light Blue Trim
                    ShopItem(itemId=3673, price=15, goldPrice=3, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Funky Wedges
                    ShopItem(itemId=2392, price=15, goldPrice=3, color1=269, color2=269, itemType="HeadItem"), # Crisp White Knit Beret
                    ShopItem(itemId=1000025, price=25, goldPrice=5, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Fluffy Puffer Top
                    ShopItem(itemId=1436, price=25, goldPrice=5, color1=215, color2=215, itemType="Skirt"), # Pewter Gray Cozy Stripes Skirt
                    ShopItem(itemId=3816, price=15, goldPrice=3, color1=207, color2=207, itemType="Shoes"), # Diamond Blue Fuzzy Ankle Boots
                    ShopItem(itemId=2310, price=15, goldPrice=3, color1=275, color2=275, itemType="HeadItem"), # Shadowy Purple Flower Knit Headwrap
                    ShopItem(itemId=1000023, price=25, goldPrice=5, color1=275, color2=275, itemType="Shirt"), # Shadowy Purple Neat Knit Top
                    ShopItem(itemId=1434, price=25, goldPrice=5, color1=275, color2=275, itemType="Skirt"), # Shadowy Purple Neat Knit Skirt
                    ShopItem(itemId=3814, price=15, goldPrice=3, color1=275, color2=275, itemType="Shoes"), # Shadowy Purple Coziest Boots
                ],
            ),
            ShopCollection(
                collectionId=84, # Themed Fashions
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2403, price=15, goldPrice=3, color1=18, color2=18, itemType="HeadItem"), # Waterfall Blue Northern Lights Tiara
                    ShopItem(itemId=2629, price=5, goldPrice=1, color1=152, color2=152, itemType="Necklace"), # Pale Purple Northern Lights Necklace
                    ShopItem(itemId=1000036, price=25, goldPrice=5, color1=18, color2=18, itemType="Shirt"), # Waterfall Blue Northern Lights Top
                    ShopItem(itemId=1444, price=25, goldPrice=5, color1=18, color2=18, itemType="Skirt"), # Waterfall Blue Northern Lights Skirt
                    ShopItem(itemId=3824, price=15, goldPrice=3, color1=18, color2=18, itemType="Shoes"), # Waterfall Blue Northern Lights Heels
                    ShopItem(itemId=2285, price=15, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Sweet Baker Hat
                    ShopItem(itemId=2591, price=5, goldPrice=1, color1=44, color2=44, itemType="Necklace"), # Plumblossom Pink Sweet Bow
                    ShopItem(itemId=344, price=25, goldPrice=5, color1=200, color2=200, itemType="Shirt"), # Ruby Pink Sweet Puff Top
                    ShopItem(itemId=631, price=5, goldPrice=1, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Sweet Bow Sash
                    ShopItem(itemId=1281, price=25, goldPrice=5, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Sweet Puff Skirt
                    ShopItem(itemId=3705, price=15, goldPrice=3, color1=200, color2=200, itemType="Shoes"), # Ruby Pink Sweet Bow Shoes
                    ShopItem(itemId=2101, price=15, goldPrice=3, color1=265, color2=265, itemType="HeadItem"), # Bright Sky Blue Straw and Blueberry Hat
                    ShopItem(itemId=248, price=25, goldPrice=5, color1=137, color2=137, itemType="Shirt"), # Lemon Yellow Serving-Talent Blouse
                    ShopItem(itemId=571, price=5, goldPrice=1, color1=45, color2=265, itemType="Belt"), # Strawberry Red Simple Apron with Bright Sky Blue Trim
                    ShopItem(itemId=1208, price=25, goldPrice=5, color1=265, color2=265, itemType="Skirt"), # Bright Sky Blue Tea-Brewer Skirt
                    ShopItem(itemId=3570, price=15, goldPrice=5, color1=265, color2=265, itemType="Shoes"), # Bright Sky Blue Really Rainy Boots
                    ShopItem(itemId=2438, price=15, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Carnival Chic Top Hat
                    ShopItem(itemId=1000075, price=25, goldPrice=5, color1=121, color2=121, itemType="Shirt"), # Daisy Pink Carnival Chic Top
                    ShopItem(itemId=1482, price=25, goldPrice=5, color1=239, color2=239, itemType="Skirt"), # Coffee Black Carnival Chic Skirt
                    ShopItem(itemId=3867, price=15, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Carnival Chic Boots
                    ShopItem(itemId=1000072, price=25, goldPrice=5, color1=111, color2=111, itemType="Shirt"), # Sparkling Yellow Siren Style Top
                    ShopItem(itemId=1478, price=25, goldPrice=5, color1=225, color2=225, itemType="Skirt"), # Eggplant Purple Siren Style Skirt
                    ShopItem(itemId=3863, price=15, goldPrice=3, color1=225, color2=225, itemType="Shoes"), # Eggplant Purple Siren Style Sandals
                    ShopItem(itemId=1000113, price=25, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Parrot Party Top
                    ShopItem(itemId=1001019, price=25, goldPrice=5, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Parrot Party Skirt
                    ShopItem(itemId=3895, price=15, goldPrice=3, color1=159, color2=159, itemType="Shoes"), # Tea Green Parrot Party Heels
                    ShopItem(itemId=1000111, price=25, goldPrice=5, color1=204, color2=204, itemType="Shirt"), # Bamboo Green Sorceress Dress Top
                    ShopItem(itemId=1001017, price=25, goldPrice=5, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Sorceress Dress Skirt
                    ShopItem(itemId=3893, price=15, goldPrice=3, color1=205, color2=205, itemType="Shoes"), # Myrtle Green Sorceress Heels
                    ShopItem(itemId=2299, price=15, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Flaptastic Cloche
                    ShopItem(itemId=383, price=25, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Flaptastic Top
                    ShopItem(itemId=1303, price=25, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Flaptastic Skirt
                    ShopItem(itemId=3721, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Flaptastic Shoes
                    ShopItem(itemId=2608, price=5, goldPrice=1, color1=110, color2=110, itemType="Necklace"), # Rosy Pink Sock Hop Scarf
                    ShopItem(itemId=399, price=25, goldPrice=5, color1=26, color2=26, itemType="Shirt"), # Raspberry Pink Sock Hop Top
                    ShopItem(itemId=1322, price=25, goldPrice=5, color1=26, color2=26, itemType="Skirt"), # Raspberry Pink Sock Hop Skirt
                    ShopItem(itemId=3746, price=15, goldPrice=3, color1=110, color2=110, itemType="Shoes"), # Rosy Pink Sock Hop Shoes
                    ShopItem(itemId=2111, price=15, goldPrice=3, color1=75, color2=75, itemType="HeadItem"), # Umber Brown Tiger Lily Head Piece
                    ShopItem(itemId=117, price=25, goldPrice=5, color1=75, color2=75, itemType="Shirt"), # Umber Brown Tiger Lily Top
                    ShopItem(itemId=1114, price=25, goldPrice=5, color1=75, color2=75, itemType="Skirt"), # Umber Brown Tassel Skirt
                    ShopItem(itemId=3585, price=15, goldPrice=3, color1=265, color2=265, itemType="Shoes"), # Bright Sky Blue Fire Dance Moccasins
                    ShopItem(itemId=341, price=25, goldPrice=5, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Top 40 Jacket
                    ShopItem(itemId=1619, price=5, goldPrice=1, color1=8, color2=8, itemType="WristItem"), # Watermelon Pink Sassy Glove
                    ShopItem(itemId=1278, price=25, goldPrice=5, color1=29, color2=29, itemType="Skirt"), # Deep Sea Blue Top 40 Pants
                    ShopItem(itemId=3702, price=15, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Top 40 Sneakers
                    ShopItem(itemId=342, price=25, goldPrice=5, color1=239, color2=239, itemType="Shirt"), # Coffee Black Rock n' Roll Top
                    ShopItem(itemId=628, price=5, goldPrice=1, color1=239, color2=239, itemType="Belt"), # Coffee Black Rock n' Roll Chain Belt
                    ShopItem(itemId=1620, price=5, goldPrice=1, color1=239, color2=239, itemType="WristItem"), # Coffee Black Rock n' Roll Cuff
                    ShopItem(itemId=1279, price=25, goldPrice=5, color1=239, color2=239, itemType="Skirt"), # Coffee Black Rock n' Roll Skirt
                    ShopItem(itemId=3703, price=15, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Rock n' Roll Boots
                    ShopItem(itemId=2280, price=15, goldPrice=3, color1=286, color2=286, itemType="HeadItem"), # Cherry Pink Far Out Funky Earrings
                    ShopItem(itemId=339, price=25, goldPrice=5, color1=286, color2=286, itemType="Shirt"), # Cherry Pink Like, Totally! Top
                    ShopItem(itemId=1276, price=25, goldPrice=5, color1=229, color2=229, itemType="Skirt"), # Electric Indigo Radical Tutu
                    ShopItem(itemId=3701, price=15, goldPrice=3, color1=229, color2=229, itemType="Shoes"), # Electric Indigo Leg Warmer Shoes
                    ShopItem(itemId=399, price=25, goldPrice=5, color1=195, color2=195, itemType="Shirt"), # Electric Blue Sock Hop Top
                    ShopItem(itemId=1274, price=25, goldPrice=5, color1=226, color2=226, itemType="Skirt"), # Goldenrod Yellow Silly Tutu
                    ShopItem(itemId=3699, price=15, goldPrice=3, color1=226, color2=226, itemType="Shoes"), # Goldenrod Yellow Polka-Stripe Socks
                    ShopItem(itemId=2177, price=15, goldPrice=3, color1=70, color2=70, itemType="HeadItem"), # Tinker Blue Teatime Hat
                    ShopItem(itemId=250, price=25, goldPrice=5, color1=70, color2=70, itemType="Shirt"), # Tinker Blue Light and Lacy Tea Top
                    ShopItem(itemId=611, price=5, goldPrice=1, color1=166, color2=166, itemType="Belt"), # Snow White Light and Lacy Sash
                    ShopItem(itemId=1209, price=25, goldPrice=5, color1=70, color2=70, itemType="Skirt"), # Tinker Blue Light and Lacy Tea Skirt
                    ShopItem(itemId=3644, price=15, goldPrice=5, color1=70, color2=70, itemType="Shoes"), # Tinker Blue Light and Lacy Boots
                    ShopItem(itemId=2188, price=15, goldPrice=3, color1=44, color2=182, itemType="HeadItem"), # Plumblossom Pink Serving-Talent Hat with Twilight Blue Trim
                    ShopItem(itemId=248, price=25, goldPrice=5, color1=159, color2=182, itemType="Shirt"), # Tea Green Serving-Talent Blouse with Twilight Blue Trim
                    ShopItem(itemId=609, price=5, goldPrice=1, color1=182, color2=182, itemType="Belt"), #  Twilight Blue Serving-Talent Sash
                    ShopItem(itemId=1207, price=25, goldPrice=5, color1=159, color2=159, itemType="Skirt"), # Tea Green Serving-Talent Skirt
                    ShopItem(itemId=3696, price=15, goldPrice=5, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Petal Slippers
                    ShopItem(itemId=2176, price=15, goldPrice=3, color1=111, color2=111, itemType="HeadItem"), # Sparkling Yellow Tea-Brewer Cap
                    ShopItem(itemId=249, price=25, goldPrice=5, color1=130, color2=130, itemType="Shirt"), # Orchid Pink Tea-Brewer Top
                    ShopItem(itemId=610, price=5, goldPrice=1, color1=111, color2=111, itemType="Belt"), # Sparkling Yellow Tea-Brewer Apron
                    ShopItem(itemId=1208, price=25, goldPrice=5, color1=111, color2=111, itemType="Skirt"), # Sparkling Yellow Tea-Brewer Skirt
                    ShopItem(itemId=3696, price=15, goldPrice=5, color1=130, color2=130, itemType="Shoes"), # Orchid Pink Petal Slippers
                    ShopItem(itemId=2157, price=15, goldPrice=3, color1=166, color2=189, itemType="HeadItem"), # Snow White Baking Hat with Ladybug Red Trim
                    ShopItem(itemId=93, price=25, goldPrice=5, color1=189, color2=189, itemType="Shirt"), # Ladybug Red Desert Adventure Top
                    ShopItem(itemId=571, price=5, goldPrice=1, color1=45, color2=45, itemType="Belt"), # Strawberry Red Simple Apron
                    ShopItem(itemId=1520, price=5, goldPrice=1, color1=45, color2=166, itemType="WristItem"), # Strawberry Red Oven Mitt with Snow White Trim
                    ShopItem(itemId=1017, price=25, goldPrice=5, color1=205, color2=205, itemType="Skirt"), # Myrtle Green Grass Petal Pushers
                    ShopItem(itemId=3515, price=15, goldPrice=5, color1=189, color2=189, itemType="Shoes"), # Ladybug Red Pea Pod Slippers
                ],
            ),
            ShopCollection(
                collectionId=95, # Princess Fashion
                currencyId=FairiesConstants.MAPLE_LEAVES,
                items=[
                    ShopItem(itemId=2217, price=15, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Princess Headband
                    ShopItem(itemId=297, price=25, goldPrice=5, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Poufy Princess Top
                    ShopItem(itemId=1247, price=25, goldPrice=5, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Poufy Princess Skirt
                    ShopItem(itemId=3675, price=15, goldPrice=3, color1=149, color2=149, itemType="Shoes"), # Snowflake Blue Glittering Glass Slippers
                    ShopItem(itemId=2282, price=15, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Blossoming Rose Headband
                    ShopItem(itemId=340, price=25, goldPrice=5, color1=227, color2=227, itemType="Shirt"), # Moonlight Gray Dreamy Meadow Blouse
                    ShopItem(itemId=1277, price=25, goldPrice=5, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Dreamy Meadow Skirt
                    ShopItem(itemId=3696, price=15, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Splendid Petal Slippers
                    ShopItem(itemId=2397, price=15, goldPrice=3, color1=110, color2=110, itemType="HeadItem"), # Rosy Pink Lovely Blooms Crown
                    ShopItem(itemId=1000038, price=25, goldPrice=5, color1=52, color2=52, itemType="Shirt"), # Lavender Purple Lovely Blooms Top
                    ShopItem(itemId=1662, price=5, goldPrice=1, color1=116, color2=116, itemType="WristItem"), # Mushroom White Lovely Blooms Lantern
                    ShopItem(itemId=1446, price=25, goldPrice=5, color1=52, color2=52, itemType="Skirt"), # Lavender Purple Lovely Blooms Skirt
                    ShopItem(itemId=3826, price=15, goldPrice=3, color1=52, color2=52, itemType="Shoes"), # Lavender Purple Lovely Blooms Heels
                    ShopItem(itemId=2607, price=5, goldPrice=1, color1=69, color2=69, itemType="Necklace"), # Powder Blue Summer Breeze Necklace
                    ShopItem(itemId=397, price=25, goldPrice=5, color1=191, color2=191, itemType="Shirt"), # Vidia Black Summer Breeze Top
                    ShopItem(itemId=1640, price=5, goldPrice=1, color1=49, color2=49, itemType="WristItem"), # Robin Egg Blue Summer Breeze Bangles
                    ShopItem(itemId=1319, price=25, goldPrice=5, color1=191, color2=191, itemType="Skirt"), # Vidia Black Summer Breeze Pants
                    ShopItem(itemId=3745, price=15, goldPrice=3, color1=49, color2=49, itemType="Shoes"), # Robin Egg Blue Summer Moccassins
                    ShopItem(itemId=2323, price=15, goldPrice=3, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Apple Headband
                    ShopItem(itemId=2585, price=5, goldPrice=1, color1=113, color2=113, itemType="Necklace"), # Pale Rose Red Fairy Friends Necklace
                    ShopItem(itemId=398, price=25, goldPrice=5, color1=38, color2=38, itemType="Shirt"), # Apple Green Wishing Apple Top
                    ShopItem(itemId=1320, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Wishing Apple Skirt
                    ShopItem(itemId=3696, price=15, goldPrice=3, color1=38, color2=38, itemType="Shoes"), # Apple Green Splendid Petal Slippers
                ],
            ),
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
                    ShopItem(itemId=1651, price=10, goldPrice=2, color1=78, color2=78, itemType="WristItem"), # Fawn Brown Football
                    ShopItem(itemId=1172, price=25, goldPrice=5, color1=118, color2=118, itemType="Skirt") # Sapphire Blue Dry Leaf Trousers
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
            ShopCollection(
                collectionId=1, # Rapid Racer - Fairies
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=2219, price=10, goldPrice=4, color1=191, color2=191, itemType="HeadItem"), # Vidia Black Racing Goggles
                    ShopItem(itemId=302, price=18, goldPrice=7, color1=129, color2=129, itemType="Shirt"), # Fig Purple Rapid Racer Top
                    ShopItem(itemId=1264, price=18, goldPrice=7, color1=129, color2=129, itemType="Skirt"), # Fig Purple Rapid Racer Knickers
                    ShopItem(itemId=3678, price=13, goldPrice=5, color1=72, color2=72, itemType="Shoes"), # Mauve Purple Riding Boots

                    ShopItem(itemId=2219, price=10, goldPrice=4, color1=55, color2=55, itemType="HeadItem"), # Pepper Black Racing Goggles
                    ShopItem(itemId=302, price=18, goldPrice=7, color1=48, color2=48, itemType="Shirt"), # Sea Green Rapid Racer Top
                    ShopItem(itemId=1264, price=18, goldPrice=7, color1=41, color2=41, itemType="Skirt"), # Moonshadow Blue Rapid Racer Knickers
                    ShopItem(itemId=3678, price=13, goldPrice=5, color1=48, color2=48, itemType="Shoes"), # Sea Green Riding Boots 
                ],
            ),
            ShopCollection(
                collectionId=42, # Rapid Racer - Sparrows
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=2225, price=10, goldPrice=4, color1=55, color2=55, itemType="HeadItem"), # Pepper Black Racing Goggles
                    ShopItem(itemId=306, price=18, goldPrice=7, color1=48, color2=48, itemType="Shirt"), # Sea Green Rapid Racer Top
                    ShopItem(itemId=1255, price=18, goldPrice=7, color1=41, color2=41, itemType="Skirt"), # Moonshadow Blue Rapid Racer Knickers
                    ShopItem(itemId=3681, price=13, goldPrice=5, color1=55, color2=48, itemType="Shoes"), # Pepper Black Riding Boots with Sea Green Trim

                    ShopItem(itemId=2225, price=10, goldPrice=4, color1=191, color2=191, itemType="HeadItem"), # Vidia Black Racing Goggles
                    ShopItem(itemId=306, price=18, goldPrice=7, color1=189, color2=189, itemType="Shirt"), # Ladybug Red Rapid Racer Top
                    ShopItem(itemId=1255, price=18, goldPrice=7, color1=191, color2=191, itemType="Skirt"), # Vidia Black Rapid Racer Knickers
                    ShopItem(itemId=3681, price=13, goldPrice=5, color1=75, color2=75, itemType="Shoes"), # Umber Brown Riding Boots
                ],
            ),
            ShopCollection(
                collectionId=69, # Super Speedster - Fairies
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=323, price=18, goldPrice=5, color1=8, color2=8, itemType="Shirt"), # Watermelon Pink Super Speedster Jacket
                    ShopItem(itemId=1263, price=18, goldPrice=7, color1=8, color2=8, itemType="Skirt"), # Watermelon Pink Super Speedster Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=81, color2=81, itemType="Shoes"), # Crimson Red Finish Line Shoes

                    ShopItem(itemId=323, price=18, goldPrice=7, color1=151, color2=151, itemType="Shirt"), # Peanut Yellow Super Speedster Jacket
                    ShopItem(itemId=1263, price=18, goldPrice=7, color1=151, color2=151, itemType="Skirt"), # Peanut Yellow Super Speedster Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=151, color2=151, itemType="Shoes"), # Peanut Yellow Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=70, # Super Speedster - Sparrow
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=318, price=18, goldPrice=7, color1=74, color2=74, itemType="Shirt"), # Soil Brown Super Speedster Jacket
                    ShopItem(itemId=1257, price=18, goldPrice=7, color1=74, color2=74, itemType="Skirt"), # Soil Brown Super Speedster Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=74, color2=74, itemType="Shoes"), # Soil Brown Finish Line Shoes

                    ShopItem(itemId=318, price=18, goldPrice=7, color1=172, color2=172, itemType="Shirt"), # Forest Green Super Speedster Jacket
                    ShopItem(itemId=1257, price=18, goldPrice=7, color1=125, color2=125, itemType="Skirt"), # Pine Green Super Speedster Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=125, color2=125, itemType="Shoes"), # Pine Green Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=71, # Fast Flash Racer - Fairies
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=322, price=18, goldPrice=7, color1=130, color2=130, itemType="Shirt"), # Orchid Pink Fast Flash Racing Top
                    ShopItem(itemId=1260, price=18, goldPrice=7, color1=130, color2=130, itemType="Skirt"), # Orchid Pink Fast Flash Racing Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=181, color2=181, itemType="Shoes"), # Cupcake Pink Finish Line Shoes

                    ShopItem(itemId=322, price=18, goldPrice=7, color1=24, color2=24, itemType="Shirt"), # Sky Blue Fast Flash Racing Top
                    ShopItem(itemId=1260, price=18, goldPrice=7, color1=24, color2=24, itemType="Skirt"), # Sky Blue Fast Flash Racing Pants
                    ShopItem(itemId=3685, price=13, goldPrice=5, color1=185, color2=185, itemType="Shoes"), # Midnight Blue Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=72, # Fast Flash Racer - Sparrow
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=319, price=18, goldPrice=7, color1=24, color2=24, itemType="Shirt"), # Sky Blue Fast Flash Racing Top
                    ShopItem(itemId=1258, price=18, goldPrice=7, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Fast Flash Racing Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=185, color2=185, itemType="Shoes"), # Midnight Blue Finish Line Shoes

                    ShopItem(itemId=319, price=18, goldPrice=7, color1=12, color2=12, itemType="Shirt"), # Tangerine Orange Fast Flash Racing Top
                    ShopItem(itemId=1258, price=18, goldPrice=7, color1=138, color2=138, itemType="Skirt"), # Persimmon Orange Fast Flash Racing Pants
                    ShopItem(itemId=3686, price=13, goldPrice=5, color1=138, color2=138, itemType="Shoes"), # Persimmon Orange Finish Line Shoes
                ],
            ),
            ShopCollection(
                collectionId=18, # Riding Helmets
                currencyId=FairiesConstants.ROSE_PETALS,
                items=[
                    ShopItem(itemId=2223, price=8, goldPrice=3, color1=105, color2=105, itemType="HeadItem"), # Siltstone Tan Walnut Shell Helmet
                    ShopItem(itemId=2223, price=8, goldPrice=3, color1=61, color2=61, itemType="HeadItem"), # Pale Lilac Purple Walnut Shell Helmet
                    ShopItem(itemId=2220, price=13, goldPrice=5, color1=52, color2=52, itemType="HeadItem"), # Lavender Purple Rapid Racer Helmet
                    ShopItem(itemId=2220, price=13, goldPrice=5, color1=48, color2=48, itemType="HeadItem"), # Sea Green Rapid Racer Helmet
                    ShopItem(itemId=2242, price=13, goldPrice=5, color1=130, color2=130, itemType="HeadItem"), # Orchid Pink Vintage Racer Helmet
                    ShopItem(itemId=2242, price=13, goldPrice=5, color1=24, color2=24, itemType="HeadItem"), # Sky Blue Vintage Racer Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=151, color2=151, itemType="HeadItem"), # Peanut Yellow Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=172, color2=172, itemType="HeadItem"), # Forest Green Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=74, color2=74, itemType="HeadItem"), # Soil Brown Dustkicker Helmet
                    # Sparrows \/
                    ShopItem(itemId=2229, price=8, goldPrice=3, color1=105, color2=105, itemType="HeadItem"), # Siltstone Tan Walnut Shell Helmet
                    ShopItem(itemId=2229, price=8, goldPrice=3, color1=61, color2=61, itemType="HeadItem"), # Pale Lilac Purple Walnut Shell Helmet
                    ShopItem(itemId=2226, price=13, goldPrice=5, color1=48, color2=48, itemType="HeadItem"), # Sea Green Rapid Racer Helmet
                    ShopItem(itemId=2226, price=13, goldPrice=5, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Rapid Racer Helmet
                    ShopItem(itemId=2244, price=13, goldPrice=5, color1=24, color2=24, itemType="HeadItem"), # Sky Blue Vintage Racer Helmet
                    ShopItem(itemId=2244, price=13, goldPrice=5, color1=12, color2=12, itemType="HeadItem"), # Tangerine Orange Vintage Racer Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=151, color2=151, itemType="HeadItem"), # Peanut Yellow Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=172, color2=172, itemType="HeadItem"), # Forest Green Dustkicker Helmet
                    ShopItem(itemId=2243, price=13, goldPrice=5, color1=74, color2=74, itemType="HeadItem"), # Soil Brown Dustkicker Helmet
                ],
            ),
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
