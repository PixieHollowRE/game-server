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
    ],
)