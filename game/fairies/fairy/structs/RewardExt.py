from __future__ import annotations

from collections.abc import Sequence

class RewardExt:
    def __init__(self) -> None:
        self.itemId: int = 0
        self.amount: int = 0
        self.color1: int = 0
        self.color2: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> RewardExt:
        if len(data) != 4:
            raise ValueError(f"Expected 4 values for RewardExt, got {len(data)}")

        item = cls()
        item.itemId, item.amount, item.color1, item.color2 = data
        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemId,
            self.amount,
            self.color1,
            self.color2
        )
