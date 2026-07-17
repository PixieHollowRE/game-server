from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.PHOEBES_PARTY_FAVORS,
    shopId=3000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.PHOEBE,
        position=(352, 810),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_PHOEBE
    ),
    collections=[
        ShopCollection(
            collectionId=3000, # Party Decorations
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=17001, price=5, goldPrice=3), # Banner Party
                ShopItem(itemId=17002, price=5, goldPrice=3), # Flower Party
                ShopItem(itemId=17003, price=5, goldPrice=3), # Neverlight Party
                ShopItem(itemId=17004, price=5, goldPrice=3), # Winter Party
                ShopItem(itemId=17005, price=5, goldPrice=3), # Spring Party
                ShopItem(itemId=17006, price=5, goldPrice=3), # Summer Party
                ShopItem(itemId=17007, price=5, goldPrice=3), # Autumn Party
            ]
        ),
        ShopCollection(
            collectionId=3001, # Party Games
            currencyId=INGREDIENTS["ROSE_PETALS"].id,
            items=[
                ShopItem(itemId=13012, price=10, goldPrice=5), # Pass The Popcorn
                ShopItem(itemId=13013, price=10, goldPrice=5), # Simone Says
                ShopItem(itemId=13016, price=10, goldPrice=5), # Rock, Paper, Scissors
                ShopItem(itemId=13017, price=10, goldPrice=5), # Crazy Cakes
                ShopItem(itemId=13018, price=10, goldPrice=5), # Two For Tea
            ]
        ),            
    ],
)