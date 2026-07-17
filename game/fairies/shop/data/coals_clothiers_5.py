from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
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
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
                ShopItem(itemId=484, price=45, goldPrice=16, color1=45, color2=248, itemType="Shirt"), # Strawberry Red Varsity Jacket
                ShopItem(itemId=1651, price=25, goldPrice=6, color1=78, color2=224, itemType="WristItem"), # Fawn Brown Football
                ShopItem(itemId=1172, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Dry Leaf Trousers
                ShopItem(itemId=3625, price=25, goldPrice=10, color1=78, color2=224, itemType="Shoes"), # Fawn Brown Woodchucks with White Trim

                ShopItem(itemId=478, price=45, goldPrice=16, color1=126, color2=208, itemType="Shirt"), # Raindrop Blue Splish-Splash Tank
                ShopItem(itemId=1394, price=45, goldPrice=16, color1=126, color2=208, itemType="Skirt"), # Raindrop Blue Splish-Splash Shorts
                ShopItem(itemId=3604, price=25, goldPrice=10, color1=208, color2=126, itemType="Shoes"), # Cerulean Blue Tick Tock

                ShopItem(itemId=286, price=45, goldPrice=16, color1=162, color2=161, itemType="Shirt"), # Sunglow Yellow Plenty Plaid Top
                ShopItem(itemId=1133, price=45, goldPrice=16, color1=161, color2=161, itemType="Skirt"), # Buried Treasure Brown Cuffed Leaf Shorts
                ShopItem(itemId=3671, price=25, goldPrice=10, color1=161, color2=162, itemType="Shoes"), # Buried Treasure Brown Plenty Plaid Deck Shoes

                ShopItem(itemId=244, price=45, goldPrice=16, color1=166, color2=206, itemType="Shirt"), # Snow White Best Dressed Suspenders
                ShopItem(itemId=1204, price=45, goldPrice=16, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Best Dressed Slacks
                ShopItem(itemId=3641, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Best Dressed Loafers

                ShopItem(itemId=2155, price=25, goldPrice=10, color1=27, color2=75, itemType="HeadItem"), # Corn Cob Yellow Sparrow Snow Cap
                ShopItem(itemId=2578, price=15, goldPrice=6, color1=27, color2=27, itemType="Necklace"), # Corn Cob Yellow Twisty Winter Warmer
                ShopItem(itemId=304, price=45, goldPrice=16, color1=75, color2=27, itemType="Shirt"), # Umber Brown Snowbound Ski Jacket
                ShopItem(itemId=1592, price=15, goldPrice=6, color1=93, color2=27, itemType="WristItem"), # Maple Brown Ski Poles
                ShopItem(itemId=1254, price=45, goldPrice=16, color1=75, color2=27, itemType="Skirt"), # Umber Brown Warm Ski Pants
                ShopItem(itemId=3677, price=25, goldPrice=10, color1=93, color2=27, itemType="Shoes"), # Maple Brown Swift Skis

                ShopItem(itemId=222, price=45, goldPrice=16, color1=224, color2=3, itemType="Shirt"), # Ivory White Scholarly Vest
                ShopItem(itemId=1172, price=45, goldPrice=16, color1=91, color2=91, itemType="Skirt"), # Coconut Brown Dry Leaf Trousers
                ShopItem(itemId=3588, price=25, goldPrice=10, color1=74, color2=236, itemType="Shoes"), # Soil Brown Bark Layer Shoes

                ShopItem(itemId=220, price=45, goldPrice=16, color1=60, color2=129, itemType="Shirt"), # Tyrian Purple Simple Cardie with Purple Trim
                ShopItem(itemId=1145, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Denim Flyers
                ShopItem(itemId=3587, price=25, goldPrice=10, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Bark Sole Dress Shoes

                ShopItem(itemId=268, price=45, goldPrice=16, color1=113, color2=161, itemType="Shirt"), # Pale Rose Red Easy Style Henley with Buried Treasure Brown Trim
                ShopItem(itemId=1217, price=45, goldPrice=16, color1=161, color2=161, itemType="Skirt"), # Buried Treasure Brown Easy Style Jeans
                ShopItem(itemId=3654, price=25, goldPrice=10, color1=78, color2=161, itemType="Shoes"), # Fawn Brown Easy Style Sneaks

                ShopItem(itemId=2330, price=25, goldPrice=10, color1=206, color2=206, itemType="HeadItem"), # Raven Black Keen Comb
                ShopItem(itemId=407, price=45, goldPrice=16, color1=206, color2=166, itemType="Shirt"), # Raven Black Sock Hop Jacket
                ShopItem(itemId=1330, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Sock Hop Pants
                ShopItem(itemId=3749, price=25, goldPrice=10, color1=206, color2=166, itemType="Shoes"), # Raven Black Cool Moto Boots

                ShopItem(itemId=277, price=45, goldPrice=16, color1=172, color2=122, itemType="Shirt"), # Forest Green Cool Breeze Roll-Up Top
                ShopItem(itemId=1227, price=45, goldPrice=16, color1=118, color2=206, itemType="Skirt"), # Sapphire Blue Breezy Casual Shorts
                ShopItem(itemId=3625, price=25, goldPrice=10, color1=78, color2=236, itemType="Shoes"), # Fawn Brown Woodchucks with Tan Trim

                ShopItem(itemId=2326, price=25, goldPrice=10, color1=224, color2=141, itemType="HeadItem"), # Ivory White Too Cool Hat
                ShopItem(itemId=406, price=45, goldPrice=16, color1=224, color2=141, itemType="Shirt"), # Ivory White Hip Zip Sweater
                ShopItem(itemId=1311, price=45, goldPrice=16, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Neat and Trim Trousers
                ShopItem(itemId=3714, price=25, goldPrice=10, color1=141, color2=224, itemType="Shoes"), # Thundercloud Gray Fast-Flying Sneakers

                ShopItem(itemId=287, price=45, goldPrice=16, color1=208, color2=267, itemType="Shirt"), # Cerulean Blue Beach Breezy Top
                ShopItem(itemId=1239, price=45, goldPrice=16, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Beach Breezy Shorts
                ShopItem(itemId=3672, price=25, goldPrice=10, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Easy Walker

                ShopItem(itemId=285, price=45, goldPrice=16, color1=63, color2=166, itemType="Shirt"), # Butterfly Blue Casual Flyer Coat
                ShopItem(itemId=1238, price=45, goldPrice=16, color1=63, color2=63, itemType="Skirt"), # Butterfly Blue Casual Flyer Pants
                ShopItem(itemId=3670, price=25, goldPrice=10, color1=63, color2=166, itemType="Shoes"), # Butterfly Blue Casual Flyer Shoes

                ShopItem(itemId=299, price=45, goldPrice=16, color1=166, color2=169, itemType="Shirt"), # Snow White Polished Pinstripe Vest with Squirrel Gray Trim
                ShopItem(itemId=1249, price=45, goldPrice=16, color1=169, color2=169, itemType="Skirt"), # Squirrel Gray Polished Pinstripe Pants
                ShopItem(itemId=3679, price=25, goldPrice=10, color1=141, color2=169, itemType="Shoes"), # Thundercloud Gray Luxurious Lace-Ups

                ShopItem(itemId=218, price=45, goldPrice=16, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Rain Hoodie
                ShopItem(itemId=1131, price=45, goldPrice=16, color1=78, color2=78, itemType="Skirt"), # Fawn Brown Tailored Leaf Jeans
                ShopItem(itemId=3627, price=25, goldPrice=10, color1=78, color2=78, itemType="Shoes"), #  Fawn Brown Sturdy Galoshes

                ShopItem(itemId=147, price=45, goldPrice=16, color1=127, color2=17, itemType="Shirt"), # Grasshopper Green Sporty Top
                ShopItem(itemId=1193, price=45, goldPrice=16, color1=127, color2=127, itemType="Skirt"), # Grasshopper Green Sporty Shorts
                ShopItem(itemId=3633, price=25, goldPrice=10, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Sporty Shoes
            
            ],
        ),
        ShopCollection(
            collectionId=56, # Themed Fashions
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
                ShopItem(itemId=2294, price=25, goldPrice=10, color1=154, color2=45, itemType="HeadItem"), # Beetle Brown Gardening Hat
                ShopItem(itemId=380, price=45, goldPrice=16, color1=118, color2=45, itemType="Shirt"), # Sapphire Blue Gardening Overall Top
                ShopItem(itemId=1298, price=45, goldPrice=16, color1=209, color2=141, itemType="Skirt"), # Deep Sea Blue Gardening Jeans
                ShopItem(itemId=3627, price=25, goldPrice=10, color1=141, color2=214, itemType="Shoes"), # Thundercloud Gray Sturdy Galoshes with Gray Trim

                ShopItem(itemId=2275, price=25, goldPrice=10, color1=239, color2=216, itemType="HeadItem"), # Coffee Black Ninja Hood
                ShopItem(itemId=336, price=45, goldPrice=16, color1=239, color2=216, itemType="Shirt"), # Coffee Black Ninja Shinobi Top
                ShopItem(itemId=1272, price=45, goldPrice=16, color1=239, color2=216, itemType="Skirt"), # Coffee Black Ninja Shinobi Pants
                ShopItem(itemId=3697, price=25, goldPrice=10, color1=239, color2=141, itemType="Shoes"), #  Coffee Black Ninja Tabi Shoes

                ShopItem(itemId=2297, price=25, goldPrice=10, color1=239, color2=168, itemType="HeadItem"), # Coffee Black Folklorico Hat
                ShopItem(itemId=381, price=45, goldPrice=16, color1=239, color2=168, itemType="Shirt"), # Coffee Black Folklorico Jacket
                ShopItem(itemId=1301, price=45, goldPrice=16, color1=239, color2=168, itemType="Skirt"), # Coffee Black Folklorico Trousers
                ShopItem(itemId=3719, price=25, goldPrice=10, color1=239, color2=168, itemType="Shoes"), # Coffee Black Folklorico Shoes

                ShopItem(itemId=352, price=45, goldPrice=16, color1=206, color2=236, itemType="Shirt"), #  Raven Black Woodsman Top
                ShopItem(itemId=633, price=15, goldPrice=6, color1=206, color2=245, itemType="Belt"), # Raven Black Woodsman's Belt
                ShopItem(itemId=1287, price=45, goldPrice=16, color1=239, color2=239, itemType="Skirt"), # Coffee Black Woodsman Trousers
                ShopItem(itemId=3712, price=25, goldPrice=10, color1=239, color2=239, itemType="Shoes"), # Coffee Black Woodsman Boots

                ShopItem(itemId=2157, price=25, goldPrice=10, color1=224, color2=224, itemType="HeadItem"), # Ivory White Baking Hat
                ShopItem(itemId=189, price=45, goldPrice=16, color1=171, color2=224, itemType="Shirt"), # Sunrise Yellow Chef's Jacket
                ShopItem(itemId=1171, price=45, goldPrice=16, color1=224, color2=224, itemType="Skirt"), # Ivory White Chef's Apron Pants
                ShopItem(itemId=3592, price=25, goldPrice=10, color1=75, color2=75, itemType="Shoes"), # Umber Brown Round Toe Shoes

                ShopItem(itemId=2184, price=25, goldPrice=10, color1=224, color2=105, itemType="HeadItem"), # Ivory White Serving-Talent Hat
                ShopItem(itemId=237, price=45, goldPrice=16, color1=224, color2=105, itemType="Shirt"), # Ivory White Serving-Talent Vest
                ShopItem(itemId=1172, price=45, goldPrice=16, color1=118, color2=118, itemType="Skirt"), # Sapphire Blue Dry Leaf Trousers
                ShopItem(itemId=3623, price=25, goldPrice=10, color1=141, color2=206, itemType="Shoes"), # Thundercloud Gray Later Skaters with Black Trim

                ShopItem(itemId=2179, price=25, goldPrice=10, color1=209, color2=180, itemType="HeadItem"), # Deep Sea Blue Teatime Top Hat
                ShopItem(itemId=2569, price=15, goldPrice=6, color1=209, color2=209, itemType="Necklace"), # Deep Sea Blue Mad Tea Party Scarf
                ShopItem(itemId=247, price=45, goldPrice=16, color1=209, color2=180, itemType="Shirt"), # Deep Sea Blue Mad Tea Party Attire
                ShopItem(itemId=1204, price=45, goldPrice=16, color1=185, color2=180, itemType="Skirt"), # Midnight Blue Best Dressed Slacks
                ShopItem(itemId=3641, price=25, goldPrice=10, color1=209, color2=180, itemType="Shoes"), # Deep Sea Blue Best Dressed Loafers

                ShopItem(itemId=2588, price=15, goldPrice=6, color1=227, color2=151, itemType="Necklace"), # Moonlight Gray Top 40 Necklace
                ShopItem(itemId=335, price=45, goldPrice=16, color1=224, color2=230, itemType="Shirt"), # Ivory White Top 40 Vest
                ShopItem(itemId=1608, price=15, goldPrice=6, color1=230, color2=227, itemType="WristItem"), # Scarlet Red Top 40 Wrist Cuff
                ShopItem(itemId=1132, price=45, goldPrice=16, color1=209, color2=209, itemType="Skirt"), # Deep Sea Blue Tailored Spider Silk Jeans
                ShopItem(itemId=3633, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Sporty Shoes

                ShopItem(itemId=2287, price=25, goldPrice=10, color1=92, color2=286, itemType="HeadItem"), # Hawk Brown Rockin' Hair
                ShopItem(itemId=2592, price=15, goldPrice=6, color1=169, color2=166, itemType="Necklace"), # Squirrel Gray Rockin' Necklace
                ShopItem(itemId=349, price=45, goldPrice=16, color1=55, color2=166, itemType="Shirt"), # Pepper Black Rockin' Jacket
                ShopItem(itemId=632, price=15, goldPrice=6, color1=45, color2=45, itemType="Belt"), # Strawberry Red Rockin' Belt
                ShopItem(itemId=1285, price=45, goldPrice=16, color1=141, color2=141, itemType="Skirt"), # Thundercloud Gray Rockin' Pants
                ShopItem(itemId=3709, price=25, goldPrice=10, color1=55, color2=166, itemType="Shoes"), # Pepper Black Rockin' Boots

                ShopItem(itemId=351, price=45, goldPrice=16, color1=206, color2=226, itemType="Shirt"), # Raven Black Glitz and Glam Top
                ShopItem(itemId=1297, price=45, goldPrice=16, color1=226, color2=206, itemType="Skirt"), # Goldenrod Yellow Glitz and Glam Pants
                ShopItem(itemId=3711, price=25, goldPrice=10, color1=206, color2=226, itemType="Shoes"), # Raven Black Glitz and Glam Boots

                ShopItem(itemId=324, price=45, goldPrice=16, color1=116, color2=248, itemType="Shirt"), # Mushroom White Royal Jacket
                ShopItem(itemId=1262, price=45, goldPrice=16, color1=26, color2=26, itemType="Skirt"), # Raspberry Red Princely Trousers
                ShopItem(itemId=3683, price=25, goldPrice=10, color1=141, color2=141, itemType="Shoes"), # Thundercloud Gray Princely Boots

                ShopItem(itemId=337, price=45, goldPrice=16, color1=170, color2=159, itemType="Shirt"), # Olive Green Agave Top
                ShopItem(itemId=1610, price=10, goldPrice=6, color1=170, color2=170, itemType="WristItem"), # Olive Green Agave Cuff
                ShopItem(itemId=1273, price=45, goldPrice=16, color1=170, color2=159, itemType="Skirt"), # Olive Green Agave Shorts
                ShopItem(itemId=3698, price=25, goldPrice=10, color1=170, color2=159, itemType="Shoes"), # Olive Green Agave Shoes

                ShopItem(itemId=2131, price=25, goldPrice=10, color1=206, color2=206, itemType="HeadItem"), # Raven Black Camp Referee Visor
                ShopItem(itemId=146, price=45, goldPrice=16, color1=166, color2=206, itemType="Shirt"), # Snow White Camp Referee Top
                ShopItem(itemId=1137, price=45, goldPrice=16, color1=166, color2=206, itemType="Skirt"), # Snow White Camp Referee Shorts
                ShopItem(itemId=3597, price=25, goldPrice=10, color1=206, color2=166, itemType="Shoes"), # Raven Black Camp Referee Shoes

                ShopItem(itemId=361, price=45, goldPrice=16, color1=183, color2=60, itemType="Shirt"), # Vidia Purple Fast-Flying Tee
                ShopItem(itemId=1291, price=45, goldPrice=16, color1=183, color2=183, itemType="Skirt"), # Vidia Purple Fast-Flying Pants
                ShopItem(itemId=3714, price=25, goldPrice=10, color1=60, color2=60, itemType="Shoes"), # Tyrian Purple Fast-Flying Sneakers

                ShopItem(itemId=2290, price=25, goldPrice=10, color1=60, color2=183, itemType="HeadItem"), # Tyrian Purple Fast-Flying Headband
                ShopItem(itemId=362, price=45, goldPrice=16, color1=183, color2=60, itemType="Shirt"), # Vidia Purple Fast-Flying Tunic
                ShopItem(itemId=634, price=15, goldPrice=6, color1=183, color2=60, itemType="Belt"), # Vidia Purple Fast-Flying Belt
                ShopItem(itemId=1292, price=45, goldPrice=16, color1=183, color2=60, itemType="Skirt"), # Vidia Purple Fast-Flying Pants
                ShopItem(itemId=3715, price=25, goldPrice=10, color1=183, color2=60, itemType="Shoes"), # Vidia Purple Fast-Flying Laceups

                ShopItem(itemId=2276, price=25, goldPrice=10, color1=166, color2=166, itemType="HeadItem"), # Snow White Wacky Rainbow Wig
                ShopItem(itemId=131, price=45, goldPrice=16, color1=226, color2=228, itemType="Shirt"), # Goldenrod Yellow Cap Sleeve Meadow Tee
                ShopItem(itemId=1288, price=45, goldPrice=16, color1=228, color2=228, itemType="Skirt"), # Duckbill Orange Silly Parachute Pants
                ShopItem(itemId=3713, price=25, goldPrice=10, color1=226, color2=226, itemType="Shoes"), # Goldenrod Yellow Polka-Stripe Socks


            ]
        ),
        ShopCollection(
            collectionId=58, # Animal Friend Costumes
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
            ShopItem(itemId=2073, price=25, goldPrice=10, color1=206, color2=142, itemType="HeadItem"), # Raven Black Buzzy Bee Mask
            ShopItem(itemId=230, price=45, goldPrice=16, color1=142, color2=206, itemType="Shirt"), # Bumble Bee Yellow Buzzy Bee Top
            ShopItem(itemId=1170, price=45, goldPrice=16, color1=206, color2=206, itemType="Skirt"), # Raven Black Pocket Pants
            ShopItem(itemId=3577, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Ivy Lace Work Boots

            ShopItem(itemId=2071, price=25, goldPrice=10, color1=44, color2=190, itemType="HeadItem"), # Plumblossom Pink Little Light Antennae
            ShopItem(itemId=175, price=45, goldPrice=16, color1=44, color2=190, itemType="Shirt"), # Plumblossom Pink Firefly Wrap
            ShopItem(itemId=1195, price=45, goldPrice=16, color1=190, color2=190, itemType="Skirt"), # Firefly Green Dry Leaf Shorts
            ShopItem(itemId=3577, price=25, goldPrice=10, color1=44, color2=44, itemType="Shoes"), # Plumblossom Pink Ivy Lace Work Boots

            ShopItem(itemId=2071, price=25, goldPrice=10, color1=206, color2=189, itemType="HeadItem"), # Raven Black Little Light Antennae
            ShopItem(itemId=177, price=45, goldPrice=16, color1=206, color2=189, itemType="Shirt"), # Raven Black Ladybug Tee
            ShopItem(itemId=1175, price=45, goldPrice=16, color1=206, color2=189, itemType="Skirt"), # Raven Black Ladybug Shorts
            ShopItem(itemId=3577, price=25, goldPrice=10, color1=206, color2=206, itemType="Shoes"), # Raven Black Ivy Lace Work Boots

            ShopItem(itemId=2149, price=25, goldPrice=10, color1=193, color2=175, itemType="HeadItem"), # Electric Green Dragonfly Mask
            ShopItem(itemId=178, price=45, goldPrice=16, color1=175, color2=175, itemType="Shirt"), # Creek Green Dragonfly Top 
            ShopItem(itemId=1173, price=45, goldPrice=16, color1=175, color2=193, itemType="Skirt"), # Creek Green Dragonfly Trousers
            ShopItem(itemId=3577, price=25, goldPrice=10, color1=175, color2=175, itemType="Shoes"), # Creek Green Ivy Lace Work Boots

            ShopItem(itemId=2153, price=25, goldPrice=10, color1=267, color2=27, itemType="HeadItem"), # Celestial Blue Hummingbird Mask
            ShopItem(itemId=190, price=45, goldPrice=16, color1=267, color2=27, itemType="Shirt"), # Celestial Blue Hummingbird Top 
            ShopItem(itemId=1174, price=45, goldPrice=16, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Hummingbird Trousers
            ShopItem(itemId=3577, price=25, goldPrice=10, color1=267, color2=267, itemType="Shoes"), # Celestial Blue Ivy Lace Work Boots
            ]
        ),
        ShopCollection(
            collectionId=62, # Sparrow Shirts and Jackets
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
            ShopItem(itemId=1000033, price=45, goldPrice=16, color1=207, color2=207, itemType="Shirt"), # Diamond Blue Sunburst Tie-Dye Tee
            ShopItem(itemId=1000034, price=45, goldPrice=16, color1=230, color2=230, itemType="Shirt"), # Scarlet Red Striped Tie-Dye Tee
            ShopItem(itemId=1000035, price=45, goldPrice=16, color1=129, color2=129, itemType="Shirt"), # Fig Purple Speckled Tie-Dye Tee
            ShopItem(itemId=354, price=45, goldPrice=16, color1=90, color2=90, itemType="Shirt"), # Custard Yellow Horizontal Leaf Hoodie with Tan Trim
            ShopItem(itemId=355, price=45, goldPrice=16, color1=221, color2=221, itemType="Shirt"), # Jade Green Colorblock Stripe Hoodie

            ShopItem(itemId=353, price=45, goldPrice=16, color1=206, color2=206, itemType="Shirt"), # Raven Black Vertical Leaf Hoodie
            ShopItem(itemId=356, price=45, goldPrice=16, color1=216, color2=216, itemType="Shirt"), # Slate Gray Layered Blazer
            ShopItem(itemId=357, price=45, goldPrice=16, color1=161, color2=161, itemType="Shirt"), # Buried Treasure Brown Casual Plaid Shirt
            ShopItem(itemId=358, price=45, goldPrice=16, color1=209, color2=209, itemType="Shirt"), # Deep Sea Blue Denim Jacket
            ShopItem(itemId=359, price=45, goldPrice=16, color1=78, color2=78, itemType="Shirt"), # Fawn Brown Casual Denim Shirt

            ShopItem(itemId=150, price=45, goldPrice=16, color1=60, color2=60, itemType="Shirt"), # Tyrian Purple Birdy Button Down
            ShopItem(itemId=151, price=45, goldPrice=16, color1=265, color2=265, itemType="Shirt"), # Bright Sky Blue Palm Tree Button Down
            ShopItem(itemId=152, price=45, goldPrice=16, color1=81, color2=81, itemType="Shirt"), # Crimson Red Wave Button Down
            ShopItem(itemId=402, price=45, goldPrice=16, color1=206, color2=206, itemType="Shirt"), # Raven Black Triple Stripes Polo

            ShopItem(itemId=403, price=45, goldPrice=16, color1=185, color2=185, itemType="Shirt"), # Midnight Blue Neat Stripes Polo
            ShopItem(itemId=404, price=45, goldPrice=16, color1=148, color2=148, itemType="Shirt"), # Pots'n'Pans Purple Super Stripes Polo
            ShopItem(itemId=224, price=45, goldPrice=16, color1=113, color2=113, itemType="Shirt"), # Pale Rose Red Zip Up Hoodie
            ShopItem(itemId=128, price=45, goldPrice=16, color1=172, color2=172, itemType="Shirt"), # Forest Green Cottonpuff Pullover
            ShopItem(itemId=366, price=45, goldPrice=16, color1=166, color2=166, itemType="Shirt"), # Snow White Vine Tee
            
            ShopItem(itemId=367, price=45, goldPrice=16, color1=113, color2=113, itemType="Shirt"), # Pale Rose Red Twisty Print Tee
            ShopItem(itemId=364, price=45, goldPrice=16, color1=221, color2=221, itemType="Shirt"), # Jade Green Sideswept Swirl Tee
            ShopItem(itemId=368, price=45, goldPrice=16, color1=180, color2=180, itemType="Shirt"), # Seashell Blue Star Print Tee
            ShopItem(itemId=371, price=45, goldPrice=16, color1=162, color2=162, itemType="Shirt"), # Sunglow Yellow Nifty Print Tee
            ShopItem(itemId=370, price=45, goldPrice=16, color1=206, color2=206, itemType="Shirt"), # Raven Black Twisty Tree Tee
            ]
        ),
        ShopCollection(
            collectionId=63, # Sparrow Man Accessories
            currencyId=INGREDIENTS["MAPLE_LEAVES"].id,
            items=[
            ShopItem(itemId=2125, price=25, goldPrice=6, color1=214, color2=224, itemType="HeadItem"), # Smokey Gray Mainland Fedora
            ShopItem(itemId=2182, price=25, goldPrice=6, color1=46, color2=154, itemType="HeadItem"), # Bark Brown Round Up Hat
            ShopItem(itemId=2132, price=25, goldPrice=6, color1=109, color2=161, itemType="HeadItem"), # Soft Orange Summer Wave Hat
            ShopItem(itemId=2205, price=25, goldPrice=6, color1=91, color2=91, itemType="HeadItem"), # Coconut Brown Straw Brim Hat
            ShopItem(itemId=2206, price=25, goldPrice=6, color1=172, color2=66, itemType="HeadItem"), # Forest Green Linen Sun Hat with Gray Trim
            ShopItem(itemId=2154, price=25, goldPrice=6, color1=224, color2=230, itemType="HeadItem"), # Ivory White Lined Winter Hat
            ShopItem(itemId=2178, price=25, goldPrice=6, color1=73, color2=148, itemType="HeadItem"), # Grape Purple Tea-brewer Cap
            ShopItem(itemId=2165, price=25, goldPrice=6, color1=180, color2=103, itemType="HeadItem"), # Seashell Blue Seashell Cap
            ShopItem(itemId=2174, price=25, goldPrice=6, color1=230, color2=100, itemType="HeadItem"), # Scarlet Red Leaf Embroidered Cap
            ShopItem(itemId=2190, price=25, goldPrice=6, color1=141, color2=126, itemType="HeadItem"), # Thundercloud Gray Conductor Cap with Blue Trim
            ShopItem(itemId=2175, price=25, goldPrice=6, color1=169, color2=169, itemType="HeadItem"), # Squirrel Gray Easy Style Cap
            ShopItem(itemId=2130, price=25, goldPrice=6, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Sporty Sparrow Band
            ShopItem(itemId=2135, price=25, goldPrice=6, color1=207, color2=55, itemType="HeadItem"), # Diamond Blue Sparrow Sun-Shades
            ShopItem(itemId=2279, price=25, goldPrice=6, color1=166, color2=81, itemType="HeadItem"), # Snow White Peppermint Swirl Glasses
            ShopItem(itemId=2230, price=25, goldPrice=6, color1=168, color2=166, itemType="HeadItem"), # Never Gold Merry Monocle

            ShopItem(itemId=2552, price=15, goldPrice=4, color1=175, color2=159, itemType="Necklace"), # Creek Green Striped Scarf
            ShopItem(itemId=2558, price=15, goldPrice=4, color1=230, color2=48, itemType="Necklace"), # Scarlet Red Fringed Scarf
            ShopItem(itemId=2542, price=15, goldPrice=4, color1=126, color2=126, itemType="Necklace"), # Raindrop Blue Meadowland Neck Band
            ShopItem(itemId=2596, price=15, goldPrice=4, color1=206, color2=253, itemType="Necklace"), # Raven Black Sunburst Necklace with Yellow Trim
            ShopItem(itemId=2583, price=15, goldPrice=4, color1=221, color2=221, itemType="Necklace"), # Jade Green Ivy Necklace
            ShopItem(itemId=2582, price=15, goldPrice=4, color1=109, color2=230, itemType="Necklace"), # Soft Orange Bamboo Necklace with Scarlet Red Trim
            ShopItem(itemId=2541, price=15, goldPrice=4, color1=30, color2=30, itemType="Necklace"), # Pumpkin Orange Triple Gem Neck Ring
            ShopItem(itemId=2540, price=15, goldPrice=4, color1=60, color2=60, itemType="Necklace"), # Tyrian Purple Neverberry Neck Band
            ShopItem(itemId=2544, price=15, goldPrice=4, color1=266, color2=266, itemType="Necklace"), # Ocean Blue Gavin's 3-2 Neck Band
            ShopItem(itemId=2577, price=15, goldPrice=4, color1=221, color2=202, itemType="Necklace"), # Jade Green Trinity Leaf Torc

            ShopItem(itemId=585, price=15, goldPrice=4, color1=78, color2=168, itemType="Belt"), # Fawn Brown Studded Belt
            ShopItem(itemId=584, price=15, goldPrice=4, color1=170, color2=2, itemType="Belt"), # Olive Green Clover Belt
            ShopItem(itemId=583, price=15, goldPrice=4, color1=154, color2=167, itemType="Belt"), # Beetle Brown Basic Belt
            ShopItem(itemId=598, price=15, goldPrice=4, color1=206, color2=166, itemType="Belt"), # Moonlight Gray Triple Gear Belt
            ShopItem(itemId=597, price=15, goldPrice=4, color1=75, color2=89, itemType="Belt"), # Umber Brown Gear Buckle Belt
            ShopItem(itemId=578, price=15, goldPrice=4, color1=28, color2=189, itemType="Belt"), # Cinnamon Brown Acorn Buckle Belt
            ShopItem(itemId=562, price=15, goldPrice=4, color1=208, color2=208, itemType="Belt"), # Cerulean Blue Sash Belt
            ShopItem(itemId=563, price=15, goldPrice=4, color1=148, color2=148, itemType="Belt"), # Pots'n'Pans Purple Cross-Stitch Belt
            ShopItem(itemId=564, price=15, goldPrice=4, color1=83, color2=83, itemType="Belt"), # Cherry Brown Bark Braid Belt
            ShopItem(itemId=561, price=15, goldPrice=4, color1=75, color2=105, itemType="Belt"), # Umber Brown Seed Band Belt
            ShopItem(itemId=627, price=15, goldPrice=4, color1=166, color2=189, itemType="Belt"), # Snow White Peppermint Swirl Belt
            ShopItem(itemId=637, price=15, goldPrice=4, color1=206, color2=186, itemType="Belt"), # Raven Black Sunburst Belt with Yellow Trim
            ShopItem(itemId=582, price=15, goldPrice=4, color1=180, color2=236, itemType="Belt"), # Seashell Blue Scallop Shell Belt
            ShopItem(itemId=581, price=15, goldPrice=4, color1=209, color2=149, itemType="Belt"), # Deep Sea Blue Seashell Belt
            ShopItem(itemId=592, price=15, goldPrice=4, color1=191, color2=189, itemType="Belt"), # Vidia Black Feather Friendship Belt

            ShopItem(itemId=1540, price=15, goldPrice=4, color1=185, color2=185, itemType="WristItem"), # Midnight Blue Ever Never-Friend Bracelet
            ShopItem(itemId=1559, price=15, goldPrice=4, color1=45, color2=185, itemType="WristItem"), # Strawberry Red Friendship Cuff with Midnight Blue Trim
            ShopItem(itemId=1595, price=15, goldPrice=4, color1=221, color2=221, itemType="WristItem"), # Jade Green Ivy Bracelet
            ShopItem(itemId=1630, price=15, goldPrice=4, color1=206, color2=111, itemType="WristItem"), # Raven Black Sunburst Cuff with Yellow Trim
            ShopItem(itemId=1536, price=15, goldPrice=4, color1=138, color2=138, itemType="WristItem"), # Persimmon Orange Meadow Grass Wrist Wrap
            ShopItem(itemId=1531, price=15, goldPrice=4, color1=126, color2=126, itemType="WristItem"), # Raindrop Blue Shield Brace
            ShopItem(itemId=1530, price=15, goldPrice=4, color1=148, color2=148, itemType="WristItem"), # Pots'n'Pans Purple Winding Wrist Wrap
            ShopItem(itemId=1529, price=15, goldPrice=4, color1=168, color2=168, itemType="WristItem"), # Never Gold Quick Brace
            ShopItem(itemId=1596, price=15, goldPrice=4, color1=109, color2=98, itemType="WristItem"), # Soft Orange Bamboo Bracelet with Tan Trim
            ShopItem(itemId=1535, price=15, goldPrice=4, color1=215, color2=215, itemType="WristItem"), # Pewter Gray X-Band Wrist Wrap
            ShopItem(itemId=1537, price=15, goldPrice=4, color1=208, color2=208, itemType="WristItem"), # Cerulean Blue Grassblade Wrist Wrap
            ShopItem(itemId=1538, price=15, goldPrice=4, color1=175, color2=175, itemType="WristItem"), # Creek Green Triple Tie Wrist Wrap
            ShopItem(itemId=1534, price=15, goldPrice=4, color1=220, color2=220, itemType="WristItem"), # Dusty Pink Triple Cuff
            ShopItem(itemId=1532, price=15, goldPrice=4, color1=183, color2=183, itemType="WristItem"), # Vidia Purple Pinfeather Brace
            ShopItem(itemId=1584, price=15, goldPrice=4, color1=221, color2=221, itemType="WristItem"), # Jade Green Trinity Leaf Bracelet

            ShopItem(itemId=3044, price=15, goldPrice=4, color1=221, color2=221, itemType="AnkleItem"), # Jade Green Trinity Leaf Anklet
            ShopItem(itemId=3029, price=15, goldPrice=4, color1=208, color2=208, itemType="AnkleItem"), # Cerulean Blue Vine Duo Anklet
            ShopItem(itemId=3047, price=15, goldPrice=4, color1=230, color2=230, itemType="AnkleItem"), # Scarlet Red Bamboo Anklet
            ShopItem(itemId=3046, price=15, goldPrice=4, color1=221, color2=221, itemType="AnkleItem"), # Jade Green Ivy Anklet

            ShopItem(itemId=3663, price=25, goldPrice=8, color1=224, color2=224, itemType="Shoes"), # Ivory White Socks'n'Sandal Combo
            ShopItem(itemId=3665, price=25, goldPrice=8, color1=113, color2=113, itemType="Shoes"), # Pale Rose Red Super Sports Foot Gear
            ShopItem(itemId=3664, price=25, goldPrice=8, color1=175, color2=175, itemType="Shoes"), # Creek Green Fun Run Foot Gear
            ShopItem(itemId=3572, price=25, goldPrice=8, color1=78, color2=78, itemType="Shoes"), # Fawn Brown Tall Tied Boots
            ShopItem(itemId=3616, price=25, goldPrice=8, color1=118, color2=118, itemType="Shoes"), # Sapphire Blue Short Sturdy Boots
            ShopItem(itemId=3615, price=25, goldPrice=8, color1=10, color2=10, itemType="Shoes"), # Cantaloupe Orange Tall Sturdy Boots
            ShopItem(itemId=3692, price=25, goldPrice=8, color1=105, color2=105, itemType="Shoes"), # Siltstone Tan Bamboo Sandals
            ShopItem(itemId=3575, price=25, goldPrice=8, color1=206, color2=206, itemType="Shoes"), # Raven Black Cross-Stitch Work Boots  
            ],
        ),
    ],
)