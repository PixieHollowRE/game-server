from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

# Pixie Post Office - OutfitId 8000 - 8999

SHOP = NPCShop(
    zone=ZoneConstants.PIXIE_POST_OFFICE,
    shopId=8,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.SPRING,
        position=(500, 350),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_SPRING
    ),
    collections=[
        ShopCollection(
            collectionId=5, # Floral Giftsets
            outfits=[
                ShopOutfit(
                    outfitId=8001,
                    items = [
                        OutfitItem(itemId=2262, price=5, goldPrice=3, color1=210, color2=44, itemType="HeadItem"), # Lotus Purple Tillandsia Headband
                        OutfitItem(itemId=329, price=9, goldPrice=5, color1=210, color2=44, itemType="Shirt"), # Lotus Purple Tillandsia Top
                        OutfitItem(itemId=625, price=2, goldPrice=1, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Tillandsia Sash
                        OutfitItem(itemId=1266, price=9, goldPrice=5, color1=210, color2=44, itemType="Skirt"), # Lotus Purple Tillandsia Skirt
                        OutfitItem(itemId=3689, price=5, goldPrice=3, color1=210, color2=210, itemType="Shoes"), # Lotus Purple Tillandsia Flats
                    ],
                ),
                ShopOutfit(
                    outfitId=8002,
                    items = [
                        OutfitItem(itemId=2263, price=5, goldPrice=3, color1=30, color2=30, itemType="HeadItem"), # Pumpkin Orange Pumpkin Headband
                        OutfitItem(itemId=330, price=9, goldPrice=5, color1=206, color2=30, itemType="Shirt"), # Raven Black Pumpkin Bodice
                        OutfitItem(itemId=1267, price=9, goldPrice=5, color1=30, color2=30, itemType="Skirt"), # Pumpkin Orange Pumpkin Skirt
                        OutfitItem(itemId=3690, price=5, goldPrice=3, color1=206, color2=30, itemType="Shoes"), # Raven Black Pumpkin Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8003,
                    items = [
                        OutfitItem(itemId=2062, price=5, goldPrice=3, color1=140, color2=140, itemType="HeadItem"), # Bunnynose Pink Curcuma Headband
                        OutfitItem(itemId=332, price=9, goldPrice=5, color1=162, color2=140, itemType="Shirt"), # Sunglow Yellow Curcuma Top
                        OutfitItem(itemId=1269, price=9, goldPrice=5, color1=162, color2=140, itemType="Skirt"), # Sunglow Yellow Curcuma Skirt
                        OutfitItem(itemId=3694, price=5, goldPrice=3, color1=162, color2=140, itemType="Shoes"), # Sunglow Yellow Curcuma Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8004,
                    items = [
                        OutfitItem(itemId=2148, price=5, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Fresh Petal Barrette
                        OutfitItem(itemId=173, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Fresh Petal Bodice
                        OutfitItem(itemId=1157, price=9, goldPrice=5, color1=27, color2=267, itemType="Skirt"), # Corn Cob Yellow Fresh Petal Skirt
                        OutfitItem(itemId=3610, price=5, goldPrice=3, color1=267, color2=27, itemType="Shoes"), # Celestial Blue Fresh Petal Pumps
                    ],
                ),
                ShopOutfit(
                    outfitId=8005,
                    items = [
                        OutfitItem(itemId=2063, price=5, goldPrice=3, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Pansy Headband
                        OutfitItem(itemId=64, price=9, goldPrice=5, color1=247, color2=247, itemType="Shirt"), # Jasmine Yellow Pansy Top
                        OutfitItem(itemId=1069, price=9, goldPrice=5, color1=247, color2=247, itemType="Skirt"), # Jasmine Yellow Pansy Skirt
                        OutfitItem(itemId=3551, price=5, goldPrice=3, color1=113, color2=113, itemType="Shoes"), # Pale Rose Red Pansy Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=8006,
                    items = [
                        OutfitItem(itemId=2122, price=5, goldPrice=3, color1=166, color2=195, itemType="HeadItem"), # Snow White Delphinium Barrette
                        OutfitItem(itemId=111, price=9, goldPrice=5, color1=166, color2=195, itemType="Shirt"), # Snow White Delphinium Top
                        OutfitItem(itemId=1123, price=9, goldPrice=5, color1=166, color2=195, itemType="Skirt"), # Snow White Delphinium Skirt
                        OutfitItem(itemId=3581, price=5, goldPrice=3, color1=166, color2=195, itemType="Shoes"), # Snow White Delphinium Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8007,
                    items = [
                        OutfitItem(itemId=2050, price=5, goldPrice=3, color1=201, color2=201, itemType="HeadItem"), # Velvet Red Gentian Original Headband
                        OutfitItem(itemId=331, price=9, goldPrice=5, color1=201, color2=166, itemType="Shirt"), # Velvet Red Gentian Top
                        OutfitItem(itemId=1268, price=9, goldPrice=5, color1=201, color2=201, itemType="Skirt"), # Velvet Red Gentian Skirt
                        OutfitItem(itemId=3691, price=5, goldPrice=3, color1=166, color2=166, itemType="Shoes"), # Snow White Gentian Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8008,
                    items = [
                        OutfitItem(itemId=2421, price=5, goldPrice=3, color1=230, color2=206, itemType="HeadItem"), # Scarlet Red Cheery Cherry Headband
                        OutfitItem(itemId=1000054, price=9, goldPrice=5, color1=230, color2=206, itemType="Shirt"), # Scarlet Red Cheery Cherry Top
                        OutfitItem(itemId=1669, price=2, goldPrice=1, color1=230, color2=206, itemType="WristItem"), # Scarlet Red Cheery Cherry Clutch
                        OutfitItem(itemId=1461, price=9, goldPrice=5, color1=230, color2=206, itemType="Skirt"), # Scarlet Red Cheery Cherry Skirt
                        OutfitItem(itemId=3842, price=5, goldPrice=3, color1=230, color2=206, itemType="Shoes"), # Scarlet Red Cheery Cherry Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=8009,
                    items = [
                        OutfitItem(itemId=2429, price=5, goldPrice=3, color1=226, color2=267, itemType="HeadItem"), # Goldenrod Yellow Starfruit Earrings
                        OutfitItem(itemId=1000062, price=9, goldPrice=5, color1=226, color2=267, itemType="Shirt"), # Goldenrod Yellow Starfruit Top
                        OutfitItem(itemId=1469, price=9, goldPrice=5, color1=226, color2=267, itemType="Skirt"), # Goldenrod Yellow Starfruit Skirt
                        OutfitItem(itemId=3854, price=5, goldPrice=3, color1=267, color2=226, itemType="Shoes"), # Celestial Blue Starfruit Heels with Goldenrod Yellow Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=8010,
                    items = [
                        OutfitItem(itemId=2010, price=5, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Fanned Flower Clip
                        OutfitItem(itemId=284, price=9, goldPrice=5, color1=185, color2=44, itemType="Shirt"), # Midnight Blue Layered Petal Top
                        OutfitItem(itemId=1234, price=9, goldPrice=5, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Layered Petal Skirt
                        OutfitItem(itemId=3539, price=5, goldPrice=3, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink White Rose Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=8011,
                    items = [
                        OutfitItem(itemId=2173, price=5, goldPrice=3, color1=224, color2=139, itemType="HeadItem"), # Ivory White Blooming Rose Headband
                        OutfitItem(itemId=295, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Formal Ruffle Top
                        OutfitItem(itemId=1236, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Formal Ruffle Skirt
                        OutfitItem(itemId=3718, price=5, goldPrice=3, color1=139, color2=224, itemType="Shoes"), # Seedling Green Ruffle Detail Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8012,
                    items = [
                        OutfitItem(itemId=2639, price=5, goldPrice=3, color1=121, color2=121, itemType="Necklace"), # Daisy Pink Spring Rose Choker
                        OutfitItem(itemId=1000073, price=9, goldPrice=5, color1=207, color2=121, itemType="Shirt"), # Diamond Blue Spring Rose Top
                        OutfitItem(itemId=653, price=2, goldPrice=1, color1=121, color2=121, itemType="Belt"), # Daisy Pink Spring Rose Sash
                        OutfitItem(itemId=1480, price=9, goldPrice=5, color1=207, color2=121, itemType="Skirt"), # Diamond Blue Spring Rose Skirt
                        OutfitItem(itemId=3865, price=5, goldPrice=3, color1=207, color2=121, itemType="Shoes"), # Diamond Blue Spring Rose Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8013,
                    items = [
                        OutfitItem(itemId=2465, price=5, goldPrice=3, color1=264, color2=264, itemType="HeadItem"), # Jungle Green Posh Pineapple Fascinator
                        OutfitItem(itemId=1000109, price=9, goldPrice=5, color1=162, color2=78, itemType="Shirt"), # Sunglow Yellow Posh Pineapple Top
                        OutfitItem(itemId=1001016, price=9, goldPrice=5, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Posh Pineapple Skirt
                        OutfitItem(itemId=3892, price=5, goldPrice=3, color1=78, color2=264, itemType="Shoes"), # Fawn Brown Posh Pineapple Pumps
                    ],
                ),
                ShopOutfit(
                    outfitId=8014,
                    items = [
                        OutfitItem(itemId=2448, price=5, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Sycamore Blossom Earrings
                        OutfitItem(itemId=1000077, price=9, goldPrice=5, color1=206, color2=175, itemType="Shirt"), # Raven Black Sycamore Leaf Top
                        OutfitItem(itemId=1483, price=9, goldPrice=5, color1=206, color2=175, itemType="Skirt"), # Raven Black Sycamore Leaf Skirt
                        OutfitItem(itemId=3868, price=5, goldPrice=3, color1=206, color2=175, itemType="Shoes"), # Raven Black Sycamore Leaf Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8015,
                    items = [
                        OutfitItem(itemId=1000115, price=9, goldPrice=5, color1=17, color2=49, itemType="Shirt"), # Tendershoot Green Sweet Pea Petal Top
                        OutfitItem(itemId=1001021, price=9, goldPrice=5, color1=17, color2=49, itemType="Skirt"), # Tendershoot Green Sweet Pea Petal Skirt
                        OutfitItem(itemId=3897, price=5, goldPrice=3, color1=17, color2=49, itemType="Shoes"), # Tendershoot Green Sweet Pea Petal Shoes
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=26, # Mainland Style Gift Sets
            outfits=[
                ShopOutfit(
                    outfitId=8016,
                    items = [
                        OutfitItem(itemId=396, price=9, goldPrice=5, color1=224, color2=206, itemType="Shirt"), # Ivory White Unstoppable Top
                        OutfitItem(itemId=638, price=2, goldPrice=1, color1=206, color2=206, itemType="Belt"), # Raven Black Unstoppable Belt
                        OutfitItem(itemId=1321, price=9, goldPrice=5, color1=45, color2=206, itemType="Skirt"), # Strawberry Red Unstoppable Skirt
                        OutfitItem(itemId=3747, price=5, goldPrice=3, color1=206, color2=224, itemType="Shoes"), # Raven Black Sky High Laceups
                    ],
                ),
                ShopOutfit(
                    outfitId=8017,
                    items = [
                        OutfitItem(itemId=2327, price=5, goldPrice=3, color1=267, color2=248, itemType="HeadItem"), # Celestial Blue Alluring Elegance Hat
                        OutfitItem(itemId=408, price=9, goldPrice=5, color1=267, color2=248, itemType="Shirt"), # Celestial Blue Alluring Elegance Dress Top
                        OutfitItem(itemId=1327, price=9, goldPrice=5, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Alluring Elegance Dress Bottom
                        OutfitItem(itemId=3750, price=5, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Alluring Elegance Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=8018,
                    items = [
                        OutfitItem(itemId=2187, price=5, goldPrice=3, color1=82, color2=248, itemType="HeadItem"), # Raspberry Red Button Headband
                        OutfitItem(itemId=401, price=9, goldPrice=5, color1=27, color2=248, itemType="Shirt"), # Corn Cob Yellow Bitsy Buttons Top
                        OutfitItem(itemId=1324, price=9, goldPrice=5, color1=27, color2=248, itemType="Skirt"), # Corn Cob Yellow Bitsy Buttons Skirt
                        OutfitItem(itemId=3656, price=5, goldPrice=3, color1=82, color2=248, itemType="Shoes"), # Raspberry Red One-Button Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8019,
                    items = [
                        OutfitItem(itemId=2621, price=2, goldPrice=1, color1=141, color2=169, itemType="Necklace"), # Thundercloud Gray Art Deco Necklace
                        OutfitItem(itemId=480, price=9, goldPrice=5, color1=182, color2=169, itemType="Shirt"), # Twilight Blue Sleek and Stylish Top
                        OutfitItem(itemId=1397, price=9, goldPrice=5, color1=169, color2=182, itemType="Skirt"), # Squirrel Gray Peplum Skirt
                        OutfitItem(itemId=3780, price=5, goldPrice=3, color1=182, color2=169, itemType="Shoes"), # Twilight Blue Stripey Wedges
                    ],
                ),
                ShopOutfit(
                    outfitId=8020,
                    items = [
                        OutfitItem(itemId=2208, price=5, goldPrice=3, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Nifty Knit Hat
                        OutfitItem(itemId=479, price=9, goldPrice=5, color1=81, color2=166, itemType="Shirt"), # Crimson Red Funky Striped Tee
                        OutfitItem(itemId=1199, price=9, goldPrice=5, color1=185, color2=81, itemType="Skirt"), # Midnight Blue Knitted Gala Skirt
                        OutfitItem(itemId=3505, price=5, goldPrice=3, color1=75, color2=75, itemType="Shoes"), # Umber Brown Twirly Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8021,
                    items = [
                        OutfitItem(itemId=2398, price=5, goldPrice=3, color1=274, color2=158, itemType="HeadItem"), #  Bellflower Purple Trendy Accessory Set
                        OutfitItem(itemId=1000032, price=9, goldPrice=5, color1=274, color2=158, itemType="Shirt"), # Bellflower Purple Trendy Tied Shirt
                        OutfitItem(itemId=1660, price=2, goldPrice=1, color1=274, color2=158, itemType="WristItem"), # Bellflower Purple Multi-Bead Bracelet
                        OutfitItem(itemId=1443, price=9, goldPrice=5, color1=274, color2=158, itemType="Skirt"), # Bellflower Purple Buttoned Up Leggings
                        OutfitItem(itemId=3823, price=5, goldPrice=3, color1=274, color2=158, itemType="Shoes"), # Bellflower Purple Glitter Sneakers
                    ],
                ),
                ShopOutfit(
                    outfitId=8022,
                    items = [
                        OutfitItem(itemId=2346, price=5, goldPrice=3, color1=219, color2=226, itemType="HeadItem"), # Crystal Blue Fun Flower Headband
                        OutfitItem(itemId=1000060, price=9, goldPrice=5, color1=199, color2=208, itemType="Shirt"), # Cherryblossom Pink Flower Power Top
                        OutfitItem(itemId=651, price=2, goldPrice=1, color1=208, color2=226, itemType="Belt"), # Cerulean Blue Flower Power Belt
                        OutfitItem(itemId=1466, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Flower Power Skirt
                        OutfitItem(itemId=3847, price=5, goldPrice=3, color1=46, color2=226, itemType="Shoes"), # Bark Brown Moccasin Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8023,
                    items = [
                        OutfitItem(itemId=1000079, price=9, goldPrice=5, color1=218, color2=258, itemType="Shirt"), # Laurel Green Ruffled Petal Bolero
                        OutfitItem(itemId=1682, price=2, goldPrice=1, color1=265, color2=91, itemType="WristItem"), # Bright Sky Blue Ruffled Petal Purse
                        OutfitItem(itemId=1380, price=9, goldPrice=5, color1=258, color2=258, itemType="Skirt"), # Spearmint Green Single Ruffle Skirt
                        OutfitItem(itemId=3870, price=5, goldPrice=3, color1=265, color2=91, itemType="Shoes"), # Bright Sky Blue Strappy Platforms
                    ],
                ),
                ShopOutfit(
                    outfitId=8024,
                    items = [
                        OutfitItem(itemId=2443, price=5, goldPrice=3, color1=171, color2=206, itemType="HeadItem"), # Sunrise Yellow Sassy Chic Fedora
                        OutfitItem(itemId=1000090, price=9, goldPrice=5, color1=166, color2=206, itemType="Shirt"), # Snow White Sassy Chic Top
                        OutfitItem(itemId=1497, price=9, goldPrice=5, color1=166, color2=206, itemType="Skirt"), # Snow White Sassy Chic Skirt
                        OutfitItem(itemId=3875, price=5, goldPrice=3, color1=171, color2=206, itemType="Shoes"), # Sunrise Yellow Sassy Chic Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8025,
                    items = [
                        OutfitItem(itemId=2610, price=2, goldPrice=1, color1=134, color2=277, itemType="Necklace"), # Heather Purple Beaded Bud Necklace
                        OutfitItem(itemId=416, price=9, goldPrice=5, color1=134, color2=277, itemType="Shirt"), # Heather Purple Lace Flower Top
                        OutfitItem(itemId=1336, price=9, goldPrice=5, color1=134, color2=277, itemType="Skirt"), # Heather Purple Lace Flower Skirt
                        OutfitItem(itemId=3759, price=5, goldPrice=3, color1=134, color2=277, itemType="Shoes"), # Heather Purple Lace Flower Wedges
                    ],
                ),
                ShopOutfit(
                    outfitId=8026,
                    items = [
                        OutfitItem(itemId=2240, price=5, goldPrice=3, color1=277, color2=152, itemType="HeadItem"), # Misty Purple Fancy Floral Headband
                        OutfitItem(itemId=298, price=9, goldPrice=5, color1=277, color2=152, itemType="Shirt"), # Misty Purple Fancy Formal Top
                        OutfitItem(itemId=1248, price=9, goldPrice=5, color1=277, color2=152, itemType="Skirt"), # Misty Purple Fancy Floral Skirt
                        OutfitItem(itemId=3676, price=5, goldPrice=3, color1=277, color2=152, itemType="Shoes"), # Misty Purple Fancy Formal Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8027,
                    items = [
                        OutfitItem(itemId=2391, price=5, goldPrice=3, color1=206, color2=169, itemType="HeadItem"), # Raven Black Cute and Cozy Cap
                        OutfitItem(itemId=1000026, price=9, goldPrice=5, color1=201, color2=206, itemType="Shirt"), # Velvet Red Stylish Buckle Vest
                        OutfitItem(itemId=1437, price=9, goldPrice=5, color1=201, color2=206, itemType="Skirt"), # Velvet Red Twist and Twirl Skirt
                        OutfitItem(itemId=3817, price=5, goldPrice=3, color1=206, color2=169, itemType="Shoes"), # Raven Black Funky Laceup Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8028,
                    items = [
                        OutfitItem(itemId=2418, price=5, goldPrice=3, color1=224, color2=206, itemType="HeadItem"), # Ivory White Sailor Cloche
                        OutfitItem(itemId=1000053, price=9, goldPrice=5, color1=224, color2=206, itemType="Shirt"), # Ivory White Sailor Top
                        OutfitItem(itemId=1460, price=9, goldPrice=5, color1=224, color2=206, itemType="Skirt"), # Ivory White Sailor Striped Skirt
                        OutfitItem(itemId=3841, price=5, goldPrice=3, color1=224, color2=206, itemType="Shoes"), # Ivory White Sailor Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=8029,
                    items = [
                        OutfitItem(itemId=2422, price=5, goldPrice=3, color1=230, color2=206, itemType="HeadItem"), # Scarlet Red Lovely Hearts Headband
                        OutfitItem(itemId=1000056, price=9, goldPrice=5, color1=230, color2=121, itemType="Shirt"), # Scarlet Red Heart Keyhole Top
                        OutfitItem(itemId=1670, price=2, goldPrice=1, color1=230, color2=121, itemType="WristItem"), # Scarlet Red Lovely Heart Purse
                        OutfitItem(itemId=1462, price=9, goldPrice=5, color1=230, color2=121, itemType="Skirt"), # Scarlet Red Lovely Hearts Skirt
                        OutfitItem(itemId=3843, price=5, goldPrice=3, color1=230, color2=206, itemType="Shoes"), # Scarlet Red Heart Buckle Boots
                    ],
                )
            ],
        ),


        ShopCollection(
            collectionId=3, # Tailoring Gift Sets - Sparrow men
            outfits=[
                ShopOutfit(
                    outfitId=8030,
                    items = [
                        OutfitItem(itemId=2195, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Buckingham Fur Hat
                        OutfitItem(itemId=254, price=9, goldPrice=5, color1=82, color2=186, itemType="Shirt"), # Raspberry Red Buckingham Fur Coat
                        OutfitItem(itemId=616, price=2, goldPrice=1, color1=116, color2=186, itemType="Belt"), # Mushroom White Buckingham Belt
                        OutfitItem(itemId=1214, price=9, goldPrice=5, color1=206, color2=141, itemType="Skirt"), # Raven Black Buckingham Fur Pants
                        OutfitItem(itemId=3648, price=5, goldPrice=3, color1=206, color2=141, itemType="Shoes"), # Raven Black Buckingham Fur Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8031,
                    items = [
                        OutfitItem(itemId=233, price=9, goldPrice=5, color1=172, color2=128, itemType="Shirt"), # Forest Green Fur Trainer Jacket
                        OutfitItem(itemId=600, price=2, goldPrice=1, color1=56, color2=128, itemType="Belt"), # Bole Brown Fur Trainer Belt
                        OutfitItem(itemId=1197, price=9, goldPrice=5, color1=206, color2=128, itemType="Skirt"), # Raven Black Fur Trainer Pants
                        OutfitItem(itemId=3635, price=5, goldPrice=3, color1=56, color2=128, itemType="Shoes"), # Bole Brown Fur Trainer Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8032,
                    items = [
                        OutfitItem(itemId=264, price=9, goldPrice=5, color1=185, color2=166, itemType="Shirt"), # Midnight Blue Striking Fur Top
                        OutfitItem(itemId=615, price=2, goldPrice=1, color1=59, color2=56, itemType="Belt"), # Bunny Brown Striking Fur Belt
                        OutfitItem(itemId=1213, price=9, goldPrice=5, color1=141, color2=166, itemType="Skirt"), # Thundercloud Gray Striking Fur Pants
                        OutfitItem(itemId=3649, price=5, goldPrice=3, color1=206, color2=186, itemType="Shoes"), # Raven Black Striking Fur Boots with Yellow Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=8033,
                    items = [
                        OutfitItem(itemId=2192, price=5, goldPrice=3, color1=60, color2=141, itemType="HeadItem"), # Tyrian Purple Birdie Best Cap
                        OutfitItem(itemId=245, price=9, goldPrice=5, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Birdie Best Top
                        OutfitItem(itemId=1205, price=9, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Birdie Best Bottoms
                        OutfitItem(itemId=607, price=2, goldPrice=1, color1=60, color2=141, itemType="Belt"), # Tyrian Purple Birdie Best Belt
                        OutfitItem(itemId=3642, price=5, goldPrice=3, color1=60, color2=141, itemType="Shoes"), # Tyrian Purple Birdie Best Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8034,
                    items = [
                        OutfitItem(itemId=240, price=9, goldPrice=5, color1=166, color2=75, itemType="Shirt"), # Snow White Tailor's Top
                        OutfitItem(itemId=606, price=2, goldPrice=1, color1=13, color2=213, itemType="Belt"), # Coral Pink Tailor's Utility Belt
                        OutfitItem(itemId=1203, price=9, goldPrice=5, color1=73, color2=75, itemType="Skirt"), # Grape Purple Tailor's Trousers
                        OutfitItem(itemId=3637, price=5, goldPrice=3, color1=206, color2=168, itemType="Shoes"), # Driftwood Brown Tailor's Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8035,
                    items = [
                        OutfitItem(itemId=267, price=9, goldPrice=5, color1=113, color2=166, itemType="Shirt"), # Pale Rose Red Knit Messenger Top
                        OutfitItem(itemId=620, price=2, goldPrice=1, color1=177, color2=168, itemType="Belt"), # Mud Brown Knit Messenger Belt
                        OutfitItem(itemId=1216, price=9, goldPrice=5, color1=93, color2=161, itemType="Skirt"), # Maple Brown Knit Messenger Pants
                        OutfitItem(itemId=3653, price=5, goldPrice=3, color1=177, color2=161, itemType="Shoes"), # Mud Brown Knit Messenger Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=8036,
                    items = [
                        OutfitItem(itemId=241, price=9, goldPrice=5, color1=161, color2=111, itemType="Shirt"), # Buried Treasure Brown Lightning Bead Coat
                        OutfitItem(itemId=1202, price=9, goldPrice=5, color1=91, color2=111, itemType="Skirt"), # Coconut Brown Lightning Bead Pants
                        OutfitItem(itemId=3593, price=5, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Ivy Wrap Slippers
                    ],
                ),
                ShopOutfit(
                    outfitId=8037,
                    items = [
                        OutfitItem(itemId=2189, price=5, goldPrice=3, color1=224, color2=169, itemType="HeadItem"), # Ivory White All Buttons Visor
                        OutfitItem(itemId=234, price=9, goldPrice=5, color1=267, color2=224, itemType="Shirt"), # Celestial Blue Button Down Jacket
                        OutfitItem(itemId=1198, price=9, goldPrice=5, color1=208, color2=224, itemType="Skirt"), # Cerulean Blue Button Down Pants
                        OutfitItem(itemId=3636, price=5, goldPrice=3, color1=215, color2=224, itemType="Shoes"), # Pewter Gray Button Down Shoes
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=19, # Costume Gift Sets
            outfits=[
                ShopOutfit(
                    outfitId=8038,
                    items = [
                        OutfitItem(itemId=2193, price=5, goldPrice=3, color1=75, color2=171, itemType="HeadItem"), # Umber Brown Never West Round Up Hat
                        OutfitItem(itemId=2568, price=2, goldPrice=1, color1=171, color2=92, itemType="Necklace"), # Sunrise Yellow Never West Necklace
                        OutfitItem(itemId=246, price=9, goldPrice=5, color1=92, color2=75, itemType="Shirt"), # Hawk Brown Never West Shirt
                        OutfitItem(itemId=608, price=2, goldPrice=1, color1=171, color2=75, itemType="Belt"), # Sunrise Yellow Never West Belt
                        OutfitItem(itemId=1206, price=9, goldPrice=5, color1=75, color2=92, itemType="Skirt"), # Umber Brown Never West Trousers
                        OutfitItem(itemId=3643, price=5, goldPrice=3, color1=75, color2=171, itemType="Shoes"), # Sunrise Yellow Never West Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8039,
                    items = [
                        OutfitItem(itemId=2415, price=5, goldPrice=3, color1=172, color2=76, itemType="HeadItem"), # Forest Green Calla Lily Hat
                        OutfitItem(itemId=1000050, price=9, goldPrice=5, color1=172, color2=76, itemType="Shirt"), # Forest Green Calla Lily Top
                        OutfitItem(itemId=649, price=2, goldPrice=1, color1=76, color2=76, itemType="Belt"), # Chocolate Brown Calla Lily Belt
                        OutfitItem(itemId=1457, price=9, goldPrice=5, color1=76, color2=76, itemType="Skirt"), # Chocolate Brown Calla Lily Pants
                        OutfitItem(itemId=3838, price=5, goldPrice=3, color1=172, color2=76, itemType="Shoes"), # Forest Green Calla Lily Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8040,
                    items = [
                        OutfitItem(itemId=2289, price=5, goldPrice=3, color1=2, color2=206, itemType="HeadItem"), # Mint Green Clover Hat
                        OutfitItem(itemId=2593, price=2, goldPrice=1, color1=2, color2=2, itemType="Necklace"), # Mint Green Clover Bowtie
                        OutfitItem(itemId=350, price=9, goldPrice=5, color1=2, color2=206, itemType="Shirt"), # Mint Green Clover Vest
                        OutfitItem(itemId=1286, price=9, goldPrice=5, color1=206, color2=2, itemType="Skirt"), # Mint Green Clover Knickers
                        OutfitItem(itemId=3710, price=5, goldPrice=3, color1=2, color2=206, itemType="Shoes"), # Mint Green Clover Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8041,
                    items = [
                        OutfitItem(itemId=2361, price=5, goldPrice=3, color1=208, color2=227, itemType="HeadItem"), # Cerulean Blue Wizard Beard
                        OutfitItem(itemId=498, price=9, goldPrice=5, color1=208, color2=267, itemType="Shirt"), # Cerulean Blue Wizard Top
                        OutfitItem(itemId=1414, price=9, goldPrice=5, color1=208, color2=267, itemType="Skirt"), # Cerulean Blue Wizard Robe
                        OutfitItem(itemId=3792, price=5, goldPrice=3, color1=206, color2=166, itemType="Shoes"), # Raven Black Wizard Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8042,
                    items = [
                        OutfitItem(itemId=2278, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Soft-Serve Hat
                        OutfitItem(itemId=348, price=9, goldPrice=5, color1=224, color2=45, itemType="Shirt"), # Ivory White Candy Fanatic Marshmallow Top
                        OutfitItem(itemId=1284, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Candy Fanatic Licorice Shorts
                        OutfitItem(itemId=3708, price=5, goldPrice=3, color1=45, color2=45, itemType="Shoes"), # Strawberry Red Candy Fanatic Jellybean Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8043,
                    items = [
                        OutfitItem(itemId=2362, price=5, goldPrice=3, color1=114, color2=256, itemType="HeadItem"), # Foxtail Orange Fox Mask
                        OutfitItem(itemId=497, price=9, goldPrice=5, color1=143, color2=114, itemType="Shirt"), # June Bug Green Fox Costume Top
                        OutfitItem(itemId=1413, price=9, goldPrice=5, color1=143, color2=114, itemType="Skirt"), # June Bug Green Fox Trousers
                        OutfitItem(itemId=3793, price=5, goldPrice=3, color1=224, color2=256, itemType="Shoes"), # Ivory White Fox Boots
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=31, # Mainland Style Gift Sets
            outfits=[
                ShopOutfit(
                    outfitId=8044,
                    items = [
                        OutfitItem(itemId=270, price=9, goldPrice=5, color1=172, color2=128, itemType="Shirt"), # Forest Green Dressy Raincoat
                        OutfitItem(itemId=624, price=2, goldPrice=1, color1=57, color2=128, itemType="Belt"), # Adobe Brown Dressy Raincoat Belt
                        OutfitItem(itemId=1221, price=9, goldPrice=5, color1=172, color2=128, itemType="Skirt"), # Forest Green Dressy Raincoat Pants
                        OutfitItem(itemId=3627, price=5, goldPrice=3, color1=76, color2=78, itemType="Shoes"), # Chocolate Brown Sturdy Galoshes
                    ],
                ),
                ShopOutfit(
                    outfitId=8045,
                    items = [
                        OutfitItem(itemId=2156, price=5, goldPrice=3, color1=206, color2=166, itemType="HeadItem"), # Raven Black Sparkly Tux Top Hat
                        OutfitItem(itemId=194, price=9, goldPrice=5, color1=206, color2=166, itemType="Shirt"), # Raven Black Sparkly 3-Piece Tux
                        OutfitItem(itemId=1177, price=9, goldPrice=5, color1=206, color2=166, itemType="Skirt"), # Raven Black Sparkly Tux Trouser
                        OutfitItem(itemId=3587, price=5, goldPrice=3, color1=206, color2=166, itemType="Shoes"), # Raven Black Bark Sole Dress Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8046,
                    items = [
                        OutfitItem(itemId=2155, price=5, goldPrice=3, color1=1, color2=116, itemType="HeadItem"), # Mint Green Sparrow Snow Cap
                        OutfitItem(itemId=218, price=9, goldPrice=5, color1=1, color2=116, itemType="Shirt"), # Mint Green Rain Hoodie
                        OutfitItem(itemId=2592, price=2, goldPrice=1, color1=1, color2=116, itemType="Necklace"), # Mint Green Rockin' Necklace
                        OutfitItem(itemId=1189, price=9, goldPrice=5, color1=1, color2=116, itemType="Skirt"), # Mint Green Camouflage Pants
                        OutfitItem(itemId=3654, price=5, goldPrice=3, color1=1, color2=116, itemType="Shoes"), # Mint Green Easy Style Sneaks
                    ],
                ),
                ShopOutfit(
                    outfitId=8047,
                    items = [
                        OutfitItem(itemId=208, price=9, goldPrice=5, color1=45, color2=56, itemType="Shirt"), # Strawberry Red Mad Plaid
                        OutfitItem(itemId=1170, price=9, goldPrice=5, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Pocket Pants
                        OutfitItem(itemId=3625, price=5, goldPrice=3, color1=141, color2=166, itemType="Shoes"), # Thundercloud Gray Woodchucks with Snow White Trim
                    ],
                )
            ]
        ),
        ShopCollection(
            collectionId=33, # Famous Fairy Gift Sets
            outfits=[
                ShopOutfit(
                    outfitId=8048,
                    items = [
                        OutfitItem(itemId=176, price=9, goldPrice=5, color1=75, color2=85, itemType="Shirt"), # Umber Brown Terence's Top
                        OutfitItem(itemId=1160, price=9, goldPrice=5, color1=75, color2=85, itemType="Skirt"), # Umber Brown Terence's Trunks
                        OutfitItem(itemId=3613, price=5, goldPrice=3, color1=85, color2=85, itemType="Shoes"), # Quail Brown Terence's Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8049,
                    items = [
                        OutfitItem(itemId=2152, price=5, goldPrice=3, color1=186, color2=186, itemType="HeadItem"), # Honeycomb Yellow Bobble's Goggles
                        OutfitItem(itemId=179, price=9, goldPrice=5, color1=65, color2=65, itemType="Shirt"), # Summer Green Bobble Vest
                        OutfitItem(itemId=575, price=2, goldPrice=1, color1=46, color2=46, itemType="Belt"), # Bark Brown Bobble Belt
                        OutfitItem(itemId=1161, price=9, goldPrice=5, color1=125, color2=125, itemType="Skirt"), # Pine Green Bobble Trunks
                        OutfitItem(itemId=3576, price=5, goldPrice=3, color1=125, color2=125, itemType="Shoes"), # Pine Green Wide Band Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8050,
                    items = [
                        OutfitItem(itemId=180, price=9, goldPrice=5, color1=64, color2=64, itemType="Shirt"), # Emerald Green Clank's Top
                        OutfitItem(itemId=1162, price=9, goldPrice=5, color1=125, color2=125, itemType="Skirt"), # Pine Green Clank's Trunks
                        OutfitItem(itemId=3576, price=5, goldPrice=3, color1=125, color2=125, itemType="Shoes"), # Pine Green Wide Band Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8051,
                    items = [
                        OutfitItem(itemId=1000010, price=9, goldPrice=5, color1=207, color2=153, itemType="Shirt"), # Diamond Blue Sled's Top
                        OutfitItem(itemId=1425, price=9, goldPrice=5, color1=216, color2=153, itemType="Skirt"), # Slate Gray Sled's Trousers
                        OutfitItem(itemId=3800, price=5, goldPrice=3, color1=153, color2=216, itemType="Shoes"), # Frostbunny Blue Sled's Shoes
                    ],
                )
            ],
        ),
    
        ShopCollection(
            collectionId=27, # Costume Gift Sets - Fairies
            outfits=[
                ShopOutfit(
                    outfitId=8052,
                    items = [
                        OutfitItem(itemId=2216, price=5, goldPrice=3, color1=206, color2=167, itemType="HeadItem"), # Raven Black Bewitching Hat with Never Silver Trim
                        OutfitItem(itemId=482, price=9, goldPrice=5, color1=206, color2=167, itemType="Shirt"), # Raven Black Bewitching Top with Never Silver Trim
                        OutfitItem(itemId=1586, price=2, goldPrice=1, color1=161, color2=161, itemType="WristItem"), # Buried Treasure Brown Bewitching Twig Broom
                        OutfitItem(itemId=1399, price=9, goldPrice=5, color1=206, color2=167, itemType="Skirt"), # Raven Black Bewitching Skirt with Never Silver Trim
                        OutfitItem(itemId=3674, price=5, goldPrice=3, color1=206, color2=167, itemType="Shoes"), # Raven Black Bewitching Boots with Never Silver Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=8053,
                    items = [
                        OutfitItem(itemId=2238, price=5, goldPrice=3, color1=221, color2=136, itemType="HeadItem"), # Jade Green Spring Peacock Headband
                        OutfitItem(itemId=317, price=9, goldPrice=5, color1=221, color2=248, itemType="Shirt"), # Jade Green Spring Peacock Top
                        OutfitItem(itemId=1256, price=9, goldPrice=5, color1=221, color2=248, itemType="Skirt"), # Jade Green Spring Peacock Skirt
                        OutfitItem(itemId=3684, price=5, goldPrice=3, color1=221, color2=248, itemType="Shoes"), # Jade Green Spring Peacock Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8054,
                    items = [
                        OutfitItem(itemId=2239, price=5, goldPrice=3, color1=169, color2=166, itemType="HeadItem"), # Squirrel Gray Fluffy Owl Fascinator
                        OutfitItem(itemId=321, price=9, goldPrice=5, color1=166, color2=169, itemType="Shirt"), # Snow White Feather Accent Capelet with Squirrel Gray Trim
                        OutfitItem(itemId=1261, price=9, goldPrice=5, color1=166, color2=169, itemType="Skirt"), # Snow White Layered Feather Skirt with Squirrel Gray Trim
                        OutfitItem(itemId=3687, price=5, goldPrice=3, color1=166, color2=169, itemType="Shoes"), # Snow White Feathered Ankle Boots with Squirrel Gray Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=8055,
                    items = [
                        OutfitItem(itemId=2017, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Tulip Petal Bow
                        OutfitItem(itemId=327, price=9, goldPrice=5, color1=126, color2=166, itemType="Shirt"), # Raindrop Blue Wonderland Top
                        OutfitItem(itemId=1265, price=9, goldPrice=5, color1=126, color2=166, itemType="Skirt"), # Raindrop Blue Wonderland Skirt
                        OutfitItem(itemId=3688, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Wonderland Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8056,
                    items = [
                        OutfitItem(itemId=2083, price=5, goldPrice=3, color1=208, color2=207, itemType="HeadItem"), # Cerulean Blue Mer-Made Crown
                        OutfitItem(itemId=400, price=9, goldPrice=5, color1=208, color2=207, itemType="Shirt"), # Cerulean Blue Magical Mermaid Top
                        OutfitItem(itemId=1323, price=9, goldPrice=5, color1=208, color2=207, itemType="Skirt"), # Cerulean Blue Magical Mermaid Skirt
                        OutfitItem(itemId=3675, price=5, goldPrice=3, color1=208, color2=208, itemType="Shoes"), # Cerulean Blue Glittering Glass Slippers
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=30, # Fashion Boutique Gift Sets
            outfits=[
                ShopOutfit(
                    outfitId=8057,
                    items = [
                        OutfitItem(itemId=447, price=9, goldPrice=5, color1=200, color2=27, itemType="Shirt"), # Ruby Pink Tri-Color Top
                        OutfitItem(itemId=1642, price=2, goldPrice=1, color1=200, color2=27, itemType="WristItem"), #  Ruby Pink Spangled Clutch
                        OutfitItem(itemId=1360, price=9, goldPrice=5, color1=200, color2=27, itemType="Skirt"), # Ruby Pink Tri-Color Skirt
                        OutfitItem(itemId=3716, price=5, goldPrice=3, color1=27, color2=200, itemType="Shoes"), # Corn Cob Yellow Morpho Butterfly Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8058,
                    items = [
                        OutfitItem(itemId=460, price=9, goldPrice=5, color1=180, color2=69, itemType="Shirt"), # Seashell Blue Furry Vest
                        OutfitItem(itemId=1377, price=9, goldPrice=5, color1=180, color2=69, itemType="Skirt"), # Seashell Blue Sweet Stripey Skirt
                        OutfitItem(itemId=3778, price=5, goldPrice=3, color1=180, color2=182, itemType="Shoes"), #  Seashell Blue Colorblock Wedges
                    ],
                ),
                ShopOutfit(
                    outfitId=8059,
                    items = [
                        OutfitItem(itemId=427, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Sweater Dress Top
                        OutfitItem(itemId=1347, price=9, goldPrice=5, color1=69, color2=224, itemType="Skirt"), # Powder Blue Sweater Dress Skirt
                        OutfitItem(itemId=3739, price=5, goldPrice=3, color1=224, color2=69, itemType="Shoes"), #  Ivory White Casual Moccasins
                    ],
                ),
                ShopOutfit(
                    outfitId=8060,
                    items = [
                        OutfitItem(itemId=426, price=9, goldPrice=5, color1=266, color2=203, itemType="Shirt"), # Ocean Blue Cozy Coat
                        OutfitItem(itemId=1343, price=9, goldPrice=5, color1=225, color2=225, itemType="Skirt"), # Eggplant Purple Skinny Jeans
                        OutfitItem(itemId=3773, price=5, goldPrice=3, color1=236, color2=109, itemType="Shoes"), # Dusty Brown Comfy Slip-Ons
                    ],
                ),
                ShopOutfit(
                    outfitId=8061,
                    items = [
                        OutfitItem(itemId=424, price=9, goldPrice=5, color1=211, color2=197, itemType="Shirt"), # Gentian Purple Cropped Cardigan
                        OutfitItem(itemId=1345, price=9, goldPrice=5, color1=275, color2=197, itemType="Skirt"), # Shadowy Purple Big Bow Skirt
                        OutfitItem(itemId=3767, price=5, goldPrice=3, color1=74, color2=74, itemType="Shoes"), # Soil Brown Knee Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8062,
                    items = [
                        OutfitItem(itemId=2317, price=5, goldPrice=3, color1=45, color2=239, itemType="HeadItem"), # Strawberry Red Blooming Headband with Coffee Black Trim
                        OutfitItem(itemId=464, price=9, goldPrice=5, color1=224, color2=239, itemType="Shirt"), # Ivory White Charleston Top
                        OutfitItem(itemId=1383, price=9, goldPrice=5, color1=224, color2=239, itemType="Skirt"), # Ivory White Charleston Skirt
                        OutfitItem(itemId=3777, price=5, goldPrice=3, color1=239, color2=224, itemType="Shoes"), # Coffee Black Charleston Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=8063,
                    items = [
                        OutfitItem(itemId=433, price=9, goldPrice=5, color1=208, color2=206, itemType="Shirt"), # Cerulean Blue Zippy Top
                        OutfitItem(itemId=1351, price=9, goldPrice=5, color1=268, color2=268, itemType="Skirt"), # Navy Blue Zippy Skirt
                        OutfitItem(itemId=3774, price=5, goldPrice=3, color1=206, color2=208, itemType="Shoes"), # Raven Black Roller Skates
                    ],
                ),
                ShopOutfit(
                    outfitId=8064,
                    items = [
                        OutfitItem(itemId=456, price=9, goldPrice=5, color1=282, color2=206, itemType="Shirt"), # Magnolia White Sassy Suspender Top
                        OutfitItem(itemId=1372, price=9, goldPrice=5, color1=165, color2=206, itemType="Skirt"), # Spring Breeze Green Layered Shorts
                        OutfitItem(itemId=3760, price=5, goldPrice=3, color1=206, color2=165, itemType="Shoes"), # Raven Black Trinket Toe Flats
                    ],
                ),
                ShopOutfit(
                    outfitId=8065,
                    items = [
                        OutfitItem(itemId=469, price=9, goldPrice=5, color1=285, color2=207, itemType="Shirt"), # Jazzberry Red Cropped Sweater
                        OutfitItem(itemId=1356, price=9, goldPrice=5, color1=266, color2=266, itemType="Skirt"), # Ocean Blue Sparkly Dotted Mini
                        OutfitItem(itemId=3772, price=5, goldPrice=3, color1=285, color2=207, itemType="Shoes"), # Jazzberry Red Platform Espadrilles
                    ],
                ),
                ShopOutfit(
                    outfitId=8066,
                    items = [
                        OutfitItem(itemId=448, price=9, goldPrice=5, color1=195, color2=27, itemType="Shirt"), # Electric Blue Fabulous Fishy Top
                        OutfitItem(itemId=1361, price=9, goldPrice=5, color1=195, color2=27, itemType="Skirt"), # Electric Blue Fabulous Fishy Skirt
                        OutfitItem(itemId=3764, price=5, goldPrice=3, color1=195, color2=27, itemType="Shoes"), # Electric Blue Spider Web Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=8067,
                    items = [
                        OutfitItem(itemId=420, price=9, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Clever Cutout Tank
                        OutfitItem(itemId=1359, price=9, goldPrice=5, color1=45, color2=25, itemType="Skirt"), # Strawberry Red Mermaid Skirt
                        OutfitItem(itemId=3763, price=5, goldPrice=3, color1=45, color2=25, itemType="Shoes"), # Strawberry Red Banded Sandals
                    ],
                ),
                ShopOutfit(
                    outfitId=8068,
                    items = [
                        OutfitItem(itemId=444, price=9, goldPrice=5, color1=165, color2=152, itemType="Shirt"), # Spring Breeze Green Grecian Top
                        OutfitItem(itemId=1357, price=9, goldPrice=5, color1=165, color2=152, itemType="Skirt"), # Spring Breeze Green Grecian Skirt with Pale Purple Trim
                        OutfitItem(itemId=3737, price=5, goldPrice=3, color1=152, color2=165, itemType="Shoes"), # Pale Purple Sweet Strappy Shoes
                    ],
                ),
                ShopOutfit(
                    outfitId=8069,
                    items = [
                        OutfitItem(itemId=445, price=9, goldPrice=5, color1=235, color2=27, itemType="Shirt"), #  Tawny Orange Autumn Leaf Top
                        OutfitItem(itemId=1358, price=9, goldPrice=5, color1=235, color2=27, itemType="Skirt"), # Tawny Orange Autumn Leaf Skirt
                        OutfitItem(itemId=3768, price=5, goldPrice=3, color1=235, color2=27, itemType="Shoes"), #  Tawny Orange Autumn Leaf Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8070,
                    items = [
                        OutfitItem(itemId=465, price=9, goldPrice=5, color1=166, color2=152, itemType="Shirt"), # Snow White Crocheted Vest
                        OutfitItem(itemId=1390, price=9, goldPrice=5, color1=18, color2=152, itemType="Skirt"), # Waterfall Blue Patchwork Skirt
                        OutfitItem(itemId=3759, price=5, goldPrice=3, color1=152, color2=18, itemType="Shoes"), # Pale Purple Lace Flower Wedges
                    ],
                ),
                ShopOutfit(
                    outfitId=8071,
                    items = [
                        OutfitItem(itemId=2341, price=5, goldPrice=3, color1=220, color2=165, itemType="HeadItem"), # Dusty Pink Rose Crown with Spring Breeze Green Trim
                        OutfitItem(itemId=461, price=9, goldPrice=5, color1=239, color2=220, itemType="Shirt"), # Coffee Black Bitsy Bolero Top with Dusty Pink Trim
                        OutfitItem(itemId=1374, price=9, goldPrice=5, color1=220, color2=220, itemType="Skirt"), # Dusty Pink Bubble Skirt
                        OutfitItem(itemId=3769, price=5, goldPrice=3, color1=239, color2=220, itemType="Shoes"), # Coffee Black Desert Rose Boots
                    ],
                ),
                ShopOutfit(
                    outfitId=8072,
                    items = [
                        OutfitItem(itemId=440, price=9, goldPrice=5, color1=282, color2=200, itemType="Shirt"), # Magnolia White Heart Tee
                        OutfitItem(itemId=1362, price=9, goldPrice=5, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Fitted Formal Skirt
                        OutfitItem(itemId=3765, price=5, goldPrice=3, color1=200, color2=54, itemType="Shoes"), # Ruby Pink Ankle Warmer Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=8073,
                    items = [
                        OutfitItem(itemId=2344, price=5, goldPrice=3, color1=118, color2=168, itemType="HeadItem"), # Sapphire Blue Sailor Hat
                        OutfitItem(itemId=443, price=9, goldPrice=5, color1=63, color2=126, itemType="Shirt"), # Butterfly Blue Chevron Blouse
                        OutfitItem(itemId=1384, price=9, goldPrice=5, color1=63, color2=168, itemType="Skirt"), # Butterfly Blue Sailor Pants
                        OutfitItem(itemId=3775, price=5, goldPrice=3, color1=118, color2=168, itemType="Shoes"), # Sapphire Blue Bow Toe Flats
                    ],
                ),
                ShopOutfit(
                    outfitId=8074,
                    items = [
                        OutfitItem(itemId=449, price=9, goldPrice=5, color1=10, color2=234, itemType="Shirt"), # Cantaloupe Orange Chandelier Top
                        OutfitItem(itemId=1364, price=9, goldPrice=5, color1=10, color2=109, itemType="Skirt"), # Cantaloupe Orange Chandelier Skirt
                        OutfitItem(itemId=3738, price=5, goldPrice=3, color1=234, color2=10, itemType="Shoes"), # Flame Orange Bow Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=8075,
                    items = [
                        OutfitItem(itemId=2316, price=5, goldPrice=3, color1=282, color2=212, itemType="HeadItem"), # Magnolia White Pixie Diamond Headband
                        OutfitItem(itemId=475, price=9, goldPrice=5, color1=277, color2=282, itemType="Shirt"), # Misty Purple Pixie Diamonds Gown
                        OutfitItem(itemId=1392, price=9, goldPrice=5, color1=212, color2=282, itemType="Skirt"), # Indigo Purple Pixie Diamonds Skirt
                        OutfitItem(itemId=3740, price=5, goldPrice=3, color1=282, color2=212, itemType="Shoes"), # Magnolia White Pixie Diamond Heels
                    ],
                ),
                ShopOutfit(
                    outfitId=8076,
                    items = [
                        OutfitItem(itemId=474, price=9, goldPrice=5, color1=165, color2=168, itemType="Shirt"), # Spring Breeze Green Striking Twelve Top
                        OutfitItem(itemId=1389, price=9, goldPrice=5, color1=165, color2=168, itemType="Skirt"), # Spring Breeze Green Striking Twelve Skirt
                        OutfitItem(itemId=3675, price=5, goldPrice=3, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Glittering Glass Slippers
                    ],
                )
            ],
        ),

        ShopCollection(
            collectionId=43, # Post Office Accessories
            items=[
                ShopItem(itemId=2581, price=2, goldPrice=1, color1=230, color2=167, itemType="Necklace"), # Scarlet Red Flying V Guitar
                ShopItem(itemId=2589, price=2, goldPrice=1, color1=126, color2=93, itemType="Necklace"), # Raindrop Blue Keytar
                ShopItem(itemId=2590, price=2, goldPrice=1, color1=206, color2=161, itemType="Necklace"), # Raven Black Electric Guitar
                ShopItem(itemId=2554, price=2, goldPrice=1, color1=180, color2=27, itemType="Necklace"), # Seashell Blue Giant Bow Tie
                ShopItem(itemId=2040, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Silly Spectacles
                ShopItem(itemId=2180, price=5, goldPrice=3, color1=126, color2=207, itemType="HeadItem"), # Raindrop Blue Stars Are Out Cap
                ShopItem(itemId=1583, price=2, goldPrice=1, color1=30, color2=35, itemType="WristItem"), # Pumpkin Orange Trick or Treat Basket
                ShopItem(itemId=2213, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Wayfairy Glasses
                ShopItem(itemId=2214, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Fairy Spotter Specs
                ShopItem(itemId=2241, price=5, goldPrice=3, color1=197, color2=197, itemType="HeadItem"), # Electric Purple Fly Shutter Shades
                ShopItem(itemId=2038, price=5, goldPrice=3, color1=153, color2=166, itemType="HeadItem"), # Frostbunny Blue Cold Weather Hat
                ShopItem(itemId=2296, price=5, goldPrice=3, color1=175, color2=258, itemType="HeadItem"), # Creek Green Stripey Sleep Cap
                ShopItem(itemId=2137, price=5, goldPrice=3, color1=10, color2=228, itemType="HeadItem"), # Cantaloupe Orange Summer Snorkel
                ShopItem(itemId=1602, price=2, goldPrice=1, color1=2, color2=168, itemType="WristItem"), # Clover Green Tinkered Clover Sundial with Never Gold Trim
                ShopItem(itemId=1603, price=2, goldPrice=1, color1=152, color2=161, itemType="WristItem"), # Pale Purple Tinkered Leaf Sundial with Buried Treasure Brown Trim
                ShopItem(itemId=1605, price=2, goldPrice=1, color1=267, color2=168, itemType="WristItem"), # Celestial Blue Tinkered Jewel Sundial
                ShopItem(itemId=2163, price=5, goldPrice=3, color1=170, color2=232, itemType="HeadItem"), # Olive Green Silly Top Hat with Red Trim
                ShopItem(itemId=2627, price=2, goldPrice=1, color1=105, color2=93, itemType="Necklace"), # Siltstone Tan Acoustic Guitar with Tan Trim
                ShopItem(itemId=2399, price=5, goldPrice=3, color1=206, color2=226, itemType="HeadItem"), # Raven Black Painter's Beret
                ShopItem(itemId=1661, price=2, goldPrice=1, color1=108, color2=108, itemType="WristItem"), # Creamy Tan Painter's Palette
                ShopItem(itemId=2635, price=2, goldPrice=1, color1=168, color2=45, itemType="Necklace"), # Never Gold Winged Heart Necklace
                ShopItem(itemId=2276, price=5, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Wacky Rainbow Wig
                ShopItem(itemId=1573, price=2, goldPrice=1, color1=264, color2=1, itemType="WristItem"), # Jungle Green Tea Tray
            ],
        ),
        # Postcards. The client treats collections listed in postOfficeAssets.xml
        # <postCardCollections collectionsIds="7001,7002"> as postcards rather than
        # gift sets, and the AI mirrors that split (see POSTCARD_COLLECTION_IDS in
        # DistributedFairyShopkeeperNPCAI).
        ShopCollection(
            collectionId=7001, # Postcards (page 1)
            items=[
                ShopItem(itemId=88506, price=1, goldPrice=1), # Animal Masquerade
                ShopItem(itemId=88507, price=1, goldPrice=1), # Arrival Day
                ShopItem(itemId=88508, price=1, goldPrice=1), # Birthday
                ShopItem(itemId=88510, price=1, goldPrice=1), # Fairy Feast
                ShopItem(itemId=88511, price=1, goldPrice=1), # Fairy Friendship Festival
                ShopItem(itemId=88513, price=1, goldPrice=1), # Never Dove Egg Hunt
                ShopItem(itemId=88518, price=1, goldPrice=1), # Silly Days
                ShopItem(itemId=88519, price=1, goldPrice=1), # Summer Splash Party
                ShopItem(itemId=88521, price=1, goldPrice=1), # Great Winter Light-up
            ],
        ),
        ShopCollection(
            collectionId=7002, # Postcards (page 2)
            items=[
                ShopItem(itemId=88501, price=1, goldPrice=1), # Animal Derby
                ShopItem(itemId=88502, price=1, goldPrice=1), # Animal Friends
                ShopItem(itemId=88503, price=1, goldPrice=1), # Farewell to Animal Friends
                ShopItem(itemId=88504, price=1, goldPrice=1), # Flying Animal Friends
                ShopItem(itemId=88505, price=1, goldPrice=1), # Get Well
                ShopItem(itemId=88509, price=1, goldPrice=1), # Congratulations
                ShopItem(itemId=88512, price=1, goldPrice=1), # Classy Owl
                ShopItem(itemId=88515, price=1, goldPrice=1), # Spring
                ShopItem(itemId=88516, price=1, goldPrice=1), # Summer
                ShopItem(itemId=88514, price=1, goldPrice=1), # Autumn
                ShopItem(itemId=88517, price=1, goldPrice=1), # Winter
                ShopItem(itemId=88520, price=1, goldPrice=1), # Thank You
            ],
        ),
    ],
)