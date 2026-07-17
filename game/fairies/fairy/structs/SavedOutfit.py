from __future__ import annotations

from collections.abc import Sequence

from dataclasses import dataclass, field

from .LiteInvItemExt2 import LiteInvItemExt2

@dataclass
class SavedOutfit:
    outfitId: int = 0
    headItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    necklaceItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    shirtItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    beltItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    skirtItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    wristItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    ankleItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)
    shoesItem: LiteInvItemExt2 = field(default_factory=LiteInvItemExt2)

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> SavedOutfit:
        if len(data) != 9:
            raise ValueError(f"Expected 9 values for SavedOutfit, got {len(data)}")

        item = cls()
        item.outfitId, item.headItem, item.necklaceItem, item.shirtItem, item.beltItem, item.skirtItem, item.wristItem, item.ankleItem, item.shoesItem = data
        return item

    def asTuple(self) -> tuple:
        return (
            self.outfitId,
            self.headItem.asTuple(),
            self.necklaceItem.asTuple(),
            self.shirtItem.asTuple(),
            self.beltItem.asTuple(),
            self.skirtItem.asTuple(),
            self.wristItem.asTuple(),
            self.ankleItem.asTuple(),
            self.shoesItem.asTuple()
        )