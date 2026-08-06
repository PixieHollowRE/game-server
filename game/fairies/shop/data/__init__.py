import pkgutil
import importlib

from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.shop.ShopHelpers import NPCShop

def load_all_shops():
    shops = []
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{__name__}.{module_name}")
        if hasattr(module, "SHOP"):
            shops.append(module.SHOP)
    return shops

SHOPS = load_all_shops()

SHOPS_BY_ZONE = {shop.zone: shop for shop in SHOPS}

for shop in SHOPS:
    shop.collectionsById = {collection.collectionId: collection for collection in shop.collections}

def getShopByZone(zone: int) -> NPCShop | None:
    return SHOPS_BY_ZONE.get(zone)

def getShopItemByIndex(shop: NPCShop, collectionId: int, itemIndex: int) -> ShopItem | None:
    collection = shop.collectionsById.get(collectionId)

    if not collection:
        return None

    if 0 <= itemIndex < len(collection.items):
        return collection.items[itemIndex]

    return None

def getShopOutfitByOutfitId(shop: NPCShop, collectionId: int, outfitId: int) -> ShopOutfit | None:
    collection = shop.collectionsById.get(collectionId)

    if not collection:
        return None

    return next((outfit for outfit in collection.outfits if outfit.outfitId == outfitId), None)


# Note from Jessi:
# In shopPanel.xml, there are 154 collectionIds that have already been taken:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 26, 
# 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 41, 42, 43, 46, 53, 56, 57, 
# 58, 59, 60, 61, 62, 63, 69, 70, 71, 72, 78, 79, 82, 83, 84, 95, 97, 100, 102, 
# 106, 108, 109, 111, 114, 115, 116, 118, 119, 120, 129, 130, 131, 132, 133, 134, 
# 135, 136, 146, 147, 153, 154, 157, 188, 189, 190, 191, 192, 193, 208, 209, 281, 
# 389, 390, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 
# 1013, 1014, 1015, 1019, 1020, 1023, 1030, 1062, 1075, 1076, 1077, 2001, 2003, 2008, 
# 2009, 2020, 3000, 3001, 3002, 3003, 3004, 4001, 4003, 4004, 4005, 4006, 4010, 4011, 
# 4012, 4013, 4014, 4015, 4017, 4018, 4019, 4020, 5001, 5002, 5003, 5004, 5005, 5006, 
# 5007, 6000, 6001, 6002, 6003, 7001, 7002
# 
# From this list, here are the missing gaps from the numerical order:
# 17, 22–25, 35–36, 44–45, 47–52, 64–68, 73–77, 80–81, 85–94, 98–99, 
# 103–105, 110, 112–113, 117, 121–128, 137–145, 148–152, 155–156, 
# 158–187, 194–207, 210–280, 282–388, 391–1000, 1016–1018, 1021–1022, 
# 1024–1029, 1031–1061, 1063–1074, 1078–2000, 2002, 2004–2007, 2010–2019, 
# 2021–2999, 3005–4000, 4007–4009, 4016, 4021–5000, 5008–5999, 6004–7000
# 
# Keep this in mind when adding new collections!