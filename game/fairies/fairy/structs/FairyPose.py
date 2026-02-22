from __future__ import annotations

from collections.abc import Sequence

class FairyPose:
    def __init__(self) -> None:
        self.head_rot: int = 0
        self.ul_arm_rot: int = 0
        self.ur_arm_rot: int = 0
        self.ll_arm_rot: int = 0
        self.lr_arm_rot: int = 0
        self.ul_leg_rot: int = 0
        self.ur_leg_rot: int = 0
        self.ll_leg_rot: int = 0
        self.lr_leg_rot: int = 0

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> FairyPose:
        if len(data) != 9:
            raise ValueError(f"Expected 9 values for FairyPose, got {len(data)}")

        pose = cls()
        (
            pose.head_rot,
            pose.ul_arm_rot,
            pose.ur_arm_rot,
            pose.ll_arm_rot,
            pose.lr_arm_rot,
            pose.ul_leg_rot,
            pose.ur_leg_rot,
            pose.ll_leg_rot,
            pose.lr_leg_rot,
        ) = data

        return pose

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.head_rot,
            self.ul_arm_rot,
            self.ur_arm_rot,
            self.ll_arm_rot,
            self.lr_arm_rot,
            self.ul_leg_rot,
            self.ur_leg_rot,
            self.ll_leg_rot,
            self.lr_leg_rot,
        )
