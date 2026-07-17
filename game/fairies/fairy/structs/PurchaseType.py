from enum import Enum

class PurchaseType(Enum):
    """
    How a purchase from a ShopCollection is fulfilled.

    The client tells us nothing about this -- every collection sends the same
    setRequestPurchase -- so the kind has to be declared on the collection in
    the shop data. It is a property of the collection rather than the shop
    because a shop can sell more than one kind: Neville's sells both homes and
    the furniture to put in them.
    """
    # Clothing, pets: pushed onto avatar.items in the Wardrobe, sent as wardrobeItem.
    WARDROBE = "wardrobe"
    # Sweets, dyes: added to the ingredient pouch rather than the inventory.
    POUCH = "pouch"
    # Hair salon, spa: writes FairyDNA fields instead of granting an item.
    DNA = "dna"
    # Furniture, lamps, decorations: avatar.items in Storage, sent as storageItem.
    # The client has no furniture concept -- furniture *is* storage.
    HOME_ITEM = "homeItem"
    # The homes themselves. Not an item at all: sets the fairy's homeType.
    HOME_TYPE = "homeType"
