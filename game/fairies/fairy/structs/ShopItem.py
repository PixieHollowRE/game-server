from __future__ import annotations

from collections.abc import Sequence

class ShopItem:
    def __init__(self) -> None:
        self.itemId: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> ShopItem:
        if len(data) != 10:
            raise ValueError(f"Expected 10 values for ShopItem, got {len(data)}")

        item = cls()
        (
            item.itemId,
            item.goldPrice,
            item.color1,
            item.color2,
            item.itemCount,
            item.specialType,
            item.price,
            item.status,
            item.howAcquired,
            item.memberGoldPrice
        ) = data

        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemId,
            self.goldPrice,
            self.color1,
            self.color2,
            self.itemCount,
            self.specialType,
            self.price,
            self.status,
            self.howAcquired,
            self.memberGoldPrice
        )
