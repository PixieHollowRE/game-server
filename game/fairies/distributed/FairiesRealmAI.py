from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from game.otp.distributed.OtpDoGlobals import *
from game.otp.distributed.DistributedDistrictAI import DistributedDistrictAI

class FairiesRealmAI(DistributedDistrictAI):
    notify = directNotify.newCategory("FairiesRealmAI")

    def __init__(self, air, name="untitled"):
        DistributedDistrictAI.__init__(self, air, name)

    def generate(self):
        DistributedDistrictAI.generate(self)

    def delete(self):
        DistributedDistrictAI.delete(self)
