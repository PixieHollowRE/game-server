from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task

from game.otp.distributed.OtpDoGlobals import *
from game.otp.distributed.DistributedDistrictAI import DistributedDistrictAI

from . import RealmGlobals

import time

class FairiesRealmAI(DistributedDistrictAI):
    notify = directNotify.newCategory("FairiesRealmAI")

    def __init__(self, air, name="untitled"):
        DistributedDistrictAI.__init__(self, air, name)

    def generate(self):
        DistributedDistrictAI.generate(self)

    def delete(self):
        DistributedDistrictAI.delete(self)

    def updatePopulationLevel(self):
        self.sendUpdate("setPopulationLevel", [self.getPopulationLevel()])

    def getPopulationLevel(self):
        # Same thresholds the capacity checks use, so what the shard chooser
        # shows as "full" is exactly what the server refuses to fly people into.
        # Everyone this AI hosts counts, home realm visitors included -- they
        # are load on the same process as the realm itself.
        return RealmGlobals.getPopulationLevel(
            self.air.getPopulation(), self.air.getRealmPopulationLevels())

    def setServerTime(self, refresh):
        if refresh:
            # NOTE: Panda3D globalClockDelta doesn't seem to work for this.
            self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), "setServerTime", [int(time.time())])
