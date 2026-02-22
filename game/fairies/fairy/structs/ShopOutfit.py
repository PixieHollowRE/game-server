from __future__ import annotations

from collections.abc import Sequence

from .ShopItem import ShopItem

class ShopOutfit:
    def __init__(self) -> None:
        self.outfitId: int = 0
        self.quality: int = 0
        self.showInCatalog: int = 0
        self.specialType: int = 0
        self.status: int = 0
        self.howAcquired: int = 0
        self.createdById: int = 0
        self.backgroundId: int = 0
        self.modelId: int = 0

        self.items: list[ShopItem] = []

    @classmethod
    def unpackFromTuple(cls, data: Sequence) -> ShopOutfit:
        if len(data) != 10:
            raise ValueError(f"Expected 10 values for ShopOutfit, got {len(data)}")

        outfit = cls()
        (
            outfit.outfitId,
            outfit.quality,
            outfit.showInCatalog,
            outfit.specialType,
            outfit.status,
            outfit.howAcquired,
            outfit.createdById,
            outfit.backgroundId,
            outfit.modelId,
            itemsData,
        ) = data

        outfit.items = [
            ShopItem.unpackFromTuple(itemData)
            for itemData in itemsData
        ]

        return outfit

    def asTuple(self) -> tuple:
        return (
            self.outfitId,
            self.quality,
            self.showInCatalog,
            self.specialType,
            self.status,
            self.howAcquired,
            self.createdById,
            self.backgroundId,
            self.modelId,
            [
                item.asTuple()
                for item in self.items
            ]
        )
