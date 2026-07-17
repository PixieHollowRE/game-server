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
    zone=ZoneConstants.NEVILLES_NEW_HOMES,
    shopId=6000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.NEVILLE,
        position=(785, 458),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_NEVILLE,
        gender=2
    ),
    collections=[
        ShopCollection(
            collectionId=6000, # Small Homes
            purchaseType=PurchaseType.HOME_TYPE,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=29001, price=40, goldPrice=20), # Knothole Nest (HOME ID 1)
                ShopItem(itemId=29002, price=40, goldPrice=20), # Blossom Bungalow (HOME ID 2)
                ShopItem(itemId=29003, price=40, goldPrice=20), # Sunflower Studio (HOME ID 3)
                ShopItem(itemId=29004, price=40, goldPrice=20), # Lotus Loft (HOME ID 4)
                ShopItem(itemId=29005, price=40, goldPrice=20), # Mosswall Cottage (HOME ID 5)
            ],
        ),
        ShopCollection(
            collectionId=6001, # Large Homes
            purchaseType=PurchaseType.HOME_TYPE,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=29026, price=160, goldPrice=80), # Snowflake Estate (HOME ID 26)
                ShopItem(itemId=29021, price=110, goldPrice=55), # Hollow Tree Heights (HOME ID 21)
                ShopItem(itemId=29022, price=110, goldPrice=55), # Petalstem Palace (HOME ID 22)
                ShopItem(itemId=29023, price=100, goldPrice=50), # Sunglow Spire (HOME ID 23)
                ShopItem(itemId=29024, price=130, goldPrice=80), # Streamside Suite (HOME ID 24)
                ShopItem(itemId=29025, price=100, goldPrice=50), # Greenleaf Tower (HOME ID 25)
            ],
        ),
        ShopCollection(
            collectionId=6003, # Platforms
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=6607, price=20, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Flooring
                ShopItem(itemId=6614, price=20, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Stacked Floor
                ShopItem(itemId=6643, price=20, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Stacked Loft
                ShopItem(itemId=6618, price=10, goldPrice=5, color1=39, color2=77), # Springtime Green Leaf Screen Wall
                ShopItem(itemId=6619, price=10, goldPrice=5, color1=39, color2=77), # Springtime Green Leaf Screen Back


            ],
        ),
    ],
)