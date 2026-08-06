from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.PurchaseType import PurchaseType
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.TREETOP_HOUSEWARES,
    shopId=1003,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.TRINKET,
        position=(425, 444),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_TRINKET
    ),
    collections=[
        ShopCollection(
            collectionId=1030, # Trinket's Faves
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=7555, price=40, goldPrice=4, color1=48, color2=139), # Sea Green Tinkering Glass
                ShopItem(itemId=7502, price=40, goldPrice=4, color1=152, color2=0), # Pale Purple Pollen Carrier Collection
                ShopItem(itemId=7504, price=40, goldPrice=4, color1=23, color2=0), # Breezy Blue Posy Pillow
                ShopItem(itemId=6517, price=40, goldPrice=4, color1=38, color2=0), # Apple Green Dewdrop Mirror
                ShopItem(itemId=7581, price=40, goldPrice=4, color1=37, color2=90), # Cloudy Blue Tinker Pot with Yellow Trim
                ShopItem(itemId=7580, price=40, goldPrice=4, color1=24, color2=118), # Sky Blue Honey Jar
                ShopItem(itemId=7549, price=40, goldPrice=4, color1=46, color2=115), # Bark Brown Acorn Timer
                ShopItem(itemId=7506, price=40, goldPrice=4, color1=121, color2=48), # Daisy Pink Lucky Fortune Flower
                ShopItem(itemId=7521, price=40, goldPrice=4, color1=79, color2=0), # Sienna Brown Forest Bins
                ShopItem(itemId=7004, price=40, goldPrice=4, color1=121, color2=0), # Daisy Pink Petal Candle
                ShopItem(itemId=7571, price=40, goldPrice=4, color1=46, color2=79), # Bark Brown Bear Doll
                ShopItem(itemId=7505, price=40, goldPrice=4, color1=110, color2=0), # Rosy Pink Crocus Bulb Pitcher
            ],
        ),
        ShopCollection(
            collectionId=1062, # Animal Friend Beds
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=6641, price=40, goldPrice=4, color1=27, color2=170), # Corn Cob Yellow Dandelion Bed
                ShopItem(itemId=6590, price=40, goldPrice=4, color1=152, color2=73), # Pale Purple Cool and Comfy Bed
                ShopItem(itemId=6592, price=40, goldPrice=4, color1=141, color2=126), # Thundercloud Gray Walnut Safety Bed
                ShopItem(itemId=6594, price=40, goldPrice=4, color1=108, color2=139), # Creamy Tan Twig Nest with Green Trim
                ShopItem(itemId=6596, price=40, goldPrice=4, color1=68, color2=131), # Huckleberry Blue Lotus Flower Bed
                ShopItem(itemId=6591, price=40, goldPrice=4, color1=134, color2=5), # Heather Purple Bottlecap Bed
                ShopItem(itemId=6593, price=40, goldPrice=4, color1=138, color2=254), # Persimmon Orange Lazy Daisy Bed
                ShopItem(itemId=6595, price=40, goldPrice=4, color1=108, color2=267), # Creamy Tan Wide Wicker Bed with Bright Blue Trim
                ShopItem(itemId=6597, price=40, goldPrice=4, color1=186, color2=234), # Honeycomb Yellow Cottonfluff Napping Bed
                ShopItem(itemId=6642, price=40, goldPrice=4, color1=18, color2=186), # Waterfall Blue Bee Bed
            ]
        ) ,
        ShopCollection(
            collectionId=1004, # Chairs, Sofas, and Benches
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=6502, price=40, goldPrice=4, color1=116, color2=116), # Mushroom White Swirled Toadstool Chairs
                ShopItem(itemId=6509, price=40, goldPrice=4, color1=15, color2=15), # Lilac Purple Blossom Bench
                ShopItem(itemId=6513, price=40, goldPrice=4, color1=247, color2=247), # Jasmine Yellow Sunflower Loveseat
                ShopItem(itemId=6515, price=40, goldPrice=4, color1=35, color2=35), # Celery Green Leaf Lounger
                ShopItem(itemId=6545, price=40, goldPrice=4, color1=261, color2=258), # Kelly Green Big Comfy Chair
                ShopItem(itemId=6551, price=40, goldPrice=4, color1=129, color2=152), # Fig Purple Bean Bag Chair
                ShopItem(itemId=6552, price=40, goldPrice=4, color1=99, color2=91), # Papyrus Tan Neverwood Chair
                ShopItem(itemId=6565, price=40, goldPrice=4, color1=261, color2=175), # Kelly Green Comfy Clover Chair
                ShopItem(itemId=6568, price=40, goldPrice=4, color1=230, color2=40), # Scarlet Red Glittery Gem Stool
                ShopItem(itemId=6571, price=40, goldPrice=4, color1=230, color2=40), # Scarlet Red Glittery Gem Chair
                ShopItem(itemId=6573, price=40, goldPrice=4, color1=206, color2=206), # Raven Black Playing Card Lounger
                ShopItem(itemId=6574, price=40, goldPrice=4, color1=123, color2=167), # Squash Orange Thimble-made Chair
                ShopItem(itemId=6577, price=40, goldPrice=4, color1=125, color2=166), # Pine Green Lost and Found Sofa
                ShopItem(itemId=6583, price=40, goldPrice=4, color1=152, color2=152), # Pale Purple High Backed Tea Chair
                ShopItem(itemId=6609, price=40, goldPrice=4, color1=99, color2=99), # Papyrus Tan Teacher's Chair
                ShopItem(itemId=6627, price=40, goldPrice=4, color1=84, color2=215), # Copper Brown Great Gears Sofa with Pewter Gray Trim
                ShopItem(itemId=6629, price=40, goldPrice=4, color1=84, color2=215), # Copper Brown Great Gears Chair with Pewter Gray Trim
                ShopItem(itemId=6632, price=40, goldPrice=4, color1=161, color2=208), # Buried Treasure Brown Farmhouse Side Chair
                ShopItem(itemId=6633, price=40, goldPrice=4, color1=162, color2=189), # Sunglow Yellow Hay There!
                ShopItem(itemId=6635, price=40, goldPrice=4, color1=95, color2=95), # Sparrow Brown Cedar Chair
                ShopItem(itemId=6639, price=40, goldPrice=4, color1=99, color2=35), # Papyrus Tan Student's Chair with Celery Green Trim
                ShopItem(itemId=6647, price=40, goldPrice=4, color1=207, color2=207), # Diamond Blue Chilly Couch
                ShopItem(itemId=6648, price=40, goldPrice=4, color1=207, color2=207), # Diamond Blue Chilly Chair
                ShopItem(itemId=6651, price=40, goldPrice=4, color1=224, color2=230), # Ivory White Sit Sweetly Chair
                ShopItem(itemId=6652, price=40, goldPrice=4, color1=224, color2=230), # Ivory White Sit Sweetly Sofa
                ShopItem(itemId=6656, price=40, goldPrice=4, color1=110, color2=139), # Rosy Pink Rose Recliner with Seedling Green Trim
                ShopItem(itemId=6661, price=40, goldPrice=4, color1=166, color2=35), # Snow White Rainbow Sofa
                ShopItem(itemId=6682, price=40, goldPrice=4, color1=135, color2=135), # Boysenberry Purple Chroma Chair
                ShopItem(itemId=6686, price=40, goldPrice=4, color1=91, color2=91), # Coconut Brown Sweet Tooth Bench
                ShopItem(itemId=6687, price=40, goldPrice=4, color1=154, color2=138), # Beetle Brown Turkey Feather Chair with Persimmon Orange Trim
                ShopItem(itemId=6690, price=40, goldPrice=4, color1=18, color2=91), # Waterfall Blue Cottonfluff Couch
                ShopItem(itemId=6691, price=40, goldPrice=4, color1=18, color2=91), # Waterfall Blue Cottonfluff Stool
                ShopItem(itemId=6694, price=40, goldPrice=4, color1=167, color2=74), # Never Silver Tasty Treat Seat
                ShopItem(itemId=6700, price=40, goldPrice=4, color1=89, color2=74), # Seashore Brown Jelly Donut Pillow Seat
                ShopItem(itemId=6701, price=40, goldPrice=4, color1=224, color2=46), # Ivory White Marshmallow Stool
                ShopItem(itemId=6702, price=40, goldPrice=4, color1=56, color2=98), # Bole Brown Pinecone Throne
                ShopItem(itemId=6712, price=40, goldPrice=4, color1=230, color2=106), # Scarlet Red Friendship Chair with Butternut Tan Trim
                ShopItem(itemId=6721, price=40, goldPrice=4, color1=261, color2=90), # Kelly Green Overgrown Bench
                ShopItem(itemId=6722, price=40, goldPrice=4, color1=261, color2=90), # Kelly Green Overgrown Chair
                ShopItem(itemId=6724, price=40, goldPrice=4, color1=45, color2=85), # Strawberry Red Wacky Chair
                ShopItem(itemId=6728, price=40, goldPrice=4, color1=199, color2=121), # Cherryblossom Pink Flitter Flutter Couch
                ShopItem(itemId=6729, price=40, goldPrice=4, color1=199, color2=121), # Cherryblossom Pink Flitter Flutter Chair
                ShopItem(itemId=6738, price=40, goldPrice=4, color1=216, color2=277), # Slate Gray Garden Hearts Bench
                ShopItem(itemId=6739, price=40, goldPrice=4, color1=277, color2=216), # Misty Purple Garden Hearts Chair
                ShopItem(itemId=6742, price=40, goldPrice=4, color1=99, color2=89), # Papyrus Tan Sunflower Chair
                ShopItem(itemId=6743, price=40, goldPrice=4, color1=224, color2=135), # Ivory White Teacup Chair with Boysenberry Purple Trim
                ShopItem(itemId=6745, price=40, goldPrice=4, color1=89, color2=106), # Seashore Brown Rustic Chair with Butternut Tan Trim
                ShopItem(itemId=6746, price=40, goldPrice=4, color1=89, color2=106), # Seashore Brown Rustic Bench with Butternut Tan Trim
                ShopItem(itemId=6750, price=40, goldPrice=4, color1=69, color2=230), # Powder Blue Seashell Lounger
                ShopItem(itemId=6754, price=40, goldPrice=4, color1=91, color2=267), # Coconut Brown Pretty Planter Bench
                ShopItem(itemId=6755, price=40, goldPrice=4, color1=258, color2=152), # Spearmint Green Beautiful Blossoms Bench
                ShopItem(itemId=6756, price=40, goldPrice=4, color1=247, color2=76), # Jasmine Yellow Sunflower Bench
                ShopItem(itemId=6759, price=40, goldPrice=4, color1=207, color2=180), # Diamond Blue Periwinkle Lounger
                ShopItem(itemId=6760, price=40, goldPrice=4, color1=91, color2=91), # Coconut Brown Snowy Bench
                ShopItem(itemId=6762, price=40, goldPrice=4, color1=18, color2=119), # Waterfall Blue Aurora Chair
                ShopItem(itemId=6763, price=40, goldPrice=4, color1=154, color2=143), # Beetle Brown Water Bog Bench
                ShopItem(itemId=6773, price=40, goldPrice=4, color1=30, color2=266), # Pumpkin Orange Anemone Bean Bag Chair
                ShopItem(itemId=7699, price=40, goldPrice=4, color1=99, color2=143), # Papyrus Tan Leaf Pram
            ]
        ),
        ShopCollection(
            collectionId=1008, # Tables and Surfaces
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=6507, price=40, goldPrice=4, color1=116, color2=116), # Mushroom White Toadstool Tableset
                ShopItem(itemId=6508, price=40, goldPrice=4, color1=139, color2=139), # Seedling Green Tenderleaf Table
                ShopItem(itemId=6511, price=40, goldPrice=4, color1=224, color2=224), # Ivory White Lily Nightstand
                ShopItem(itemId=6512, price=40, goldPrice=4, color1=113, color2=113), # Pale Rose Red Tulip Leaf Table
                ShopItem(itemId=6535, price=40, goldPrice=4, color1=128, color2=128), # Carnation White Eggshell Tea Table
                ShopItem(itemId=6536, price=40, goldPrice=4, color1=64, color2=64), # Emerald Green Carved Riverstone Table
                ShopItem(itemId=6542, price=40, goldPrice=4, color1=125, color2=125), # Pine Green Lily Pad Sponge Table
                ShopItem(itemId=6543, price=40, goldPrice=4, color1=99, color2=70), # Papyrus Tan Tinker's Workbench
                ShopItem(itemId=6546, price=40, goldPrice=4, color1=79, color2=161), # Sienna Brown Dear Diary Desk
                ShopItem(itemId=6547, price=40, goldPrice=4, color1=224, color2=83), # Ivory White Elegant Vanity
                ShopItem(itemId=6548, price=40, goldPrice=4, color1=274, color2=154), # Bellflower Purple Tea Table
                ShopItem(itemId=6559, price=40, goldPrice=4, color1=45, color2=236), # Strawberry Red Harvest Table
                ShopItem(itemId=6567, price=40, goldPrice=4, color1=267, color2=27), # Celestial Blue Glittery Gem Table
                ShopItem(itemId=6572, price=40, goldPrice=4, color1=230, color2=167), # Scarlet Red Thimble-made Table
                ShopItem(itemId=6581, price=40, goldPrice=4, color1=152, color2=129), # Pale Purple Leaf Top Tea Table
                ShopItem(itemId=6582, price=40, goldPrice=4, color1=152, color2=129), # Pale Purple Leaf Top Tea Side Table
                ShopItem(itemId=6608, price=40, goldPrice=4, color1=85, color2=74), # Quail Brown Everything Table
                ShopItem(itemId=6625, price=40, goldPrice=4, color1=84, color2=215), # Copper Brown Great Gears Dinette with Pewter Gray Trim
                ShopItem(itemId=6628, price=40, goldPrice=4, color1=84, color2=215), # Copper Brown Great Gears Side Table with Pewter Gray Trim
                ShopItem(itemId=6631, price=40, goldPrice=4, color1=99, color2=99), # Papyrus Tan Farmhouse Table
                ShopItem(itemId=6634, price=40, goldPrice=4, color1=267, color2=30), # Celestial Blue Pumpkin Picnic Table
                ShopItem(itemId=6637, price=40, goldPrice=4, color1=99, color2=224), # Papyrus Tan Teacher's Desk with Ivory White Trim
                ShopItem(itemId=6638, price=40, goldPrice=4, color1=99, color2=35), # Papyrus Tan Student's Desk with Celery Green Trim
                ShopItem(itemId=6646, price=40, goldPrice=4, color1=207, color2=207), # Diamond Blue Chilly Table
                ShopItem(itemId=6653, price=40, goldPrice=4, color1=111, color2=230), # Sparkling Yellow Sit Sweetly Table
                ShopItem(itemId=6679, price=40, goldPrice=4, color1=154, color2=216), # Beetle Brown Picnic Table with Slate Gray Trim
                ShopItem(itemId=6683, price=40, goldPrice=4, color1=125, color2=166), # Pine Green Harvest Buffet Table
                ShopItem(itemId=6684, price=40, goldPrice=4, color1=162, color2=207), # Sunglow Yellow Sweet Wheat Table with Diamond Blue Trim
                ShopItem(itemId=6685, price=40, goldPrice=4, color1=88, color2=88), # Fruitwood Brown Artiste Table
                ShopItem(itemId=6697, price=40, goldPrice=4, color1=220, color2=227), # Dusty Pink Silver Trees Table
                ShopItem(itemId=6698, price=40, goldPrice=4, color1=91, color2=96), # Coconut Brown Pinecone Table
                ShopItem(itemId=6706, price=40, goldPrice=4, color1=236, color2=236), # Dusty Brown Puzzle Piece Table
                ShopItem(itemId=6707, price=40, goldPrice=4, color1=236, color2=236), # Dusty Brown Corner Piece Table
                ShopItem(itemId=6708, price=40, goldPrice=4, color1=236, color2=236), # Dusty Brown End Piece Table
                ShopItem(itemId=6714, price=40, goldPrice=4, color1=230, color2=106), # Scarlet Red Friendship Table with Butternut Tan Trim
                ShopItem(itemId=6725, price=40, goldPrice=4, color1=45, color2=89), # Strawberry Red Wacky Side Table
                ShopItem(itemId=6726, price=40, goldPrice=4, color1=45, color2=89), # Strawberry Red Wacky Coffee Table
                ShopItem(itemId=6731, price=40, goldPrice=4, color1=199, color2=121), # Cherryblossom Pink Flitter Flutter Table
                ShopItem(itemId=6736, price=40, goldPrice=4, color1=269, color2=216), # Crisp White Garden Hearts Table
                ShopItem(itemId=6741, price=40, goldPrice=4, color1=215, color2=247), # Pewter Gray Sunflower Table with Jasmine Yellow Trim
                ShopItem(itemId=6744, price=40, goldPrice=4, color1=89, color2=106), # Seashore Brown Rustic Table with Butternut Tan Trim
                ShopItem(itemId=6749, price=40, goldPrice=4, color1=154, color2=161), # Beetle Brown Beachy Side Table with Buried Treasure Brown Trim
                ShopItem(itemId=6761, price=40, goldPrice=4, color1=18, color2=119), # Waterfall Blue Aurora Table
                ShopItem(itemId=6777, price=40, goldPrice=4, color1=267, color2=168), # Celestial Blue Desert Nights Vanity
            ]
        ),
        ShopCollection(
            collectionId=1012, # Art and Wall Decor
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=6576, price=40, goldPrice=4, color1=215, color2=93), # Pewter Gray Lost and Found Mirror
                ShopItem(itemId=6585, price=40, goldPrice=4, color1=162, color2=267), # Sunglow Yellow Landscape Stained Glass
                ShopItem(itemId=6586, price=40, goldPrice=4, color1=230, color2=207), # Scarlet Red Single Rose Stained Glass
                ShopItem(itemId=6587, price=40, goldPrice=4, color1=190, color2=268), # Firefly Green Firefly Stained Glass
                ShopItem(itemId=7545, price=40, goldPrice=4, color1=18, color2=18), # Waterfall Blue Oyster Shell Mirror
                ShopItem(itemId=7559, price=40, goldPrice=4, color1=287, color2=218), # Dianthus Red Berry Wreath
                ShopItem(itemId=7560, price=40, goldPrice=4, color1=218, color2=129), # Laurel Green Harvest Garland
                ShopItem(itemId=7589, price=40, goldPrice=4, color1=196, color2=101), # Electric Orange Drama Poster
                ShopItem(itemId=7591, price=40, goldPrice=4, color1=177, color2=177), # Mud Brown Cake, Cherry, Cherry, Treat
                ShopItem(itemId=7592, price=40, goldPrice=4, color1=91, color2=143), # Coconut Brown Crouching Bunny
                ShopItem(itemId=7646, price=40, goldPrice=4, color1=194, color2=193), # Electric Pink Ribbon Streamers
                ShopItem(itemId=7677, price=40, goldPrice=4, color1=79, color2=79), # Sienna Brown Never Dove Portrait
                ShopItem(itemId=7680, price=40, goldPrice=4, color1=99, color2=99), # Papyrus Tan Rainbow Stained Glass
                ShopItem(itemId=7689, price=40, goldPrice=4, color1=98, color2=35), # Sandstone Tan Mother Chipmunk
                ShopItem(itemId=7696, price=40, goldPrice=4, color1=207, color2=185), # Diamond Blue Mother Owl
                ShopItem(itemId=7697, price=40, goldPrice=4, color1=27, color2=204), # Corn Cob Yellow Mother Bunny
                ShopItem(itemId=7762, price=40, goldPrice=4, color1=45, color2=125), # Strawberry Red Peppermint Wreath with Pine Green Trim
                ShopItem(itemId=7763, price=40, goldPrice=4, color1=224, color2=151), # Ivory White Lovely Lily Wreath
                ShopItem(itemId=7764, price=40, goldPrice=4, color1=84, color2=230), # Copper Brown Friendship Mirror with Scarlet Red Trim
                ShopItem(itemId=7767, price=40, goldPrice=4, color1=203, color2=151), # Shadow Green Overgrown Mirror
                ShopItem(itemId=7770, price=40, goldPrice=4, color1=230, color2=3), # Scarlet Red Rambling Rose Wreath
                ShopItem(itemId=7778, price=40, goldPrice=4, color1=267, color2=90), # Celestial Blue Daisy Wreath
                ShopItem(itemId=7784, price=40, goldPrice=4, color1=154, color2=154), # Beetle Brown Baby Animal Portrait
                ShopItem(itemId=7844, price=40, goldPrice=4, color1=155, color2=207), # Frosty Blue Flitterific Crystal Strand
                ShopItem(itemId=7845, price=40, goldPrice=4, color1=155, color2=207), # Frosty Blue Ice Blossom Crystal Strand
                ShopItem(itemId=7861, price=40, goldPrice=4, color1=18, color2=119), # Waterfall Blue Aurora Mirror
                ShopItem(itemId=7585, price=40, goldPrice=4, color1=208, color2=155), # Cerulean Blue Fairy Light Catcher
                ShopItem(itemId=7645, price=40, goldPrice=4, color1=155, color2=207), # Frosty Blue Lovely Snowflake Ornament
                ShopItem(itemId=7654, price=40, goldPrice=4, color1=155, color2=207), # Frosty Blue Dainty Snowflake Ornament
                ShopItem(itemId=6544, price=40, goldPrice=4, color1=99, color2=128), # Papyrus Tan Cozy Fireplace
                ShopItem(itemId=6588, price=40, goldPrice=4, color1=95, color2=86), # Sparrow Brown Piping Hot Fireplace
                ShopItem(itemId=7637, price=40, goldPrice=4, color1=0, color2=0), # Lizzy's Artwork
                ShopItem(itemId=7864, price=40, goldPrice=4, color1=69, color2=5), # Powder Blue Flitterific Fairy Frame
                ShopItem(itemId=7855, price=40, goldPrice=4, color1=99, color2=99), # Papyrus Tan Snowy Window
                ShopItem(itemId=7710, price=40, goldPrice=4, color1=154, color2=203), # Beetle Brown Palm Window Frame
            ]
        ),
        ShopCollection(
            collectionId=1013, # Rugs and Drapery
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=6505, price=40, goldPrice=4, color1=45, color2=45), # Strawberry Red Maple Mat
                ShopItem(itemId=6506, price=40, goldPrice=4, color1=139, color2=139), # Seedling Green Lily Pad Mat
                ShopItem(itemId=6518, price=40, goldPrice=4, color1=35, color2=35), # Celery Green Oak Throw Rug
                ShopItem(itemId=6538, price=40, goldPrice=4, color1=127, color2=127), # Grasshopper Green Leaf Panel Curtains
                ShopItem(itemId=6549, price=40, goldPrice=4, color1=194, color2=195), # Electric Pink Dance Pad
                ShopItem(itemId=6563, price=40, goldPrice=4, color1=264, color2=21), # Jungle Green Clover Curtain
                ShopItem(itemId=6564, price=40, goldPrice=4, color1=264, color2=21), # Jungle Green Small Clover Cluster Rug
                ShopItem(itemId=6566, price=40, goldPrice=4, color1=264, color2=21), # Jungle Green Large Clover Cluster Rug
                ShopItem(itemId=6636, price=40, goldPrice=4, color1=45, color2=98), # Strawberry Red Maple Drapes
                ShopItem(itemId=6688, price=40, goldPrice=4, color1=18, color2=18), # Waterfall Blue Cottonfluff Rug
                ShopItem(itemId=6776, price=40, goldPrice=4, color1=136, color2=129), # Peacock Blue Flying Carpet
                ShopItem(itemId=7516, price=40, goldPrice=4, color1=224, color2=224), # Ivory White Spider Silk Curtains
                ShopItem(itemId=7634, price=40, goldPrice=4, color1=282, color2=35), # Magnolia White Lizzy's Lace Curtains
                ShopItem(itemId=7681, price=40, goldPrice=4, color1=230, color2=36), # Scarlet Red Rose Window Drapery
                ShopItem(itemId=7694, price=40, goldPrice=4, color1=35, color2=57), # Celery Green Leafy curtains
                ShopItem(itemId=7703, price=40, goldPrice=4, color1=174, color2=130), # Rosetta Red Garden-Talent Pennant
                ShopItem(itemId=7704, price=40, goldPrice=4, color1=178, color2=78), # Fawn Orange Animal-Talent Pennant
                ShopItem(itemId=7705, price=40, goldPrice=4, color1=145, color2=115), # Tinker Bell Green Tinker-Talent Pennant
                ShopItem(itemId=7706, price=40, goldPrice=4, color1=176, color2=133), # Silvermist Blue Water-Talent Pennant
                ShopItem(itemId=7707, price=40, goldPrice=4, color1=179, color2=74), # Iridessa Yellow Light-Talent Pennant
                ShopItem(itemId=7709, price=40, goldPrice=4, color1=44, color2=69), # Plumblossom Pink Seashell Country Curtains with Powder Blue Trim
                ShopItem(itemId=7743, price=40, goldPrice=4, color1=172, color2=150), # Forest Green Mossy Drapes with Dry Moss Green Trim
                ShopItem(itemId=7772, price=40, goldPrice=4, color1=121, color2=199), # Daisy Pink Flitter Flutter Curtains
                ShopItem(itemId=7786, price=40, goldPrice=4, color1=145, color2=145), # Tinker Bell Green Troop Turtle Pennant
                ShopItem(itemId=7818, price=40, goldPrice=4, color1=178, color2=74), # Fawn Orange Troop Rabbit Pennant
                ShopItem(itemId=7819, price=40, goldPrice=4, color1=176, color2=133), # Silvermist Blue Troop Otter Pennant
                ShopItem(itemId=7820, price=40, goldPrice=4, color1=179, color2=74), # Iridessa Yellow Troop Glowworm Pennant
                ShopItem(itemId=7821, price=40, goldPrice=4, color1=174, color2=156), # Rosetta Red Troop Butterfly Pennant
                ShopItem(itemId=7880, price=40, goldPrice=4, color1=69, color2=69), # Powder Blue Rainbow Rug
                ShopItem(itemId=7831, price=40, goldPrice=4, color1=224, color2=227), # Ivory White Cobweb Curtains with Moonlight Gray Trim
            ]
        ),
        ShopCollection(
            collectionId=1009, # Lamps and Chandeliers
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=7001, price=40, goldPrice=4, color1=26, color2=26), # Raspberry Pink Tulip Floor Lamp
                ShopItem(itemId=7002, price=40, goldPrice=4, color1=27, color2=27), # Corn Cob Yellow Buttercup Floor Lamp
                ShopItem(itemId=6501, price=40, goldPrice=4, color1=277, color2=277), # Misty Purple Seedpod Fan
                ShopItem(itemId=7003, price=40, goldPrice=4, color1=267, color2=267), # Celestial Blue Daisy Table Lamp
                ShopItem(itemId=7005, price=40, goldPrice=4, color1=30, color2=11), # Pumpkin Orange Glowing Gourd Lamp
                ShopItem(itemId=7006, price=40, goldPrice=4, color1=116, color2=116), # Mushroom White Hanging Hibiscus Lantern
                ShopItem(itemId=7007, price=40, goldPrice=4, color1=258, color2=258), # Spearmint Green Rose of Sharon Lamp
                ShopItem(itemId=7008, price=40, goldPrice=4, color1=189, color2=189), # Ladybug Red Toadstool Table Lamp
                ShopItem(itemId=7014, price=40, goldPrice=4, color1=165, color2=125), # Spring Breeze Green Curly Glow Lamp
                ShopItem(itemId=7015, price=40, goldPrice=4, color1=139, color2=59), # Seedling Green Leaf Basket Lantern
                ShopItem(itemId=7016, price=40, goldPrice=4, color1=129, color2=5), # Fig Purple All-Night Glow Light
                ShopItem(itemId=7017, price=40, goldPrice=4, color1=99, color2=230), # Papyrus Tan Hanging Heart Lanterns
                ShopItem(itemId=7018, price=40, goldPrice=4, color1=171, color2=162), # Sunrise Yellow Candelabra
                ShopItem(itemId=7019, price=40, goldPrice=4, color1=18, color2=119), # Waterfall Blue Sweet Tea Light
                ShopItem(itemId=7020, price=40, goldPrice=4, color1=194, color2=35), # Electric Pink Hanging Flower Light with Celery Green Trim
                ShopItem(itemId=7021, price=40, goldPrice=4, color1=99, color2=74), # Papyrus Tan Tiki Light
                ShopItem(itemId=7023, price=40, goldPrice=4, color1=30, color2=35), # Pumpkin Orange Pumpkin Lamp with Celery Green Trim
                ShopItem(itemId=7024, price=40, goldPrice=4, color1=99, color2=74), # Papyrus Tan Tiki Torch
                ShopItem(itemId=7025, price=40, goldPrice=4, color1=18, color2=46), # Waterfall Blue Cottonfluff Lamp
                ShopItem(itemId=6569, price=40, goldPrice=4, color1=267, color2=90), # Celestial Blue Glittery Chandelier
                ShopItem(itemId=7026, price=40, goldPrice=4, color1=116, color2=89), # Mushroom White Soft Serve Lamp
                ShopItem(itemId=7027, price=40, goldPrice=4, color1=35, color2=90), # Celery Green Cheerful Corn Lamp
                ShopItem(itemId=7029, price=40, goldPrice=4, color1=56, color2=203), # Bole Brown Pinecone Lamp
                ShopItem(itemId=7030, price=40, goldPrice=4, color1=56, color2=161), # Bole Brown Pinecone Candles
                ShopItem(itemId=7031, price=40, goldPrice=4, color1=230, color2=121), # Scarlet Red Friendship Lamp
                ShopItem(itemId=7032, price=40, goldPrice=4, color1=45, color2=89), # Strawberry Red Peppermint Light
                ShopItem(itemId=7033, price=40, goldPrice=4, color1=261, color2=151), # Kelly Green Overgrown Lamp
                ShopItem(itemId=7034, price=40, goldPrice=4, color1=199, color2=121), # Cherryblossom Pink Flitter Flutter Lamp
                ShopItem(itemId=7035, price=40, goldPrice=4, color1=45, color2=89), # Strawberry Red Wacky Lamp
                ShopItem(itemId=7036, price=40, goldPrice=4, color1=70, color2=19), # Tinker Blue Radiant Bloom Lamp
                ShopItem(itemId=7037, price=40, goldPrice=4, color1=171, color2=171), # Sunrise Yellow Plentiful Petal Lamp
                ShopItem(itemId=7038, price=40, goldPrice=4, color1=5, color2=134), # Wysteria Purple Perfect Petal Lamp
                ShopItem(itemId=7039, price=40, goldPrice=4, color1=99, color2=162), # Papyrus Tan Sunflower Lamp
                ShopItem(itemId=7040, price=40, goldPrice=4, color1=264, color2=254), # Jungle Green Blissflower Chandelier
                ShopItem(itemId=7042, price=40, goldPrice=4, color1=224, color2=215), # Ivory White Teacup Candle
                ShopItem(itemId=7044, price=40, goldPrice=4, color1=30, color2=35), # Pumpkin Orange Gourd Lights with Celery Green Trim
                ShopItem(itemId=7045, price=40, goldPrice=4, color1=239, color2=167), # Coffee Black Spider Web Lantern
                ShopItem(itemId=7046, price=40, goldPrice=4, color1=215, color2=262), # Pewter Gray Spider Web Chandelier
                ShopItem(itemId=7047, price=40, goldPrice=4, color1=216, color2=216), # Slate Gray Glowing Lamppost
                ShopItem(itemId=7048, price=40, goldPrice=4, color1=18, color2=119), # Waterfall Blue Aurora Candle
                ShopItem(itemId=7049, price=40, goldPrice=4, color1=30, color2=30), # Pumpkin Orange Jellyfish Lamp
                ShopItem(itemId=7051, price=40, goldPrice=4, color1=45, color2=116), # Strawberry Red Mushroom Lamps
                ShopItem(itemId=7052, price=40, goldPrice=4, color1=162, color2=168), # Sunglow Yellow Desert Nights Lamp
                ShopItem(itemId=7053, price=40, goldPrice=4, color1=199, color2=121), # Cherryblossom Pink Starbright Lamp with Daisy Pink Trim
                ShopItem(itemId=7054, price=40, goldPrice=4, color1=135, color2=135), # Boysenberry Purple Starlight Lamp
                ShopItem(itemId=7644, price=40, goldPrice=4, color1=207, color2=207), # Diamond Blue Icy Chandelier
                ShopItem(itemId=7664, price=40, goldPrice=4, color1=16, color2=180), # Camellia Pink Winter Wonderland Lanterns
                ShopItem(itemId=7671, price=40, goldPrice=4, color1=230, color2=143), # Scarlet Red Rosebud Chandelier
                ShopItem(itemId=7679, price=40, goldPrice=4, color1=126, color2=126), # Raindrop Blue Raincloud Chandelier
                ShopItem(itemId=7739, price=40, goldPrice=4, color1=168, color2=70), # Never Gold Never Mine Gem Fan
                ShopItem(itemId=7742, price=40, goldPrice=4, color1=56, color2=59), # Bole Brown Pinecone Candle
                ShopItem(itemId=7745, price=40, goldPrice=4, color1=28, color2=128), # Cinnamon Brown Cinnamon Roll Candle Trio
                ShopItem(itemId=7747, price=40, goldPrice=4, color1=99, color2=128), # Papyrus Tan Branch n' Bough Chandelier
                ShopItem(itemId=7790, price=40, goldPrice=4, color1=215, color2=254), # Pewter Gray Sunflower Chandelier
                ShopItem(itemId=7830, price=40, goldPrice=4, color1=30, color2=239), # Pumpkin Orange Jack O'Lantern Stand with Coffee Black Trim
                ShopItem(itemId=7846, price=40, goldPrice=4, color1=155, color2=207), # Frosty Blue Ice Crystal Chandelier
                ShopItem(itemId=7878, price=40, goldPrice=4, color1=99, color2=99), # Papyrus Tan Rainbow Lamp
                ShopItem(itemId=7897, price=40, goldPrice=4, color1=30, color2=267), # Pumpkin Orange Octopus Chandelier
            ]
        )
    ],
)