from __future__ import annotations

from collections.abc import Sequence

class BadgeProgress:
    def __init__(self) -> None:
        self.badgeId: int = 0
        self.progress: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> BadgeProgress:
        if len(data) != 2:
            raise ValueError(f"Expected 2 values for BadgeProgress, got {len(data)}")

        item = cls()
        item.badgeId, item.progress = data
        return item

    def asTuple(self) -> tuple[int, int]:
        return (
            self.badgeId,
            self.progress
        )
