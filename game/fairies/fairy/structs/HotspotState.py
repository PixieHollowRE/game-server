from __future__ import annotations

from collections.abc import Sequence

class HotspotState:
    def __init__(self) -> None:
        self.hotspotId: int = 0
        self.frameId: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> HotspotState:
        if len(data) != 2:
            raise ValueError(f"Expected 2 values for HotspotState, got {len(data)}")

        item = cls()
        item.hotspotId, item.frameId = data
        return item

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.hotspotId,
            self.frameId,
        )
