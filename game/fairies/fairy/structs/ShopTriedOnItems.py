from __future__ import annotations

from collections.abc import Sequence

from game.fairies.fairy.structs.LiteShopItem import LiteShopItem

class ShopTriedOnItems:
    def __init__(self) -> None:
        self.fairyId: int = 0
        self.itemsTriedOn: list[LiteShopItem] = []

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> ShopTriedOnItems:
        if len(data) != 2:
            raise ValueError(f"Expected 2 values for ShopTriedOnItems, got {len(data)}")

        item = cls()
        item.fairyId, item.itemsTriedOn = data
        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.fairyId,
            self.itemsTriedOn
        )