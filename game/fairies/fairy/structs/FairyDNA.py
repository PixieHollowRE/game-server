from __future__ import annotations

from collections.abc import Sequence

class FairyDNA:
    def __init__(self) -> None:
        self.talent: int = 0
        self.head: int = 0
        self.height: int = 0
        self.body: int = 0
        self.hair_back: int = 0
        self.hair_front: int = 0
        self.face: int = 0
        self.eye: int = 0
        self.wing: int = 0
        self.hair_color: int = 0
        self.hair_color2: int = 0
        self.eye_color: int = 0
        self.skin_color: int = 0
        self.wing_color: int = 0
        self.gender: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> FairyDNA:
        if len(data) != 15:
            raise ValueError(f"Expected 15 values for FairyDNA, got {len(data)}")

        dna = cls()
        (
            dna.talent,
            dna.head,
            dna.height,
            dna.body,
            dna.hair_back,
            dna.hair_front,
            dna.face,
            dna.eye,
            dna.wing,
            dna.hair_color,
            dna.hair_color2,
            dna.eye_color,
            dna.skin_color,
            dna.wing_color,
            dna.gender,
        ) = data

        return dna

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.talent,
            self.head,
            self.height,
            self.body,
            self.hair_back,
            self.hair_front,
            self.face,
            self.eye,
            self.wing,
            self.hair_color,
            self.hair_color2,
            self.eye_color,
            self.skin_color,
            self.wing_color,
            self.gender,
        )
