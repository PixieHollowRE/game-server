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