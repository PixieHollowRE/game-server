from __future__ import annotations

from collections.abc import Sequence

from .ShopItem import ShopItem
from .ShopOutfit import ShopOutfit

class ShopCollection:
    def __init__(self) -> None:
        self.collectionId: int = 0
        self.currencyId: int = 0

        self.items: list[ShopItem] = []

        self.outfits: list[ShopOutfit] = []

    @classmethod
    def unpackFromTuple(cls, data: Sequence) -> ShopCollection:
        if len(data) != 4:
            raise ValueError(f"Expected 4 values for ShopCollection, got {len(data)}")

        collection = cls()
        (
            collection.collectionId,
            collection.currencyId,
            itemsData,
            outfitsData,
        ) = data

        collection.items = [
            ShopItem.unpackFromTuple(itemData)
            for itemData in itemsData
        ]

        collection.outfits = [
            ShopOutfit.unpackFromTuple(outfitData)
            for outfitData in outfitsData
        ]

        return collection

    def asTuple(self) -> tuple:
        return (
            self.collectionId,
            self.currencyId,
            [
                item.asTuple()
                for item in self.items
            ],
            [
                outfit.asTuple()
                for outfit in self.outfits
            ]
        )
