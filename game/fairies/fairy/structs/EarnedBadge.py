from __future__ import annotations

class EarnedBadge:
    def __init__(self) -> None:
        self.badgeId: int = 0
        self.dateEarned: str = ""

    @classmethod
    def unpackFromTuple(cls, data: tuple[int, str]) -> EarnedBadge:
        if len(data) != 2:
            raise ValueError(f"Expected 2 values for EarnedBadge, got {len(data)}")

        item = cls()
        item.badgeId, item.dateEarned = data
        return item

    def asTuple(self) -> tuple[int, str]:
        return (
            self.badgeId,
            self.dateEarned
        )
