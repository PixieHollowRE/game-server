from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import DYE_ITEM_ID_OFFSET, FACE_TO_EYE_OFFSET, INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.PurchaseType import PurchaseType
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.PRISMS_PIXIE_SPA,
    shopId=9000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.PRISM,
        position=(290, 460),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_PRISM,
    ),
    collections=[
        ShopCollection(
            collectionId=4017, # Wings
            purchaseType=PurchaseType.DNA,
            dnaFields=(("wing", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=6001, price=25, goldPrice=5),
                ShopItem(itemId=6002, price=25, goldPrice=5),
                ShopItem(itemId=6003, price=25, goldPrice=5),
                ShopItem(itemId=6004, price=25, goldPrice=5),
                ShopItem(itemId=6005, price=25, goldPrice=5),
                ShopItem(itemId=6006, price=25, goldPrice=5),
            ],
        ),
        ShopCollection(
            collectionId=4018, # Expressions
            purchaseType=PurchaseType.DNA,
            dnaFields=(("face", 0), ("eye", FACE_TO_EYE_OFFSET)),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                # Fairies
                ShopItem(itemId=4501, price=10, goldPrice=2),
                ShopItem(itemId=4502, price=10, goldPrice=2),
                ShopItem(itemId=4503, price=10, goldPrice=2),
                ShopItem(itemId=4504, price=10, goldPrice=2),
                ShopItem(itemId=4505, price=10, goldPrice=2),
                ShopItem(itemId=4506, price=10, goldPrice=2),
                ShopItem(itemId=4507, price=10, goldPrice=2),
                ShopItem(itemId=4508, price=10, goldPrice=2),
                ShopItem(itemId=4509, price=10, goldPrice=2),
                ShopItem(itemId=4510, price=10, goldPrice=2),
                ShopItem(itemId=4511, price=10, goldPrice=2),
                ShopItem(itemId=4512, price=10, goldPrice=2),
                ShopItem(itemId=4513, price=10, goldPrice=2),
                ShopItem(itemId=4514, price=10, goldPrice=2),
                ShopItem(itemId=4515, price=10, goldPrice=2),
                ShopItem(itemId=4516, price=10, goldPrice=2),
                ShopItem(itemId=4517, price=10, goldPrice=2),
                ShopItem(itemId=4518, price=10, goldPrice=2),
                ShopItem(itemId=4519, price=10, goldPrice=2),
                ShopItem(itemId=4520, price=10, goldPrice=2),
                ShopItem(itemId=4521, price=10, goldPrice=2),
                ShopItem(itemId=4522, price=10, goldPrice=2),
                ShopItem(itemId=4523, price=10, goldPrice=2),
                # Sparrowmen
                ShopItem(itemId=4535, price=10, goldPrice=2), 
                ShopItem(itemId=4536, price=10, goldPrice=2), 
                ShopItem(itemId=4537, price=10, goldPrice=2),
                ShopItem(itemId=4538, price=10, goldPrice=2),
                ShopItem(itemId=4539, price=10, goldPrice=2),
                ShopItem(itemId=4540, price=10, goldPrice=2),
                ShopItem(itemId=4541, price=10, goldPrice=2),
                ShopItem(itemId=4542, price=10, goldPrice=2),                   
                ShopItem(itemId=4543, price=10, goldPrice=2),
                ShopItem(itemId=4544, price=10, goldPrice=2),
                
            ],
        ),
        ShopCollection(
            collectionId=4019, # Skin Colors
            purchaseType=PurchaseType.DNA,
            dnaFields=(("skin_color", -DYE_ITEM_ID_OFFSET),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=14091, price=5, goldPrice=1),
                ShopItem(itemId=14092, price=5, goldPrice=1),
                ShopItem(itemId=14093, price=5, goldPrice=1),
                ShopItem(itemId=14094, price=5, goldPrice=1),
                ShopItem(itemId=14095, price=5, goldPrice=1),
                ShopItem(itemId=14096, price=5, goldPrice=1),
                ShopItem(itemId=14097, price=5, goldPrice=1),
                ShopItem(itemId=14098, price=5, goldPrice=1),
                ShopItem(itemId=14099, price=5, goldPrice=1),
                ShopItem(itemId=14100, price=5, goldPrice=1),
                ShopItem(itemId=14101, price=5, goldPrice=1),
                ShopItem(itemId=14102, price=5, goldPrice=1),
                ShopItem(itemId=14103, price=5, goldPrice=1),
                ShopItem(itemId=14104, price=5, goldPrice=1),
                ShopItem(itemId=14105, price=5, goldPrice=1),
                ShopItem(itemId=14106, price=5, goldPrice=1),
                ShopItem(itemId=14107, price=5, goldPrice=1),
                ShopItem(itemId=14108, price=5, goldPrice=1),
                ShopItem(itemId=14028, price=5, goldPrice=1),
                ShopItem(itemId=14057, price=5, goldPrice=1),
                ShopItem(itemId=14160, price=5, goldPrice=1),
                ShopItem(itemId=14007, price=5, goldPrice=1),
            ],
        ),
        ShopCollection(
            collectionId=4020, # Eye Colors
            purchaseType=PurchaseType.DNA,
            dnaFields=(("eye_color", -DYE_ITEM_ID_OFFSET),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=14055, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14056, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14057, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14058, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14059, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14060, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14061, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14062, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14063, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14064, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14065, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14066, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14067, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14068, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14069, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14070, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14071, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14072, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14136, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14221, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14172, price=5, goldPrice=1, specialType=4),
                ShopItem(itemId=14032, price=5, goldPrice=1, specialType=4),
            ],
        )
    ],
)