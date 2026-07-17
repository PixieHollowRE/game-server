from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

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
            items=[
                ShopItem(itemId=2262, price=5, goldPrice=3, color1=210, color2=210, itemType="HeadItem"), # Lotus Purple Tillandsia Headband
                ShopItem(itemId=329, price=9, goldPrice=5, color1=210, color2=210, itemType="Shirt"), # Lotus Purple Tillandsia Top
                ShopItem(itemId=625, price=2, goldPrice=1, color1=44, color2=44, itemType="Belt"), # Plumblossom Pink Tillandsia Sash
                ShopItem(itemId=1266, price=9, goldPrice=5, color1=210, color2=210, itemType="Skirt"), # Lotus Purple Tillandsia Skirt
                ShopItem(itemId=3689, price=5, goldPrice=3, color1=210, color2=210, itemType="Shoes"), # Lotus Purple Tillandsia Flats
                ShopItem(itemId=2263, price=5, goldPrice=3, color1=30, color2=30, itemType="HeadItem"), # Pumpkin Orange Pumpkin Headband
                ShopItem(itemId=330, price=9, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Pumpkin Bodice
                ShopItem(itemId=1267, price=9, goldPrice=5, color1=30, color2=30, itemType="Skirt"), # Pumpkin Orange Pumpkin Skirt
                ShopItem(itemId=3690, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Pumpkin Boots
                ShopItem(itemId=2062, price=5, goldPrice=3, color1=140, color2=140, itemType="HeadItem"), # Bunnynose Pink Curcuma Headband
                ShopItem(itemId=332, price=9, goldPrice=5, color1=162, color2=140, itemType="Shirt"), # Sunglow Yellow Curcuma Top
                ShopItem(itemId=1269, price=9, goldPrice=5, color1=162, color2=140, itemType="Skirt"), # Sunglow Yellow Curcuma Skirt
                ShopItem(itemId=3694, price=5, goldPrice=3, color1=162, color2=140, itemType="Shoes"), # Sunglow Yellow Curcuma Shoes
                ShopItem(itemId=2148, price=5, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Fresh Petal Barrette
                ShopItem(itemId=173, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Fresh Petal Bodice
                ShopItem(itemId=1157, price=9, goldPrice=5, color1=27, color2=27, itemType="Skirt"), # Corn Cob Yellow Fresh Petal Skirt
                ShopItem(itemId=3610, price=5, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Fresh Petal Pumps
                ShopItem(itemId=2063, price=5, goldPrice=3, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Pansy Headband
                ShopItem(itemId=64, price=9, goldPrice=5, color1=247, color2=247, itemType="Shirt"), # Jasmine Yellow Pansy Top
                ShopItem(itemId=1069, price=9, goldPrice=5, color1=247, color2=247, itemType="Skirt"), # Jasmine Yellow Pansy Skirt
                ShopItem(itemId=3551, price=5, goldPrice=3, color1=113, color2=113, itemType="Shoes"), # Pale Rose Red Pansy Slippers
                ShopItem(itemId=2122, price=5, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Delphinium Barrette
                ShopItem(itemId=111, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Delphinium Top
                ShopItem(itemId=1123, price=9, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Delphinium Skirt
                ShopItem(itemId=3581, price=5, goldPrice=3, color1=166, color2=166, itemType="Shoes"), # Snow White Delphinium Shoes
                ShopItem(itemId=2050, price=5, goldPrice=3, color1=201, color2=201, itemType="HeadItem"), # Velvet Red Gentian Original Headband
                ShopItem(itemId=331, price=9, goldPrice=5, color1=201, color2=201, itemType="Shirt"), # Velvet Red Gentian Top
                ShopItem(itemId=1268, price=9, goldPrice=5, color1=201, color2=201, itemType="Skirt"), # Velvet Red Gentian Skirt
                ShopItem(itemId=3691, price=5, goldPrice=3, color1=166, color2=166, itemType="Shoes"), # Snow White Gentian Shoes
                ShopItem(itemId=2421, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Cheery Cherry Headband
                ShopItem(itemId=1000054, price=9, goldPrice=5, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Cheery Cherry Top
                ShopItem(itemId=1669, price=2, goldPrice=1, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Cheery Cherry Clutch
                ShopItem(itemId=1461, price=9, goldPrice=5, color1=230, color2=230, itemType="Skirt"), # Scarlet Red Cheery Cherry Skirt
                ShopItem(itemId=3842, price=5, goldPrice=3, color1=230, color2=230, itemType="Shoes"), # Scarlet Red Cheery Cherry Heels
                ShopItem(itemId=2429, price=5, goldPrice=3, color1=226, color2=226, itemType="HeadItem"), # Goldenrod Yellow Starfruit Earrings
                ShopItem(itemId=1000062, price=9, goldPrice=5, color1=226, color2=226, itemType="Shirt"), # Goldenrod Yellow Starfruit Top
                ShopItem(itemId=1469, price=9, goldPrice=5, color1=226, color2=226, itemType="Skirt"), # Goldenrod Yellow Starfruit Skirt
                ShopItem(itemId=3854, price=5, goldPrice=3, color1=267, color2=226, itemType="Shoes"), # Celestial Blue Starfruit Heels with Goldenrod Yellow Trim
                ShopItem(itemId=2010, price=5, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Fanned Flower Clip
                ShopItem(itemId=284, price=9, goldPrice=5, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Layered Petal Top
                ShopItem(itemId=1234, price=9, goldPrice=5, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Layered Petal Skirt
                ShopItem(itemId=3539, price=5, goldPrice=3, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink White Rose Slippers
                ShopItem(itemId=2173, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Blooming Rose Headband
                ShopItem(itemId=295, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Formal Ruffle Top
                ShopItem(itemId=1236, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Formal Ruffle Skirt
                ShopItem(itemId=3718, price=5, goldPrice=3, color1=139, color2=139, itemType="Shoes"), # Seedling Green Ruffle Detail Shoes
                ShopItem(itemId=2639, price=5, goldPrice=3, color1=121, color2=121, itemType="Necklace"), # Daisy Pink Spring Rose Choker
                ShopItem(itemId=1000073, price=9, goldPrice=5, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Spring Rose Top
                ShopItem(itemId=653, price=2, goldPrice=1, color1=121, color2=121, itemType="Belt"), # Daisy Pink Spring Rose Sash
                ShopItem(itemId=1480, price=9, goldPrice=5, color1=207, color2=207, itemType="Skirt"), # Diamond Blue Spring Rose Skirt
                ShopItem(itemId=3865, price=5, goldPrice=3, color1=207, color2=207, itemType="Shoes"), # Diamond Blue Spring Rose Shoes
                ShopItem(itemId=2465, price=5, goldPrice=3, color1=264, color2=264, itemType="HeadItem"), # Jungle Green Posh Pineapple Fascinator
                ShopItem(itemId=1000109, price=9, goldPrice=5, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Posh Pineapple Top
                ShopItem(itemId=1001016, price=9, goldPrice=5, color1=162, color2=162, itemType="Skirt"), # Sunglow Yellow Posh Pineapple Skirt
                ShopItem(itemId=3892, price=5, goldPrice=3, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Posh Pineapple Pumps
                ShopItem(itemId=2448, price=5, goldPrice=3, color1=44, color2=44, itemType="HeadItem"), # Plumblossom Pink Sycamore Blossom Earrings
                ShopItem(itemId=1000077, price=9, goldPrice=5, color1=206, color2=206, itemType="Shirt"), # Raven Black Sycamore Leaf Top
                ShopItem(itemId=1483, price=9, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Sycamore Leaf Skirt
                ShopItem(itemId=3868, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Sycamore Leaf Shoes
                ShopItem(itemId=1000115, price=9, goldPrice=5, color1=17, color2=17, itemType="Shirt"), # Tendershoot Green Sweet Pea Petal Top
                ShopItem(itemId=1001021, price=9, goldPrice=5, color1=17, color2=17, itemType="Skirt"), # Tendershoot Green Sweet Pea Petal Skirt
                ShopItem(itemId=3897, price=5, goldPrice=3, color1=17, color2=17, itemType="Shoes"), # Tendershoot Green Sweet Pea Petal Shoes

            ],
        ),
        ShopCollection(
            collectionId=26, # Mainland Style Gift Sets
            items=[
                ShopItem(itemId=396, price=9, goldPrice=5, color1=224, color2=206, itemType="Shirt"), # Ivory White Unstoppable Top
                ShopItem(itemId=638, price=2, goldPrice=1, color1=206, color2=206, itemType="Belt"), # Raven Black Unstoppable Belt
                ShopItem(itemId=1321, price=9, goldPrice=5, color1=45, color2=206, itemType="Skirt"), # Strawberry Red Unstoppable Skirt
                ShopItem(itemId=3747, price=5, goldPrice=3, color1=206, color2=224, itemType="Shoes"), # Raven Black Sky High Laceups
                ShopItem(itemId=2327, price=5, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Alluring Elegance Hat
                ShopItem(itemId=408, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Alluring Elegance Dress Top
                ShopItem(itemId=1327, price=9, goldPrice=5, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Alluring Elegance Dress Bottom
                ShopItem(itemId=3750, price=5, goldPrice=3, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Alluring Elegance Sandals
                ShopItem(itemId=2187, price=5, goldPrice=3, color1=82, color2=82, itemType="HeadItem"), # Raspberry Red Button Headband
                ShopItem(itemId=401, price=9, goldPrice=5, color1=27, color2=27, itemType="Shirt"), # Corn Cob Yellow Bitsy Buttons Top
                ShopItem(itemId=1324, price=9, goldPrice=5, color1=27, color2=27, itemType="Skirt"), # Corn Cob Yellow Bitsy Buttons Skirt
                ShopItem(itemId=3656, price=5, goldPrice=3, color1=82, color2=82, itemType="Shoes"), # Raspberry Red One-Button Boots
                ShopItem(itemId=2621, price=2, goldPrice=1, color1=141, color2=141, itemType="Necklace"), # Thundercloud Gray Art Deco Necklace
                ShopItem(itemId=480, price=9, goldPrice=5, color1=182, color2=182, itemType="Shirt"), # Twilight Blue Sleek and Stylish Top
                ShopItem(itemId=1397, price=9, goldPrice=5, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Peplum Skirt
                ShopItem(itemId=3780, price=5, goldPrice=3, color1=182, color2=182, itemType="Shoes"), # Twilight Blue Stripey Wedges
                ShopItem(itemId=2208, price=5, goldPrice=3, color1=81, color2=81, itemType="HeadItem"), # Crimson Red Nifty Knit Hat
                ShopItem(itemId=479, price=9, goldPrice=5, color1=81, color2=81, itemType="Shirt"), # Crimson Red Funky Striped Tee
                ShopItem(itemId=1199, price=9, goldPrice=5, color1=185, color2=185, itemType="Skirt"), # Midnight Blue Knitted Gala Skirt
                ShopItem(itemId=3505, price=5, goldPrice=3, color1=75, color2=75, itemType="Shoes"), # Umber Brown Twirly Boots
                ShopItem(itemId=2398, price=5, goldPrice=3, color1=274, color2=274, itemType="HeadItem"), #  Bellflower Purple Trendy Accessory Set
                ShopItem(itemId=1000032, price=9, goldPrice=5, color1=274, color2=274, itemType="Shirt"), # Bellflower Purple Trendy Tied Shirt
                ShopItem(itemId=1660, price=2, goldPrice=1, color1=274, color2=274, itemType="WristItem"), # Bellflower Purple Multi-Bead Bracelet
                ShopItem(itemId=1443, price=9, goldPrice=5, color1=274, color2=274, itemType="Skirt"), # Bellflower Purple Buttoned Up Leggings
                ShopItem(itemId=3823, price=5, goldPrice=3, color1=274, color2=274, itemType="Shoes"), # Bellflower Purple Glitter Sneakers
                ShopItem(itemId=2346, price=5, goldPrice=3, color1=219, color2=219, itemType="HeadItem"), # Crystal Blue Fun Flower Headband
                ShopItem(itemId=1000060, price=9, goldPrice=5, color1=199, color2=199, itemType="Shirt"), # Cherryblossom Pink Flower Power Top
                ShopItem(itemId=651, price=2, goldPrice=1, color1=208, color2=208, itemType="Belt"), # Cerulean Blue Flower Power Belt
                ShopItem(itemId=1466, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Flower Power Skirt
                ShopItem(itemId=3847, price=5, goldPrice=3, color1=46, color2=46, itemType="Shoes"), # Bark Brown Moccasin Boots
                ShopItem(itemId=1000079, price=9, goldPrice=5, color1=218, color2=218, itemType="Shirt"), # Laurel Green Ruffled Petal Bolero
                ShopItem(itemId=1682, price=2, goldPrice=1, color1=265, color2=265, itemType="WristItem"), # Bright Sky Blue Ruffled Petal Purse
                ShopItem(itemId=1380, price=9, goldPrice=5, color1=258, color2=258, itemType="Skirt"), # Spearmint Green Single Ruffle Skirt
                ShopItem(itemId=3870, price=5, goldPrice=3, color1=265, color2=265, itemType="Shoes"), # Bright Sky Blue Strappy Platforms
                ShopItem(itemId=2443, price=5, goldPrice=3, color1=171, color2=171, itemType="HeadItem"), # Sunrise Yellow Sassy Chic Fedora
                ShopItem(itemId=1000090, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Sassy Chic Top
                ShopItem(itemId=1497, price=9, goldPrice=5, color1=166, color2=166, itemType="Skirt"), # Snow White Sassy Chic Skirt
                ShopItem(itemId=3875, price=5, goldPrice=3, color1=171, color2=171, itemType="Shoes"), # Sunrise Yellow Sassy Chic Boots
                ShopItem(itemId=2610, price=2, goldPrice=1, color1=134, color2=134, itemType="Necklace"), # Heather Purple Beaded Bud Necklace
                ShopItem(itemId=416, price=9, goldPrice=5, color1=134, color2=134, itemType="Shirt"), # Heather Purple Lace Flower Top
                ShopItem(itemId=1336, price=9, goldPrice=5, color1=134, color2=134, itemType="Skirt"), # Heather Purple Lace Flower Skirt
                ShopItem(itemId=3759, price=5, goldPrice=3, color1=134, color2=134, itemType="Shoes"), # Heather Purple Lace Flower Wedges
                ShopItem(itemId=2240, price=5, goldPrice=3, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Fancy Floral Headband
                ShopItem(itemId=298, price=9, goldPrice=5, color1=277, color2=277, itemType="Shirt"), # Misty Purple Fancy Formal Top
                ShopItem(itemId=1248, price=9, goldPrice=5, color1=277, color2=277, itemType="Skirt"), # Misty Purple Fancy Floral Skirt
                ShopItem(itemId=3676, price=5, goldPrice=3, color1=277, color2=277, itemType="Shoes"), # Misty Purple Fancy Formal Boots
                ShopItem(itemId=2391, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Cute and Cozy Cap
                ShopItem(itemId=1000026, price=9, goldPrice=5, color1=201, color2=201, itemType="Shirt"), # Velvet Red Stylish Buckle Vest
                ShopItem(itemId=1437, price=9, goldPrice=5, color1=201, color2=201, itemType="Skirt"), # Velvet Red Twist and Twirl Skirt
                ShopItem(itemId=3817, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Funky Laceup Boots
                ShopItem(itemId=2418, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Sailor Cloche
                ShopItem(itemId=1000053, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Sailor Top
                ShopItem(itemId=1460, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Sailor Striped Skirt
                ShopItem(itemId=3841, price=5, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Sailor Slippers
                ShopItem(itemId=2422, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Lovely Hearts Headband
                ShopItem(itemId=1000056, price=9, goldPrice=5, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Heart Keyhole Top
                ShopItem(itemId=1670, price=2, goldPrice=1, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Lovely Heart Purse
                ShopItem(itemId=1462, price=9, goldPrice=5, color1=230, color2=230, itemType="Skirt"), # Scarlet Red Lovely Hearts Skirt
                ShopItem(itemId=3843, price=5, goldPrice=3, color1=230, color2=230, itemType="Shoes"), # Scarlet Red Heart Buckle Boots
            ],
        ),


        ShopCollection(
            collectionId=3, # Tailoring Gift Sets - Sparrow men
            items=[
                ShopItem(itemId=2195, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Buckingham Fur Hat
                ShopItem(itemId=254, price=9, goldPrice=5, color1=82, color2=82, itemType="Shirt"), # Raspberry Red Buckingham Fur Coat
                ShopItem(itemId=616, price=2, goldPrice=1, color1=116, color2=116, itemType="Belt"), # Mushroom White Buckingham Belt
                ShopItem(itemId=1214, price=9, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Buckingham Fur Pants
                ShopItem(itemId=3648, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Buckingham Fur Boots
                ShopItem(itemId=233, price=9, goldPrice=5, color1=172, color2=172, itemType="Shirt"), # Forest Green Fur Trainer Jacket
                ShopItem(itemId=600, price=2, goldPrice=1, color1=56, color2=56, itemType="Belt"), # Bole Brown Fur Trainer Belt
                ShopItem(itemId=1197, price=9, goldPrice=5, color1=206, color2=206, itemType="Skirt"), # Raven Black Fur Trainer Pants
                ShopItem(itemId=3635, price=5, goldPrice=3, color1=56, color2=56, itemType="Shoes"), # Bole Brown Fur Trainer Boots
                ShopItem(itemId=264, price=9, goldPrice=5, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Striking Fur Top
                ShopItem(itemId=615, price=2, goldPrice=1, color1=59, color2=59, itemType="Belt"), # Bunny Brown Striking Fur Belt
                ShopItem(itemId=1213, price=9, goldPrice=5, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Striking Fur Pants
                ShopItem(itemId=3649, price=5, goldPrice=3, color1=206, color2=186, itemType="Shoes"), # Raven Black Striking Fur Boots with Yellow Trim
                ShopItem(itemId=2192, price=5, goldPrice=3, color1=60, color2=60, itemType="HeadItem"), # Tyrian Purple Birdie Best Cap
                ShopItem(itemId=245, price=9, goldPrice=5, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Birdie Best Top
                ShopItem(itemId=607, price=2, goldPrice=1, color1=169, color2=169, itemType="Belt"), # Squirrel Gray Birdie Best Belt
                ShopItem(itemId=3642, price=5, goldPrice=3, color1=169, color2=169, itemType="Shoes"), # Squirrel Gray Birdie Best Shoes
                ShopItem(itemId=240, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Tailor's Top
                ShopItem(itemId=606, price=2, goldPrice=1, color1=13, color2=13, itemType="Belt"), # Coral Pink Tailor's Utility Belt
                ShopItem(itemId=1203, price=9, goldPrice=5, color1=73, color2=73, itemType="Skirt"), # Grape Purple Tailor's Trousers
                ShopItem(itemId=3637, price=5, goldPrice=3, color1=87, color2=87, itemType="Shoes"), # Driftwood Brown Tailor's Boots
                ShopItem(itemId=267, price=9, goldPrice=5, color1=113, color2=113, itemType="Shirt"), # Pale Rose Red Knit Messenger Top
                ShopItem(itemId=620, price=2, goldPrice=1, color1=177, color2=177, itemType="Belt"), # Mud Brown Knit Messenger Belt
                ShopItem(itemId=1216, price=9, goldPrice=5, color1=93, color2=93, itemType="Skirt"), # Maple Brown Knit Messenger Pants
                ShopItem(itemId=3653, price=5, goldPrice=3, color1=177, color2=177, itemType="Shoes"), # Mud Brown Knit Messenger Slippers
                ShopItem(itemId=241, price=9, goldPrice=5, color1=161, color2=161, itemType="Shirt"), # Buried Treasure Brown Lightning Bead Coat
                ShopItem(itemId=1202, price=9, goldPrice=5, color1=91, color2=91, itemType="Skirt"), # Coconut Brown Lightning Bead Pants
                ShopItem(itemId=3593, price=5, goldPrice=3, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Ivy Wrap Slippers
                ShopItem(itemId=2189, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White All Buttons Visor
                ShopItem(itemId=234, price=9, goldPrice=5, color1=267, color2=267, itemType="Shirt"), # Celestial Blue Button Down Jacket
                ShopItem(itemId=1198, price=9, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Button Down Pants
                ShopItem(itemId=3636, price=5, goldPrice=3, color1=215, color2=215, itemType="Shoes"), # Pewter Gray Button Down Shoes
            ],
        ),
        ShopCollection(
            collectionId=19, # Costume Gift Sets
            items=[
                ShopItem(itemId=2193, price=5, goldPrice=3, color1=75, color2=75, itemType="HeadItem"), # Umber Brown Never West Round Up Hat
                ShopItem(itemId=2568, price=2, goldPrice=1, color1=171, color2=171, itemType="Necklace"), # Sunrise Yellow Never West Necklace
                ShopItem(itemId=246, price=9, goldPrice=5, color1=92, color2=92, itemType="Shirt"), # Hawk Brown Never West Shirt
                ShopItem(itemId=608, price=2, goldPrice=1, color1=171, color2=171, itemType="Belt"), # Sunrise Yellow Never West Belt
                ShopItem(itemId=1206, price=9, goldPrice=5, color1=75, color2=75, itemType="Skirt"), # Umber Brown Never West Trousers
                ShopItem(itemId=3643, price=5, goldPrice=3, color1=171, color2=171, itemType="Shoes"), # Sunrise Yellow Never West Boots
                ShopItem(itemId=2415, price=5, goldPrice=3, color1=172, color2=172, itemType="HeadItem"), # Forest Green Calla Lily Hat
                ShopItem(itemId=1000050, price=9, goldPrice=5, color1=172, color2=172, itemType="Shirt"), # Forest Green Calla Lily Top
                ShopItem(itemId=649, price=2, goldPrice=1, color1=76, color2=76, itemType="Belt"), # Chocolate Brown Calla Lily Belt
                ShopItem(itemId=1457, price=9, goldPrice=5, color1=76, color2=76, itemType="Skirt"), # Chocolate Brown Calla Lily Pants
                ShopItem(itemId=3838, price=5, goldPrice=3, color1=172, color2=172, itemType="Shoes"), # Forest Green Calla Lily Boots
                ShopItem(itemId=2289, price=5, goldPrice=3, color1=1, color2=1, itemType="HeadItem"), # Mint Green Clover Hat
                ShopItem(itemId=2593, price=2, goldPrice=1, color1=1, color2=1, itemType="Necklace"), # Mint Green Clover Bowtie
                ShopItem(itemId=350, price=9, goldPrice=5, color1=1, color2=1, itemType="Shirt"), # Mint Green Clover Vest
                ShopItem(itemId=1286, price=9, goldPrice=5, color1=1, color2=1, itemType="Skirt"), # Mint Green Clover Knickers
                ShopItem(itemId=3710, price=5, goldPrice=3, color1=1, color2=1, itemType="Shoes"), # Mint Green Clover Boots
                ShopItem(itemId=2361, price=5, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Wizard Beard
                ShopItem(itemId=498, price=9, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Wizard Top
                ShopItem(itemId=1414, price=9, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Wizard Robe
                ShopItem(itemId=3792, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Wizard Boots
                ShopItem(itemId=291, price=9, goldPrice=5, color1=145, color2=145, itemType="Shirt"), #  Tinker Bell Green Tinker Training Jersey
                ShopItem(itemId=1245, price=9, goldPrice=5, color1=186, color2=186, itemType="Skirt"), # Honeycomb Yellow Tinker Training Shorts
                ShopItem(itemId=3668, price=5, goldPrice=3, color1=166, color2=145, itemType="Shoes"), #  Snow White All-Terrain Training Shoes with Tinker Bell Green Trim
                ShopItem(itemId=289, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Garden Training Jersey
                ShopItem(itemId=1242, price=9, goldPrice=5, color1=174, color2=166, itemType="Skirt"), # Rosetta Red Garden Training Shorts with Snow White Trim
                ShopItem(itemId=3668, price=5, goldPrice=3, color1=174, color2=174, itemType="Shoes"), #  Rosetta Red All-Terrain Training Shoes
                ShopItem(itemId=292, price=9, goldPrice=5, color1=176, color2=126, itemType="Shirt"), # Silvermist Blue Water Training Jersey with Raindrop Blue Trim
                ShopItem(itemId=1244, price=9, goldPrice=5, color1=126, color2=126, itemType="Skirt"), # Raindrop Blue Water Training Shorts
                ShopItem(itemId=3668, price=5, goldPrice=3, color1=176, color2=176, itemType="Shoes"), #  Silvermist Blue All-Terrain Training Shoes
                ShopItem(itemId=288, price=9, goldPrice=5, color1=178, color2=237, itemType="Shirt"), # Fawn Orange Animal Training Jersey with Cantaloupe Orange Trim
                ShopItem(itemId=1241, price=9, goldPrice=5, color1=237, color2=237, itemType="Skirt"), # Cantaloupe Orange Animal Training Shorts
                ShopItem(itemId=3666, price=5, goldPrice=3, color1=178, color2=178, itemType="Shoes"), # Fawn Orange Super Winged Sneakers
                ShopItem(itemId=290, price=9, goldPrice=5, color1=47, color2=111, itemType="Shirt"), # Iridessa Yellow Light Training Jersey with Sparkling Yellow Trim
                ShopItem(itemId=1243, price=9, goldPrice=5, color1=111, color2=111, itemType="Skirt"), # Sparkling Yellow Light Training Shorts
                ShopItem(itemId=3668, price=5, goldPrice=3, color1=47, color2=47, itemType="Shoes"), # Iridessa Yellow All-Terrain Training Shoes
                ShopItem(itemId=2278, price=5, goldPrice=3, color1=224, color2=224, itemType="HeadItem"), # Ivory White Soft-Serve Hat
                ShopItem(itemId=348, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Candy Fanatic Marshmallow Top
                ShopItem(itemId=1284, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Candy Fanatic Licorice Shorts
                ShopItem(itemId=3708, price=5, goldPrice=3, color1=45, color2=45, itemType="Shoes"), # Strawberry Red Candy Fanatic Jellybean Shoes
                ShopItem(itemId=2362, price=5, goldPrice=3, color1=114, color2=114, itemType="HeadItem"), # Foxtail Orange Fox Mask
                ShopItem(itemId=497, price=9, goldPrice=5, color1=143, color2=143, itemType="Shirt"), # June Bug Green Fox Costume Top
                ShopItem(itemId=1413, price=9, goldPrice=5, color1=143, color2=143, itemType="Skirt"), # June Bug Green Fox Trousers
                ShopItem(itemId=3793, price=5, goldPrice=3, color1=224, color2=224, itemType="Shoes"), # Ivory White Fox Boots
            ],
        ),
        ShopCollection(
            collectionId=33, # Famous Fairy Gift Sets
            items=[
                ShopItem(itemId=176, price=9, goldPrice=5, color1=75, color2=75, itemType="Shirt"), # Umber Brown Terence's Top
                ShopItem(itemId=1160, price=9, goldPrice=5, color1=75, color2=75, itemType="Skirt"), # Umber Brown Terence's Trunks
                ShopItem(itemId=3613, price=5, goldPrice=3, color1=86, color2=86, itemType="Shoes"), # Nutmeg Brown Terence's Shoes
                ShopItem(itemId=2152, price=5, goldPrice=3, color1=186, color2=186, itemType="HeadItem"), # Honeycomb Yellow Bobble's Goggles
                ShopItem(itemId=179, price=9, goldPrice=5, color1=65, color2=65, itemType="Shirt"), # Summer Green Bobble Vest
                ShopItem(itemId=575, price=2, goldPrice=1, color1=46, color2=46, itemType="Belt"), # Bark Brown Bobble Belt
                ShopItem(itemId=1161, price=9, goldPrice=5, color1=125, color2=125, itemType="Skirt"), # Pine Green Bobble Trunks
                ShopItem(itemId=3576, price=5, goldPrice=3, color1=125, color2=125, itemType="Shoes"), # Pine Green Wide Band Boots
                ShopItem(itemId=180, price=9, goldPrice=5, color1=64, color2=64, itemType="Shirt"), # Emerald Green Clank's Top
                ShopItem(itemId=1162, price=9, goldPrice=5, color1=125, color2=125, itemType="Skirt"), # Pine Green Clank's Trunks
                ShopItem(itemId=3576, price=5, goldPrice=3, color1=125, color2=125, itemType="Shoes"), # Pine Green Wide Band Boots
                ShopItem(itemId=1000010, price=9, goldPrice=5, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Sled's Top
                ShopItem(itemId=1425, price=9, goldPrice=5, color1=216, color2=216, itemType="Skirt"), # Slate Gray Sled's Trousers
                ShopItem(itemId=3800, price=5, goldPrice=3, color1=153, color2=153, itemType="Shoes"), # Frostbunny Blue Sled's Shoes
            ],
        ),
    


        ShopCollection(
            collectionId=27, # Costume Gift Sets
            items=[
                ShopItem(itemId=2216, price=5, goldPrice=3, color1=206, color2=167, itemType="HeadItem"), # Raven Black Bewitching Hat with Never Silver Trim
                ShopItem(itemId=482, price=9, goldPrice=5, color1=206, color2=167, itemType="Shirt"), # Raven Black Bewitching Top with Never Silver Trim
                ShopItem(itemId=1586, price=2, goldPrice=1, color1=206, color2=167, itemType="WristItem"), # Buried Treasure Brown Bewitching Twig Broom
                ShopItem(itemId=1399, price=9, goldPrice=5, color1=206, color2=167, itemType="Skirt"), # Raven Black Bewitching Skirt with Never Silver Trim
                ShopItem(itemId=3674, price=5, goldPrice=3, color1=206, color2=167, itemType="Shoes"), # Raven Black Bewitching Boots with Never Silver Trim
                ShopItem(itemId=2238, price=5, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Spring Peacock Headband
                ShopItem(itemId=317, price=9, goldPrice=5, color1=221, color2=221, itemType="Shirt"), # Jade Green Spring Peacock Top
                ShopItem(itemId=1256, price=9, goldPrice=5, color1=221, color2=221, itemType="Skirt"), # Jade Green Spring Peacock Skirt
                ShopItem(itemId=3684, price=5, goldPrice=3, color1=221, color2=221, itemType="Shoes"), # Jade Green Spring Peacock Shoes
                ShopItem(itemId=2239, price=5, goldPrice=3, color1=169, color2=169, itemType="HeadItem"), # Squirrel Gray Fluffy Owl Fascinator
                ShopItem(itemId=321, price=9, goldPrice=5, color1=166, color2=169, itemType="Shirt"), # Snow White Feather Accent Capelet with Squirrel Gray Trim
                ShopItem(itemId=1261, price=9, goldPrice=5, color1=166, color2=169, itemType="Skirt"), # Snow White Layered Feather Skirt with Squirrel Gray Trim
                ShopItem(itemId=3687, price=5, goldPrice=3, color1=166, color2=169, itemType="Shoes"), # Snow White Feathered Ankle Boots with Squirrel Gray Trim
                ShopItem(itemId=2017, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Tulip Petal Bow
                ShopItem(itemId=327, price=9, goldPrice=5, color1=126, color2=126, itemType="Shirt"), # Raindrop Blue Wonderland Top
                ShopItem(itemId=1265, price=9, goldPrice=5, color1=126, color2=126, itemType="Skirt"), # Raindrop Blue Wonderland Skirt
                ShopItem(itemId=3688, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Wonderland Shoes
                ShopItem(itemId=2083, price=5, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Mer-Made Crown
                ShopItem(itemId=400, price=9, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Magical Mermaid Top
                ShopItem(itemId=1323, price=9, goldPrice=5, color1=208, color2=208, itemType="Skirt"), # Cerulean Blue Magical Mermaid Skirt
                ShopItem(itemId=3675, price=5, goldPrice=3, color1=208, color2=208, itemType="Shoes"), # Cerulean Blue Glittering Glass Slippers
            ],
        ),
        ShopCollection(
            collectionId=30, # Fashion Boutique Gift Sets
            items=[
                ShopItem(itemId=447, price=9, goldPrice=5, color1=200, color2=200, itemType="Shirt"), # Ruby Pink Tri-Color Top
                ShopItem(itemId=1642, price=2, goldPrice=1, color1=200, color2=200, itemType="WristItem"), #  Ruby Pink Spangled Clutch
                ShopItem(itemId=1360, price=9, goldPrice=5, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Tri-Color Skirt
                ShopItem(itemId=3716, price=5, goldPrice=3, color1=27, color2=27, itemType="Shoes"), # Corn Cob Yellow Morpho Butterfly Shoes
                ShopItem(itemId=460, price=9, goldPrice=5, color1=180, color2=180, itemType="Shirt"), # Seashell Blue Furry Vest
                ShopItem(itemId=1377, price=9, goldPrice=5, color1=180, color2=180, itemType="Skirt"), # Seashell Blue Sweet Stripey Skirt
                ShopItem(itemId=3778, price=5, goldPrice=3, color1=180, color2=180, itemType="Shoes"), #  Seashell Blue Colorblock Wedges
                ShopItem(itemId=427, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Sweater Dress Top
                ShopItem(itemId=1347, price=9, goldPrice=5, color1=69, color2=69, itemType="Skirt"), # Powder Blue Sweater Dress Skirt
                ShopItem(itemId=3739, price=5, goldPrice=3, color1=224, color2=224, itemType="Shoes"), #  Ivory White Casual Moccasins
                ShopItem(itemId=426, price=9, goldPrice=5, color1=266, color2=266, itemType="Shirt"), # Ocean Blue Cozy Coat
                ShopItem(itemId=1343, price=9, goldPrice=5, color1=225, color2=225, itemType="Skirt"), # Eggplant Purple Skinny Jeans
                ShopItem(itemId=3773, price=5, goldPrice=3, color1=236, color2=236, itemType="Shoes"), # Dusty Brown Comfy Slip-Ons
                ShopItem(itemId=424, price=9, goldPrice=5, color1=211, color2=211, itemType="Shirt"), # Gentian Purple Cropped Cardigan
                ShopItem(itemId=1345, price=9, goldPrice=5, color1=275, color2=275, itemType="Skirt"), # Shadowy Purple Big Bow Skirt
                ShopItem(itemId=3767, price=5, goldPrice=3, color1=74, color2=74, itemType="Shoes"), # Soil Brown Knee Boots
                ShopItem(itemId=2317, price=5, goldPrice=3, color1=45, color2=239, itemType="HeadItem"), # Strawberry Red Blooming Headband with Coffee Black Trim
                ShopItem(itemId=464, price=9, goldPrice=5, color1=224, color2=224, itemType="Shirt"), # Ivory White Charleston Top
                ShopItem(itemId=1383, price=9, goldPrice=5, color1=224, color2=224, itemType="Skirt"), # Ivory White Charleston Skirt
                ShopItem(itemId=3777, price=5, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Charleston Heels
                ShopItem(itemId=433, price=9, goldPrice=5, color1=208, color2=208, itemType="Shirt"), # Cerulean Blue Zippy Top
                ShopItem(itemId=1351, price=9, goldPrice=5, color1=268, color2=268, itemType="Skirt"), # Navy Blue Zippy Skirt
                ShopItem(itemId=3774, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Roller Skates
                ShopItem(itemId=456, price=9, goldPrice=5, color1=282, color2=282, itemType="Shirt"), # Magnolia White Sassy Suspender Top
                ShopItem(itemId=1372, price=9, goldPrice=5, color1=165, color2=165, itemType="Skirt"), # Spring Breeze Green Layered Shorts
                ShopItem(itemId=3760, price=5, goldPrice=3, color1=206, color2=206, itemType="Shoes"), # Raven Black Trinket Toe Flats
                ShopItem(itemId=469, price=9, goldPrice=5, color1=285, color2=285, itemType="Shirt"), # Jazzberry Red Cropped Sweater
                ShopItem(itemId=1356, price=9, goldPrice=5, color1=266, color2=266, itemType="Skirt"), # Ocean Blue Sparkly Dotted Mini
                ShopItem(itemId=3772, price=5, goldPrice=3, color1=285, color2=285, itemType="Shoes"), # Jazzberry Red Platform Espadrilles
                ShopItem(itemId=448, price=9, goldPrice=5, color1=195, color2=195, itemType="Shirt"), # Electric Blue Fabulous Fishy Top
                ShopItem(itemId=1361, price=9, goldPrice=5, color1=195, color2=195, itemType="Skirt"), # Electric Blue Fabulous Fishy Skirt
                ShopItem(itemId=3764, price=5, goldPrice=3, color1=195, color2=195, itemType="Shoes"), # Electric Blue Spider Web Heels
                ShopItem(itemId=420, price=9, goldPrice=5, color1=45, color2=45, itemType="Shirt"), # Strawberry Red Clever Cutout Tank
                ShopItem(itemId=1359, price=9, goldPrice=5, color1=45, color2=45, itemType="Skirt"), # Strawberry Red Mermaid Skirt
                ShopItem(itemId=3763, price=5, goldPrice=3, color1=45, color2=45, itemType="Shoes"), # Strawberry Red Banded Sandals
                ShopItem(itemId=444, price=9, goldPrice=5, color1=165, color2=165, itemType="Shirt"), # Spring Breeze Green Grecian Top
                ShopItem(itemId=1357, price=9, goldPrice=5, color1=165, color2=152, itemType="Skirt"), # Spring Breeze Green Grecian Skirt with Pale Purple Trim
                ShopItem(itemId=3737, price=5, goldPrice=3, color1=152, color2=152, itemType="Shoes"), # Pale Purple Sweet Strappy Shoes
                ShopItem(itemId=445, price=9, goldPrice=5, color1=235, color2=235, itemType="Shirt"), #  Tawny Orange Autumn Leaf Top
                ShopItem(itemId=1358, price=9, goldPrice=5, color1=235, color2=235, itemType="Skirt"), # Tawny Orange Autumn Leaf Skirt
                ShopItem(itemId=3768, price=5, goldPrice=3, color1=235, color2=235, itemType="Shoes"), #  Tawny Orange Autumn Leaf Boots
                ShopItem(itemId=465, price=9, goldPrice=5, color1=166, color2=166, itemType="Shirt"), # Snow White Crocheted Vest
                ShopItem(itemId=1390, price=9, goldPrice=5, color1=18, color2=18, itemType="Skirt"), # Waterfall Blue Patchwork Skirt
                ShopItem(itemId=3759, price=5, goldPrice=3, color1=152, color2=152, itemType="Shoes"), # Pale Purple Lace Flower Wedges
                ShopItem(itemId=2341, price=5, goldPrice=3, color1=220, color2=165, itemType="HeadItem"), # Dusty Pink Rose Crown with Spring Breeze Green Trim
                ShopItem(itemId=461, price=9, goldPrice=5, color1=239, color2=220, itemType="Shirt"), # Coffee Black Bitsy Bolero Top with Dusty Pink Trim
                ShopItem(itemId=1374, price=9, goldPrice=5, color1=220, color2=220, itemType="Skirt"), # Dusty Pink Bubble Skirt
                ShopItem(itemId=3769, price=5, goldPrice=3, color1=239, color2=239, itemType="Shoes"), # Coffee Black Desert Rose Boots
                ShopItem(itemId=440, price=9, goldPrice=5, color1=282, color2=282, itemType="Shirt"), # Magnolia White Heart Tee
                ShopItem(itemId=1362, price=9, goldPrice=5, color1=200, color2=200, itemType="Skirt"), # Ruby Pink Fitted Formal Skirt
                ShopItem(itemId=3765, price=5, goldPrice=3, color1=200, color2=200, itemType="Shoes"), # Ruby Pink Ankle Warmer Heels
                ShopItem(itemId=2344, price=5, goldPrice=3, color1=118, color2=118, itemType="HeadItem"), # Sapphire Blue Sailor Hat
                ShopItem(itemId=443, price=9, goldPrice=5, color1=63, color2=63, itemType="Shirt"), # Butterfly Blue Chevron Blouse
                ShopItem(itemId=1384, price=9, goldPrice=5, color1=63, color2=63, itemType="Skirt"), # Butterfly Blue Sailor Pants
                ShopItem(itemId=3775, price=5, goldPrice=3, color1=118, color2=118, itemType="Shoes"), # Sapphire Blue Bow Toe Flats
                ShopItem(itemId=449, price=9, goldPrice=5, color1=10, color2=10, itemType="Shirt"), # Cantaloupe Orange Chandelier Top
                ShopItem(itemId=1364, price=9, goldPrice=5, color1=10, color2=10, itemType="Skirt"), # Cantaloupe Orange Chandelier Skirt
                ShopItem(itemId=3738, price=5, goldPrice=3, color1=234, color2=234, itemType="Shoes"), # Flame Orange Bow Heels
                ShopItem(itemId=2316, price=5, goldPrice=3, color1=282, color2=282, itemType="HeadItem"), # Magnolia White Pixie Diamond Headband
                ShopItem(itemId=475, price=9, goldPrice=5, color1=277, color2=277, itemType="Shirt"), # Misty Purple Pixie Diamonds Gown
                ShopItem(itemId=1392, price=9, goldPrice=5, color1=212, color2=212, itemType="Skirt"), # Indigo Purple Pixie Diamonds Skirt
                ShopItem(itemId=3740, price=5, goldPrice=3, color1=282, color2=282, itemType="Shoes"), # Magnolia White Pixie Diamond Heels
                ShopItem(itemId=474, price=9, goldPrice=5, color1=165, color2=165, itemType="Shirt"), # Spring Breeze Green Striking Twelve Top
                ShopItem(itemId=1389, price=9, goldPrice=5, color1=165, color2=165, itemType="Skirt"), # Spring Breeze Green Striking Twelve Skirt
                ShopItem(itemId=3675, price=5, goldPrice=3, color1=165, color2=165, itemType="Shoes"), # Spring Breeze Green Glittering Glass Slippers
            ],
        ),

        ShopCollection(
            collectionId=43, # Post Office Accessories
            items=[
                ShopItem(itemId=2581, price=2, goldPrice=1, color1=230, color2=230, itemType="Necklace"), # Scarlet Red Flying V Guitar
                ShopItem(itemId=2589, price=2, goldPrice=1, color1=126, color2=126, itemType="Necklace"), # Raindrop Blue Keytar
                ShopItem(itemId=2590, price=2, goldPrice=1, color1=206, color2=206, itemType="Necklace"), # Raven Black Electric Guitar
                ShopItem(itemId=2554, price=2, goldPrice=1, color1=180, color2=180, itemType="Necklace"), # Seashell Blue Giant Bow Tie
                ShopItem(itemId=2040, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Silly Spectacles
                ShopItem(itemId=2180, price=5, goldPrice=3, color1=126, color2=126, itemType="HeadItem"), # Raindrop Blue Stars Are Out Cap
                ShopItem(itemId=1583, price=2, goldPrice=1, color1=30, color2=30, itemType="WristItem"), # Pumpkin Orange Trick or Treat Basket
                ShopItem(itemId=2213, price=5, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Wayfairy Glasses
                ShopItem(itemId=2214, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Fairy Spotter Specs
                ShopItem(itemId=2241, price=5, goldPrice=3, color1=197, color2=197, itemType="HeadItem"), # Electric Purple Fly Shutter Shades
                ShopItem(itemId=2038, price=5, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Cold Weather Hat
                ShopItem(itemId=2296, price=5, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Stripey Sleep Cap
                ShopItem(itemId=2137, price=5, goldPrice=3, color1=10, color2=10, itemType="HeadItem"), # Cantaloupe Orange Summer Snorkel
                ShopItem(itemId=1602, price=2, goldPrice=1, color1=2, color2=168, itemType="WristItem"), # Clover Green Tinkered Clover Sundial with Never Gold Trim
                ShopItem(itemId=1603, price=2, goldPrice=1, color1=152, color2=161, itemType="WristItem"), # Pale Purple Tinkered Leaf Sundial with Buried Treasure Brown Trim
                ShopItem(itemId=1605, price=2, goldPrice=1, color1=267, color2=267, itemType="WristItem"), # Celestial Blue Tinkered Jewel Sundial
                ShopItem(itemId=2163, price=5, goldPrice=3, color1=170, color2=230, itemType="HeadItem"), # Olive Green Silly Top Hat with Red Trim
                ShopItem(itemId=2627, price=2, goldPrice=1, color1=105, color2=108, itemType="Necklace"), # Siltstone Tan Acoustic Guitar with Tan Trim
                ShopItem(itemId=2399, price=5, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Painter's Beret
                ShopItem(itemId=1661, price=2, goldPrice=1, color1=108, color2=108, itemType="WristItem"), # Creamy Tan Painter's Palette
                ShopItem(itemId=263, price=2, goldPrice=1, color1=168, color2=168, itemType="Necklace"), # Never Gold Winged Heart Necklace
                ShopItem(itemId=2276, price=5, goldPrice=3, color1=166, color2=166, itemType="HeadItem"), # Snow White Wacky Rainbow Wig
                ShopItem(itemId=1573, price=2, goldPrice=1, color1=264, color2=264, itemType="WristItem"), # Jungle Green Tea Tray
            ],
        ),
        ShopCollection(
            collectionId=5,
            outfits=[
                ShopOutfit(
                    outfitId=2001, # Outfit of the Month
                    items=[
                        OutfitItem(itemId=2388, goldPrice=30, color1=41, color2=209, itemType="HeadItem"),
                        OutfitItem(itemId=1000090, goldPrice=0, color1=209, color2=40, itemType="Shirt"),
                        OutfitItem(itemId=1077, goldPrice=0, color1=49, color2=40, itemType="Skirt"),
                        OutfitItem(itemId=647, goldPrice=0, color1=41, color2=40, itemType="Belt"),
                        OutfitItem(itemId=3870, goldPrice=0, color1=41, color2=40, itemType="Shoes"),
                    ],
                ),

                ShopOutfit(
                    outfitId=2002, # Tillandsia Dress
                    items=[
                        OutfitItem(itemId=2262, goldPrice=20, color1=210, color2=210, itemType="HeadItem"),
                        OutfitItem(itemId=329, goldPrice=0, color1=210, color2=44, itemType="Shirt"),
                        OutfitItem(itemId=1266, goldPrice=0, color1=210, color2=44, itemType="Skirt"),
                        OutfitItem(itemId=625, goldPrice=0, color1=44, color2=44, itemType="Belt"),
                        OutfitItem(itemId=3689, goldPrice=0, color1=210, color2=210, itemType="Shoes"),
                    ],
                ),
                ShopOutfit(
                    outfitId=2003, # Pumpkim' Dress
                    items=[
                        OutfitItem(itemId=2263, goldPrice=20, color1=30, color2=30, itemType="HeadItem"),
                        OutfitItem(itemId=330, goldPrice=0, color1=206, color2=30, itemType="Shirt"),
                        OutfitItem(itemId=1267, goldPrice=0, color1=30, color2=30, itemType="Skirt"),
                        OutfitItem(itemId=3690, goldPrice=0, color1=206, color2=30, itemType="Shoes"),
                    ],
                ),
                ShopOutfit(
                    outfitId=2004, # Curcuma Dress
                    items=[
                        OutfitItem(itemId=2062, goldPrice=20, color1=140, color2=0, itemType="HeadItem"),
                        OutfitItem(itemId=332, goldPrice=0, color1=162, color2=140, itemType="Shirt"),
                        OutfitItem(itemId=1269, goldPrice=0, color1=162, color2=140, itemType="Skirt"),
                        OutfitItem(itemId=3694, goldPrice=0, color1=162, color2=140, itemType="Shoes"),
                    ],
                ),
            ],
        ),
    ],
)