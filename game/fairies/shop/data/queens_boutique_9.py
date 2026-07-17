from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.QUEENS_BOUTIQUE,
    shopId=9,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.ERICA,
        position=(417, 455),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_ERICA
    ),
    collections=[
        ShopCollection(
            collectionId=2, # The Queen's Collections (Red)
            outfits=[
                ShopOutfit(
                    outfitId=1000, # Ravishing Rosette Gown
                    items=[
                        OutfitItem(itemId=2357, goldPrice=75, itemType="HeadItem"),
                        OutfitItem(itemId=486, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1402, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=643, goldPrice=0, itemType="Belt"),
                        OutfitItem(itemId=3784, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1001, # Chic Crimson Gown
                    items=[
                        OutfitItem(itemId=487, goldPrice=80, itemType="Shirt"),
                        OutfitItem(itemId=1403, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3785, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1002, # Resplendent Ruby Gown
                    items=[
                        OutfitItem(itemId=2376, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=1000002, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1416, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3803, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1003, # Blooming Couture Gown
                    items=[
                        OutfitItem(itemId=2408, goldPrice=120, itemType="HeadItem"),
                        OutfitItem(itemId=1000041, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1449, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3829, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1004, # Princess of Hearts Gown
                    items=[
                        OutfitItem(itemId=2453, goldPrice=150, itemType="HeadItem"),
                        OutfitItem(itemId=1000095, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001003, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3880, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1005, # Bewitching Blossoms Gown
                    items=[
                        OutfitItem(itemId=2454, goldPrice=140, itemType="HeadItem"),
                        OutfitItem(itemId=1000096, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001004, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3881, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1006, # Flowing Floral Gown
                    items=[
                        OutfitItem(itemId=2463, goldPrice=130, itemType="HeadItem"),
                        OutfitItem(itemId=1000106, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001014, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3890, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        ),
        ShopCollection(
            collectionId=106, # The Queen's Collections (Orange)
            outfits=[
                ShopOutfit(
                    outfitId=1007, # Delicate Dahlia Gown
                    items=[
                        OutfitItem(itemId=2329, goldPrice=85, itemType="HeadItem"),
                        OutfitItem(itemId=410, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1325, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3752, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1008, # Perfect Peacock Gown
                    items=[
                        OutfitItem(itemId=2378, goldPrice=100, itemType="HeadItem"),
                        OutfitItem(itemId=1000014, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1428, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3805, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1009, # Autumn Couture Gown
                    items=[
                        OutfitItem(itemId=2380, goldPrice=100, itemType="HeadItem"),
                        OutfitItem(itemId=1000016, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1430, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3807, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1010, # Critterific Couture
                    items=[
                        OutfitItem(itemId=2409, goldPrice=130, itemType="HeadItem"),
                        OutfitItem(itemId=1000042, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1450, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3830, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1011, # Sensational Sparkle Gown
                    items=[
                        OutfitItem(itemId=2436, goldPrice=130, itemType="HeadItem"),
                        OutfitItem(itemId=1000071, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1479, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3864, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1012, # Autumn Revelry Gown
                    items=[
                        OutfitItem(itemId=2460, goldPrice=140, itemType="HeadItem"),
                        OutfitItem(itemId=1000103, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001011, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3887, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1013, # Savannah Sunset Gown
                    items=[
                        OutfitItem(itemId=2471, goldPrice=140, itemType="HeadItem"),
                        OutfitItem(itemId=1000119, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001026, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3901, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1014, # Perfect Poinsettia Gown
                    items=[
                        OutfitItem(itemId=2458, goldPrice=140, itemType="HeadItem"),
                        OutfitItem(itemId=1000100, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001008, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3885, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        ),
        ShopCollection(
            collectionId=108, # The Queen's Collections (Yellow)
            outfits=[
                ShopOutfit(
                    outfitId=1015, # Soverign Hearts Gown
                    items=[
                        OutfitItem(itemId=2451, goldPrice=160, itemType="HeadItem"),
                        OutfitItem(itemId=2641, goldPrice=0, itemType="Necklace"),
                        OutfitItem(itemId=1000093, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001001, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=1683, goldPrice=0, itemType="WristItem"),
                        OutfitItem(itemId=3878, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1016, # Sublime Splendor Gown
                    items=[
                        OutfitItem(itemId=2307, goldPrice=85, itemType="HeadItem"),
                        OutfitItem(itemId=392, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1314, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3731, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1017, # Gilded Glamour Gown
                    items=[
                        OutfitItem(itemId=2332, goldPrice=80, itemType="HeadItem"),
                        OutfitItem(itemId=412, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1331, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3754, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1018, # Golden Flutter Gown
                    items=[
                        OutfitItem(itemId=2430, goldPrice=120, itemType="HeadItem"),
                        OutfitItem(itemId=1000064, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1471, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3856, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1019, # Royal Couture Gown
                    items=[
                        OutfitItem(itemId=2432, goldPrice=150, itemType="HeadItem"),
                        OutfitItem(itemId=1000066, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1473, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3858, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1020, # Radiant Rosebud Gown
                    items=[
                        OutfitItem(itemId=2433, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=1000068, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1475, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3860, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1021, # Golden Roses Gown
                    items=[
                        OutfitItem(itemId=2298, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=384, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1304, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3720, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1022, # Vivacious Vines Gown
                    items=[
                        OutfitItem(itemId=2328, goldPrice=85, itemType="HeadItem"),
                        OutfitItem(itemId=409, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1328, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3751, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        ),
        ShopCollection(
            collectionId=109, # The Queen's Collections (Green)
            outfits=[
                ShopOutfit(
                    outfitId=1023, # Emerald Dreams Gown
                    items=[
                        OutfitItem(itemId=395, goldPrice=70, itemType="Shirt"),
                        OutfitItem(itemId=1316, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3735, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1024, # Fanciful Feathers Gown
                    items=[
                        OutfitItem(itemId=2381, goldPrice=90, itemType="HeadItem"),
                        OutfitItem(itemId=1000017, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1431, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3808, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1025, # Tinkered Couture
                    items=[
                        OutfitItem(itemId=2395, goldPrice=130, itemType="HeadItem"),
                        OutfitItem(itemId=2625, goldPrice=0, itemType="Necklace"),
                        OutfitItem(itemId=1000029, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1440, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3820, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1026, # Feathered Fringe Gown
                    items=[
                        OutfitItem(itemId=2459, goldPrice=140, itemType="HeadItem"),
                        OutfitItem(itemId=2642, goldPrice=0, itemType="Necklace"),
                        OutfitItem(itemId=1000101, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001009, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3886, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1027, # Alluring Artisan Gown
                    items=[
                        OutfitItem(itemId=2470, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=2644, goldPrice=0, itemType="Necklace"),
                        OutfitItem(itemId=1000118, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001025, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3900, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1028, # Chic Sari
                    items=[
                        OutfitItem(itemId=2473, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=1000121, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001028, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3903, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1029, # Splendid Solstice Gown
                    items=[
                        OutfitItem(itemId=2407, goldPrice=140, itemType="HeadItem"),
                        OutfitItem(itemId=1000040, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1448, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3825, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        ),
        ShopCollection(
            collectionId=114, # The Queen's Collections (Blue)
            outfits=[
                ShopOutfit(
                    outfitId=1030, # Fine Flowing Gown
                    items=[
                        OutfitItem(itemId=387, goldPrice=75, itemType="Shirt"),
                        OutfitItem(itemId=1313, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3730, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1031, # Grand and Graceful Gown
                    items=[
                        OutfitItem(itemId=391, goldPrice=70, itemType="Shirt"),
                        OutfitItem(itemId=1307, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3729, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1032, # Stunning Seafoam Gown
                    items=[
                        OutfitItem(itemId=2333, goldPrice=90, itemType="HeadItem"),
                        OutfitItem(itemId=413, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1332, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3755, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1033, # Gossamer Gown
                    items=[
                        OutfitItem(itemId=2334, goldPrice=85, itemType="HeadItem"),
                        OutfitItem(itemId=414, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1333, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3756, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1034, # Spectacular Swirl
                    items=[
                        OutfitItem(itemId=2379, goldPrice=95, itemType="HeadItem"),
                        OutfitItem(itemId=1000015, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1429, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3806, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1035, # Smashing Splash Gown
                    items=[
                        OutfitItem(itemId=2393, goldPrice=70, itemType="HeadItem"),
                        OutfitItem(itemId=1000027, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1438, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3818, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1036, # Winter Couture Gown
                    items=[
                        OutfitItem(itemId=2405, goldPrice=115, itemType="HeadItem"),
                        OutfitItem(itemId=1000039, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1447, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3828, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1037, # Pretty Panache Gown
                    items=[
                        OutfitItem(itemId=2384, goldPrice=115, itemType="HeadItem"),
                        OutfitItem(itemId=1000022, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1432, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3809, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1038, # Majestic Charm Gown
                    items=[
                        OutfitItem(itemId=2377, goldPrice=90, itemType="HeadItem"),
                        OutfitItem(itemId=1000013, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1427, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3804, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1039, # Finely Feathered Gown
                    items=[
                        OutfitItem(itemId=2452, goldPrice=120, itemType="HeadItem"),
                        OutfitItem(itemId=1000094, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001002, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3879, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1040, # Mystical Mist Gown
                    items=[
                        OutfitItem(itemId=2455, goldPrice=135, itemType="HeadItem"),
                        OutfitItem(itemId=1000097, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001005, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3882, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1041, # Riverine Elegance Gown
                    items=[
                        OutfitItem(itemId=2472, goldPrice=135, itemType="HeadItem"),
                        OutfitItem(itemId=1000120, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001027, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3902, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1042, # Radiant Regalia
                    items=[
                        OutfitItem(itemId=2476, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=1000131, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001040, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3905, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1043, # Summer Couture Gown
                    items=[
                        OutfitItem(itemId=390, goldPrice=90, itemType="Shirt"),
                        OutfitItem(itemId=1310, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3727, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        ),
        ShopCollection(
            collectionId=115, # The Queen's Collections (Purple)
            outfits=[
                ShopOutfit(
                    outfitId=1044, # Morning Glory Gown
                    items=[
                        OutfitItem(itemId=2331, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=411, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1326, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3058, goldPrice=0, itemType="AnkleItem"),
                        OutfitItem(itemId=3753, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1045, # Moonlight Magic Gown
                    items=[
                        OutfitItem(itemId=2359, goldPrice=80, itemType="HeadItem"),
                        OutfitItem(itemId=490, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1406, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3788, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1046, # Fast-Flying Couture
                    items=[
                        OutfitItem(itemId=2394, goldPrice=100, itemType="HeadItem"),
                        OutfitItem(itemId=1000028, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1439, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3819, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1047, # Petal Twirl Gown
                    items=[
                        OutfitItem(itemId=2435, goldPrice=100, itemType="HeadItem"),
                        OutfitItem(itemId=1000070, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1477, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3862, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1048, # Magnificent Evening Gown
                    items=[
                        OutfitItem(itemId=2457, goldPrice=150, itemType="HeadItem"),
                        OutfitItem(itemId=1000099, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001007, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=1684, goldPrice=0, itemType="WristItem"),
                        OutfitItem(itemId=3884, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1049, # Irresistible Indigo Gown
                    items=[
                        OutfitItem(itemId=2461, goldPrice=105, itemType="HeadItem"),
                        OutfitItem(itemId=1000104, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1001012, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3888, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        ),
        ShopCollection(
            collectionId=116, # The Queen's Collections (Other)
            outfits=[
                ShopOutfit(
                    outfitId=1050, # Incredible Iris Dress
                    items=[
                        OutfitItem(itemId=2303, goldPrice=80, itemType="HeadItem"),
                        OutfitItem(itemId=393, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1312, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3732, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1051, # Marvelous Magenta Gown
                    items=[
                        OutfitItem(itemId=488, goldPrice=70, itemType="Shirt"),
                        OutfitItem(itemId=1404, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3786, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1052, # Graceful Glamor Gown
                    items=[
                        OutfitItem(itemId=2358, goldPrice=85, itemType="HeadItem"),
                        OutfitItem(itemId=489, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1405, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3787, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1053, # Amethyst Flutter Gown
                    items=[
                        OutfitItem(itemId=2431, goldPrice=120, itemType="HeadItem"),
                        OutfitItem(itemId=1000065, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=1472, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3857, goldPrice=0, itemType="Shoes")
                    ]
                ),
                ShopOutfit(
                    outfitId=1054, # Plush Plumes Gown
                    items=[
                        OutfitItem(itemId=2434, goldPrice=130, itemType="HeadItem"),
                        OutfitItem(itemId=1000069, goldPrice=0, itemType="Shirt"),
                        OutfitItem(itemId=652, goldPrice=0, itemType="Belt"),
                        OutfitItem(itemId=1476, goldPrice=0, itemType="Skirt"),
                        OutfitItem(itemId=3861, goldPrice=0, itemType="Shoes")
                    ]
                ),
            ]
        )
    ]
)