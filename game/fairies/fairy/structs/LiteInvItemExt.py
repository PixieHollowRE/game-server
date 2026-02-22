from __future__ import annotations

from collections.abc import Sequence

class LiteInvItemExt:
    def __init__(self) -> None:
        self.invId: int = 0
        self.itemId: int = 0
        self.color1: int = 0
        self.color2: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> LiteInvItemExt:
        if len(data) != 4:
            raise ValueError(f"Expected 4 values for LiteInvItemExt, got {len(data)}")

        item = cls()
        item.invId, item.itemId, item.color1, item.color2 = data
        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.invId,
            self.itemId,
            self.color1,
            self.color2,
        )
