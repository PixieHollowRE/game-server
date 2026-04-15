from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class ShopItem:
    itemId: int = 0
    goldPrice: int = 0
    color1: int = 0
    color2: int = 0
    itemCount: int = 1
    specialType: int = 0
    price: int = 0
    status: int = 0
    howAcquired: int = 0
    memberGoldPrice: int = None

    # This is used by the server-side only.
    itemType: str = ""

    def __post_init__(self):
        if self.memberGoldPrice is None:
            self.memberGoldPrice = self.goldPrice

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> ShopItem:
        if len(data) != 10:
            raise ValueError(f"Expected 10 values for ShopItem, got {len(data)}")
        return cls(*data)

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemId, self.goldPrice, self.color1, self.color2,
            self.itemCount, self.specialType, self.price, self.status,
            self.howAcquired, self.memberGoldPrice
        )
