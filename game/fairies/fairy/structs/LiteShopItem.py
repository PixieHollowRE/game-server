from __future__ import annotations

from collections.abc import Sequence

class LiteShopItem:
    def __init__(self) -> None:
        self.itemIndex: int = 0
        self.collectionId: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> LiteShopItem:
        if len(data) != 2:
            raise ValueError(f"Expected 2 values for LiteShopItem, got {len(data)}")

        item = cls()
        item.itemIndex, item.collectionId = data
        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemIndex,
            self.collectionId,
        )
