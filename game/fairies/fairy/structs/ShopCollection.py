from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .PurchaseType import PurchaseType
from .ShopItem import ShopItem
from .ShopOutfit import ShopOutfit

@dataclass
class ShopCollection:
    collectionId: int = 0
    currencyId: int = 0
    items: list[ShopItem] = field(default_factory=list)
    outfits: list[ShopOutfit] = field(default_factory=list)

    # Server-side only, like ShopItem.itemType: these are not part of the
    # ShopCollection dclass struct, so they stay out of asTuple(). That also
    # means they do not survive a setShopItems round trip -- read them off the
    # shop data (getShopByZone) rather than off a generated shopkeeper.
    purchaseType: PurchaseType = PurchaseType.WARDROBE
    # (FairyDNA field name, itemId offset) pairs applied on a DNA purchase.
    dnaFields: tuple[tuple[str, int], ...] = ()

    @classmethod
    def unpackFromTuple(cls, data: Sequence) -> ShopCollection:
        if len(data) != 4:
            raise ValueError(f"Expected 4 values for ShopCollection, got {len(data)}")

        collectionId, currencyId, items_data, outfits_data = data

        return cls(
            collectionId=collectionId,
            currencyId=currencyId,
            items=[ShopItem.unpackFromTuple(item) for item in items_data],
            outfits=[ShopOutfit.unpackFromTuple(outfit) for outfit in outfits_data],
        )

    def asTuple(self) -> tuple:
        return (
            self.collectionId,
            self.currencyId,
            [item.asTuple() for item in self.items],
            [outfit.asTuple() for outfit in self.outfits],
        )
