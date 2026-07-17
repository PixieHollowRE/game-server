from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

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
            collectionId=39, # Troop Uniforms
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            items=[
                # Rabbit - Fairies
                ShopItem(itemId=2126, price=20, goldPrice=7, color1=178, color2=178, itemType="HeadItem"), # Fawn Orange
                ShopItem(itemId=1000088, price=37, goldPrice=11, color1=178, color2=237, itemType="Shirt"), # Fawn Orange, Melon Orange
                ShopItem(itemId=1496, price=33, goldPrice=10, color1=178, color2=237, itemType="Skirt"), # Fawn Orange, Melon Orange
                ShopItem(itemId=3595, price=33, goldPrice=10, color1=178, color2=237, itemType="Shoes"), # Fawn Orange, Melon Orange
                # Butterfly - Fairies
                ShopItem(itemId=2126, price=20, goldPrice=7, color1=174, color2=174, itemType="HeadItem"), # Rosetta Red
                ShopItem(itemId=1000084, price=37, goldPrice=11, color1=174, color2=121, itemType="Shirt"), # Rosetta Red, Daisy Pink
                ShopItem(itemId=1491, price=33, goldPrice=10, color1=174, color2=121, itemType="Skirt"), # Rosetta Red, Daisy Pink
                ShopItem(itemId=3595, price=33, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red, Daisy Pink
                # Otter - Fairies
                ShopItem(itemId=2126, price=20, goldPrice=7, color1=176, color2=176, itemType="HeadItem"), # Silvermist Blue
                ShopItem(itemId=1000087, price=37, goldPrice=11, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue, Crystal Blue
                ShopItem(itemId=1494, price=33, goldPrice=10, color1=176, color2=219, itemType="Skirt"), # Silvermist Blue, Crystal Blue
                ShopItem(itemId=3595, price=33, goldPrice=10, color1=176, color2=219, itemType="Shoes"), # Silvermist Blue, Crystal Blue
                # Turtle - Fairies
                ShopItem(itemId=2126, price=20, goldPrice=7, color1=145, color2=145, itemType="HeadItem"), # Tinker Bell Green
                ShopItem(itemId=1000089, price=37, goldPrice=11, color1=145, color2=250, itemType="Shirt"), # Tinker Bell Green, Caramel Tan
                ShopItem(itemId=1495, price=33, goldPrice=10, color1=145, color2=250, itemType="Skirt"), # Tinker Bell Green, Caramel Tan
                ShopItem(itemId=3595, price=33, goldPrice=10, color1=145, color2=250, itemType="Shoes"), # Tinker Bell Green, Caramel Tan
                # Gloworm - Fairies
                ShopItem(itemId=2126, price=20, goldPrice=7, color1=179, color2=179, itemType="HeadItem"), # Iridessa Yellow
                ShopItem(itemId=1000085, price=37, goldPrice=11, color1=179, color2=137, itemType="Shirt"), # Iridessa Yellow, Lemon Yellow
                ShopItem(itemId=1492, price=33, goldPrice=10, color1=179, color2=137, itemType="Skirt"), # Iridessa Yellow, Lemon Yellow
                ShopItem(itemId=3595, price=33, goldPrice=10, color1=179, color2=137, itemType="Shoes"), # Iridessa Yellow, Lemon Yellow
                # Rabbit - Sparrowmen
                ShopItem(itemId=2127, price=20, goldPrice=7, color1=178, color2=178, itemType="HeadItem"), # Fawn Orange
                ShopItem(itemId=142, price=37, goldPrice=11, color1=237, color2=78, itemType="Shirt"), # Melon Orange Animal-Talent Tee 
                ShopItem(itemId=1193, price=33, goldPrice=10, color1=178, color2=178, itemType="Skirt"), # Fawn Orange Sporty Shorts
                ShopItem(itemId=3597, price=33, goldPrice=10, color1=178, color2=237, itemType="Shoes"), # Fawn Orange Camp Referee Shoes with Melon Orange Trim
                # Butterfly - Sparrowmen
                ShopItem(itemId=2127, price=20, goldPrice=7, color1=174, color2=174, itemType="HeadItem"), # Rosetta Red
                ShopItem(itemId=139, price=37, goldPrice=11, color1=174, color2=121, itemType="Shirt"), # Rosetta Red Garden-Talent Tee 
                ShopItem(itemId=1193, price=33, goldPrice=10, color1=174, color2=174, itemType="Skirt"), # Rosetta Red Sporty Shorts
                ShopItem(itemId=3597, price=33, goldPrice=10, color1=174, color2=121, itemType="Shoes"), # Rosetta Red Camp Referee Shoes with Daisy Pink Trim
                # Otters - Sparrowmen
                ShopItem(itemId=2127, price=20, goldPrice=7, color1=176, color2=176, itemType="HeadItem"), # Silvermist Blue
                ShopItem(itemId=141, price=37, goldPrice=11, color1=176, color2=219, itemType="Shirt"), # Silvermist Blue Water-Talent Tee
                ShopItem(itemId=1193, price=33, goldPrice=10, color1=176, color2=176, itemType="Skirt"), # Silvermist Blue Sporty Shorts
                ShopItem(itemId=3597, price=33, goldPrice=10, color1=176, color2=219, itemType="Shoes"), # Silvermist Blue Camp Referee Shoes with Crystal Blue Trim
                # Turtle - Sparrowmen
                ShopItem(itemId=2127, price=20, goldPrice=7, color1=145, color2=145, itemType="HeadItem"), # Tinker Bell Green
                ShopItem(itemId=143, price=37, goldPrice=11, color1=145, color2=250, itemType="Shirt"), # Tinker Bell Green Tinker-Talent Tee
                ShopItem(itemId=1193, price=33, goldPrice=10, color1=145, color2=145, itemType="Skirt"), # Tinker Bell Green Sporty Shorts
                ShopItem(itemId=3597, price=33, goldPrice=10, color1=145, color2=250, itemType="Shoes"), # Tinker Bell Green Camp Referee Shoes with Caramel Tan Trim 
                # Gloworm - Sparrowmen
                ShopItem(itemId=2127, price=20, goldPrice=7, color1=179, color2=179, itemType="HeadItem"), # Iridessa Yellow
                ShopItem(itemId=140, price=37, goldPrice=11, color1=179, color2=137, itemType="Shirt"), # Iridessa Yellow Light-Talent Tee 
                ShopItem(itemId=1193, price=33, goldPrice=10, color1=179, color2=179, itemType="Skirt"), # Iridessa Yellow Sporty Shorts
                ShopItem(itemId=3597, price=33, goldPrice=10, color1=179, color2=137, itemType="Shoes"), # Iridessa Yellow Camp Referee Shoes with Lemon Yellow Trim
            ],
        ),
        ShopCollection(
            collectionId=133, # Lobster
            currencyId=INGREDIENTS["MEADOW_GRASS"].id,
            items=[
                ShopItem(itemId=2286, price=33, goldPrice=10, color1=189, color2=7, itemType="HeadItem"), # Lobster Mask
                ShopItem(itemId=347, price=37, goldPrice=11, color1=189, color2=7, itemType="Shirt"), # Lobster Top
                ShopItem(itemId=1293, price=33, goldPrice=10, color1=189, color2=7, itemType="Skirt"),
            ],
        ),
    ],
)