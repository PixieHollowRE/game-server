from __future__ import annotations

from collections.abc import Sequence

class Reward:
    def __init__(self) -> None:
        self.itemId: int = 0
        self.amount: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> Reward:
        if len(data) != 2:
            raise ValueError(f"Expected 2 values for Reward, got {len(data)}")

        item = cls()
        item.itemId, item.amount = data
        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemId,
            self.amount,
        )
