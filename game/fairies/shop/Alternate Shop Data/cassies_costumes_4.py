from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

# Cassie's - OutfitId 4000 - 4999

SHOP = NPCShop(
    zone=ZoneConstants.CASSIES_COSTUME_SHOP,
    shopId=4,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.CASSIE,
        position=(500, 350),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_CASSIE
    ),
    collections=[
        ShopCollection(
            collectionId=4022, # Troop Rabbit Uniforms
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Rabbit 2013 - Fairies
                ShopOutfit(
                    outfitId=4001,
                    items = [
                        OutfitItem(itemId=1000088, price=37, goldPrice=11, color1=178, color2=237, itemType="Shirt"), # Fawn Orange, Melon Orange
                        OutfitItem(itemId=1496, price=33, goldPrice=10, color1=178, color2=237, itemType="Skirt"), # Fawn Orange, Melon Orange
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=178, color2=237, itemType="Shoes"), # Fawn Orange, Melon Orange
                    ],
                ),
                ShopOutfit(
                    outfitId=4002,
                    items = [
                        OutfitItem(itemId=1000088, price=37, goldPrice=11, color1=239, color2=154, itemType="Shirt"), # Coffee Black, Beetle Brown
                        OutfitItem(itemId=1496, price=33, goldPrice=10, color1=239, color2=154, itemType="Skirt"), # Coffee Black, Beetle Brown
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=239, color2=154, itemType="Shoes"), # Coffee Black, Beetle Brown
                    ],
                ),
                # Rabbit 2013 - Sparrowmen
                ShopOutfit(
                    outfitId=4003,
                    items = [
                        OutfitItem(itemId=142, price=37, goldPrice=11, color1=237, color2=178, itemType="Shirt"), # Melon Orange Animal-Talent Tee 
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=178, color2=178, itemType="Skirt"), # Fawn Orange Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=178, color2=237, itemType="Shoes"), # Fawn Orange Camp Referee Shoes with Melon Orange Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4004,
                    items = [
                        OutfitItem(itemId=142, price=37, goldPrice=11, color1=108, color2=91, itemType="Shirt"), # Creamy Tan, Coconut Brown Animal-Talent Tee
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=91, color2=91, itemType="Skirt"), # Coconut Brown Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=91, color2=108, itemType="Shoes"), # Coconut Brown Camp Referee Shoes with Creamy Tan Trim
                    ],
                ),
                # Rabbit 2012 - Fairies
                ShopOutfit(
                    outfitId=4005,
                    items = [
                        OutfitItem(itemId=2126, price=20, goldPrice=7, color1=178, color2=178, itemType="HeadItem"), # Fawn Orange
                        OutfitItem(itemId=2546, price=20, goldPrice=7, color1=90, color2=178, itemType="Necklace"), # Custard Yellow, Fawn Orange
                        OutfitItem(itemId=136, price=37, goldPrice=11, color1=166, color2=161, itemType="Shirt"), # Snow White, Buried Treasure Brown
                        OutfitItem(itemId=1048, price=33, goldPrice=10, color1=166, color2=161, itemType="Skirt"), # Snow White, Buried Treasure Brown
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=178, color2=166, itemType="Shoes"), # Fawn Orange, Snow White
                    ],
                ),
                # Rabbit 2012 - Sparrow Men
                ShopOutfit(
                    outfitId=4006,
                    items = [
                        OutfitItem(itemId=2127, price=20, goldPrice=7, color1=178, color2=178, itemType="HeadItem"), # Fawn Orange
                        OutfitItem(itemId=2547, price=20, goldPrice=7, color1=90, color2=178, itemType="Necklace"), # Custard Yellow, Fawn Orange
                        OutfitItem(itemId=142, price=37, goldPrice=11, color1=166, color2=161, itemType="Shirt"), # Snow White, Buried Treasure Brown
                        OutfitItem(itemId=1133, price=33, goldPrice=10, color1=161, color2=161, itemType="Skirt"), # Snow White, Buried Treasure Brown
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=178, color2=166, itemType="Shoes"), # Fawn Orange, Snow White
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=4023, # Troop Butterfly Uniforms
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Butterfly 2013 - Fairies
                ShopOutfit(
                    outfitId=4007,
                    items = [
                        OutfitItem(itemId=1000084, price=37, goldPrice=11, color1=174, color2=121, itemType="Shirt"), # Rosetta Red, Daisy Pink
                        OutfitItem(itemId=1491, price=33, goldPrice=10, color1=174, color2=121, itemType="Skirt"), # Rosetta Red, Daisy Pink
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red, Daisy Pink
                    ],
                ),
                ShopOutfit(
                    outfitId=4008,
                    items = [
                        OutfitItem(itemId=1000084, price=37, goldPrice=11, color1=194, color2=16, itemType="Shirt"), # Electric Pink, Camellia Pink
                        OutfitItem(itemId=1491, price=33, goldPrice=10, color1=194, color2=16, itemType="Skirt"), # Electric Pink, Camellia Pink
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=194, color2=16, itemType="Shoes"), # Electric Pink, Camellia Pink
                    ],
                ),
                # Butterfly 2013 - Sparrowmen
                ShopOutfit(
                    outfitId=4009,
                    items = [
                        OutfitItem(itemId=139, price=37, goldPrice=11, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Garden-Talent Tee 
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=174, color2=174, itemType="Skirt"), # Rosetta Red Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red Camp Referee Shoes with Daisy Pink Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4010,
                    items = [
                        OutfitItem(itemId=139, price=37, goldPrice=11, color1=81, color2=282, itemType="Shirt"), # Crimson Red, Magnolia White
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=81, color2=282, itemType="Skirt"), # Crimson Red, Magnolia White
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=81, color2=282, itemType="Shoes"), # Crimson Red, Magnolia White
                    ],
                ),
                # Butterfly 2012 - Fairies
                ShopOutfit(
                    outfitId=4011,
                    items = [
                        OutfitItem(itemId=2126, price=20, goldPrice=7, color1=174, color2=174, itemType="HeadItem"), # Rosetta Red
                        OutfitItem(itemId=2546, price=20, goldPrice=7, color1=86, color2=174, itemType="Necklace"), # Nutmeg Brown, Rosetta Red
                        OutfitItem(itemId=135, price=37, goldPrice=11, color1=166, color2=16, itemType="Shirt"), # Snow White, Camellia Pink
                        OutfitItem(itemId=1048, price=33, goldPrice=10, color1=166, color2=16, itemType="Skirt"), # Snow White, Camellia Pink
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=174, color2=166, itemType="Shoes"), # Rosetta Red, Snow White
                    ],
                ),
                # Butterfly 2012 - Sparrow Men
                ShopOutfit(
                    outfitId=4012,
                    items = [
                        OutfitItem(itemId=2127, price=20, goldPrice=7, color1=174, color2=174, itemType="HeadItem"), # Rosetta Red
                        OutfitItem(itemId=2547, price=20, goldPrice=7, color1=86, color2=174, itemType="Necklace"), # Nutmeg Brown, Rosetta Red
                        OutfitItem(itemId=139, price=37, goldPrice=11, color1=166, color2=113, itemType="Shirt"), # Snow White, Pale Rose Red
                        OutfitItem(itemId=1133, price=33, goldPrice=10, color1=113, color2=113, itemType="Skirt"), # Snow White, Pale Rose Red
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=174, color2=166, itemType="Shoes"), # Rosetta Red, Snow White
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=4024, # Troop Otter Uniforms
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Otter 2013 - Fairies
                ShopOutfit(
                    outfitId=4013,
                    items = [
                        OutfitItem(itemId=1000087, price=37, goldPrice=11, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue, Crystal Blue
                        OutfitItem(itemId=1494, price=33, goldPrice=10, color1=176, color2=219, itemType="Skirt"), # Silvermist Blue, Crystal Blue
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=176, color2=219, itemType="Shoes"), # Silvermist Blue, Crystal Blue
                    ],
                ),
                ShopOutfit(
                    outfitId=4014,
                    items = [
                        OutfitItem(itemId=1000087, price=37, goldPrice=11, color1=267, color2=207, itemType="Shirt"), # Celestial Blue, Diamond Blue
                        OutfitItem(itemId=1494, price=33, goldPrice=10, color1=267, color2=207, itemType="Skirt"), # Celestial Blue, Diamond Blue
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=267, color2=207, itemType="Shoes"), # Celestial Blue, Diamond Blue
                    ],
                ),
                # Otters 2013 - Sparrowmen
                ShopOutfit(
                    outfitId=4015,
                    items = [
                        OutfitItem(itemId=141, price=37, goldPrice=11, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue Water-Talent Tee
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=176, color2=176, itemType="Skirt"), # Silvermist Blue Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=176, color2=219, itemType="Shoes"), # Silvermist Blue Camp Referee Shoes with Crystal Blue Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4016,
                    items = [
                        OutfitItem(itemId=141, price=37, goldPrice=11, color1=267, color2=207, itemType="Shirt"), # Celestial Blue Water-Talent Tee
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=267, color2=267, itemType="Skirt"), # Celestial Blue Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=267, color2=207, itemType="Shoes"), # Celestial Blue Camp Referee Shoes with Diamond Blue Trim
                    ],
                ),
                # Otter 2012 - Fairies
                ShopOutfit(
                    outfitId=4017,
                    items = [
                        OutfitItem(itemId=2126, price=20, goldPrice=7, color1=176, color2=176, itemType="HeadItem"), # Silvermist Blue
                        OutfitItem(itemId=2546, price=20, goldPrice=7, color1=161, color2=176, itemType="Necklace"), # Buried Treasure Brown, Silvermist Blue
                        OutfitItem(itemId=137, price=37, goldPrice=11, color1=166, color2=126, itemType="Shirt"), # Snow White, Raindrop Blue
                        OutfitItem(itemId=1048, price=33, goldPrice=10, color1=166, color2=126, itemType="Skirt"), # Snow White, Raindrop Blue
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=176, color2=166, itemType="Shoes"), # Silvermist Blue, Snow White
                    ],
                ),
                # Otter 2012 - Sparrow Men
                ShopOutfit(
                    outfitId=4018,
                    items = [
                        OutfitItem(itemId=2127, price=20, goldPrice=7, color1=176, color2=176, itemType="HeadItem"), # Silvermist Blue
                        OutfitItem(itemId=2547, price=20, goldPrice=7, color1=161, color2=176, itemType="Necklace"), # Buried Treasure Brown, Silvermist Blue
                        OutfitItem(itemId=141, price=37, goldPrice=11, color1=166, color2=126, itemType="Shirt"), # Snow White, Raindrop Blue
                        OutfitItem(itemId=1133, price=33, goldPrice=10, color1=126, color2=126, itemType="Skirt"), # Raindrop Blue
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=176, color2=166, itemType="Shoes"), # Silvermist Blue, Snow White
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=4025, # Troop Turtle Uniforms
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Turtle 2013 - Fairies
                ShopOutfit(
                    outfitId=4019,
                    items = [
                        OutfitItem(itemId=1000089, price=37, goldPrice=11, color1=145, color2=250, itemType="Shirt"), # Tinker Bell Green, Caramel Tan
                        OutfitItem(itemId=1495, price=33, goldPrice=10, color1=145, color2=250, itemType="Skirt"), # Tinker Bell Green, Caramel Tan
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=145, color2=250, itemType="Shoes"), # Tinker Bell Green, Caramel Tan
                    ],
                ),
                ShopOutfit(
                    outfitId=4020,
                    items = [
                        OutfitItem(itemId=1000089, price=37, goldPrice=11, color1=261, color2=222, itemType="Shirt"), # Kelly Green, Keylime Green
                        OutfitItem(itemId=1495, price=33, goldPrice=10, color1=261, color2=222, itemType="Skirt"), # Kelly Green, Keylime Green
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=261, color2=222, itemType="Shoes"), # Kelly Green, Keylime Green
                    ],
                ),
                # Turtle 2013 - Sparrowmen
                ShopOutfit(
                    outfitId=4021,
                    items = [
                        OutfitItem(itemId=143, price=37, goldPrice=11, color1=145, color2=250, itemType="Shirt"), # Tinker Bell Green Tinker-Talent Tee
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=145, color2=145, itemType="Skirt"), # Tinker Bell Green Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=145, color2=250, itemType="Shoes"), # Tinker Bell Green Camp Referee Shoes with Caramel Tan Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4022,
                    items = [
                        OutfitItem(itemId=143, price=37, goldPrice=11, color1=261, color2=222, itemType="Shirt"), # Kelly Green, Keylime Green
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=261, color2=261, itemType="Skirt"), # Kelly Green, Keylime Green
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=261, color2=222, itemType="Shoes"), # Kelly Green, Keylime Green
                    ],
                ),
                # Turtle 2012 - Fairies
                ShopOutfit(
                    outfitId=4023,
                    items = [
                        OutfitItem(itemId=2126, price=20, goldPrice=7, color1=145, color2=145, itemType="HeadItem"), # Tinker Bell Green
                        OutfitItem(itemId=2546, price=20, goldPrice=7, color1=28, color2=145, itemType="Necklace"), # Cinnamon Brown, Tinkerbell Green
                        OutfitItem(itemId=134, price=37, goldPrice=11, color1=166, color2=2, itemType="Shirt"), # Snow White, Clover Green
                        OutfitItem(itemId=1048, price=33, goldPrice=10, color1=166, color2=2, itemType="Skirt"), # Snow White, Clover Green
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=145, color2=166, itemType="Shoes"), # Tinker Bell Green, Snow White
                    ],
                ),
                # Turtle 2012 - Sparrow Men
                ShopOutfit(
                    outfitId=4024,
                    items = [
                        OutfitItem(itemId=2127, price=20, goldPrice=7, color1=145, color2=145, itemType="HeadItem"), # Tinker Bell Green
                        OutfitItem(itemId=2547, price=20, goldPrice=7, color1=28, color2=145, itemType="Necklace"), # Cinnamon Brown, Tinkerbell Green
                        OutfitItem(itemId=143, price=37, goldPrice=11, color1=166, color2=2, itemType="Shirt"), # Snow White, Clover Green
                        OutfitItem(itemId=1133, price=33, goldPrice=10, color1=2, color2=2, itemType="Skirt"), # Clover Green
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=145, color2=166, itemType="Shoes"), # Tinker Bell Green, Snow White
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=4026, # Troop Glowworm Uniforms
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Glowworm 2013 - Fairies
                ShopOutfit(
                    outfitId=4025,
                    items = [
                        OutfitItem(itemId=1000085, price=37, goldPrice=11, color1=179, color2=137, itemType="Shirt"), # Iridessa Yellow, Lemon Yellow
                        OutfitItem(itemId=1492, price=33, goldPrice=10, color1=179, color2=137, itemType="Skirt"), # Iridessa Yellow, Lemon Yellow
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=179, color2=137, itemType="Shoes"), # Iridessa Yellow, Lemon Yellow
                    ],
                ),
                ShopOutfit(
                    outfitId=4026,
                    items = [
                        OutfitItem(itemId=1000085, price=37, goldPrice=11, color1=162, color2=224, itemType="Shirt"), # Sunglow Yellow, Ivory White
                        OutfitItem(itemId=1492, price=33, goldPrice=10, color1=162, color2=224, itemType="Skirt"), # Sunglow Yellow, Ivory White
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=162, color2=224, itemType="Shoes"), # Sunglow Yellow, Ivory White
                    ],
                ),
                # Glowworm 2013 - Sparrow Men
                ShopOutfit(
                    outfitId=4027,
                    items = [
                        OutfitItem(itemId=140, price=37, goldPrice=11, color1=179, color2=137, itemType="Shirt"), # Iridessa Yellow Light-Talent Tee 
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=179, color2=179, itemType="Skirt"), # Iridessa Yellow Sporty Shorts
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=179, color2=137, itemType="Shoes"), # Iridessa Yellow Camp Referee Shoes with Lemon Yellow Trim
                    ],
                ),
                ShopOutfit(
                    outfitId=4028,
                    items = [
                        OutfitItem(itemId=140, price=37, goldPrice=11, color1=162, color2=224, itemType="Shirt"), # Sunglow Yellow, Ivory White
                        OutfitItem(itemId=1193, price=33, goldPrice=10, color1=162, color2=224, itemType="Skirt"), # Sunglow Yellow, Ivory White
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=162, color2=224, itemType="Shoes"), # Sunglow Yellow, Ivory White
                    ],
                ),
                # Glowworm 2012 - Fairies
                ShopOutfit(
                    outfitId=4029,
                    items = [
                        OutfitItem(itemId=2126, price=20, goldPrice=7, color1=179, color2=179, itemType="HeadItem"), # Iridessa Yellow
                        OutfitItem(itemId=2546, price=20, goldPrice=7, color1=84, color2=179, itemType="Necklace"), # Copper Brown, Iridessa Yellow
                        OutfitItem(itemId=138, price=37, goldPrice=11, color1=166, color2=9, itemType="Shirt"), # Snow White, Daffodil Yellow
                        OutfitItem(itemId=1048, price=33, goldPrice=10, color1=166, color2=9, itemType="Skirt"), # Snow White, Daffodil Yellow
                        OutfitItem(itemId=3595, price=33, goldPrice=10, color1=179, color2=166, itemType="Shoes"), # Iridessa Yellow, Snow White
                    ],
                ),
                # Glowworm 2012 - Sparrow Men
                ShopOutfit(
                    outfitId=4030,
                    items = [
                        OutfitItem(itemId=2127, price=20, goldPrice=7, color1=179, color2=179, itemType="HeadItem"), # Iridessa Yellow
                        OutfitItem(itemId=2547, price=20, goldPrice=7, color1=84, color2=179, itemType="Necklace"), # Copper Brown, Iridessa Yellow
                        OutfitItem(itemId=140, price=37, goldPrice=11, color1=166, color2=9, itemType="Shirt"), # Snow White, Daffodil Yellow
                        OutfitItem(itemId=1133, price=33, goldPrice=10, color1=9, color2=9, itemType="Skirt"), # Snow White, Daffodil Yellow
                        OutfitItem(itemId=3597, price=33, goldPrice=10, color1=179, color2=166, itemType="Shoes"), # Iridessa Yellow, Snow White
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=4027, # Pep Squad
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Animal Talent Pep Squad
                # F
                ShopOutfit(
                    outfitId=4031,
                    items = [
                        OutfitItem(itemId=307, price=37, goldPrice=11, color1=178, color2=56, itemType="Shirt"), # Fawn Orange, Bole Brown
                        OutfitItem(itemId=1575, price=20, goldPrice=7, color1=178, color2=56, itemType="WristItem"), # Fawn Orange, Bole Brown
                        OutfitItem(itemId=1224, price=33, goldPrice=10, color1=178, color2=56, itemType="Skirt"), # Fawn Orange, Bole Brown
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=178, color2=16, itemType="Shoes"), # Fawn Orange, Snow White
                    ],
                ),
                # SM
                ShopOutfit(
                    outfitId=4032,
                    items = [
                        OutfitItem(itemId=312, price=37, goldPrice=11, color1=178, color2=56, itemType="Shirt"), # Fawn Orange, Bole Brown
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=178, color2=56, itemType="Skirt"), # Fawn Orange, Bole Brown
                        OutfitItem(itemId=3633, price=33, goldPrice=10, color1=178, color2=0, itemType="Shoes"), # Fawn Orange
                    ],
                ),
                # Garden Talent Pep Squad
                # F
                ShopOutfit(
                    outfitId=4033,
                    items = [
                        OutfitItem(itemId=308, price=37, goldPrice=11, color1=174, color2=121, itemType="Shirt"), # Rosetta Red, Daisy Pink
                        OutfitItem(itemId=1575, price=20, goldPrice=7, color1=174, color2=121, itemType="WristItem"), # Rosetta Red, Daisy Pink
                        OutfitItem(itemId=1224, price=33, goldPrice=10, color1=174, color2=121, itemType="Skirt"), # Rosetta Red, Daisy Pink
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=174, color2=16, itemType="Shoes"), # Rosetta Red, Snow White
                    ],
                ),
                # SM
                ShopOutfit(
                    outfitId=4034,
                    items = [
                        OutfitItem(itemId=314, price=37, goldPrice=11, color1=174, color2=81, itemType="Shirt"), # Rosetta Red, Crimson Red
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=174, color2=81, itemType="Skirt"), # Rosetta Red, Crimson Red
                        OutfitItem(itemId=3633, price=33, goldPrice=10, color1=174, color2=0, itemType="Shoes"), # Rosetta Red
                    ],
                ),
                # Water Talent Pep Squad
                # F
                ShopOutfit(
                    outfitId=4035,
                    items = [
                        OutfitItem(itemId=311, price=37, goldPrice=11, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue, Crystal Blue
                        OutfitItem(itemId=1575, price=20, goldPrice=7, color1=176, color2=219, itemType="WristItem"), # Silvermist Blue, Crystal Blue
                        OutfitItem(itemId=1224, price=33, goldPrice=10, color1=176, color2=219, itemType="Skirt"), # Silvermist Blue, Crystal Blue
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=176, color2=16, itemType="Shoes"), # Silvermist Blue, Snow White
                    ],
                ),
                # SM
                ShopOutfit(
                    outfitId=4036,
                    items = [
                        OutfitItem(itemId=316, price=37, goldPrice=11, color1=132, color2=176, itemType="Shirt"), # Bubble Blue, Silvermist Blue
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=176, color2=132, itemType="Skirt"), # Silvermist Blue, Bubble Blue
                        OutfitItem(itemId=3633, price=33, goldPrice=10, color1=176, color2=0, itemType="Shoes"), # Silvermist Blue
                    ],
                ),
                # Tinker Talent Pep Squad
                # F
                ShopOutfit(
                    outfitId=4037,
                    items = [
                        OutfitItem(itemId=310, price=37, goldPrice=11, color1=145, color2=1, itemType="Shirt"), # Tinker Bell Green, Mint Green
                        OutfitItem(itemId=1575, price=20, goldPrice=7, color1=145, color2=1, itemType="WristItem"), # Tinker Bell Green, Mint Green
                        OutfitItem(itemId=1224, price=33, goldPrice=10, color1=145, color2=1, itemType="Skirt"), # Tinker Bell Green, Mint Green
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=145, color2=16, itemType="Shoes"), # Tinker Bell Green, Snow White
                    ],
                ),
                # SM
                ShopOutfit(
                    outfitId=4038,
                    items = [
                        OutfitItem(itemId=313, price=37, goldPrice=11, color1=1, color2=145, itemType="Shirt"), # Mint Green, Tinker Bell Green
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=145, color2=1, itemType="Skirt"), # Tinker Bell Green, Mint Green
                        OutfitItem(itemId=3633, price=33, goldPrice=10, color1=145, color2=0, itemType="Shoes"), # Tinker Bell Green
                    ],
                ),
                # Light Talent Pep Squad
                # F
                ShopOutfit(
                    outfitId=4039,
                    items = [
                        OutfitItem(itemId=309, price=37, goldPrice=11, color1=179, color2=111, itemType="Shirt"), # Iridessa Yellow, Sparkling Yellow
                        OutfitItem(itemId=1575, price=20, goldPrice=7, color1=179, color2=111, itemType="WristItem"), # Iridessa Yellow, Sparkling Yellow
                        OutfitItem(itemId=1224, price=33, goldPrice=10, color1=179, color2=111, itemType="Skirt"), # Iridessa Yellow, Sparkling Yellow
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=179, color2=16, itemType="Shoes"), # Iridessa Yellow, Sparkling Yellow
                    ],
                ),
                # SM
                ShopOutfit(
                    outfitId=4040,
                    items = [
                        OutfitItem(itemId=315, price=37, goldPrice=11, color1=111, color2=179, itemType="Shirt"), # Sparkling Yellow, Iridessa Yellow
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=179, color2=111, itemType="Skirt"), # Iridessa Yellow, Sparkling Yellow
                        OutfitItem(itemId=3633, price=33, goldPrice=10, color1=179, color2=0, itemType="Shoes"), # Iridessa Yellow
                    ],
                )
            ],
        ),
        ShopCollection(
            collectionId=4028, # Training Outfits
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            outfits=[
                # Fairies
                ShopOutfit(
                    outfitId=4041,
                    items = [
                        OutfitItem(itemId=278, price=37, goldPrice=11, color1=178, color2=186, itemType="Shirt"), # Fawn Orange, Honeycomb Yellow
                        OutfitItem(itemId=1228, price=33, goldPrice=10, color1=178, color2=186, itemType="Skirt"), # Fawn Orange, Honeycomb Yellow
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=178, color2=0, itemType="Shoes"), # Fawn Orange, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4042,
                    items = [
                        OutfitItem(itemId=278, price=37, goldPrice=11, color1=12, color2=29, itemType="Shirt"), # Tangerine Orange, Goldfish Orange
                        OutfitItem(itemId=1228, price=33, goldPrice=10, color1=12, color2=29, itemType="Skirt"), # Tangerine Orange, Goldfish Orange
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=12, color2=0, itemType="Shoes"), # Tangerine Orange, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4043,
                    items = [
                        OutfitItem(itemId=279, price=37, goldPrice=11, color1=174, color2=54, itemType="Shirt"), # Rosetta Red, Peony Pink
                        OutfitItem(itemId=1229, price=33, goldPrice=10, color1=174, color2=54, itemType="Skirt"), # Rosetta Red, Peony Pink
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=174, color2=0, itemType="Shoes"), # Rosetta Red, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4044,
                    items = [
                        OutfitItem(itemId=279, price=37, goldPrice=11, color1=8, color2=81, itemType="Shirt"), # Watermelon Pink, Crimson Red
                        OutfitItem(itemId=1229, price=33, goldPrice=10, color1=8, color2=81, itemType="Skirt"), # Watermelon Pink, Crimson Red
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=8, color2=0, itemType="Shoes"), # Watermelon Pink, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4045,
                    items = [
                        OutfitItem(itemId=282, price=37, goldPrice=11, color1=176, color2=18, itemType="Shirt"), # Silvermist Blue, Waterfall Blue
                        OutfitItem(itemId=1232, price=33, goldPrice=10, color1=176, color2=18, itemType="Skirt"), # Silvermist Blue, Waterfall Blue
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=176, color2=0, itemType="Shoes"), # Silvermist Blue, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4046,
                    items = [
                        OutfitItem(itemId=282, price=37, goldPrice=11, color1=118, color2=124, itemType="Shirt"), # Sapphire Blue, Forget-Me-Not Blue
                        OutfitItem(itemId=1232, price=33, goldPrice=10, color1=118, color2=124, itemType="Skirt"), # Sapphire Blue, Forget-Me-Not Blue
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=118, color2=0, itemType="Shoes"), # Sapphire Blue, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4047,
                    items = [
                        OutfitItem(itemId=281, price=37, goldPrice=11, color1=145, color2=186, itemType="Shirt"), # Tinker Bell Green, Honeycomb Yellow
                        OutfitItem(itemId=1231, price=33, goldPrice=10, color1=145, color2=186, itemType="Skirt"), # Tinker Bell Green, Honeycomb Yellow
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=145, color2=0, itemType="Shoes"), # Tinker Bell Green, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4048,
                    items = [
                        OutfitItem(itemId=281, price=37, goldPrice=11, color1=64, color2=1, itemType="Shirt"), # Emerald Green, Mint Green
                        OutfitItem(itemId=1231, price=33, goldPrice=10, color1=64, color2=1, itemType="Skirt"), # Emerald Green, Mint Green
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=64, color2=0, itemType="Shoes"), # Emerald Green, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4049,
                    items = [
                        OutfitItem(itemId=280, price=37, goldPrice=11, color1=179, color2=9, itemType="Shirt"), # Iridessa Yellow, Daffodil Yellow
                        OutfitItem(itemId=1230, price=33, goldPrice=10, color1=179, color2=9, itemType="Skirt"), # Iridessa Yellow, Daffodil Yellow
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=179, color2=0, itemType="Shoes"), # Iridessa Yellow, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4050,
                    items = [
                        OutfitItem(itemId=280, price=37, goldPrice=11, color1=116, color2=151, itemType="Shirt"), # Mushroom White, Peanut Yellow
                        OutfitItem(itemId=1230, price=33, goldPrice=10, color1=116, color2=151, itemType="Skirt"), # Mushroom White, Peanut Yellow
                        OutfitItem(itemId=3504, price=33, goldPrice=10, color1=116, color2=0, itemType="Shoes"), # Mushroom White, Snow White
                    ],
                ),
                # Sparrow Men
                ShopOutfit(
                    outfitId=4051,
                    items = [
                        OutfitItem(itemId=288, price=37, goldPrice=11, color1=178, color2=186, itemType="Shirt"), # Fawn Orange, Honeycomb Yellow
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=186, color2=178, itemType="Skirt"), # Honeycomb Yellow, Fawn Orange 
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=178, color2=186, itemType="Shoes"), # Fawn Orange, Honeycomb Yellow
                    ],
                ),
                ShopOutfit(
                    outfitId=4052,
                    items = [
                        OutfitItem(itemId=288, price=37, goldPrice=11, color1=12, color2=29, itemType="Shirt"), # Tangerine Orange, Goldfish Orange
                        OutfitItem(itemId=1241, price=33, goldPrice=10, color1=29, color2=12, itemType="Skirt"), # Goldfish Orange, Tangerine Orange
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=12, color2=29, itemType="Shoes"), # Tangerine Orange, Goldfish Orange
                    ],
                ),
                ShopOutfit(
                    outfitId=4053,
                    items = [
                        OutfitItem(itemId=289, price=37, goldPrice=11, color1=174, color2=54, itemType="Shirt"), # Rosetta Red, Peony Pink
                        OutfitItem(itemId=1242, price=33, goldPrice=10, color1=54, color2=174, itemType="Skirt"), # Peony Pink, Rosetta Red
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=174, color2=54, itemType="Shoes"), # Rosetta Red, Peony Pink
                    ],
                ),
                ShopOutfit(
                    outfitId=4054,
                    items = [
                        OutfitItem(itemId=289, price=37, goldPrice=11, color1=81, color2=8, itemType="Shirt"), # Crimson Red, Watermelon Pink
                        OutfitItem(itemId=1242, price=33, goldPrice=10, color1=8, color2=81, itemType="Skirt"), # Watermelon Pink, Crimson Red
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=81, color2=8, itemType="Shoes"), # Crimson Red, Watermelon Pink
                    ],
                ),
                ShopOutfit(
                    outfitId=4055,
                    items = [
                        OutfitItem(itemId=292, price=37, goldPrice=11, color1=176, color2=18, itemType="Shirt"), # Silvermist Blue, Waterfall Blue
                        OutfitItem(itemId=1244, price=33, goldPrice=10, color1=18, color2=176, itemType="Skirt"), # Waterfall Blue, Silvermist Blue
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=176, color2=18, itemType="Shoes"), # Silvermist Blue, Waterfall Blue
                    ],
                ),
                ShopOutfit(
                    outfitId=4056,
                    items = [
                        OutfitItem(itemId=292, price=37, goldPrice=11, color1=118, color2=124, itemType="Shirt"), # Sapphire Blue, Forget-Me-Not Blue
                        OutfitItem(itemId=1244, price=33, goldPrice=10, color1=124, color2=118, itemType="Skirt"), # Forget-Me-Not Blue, Sapphire Blue
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=118, color2=124, itemType="Shoes"), # Sapphire Blue, Forget-Me-Not Blue
                    ],
                ),
                ShopOutfit(
                    outfitId=4057,
                    items = [
                        OutfitItem(itemId=291, price=37, goldPrice=11, color1=145, color2=186, itemType="Shirt"), # Tinker Bell Green, Honeycomb Yellow
                        OutfitItem(itemId=1245, price=33, goldPrice=10, color1=186, color2=145, itemType="Skirt"), # Honeycomb Yellow, Tinker Bell Green
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=145, color2=186, itemType="Shoes"), # Tinker Bell Green, Honeycomb Yellow
                    ],
                ),
                ShopOutfit(
                    outfitId=4058,
                    items = [
                        OutfitItem(itemId=291, price=37, goldPrice=11, color1=64, color2=1, itemType="Shirt"), # Emerald Green, Mint Green
                        OutfitItem(itemId=1245, price=33, goldPrice=10, color1=1, color2=64, itemType="Skirt"), # Mint Green, Emerald Green
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=64, color2=1, itemType="Shoes"), # Emerald Green, Snow White
                    ],
                ),
                ShopOutfit(
                    outfitId=4059,
                    items = [
                        OutfitItem(itemId=290, price=37, goldPrice=11, color1=179, color2=9, itemType="Shirt"), # Iridessa Yellow, Daffodil Yellow
                        OutfitItem(itemId=1243, price=33, goldPrice=10, color1=9, color2=179, itemType="Skirt"), # Daffodil Yellow, Iridessa Yellow
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=179, color2=9, itemType="Shoes"), # Iridessa Yellow, Daffodil Yellow
                    ],
                ),
                ShopOutfit(
                    outfitId=4060,
                    items = [
                        OutfitItem(itemId=290, price=37, goldPrice=11, color1=116, color2=151, itemType="Shirt"), # Mushroom White, Peanut Yellow
                        OutfitItem(itemId=1243, price=33, goldPrice=10, color1=151, color2=116, itemType="Skirt"), # Peanut Yellow, Mushroom White 
                        OutfitItem(itemId=3625, price=33, goldPrice=10, color1=116, color2=151, itemType="Shoes"), # Mushroom White, Peanut Yellow
                    ],
                )
            ],
        ),
    ],
)