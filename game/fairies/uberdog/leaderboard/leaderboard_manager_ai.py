from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI


class LeaderBoardMgrAI(DistributedObjectGlobalAI):
    """District stub only; lbRequest is handled authoritatively on LeaderBoardMgrUD."""

    def __init__(self, air) -> None:
        super().__init__(air)
