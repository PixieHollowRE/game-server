from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedInstanceBaseAI(DistributedObjectAI):
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
