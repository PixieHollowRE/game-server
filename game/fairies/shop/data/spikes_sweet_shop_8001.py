
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
    zone=ZoneConstants.SPIKES_SWEETS,
    shopId=8001,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.SPIKE,
        position=(417, 355),
        famousFairyId=45,
    ),
    collections=[
        ShopCollection(
            collectionId=4, # Holiday Treats
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22554, goldPrice=1), # Jack o' Lantern Cookie
                ShopItem(itemId=22531, goldPrice=1), # Tea Scone
                ShopItem(itemId=22513, goldPrice=1), # Clover Cookie
                ShopItem(itemId=22512, goldPrice=1), # Pumpkin Cake
                ShopItem(itemId=22511, goldPrice=1), # S'more
                ShopItem(itemId=22587, goldPrice=1), # Magic Tea Cake
                ShopItem(itemId=22588, goldPrice=1), # Magic Tea Drink

            ],
        ),
        ShopCollection(
            collectionId=57, # Baby Animal Sweets
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22582, goldPrice=1), # Baby Bunny Silly Sweet
                ShopItem(itemId=22583, goldPrice=1), # Baby Chipmunk Silly Sweet
                ShopItem(itemId=22584, goldPrice=1), # Baby Owl Silly Sweet
                ShopItem(itemId=22585, goldPrice=1), # Baby Kitten Silly Sweet

            ],
        ),
        ShopCollection(
            collectionId=157, # Deluxe Silly Sweets
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22555, goldPrice=1), # Blackberry Silly Sweet
                ShopItem(itemId=22556, goldPrice=1), # Deluxe Silly Sweet
                ShopItem(itemId=22557, goldPrice=1), # Ice Cream Silly Sweet
                ShopItem(itemId=22570, goldPrice=1), # Candy Corn Silly Sweet
                ShopItem(itemId=22586, goldPrice=1), # Bunny Bubble Silly Sweet
            ],
        ),
    ],
)