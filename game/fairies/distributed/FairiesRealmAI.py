from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task

from game.otp.distributed.OtpDoGlobals import *
from game.otp.distributed.DistributedDistrictAI import DistributedDistrictAI

from . import RealmGlobals

import time
import json

class FairiesRealmAI(DistributedDistrictAI):
    notify = directNotify.newCategory("FairiesRealmAI")

    def __init__(self, air, name="untitled"):
        DistributedDistrictAI.__init__(self, air, name)

        self.realmPopulationLevels: list[int] = json.loads(config.GetString("realm-population-levels"))

    def generate(self):
        DistributedDistrictAI.generate(self)

    def delete(self):
        DistributedDistrictAI.delete(self)

    def updatePopulationLevel(self):
        self.sendUpdate("setPopulationLevel", [self.getPopulationLevel()])

    def getPopulationLevel(self):
        realmPop = self.air.getPopulation()

        if realmPop >= self.realmPopulationLevels[3]:
            return RealmGlobals.FULL_LEVEL
        elif realmPop >= self.realmPopulationLevels[2]:
            return RealmGlobals.CROWDED_LEVEL
        elif realmPop >= self.realmPopulationLevels[1]:
            return RealmGlobals.IDEAL_LEVEL
        else:
            return RealmGlobals.QUIET_LEVEL

    def setServerTime(self, refresh):
        if refresh:
            # NOTE: Panda3D globalClockDelta doesn't seem to work for this.
            self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), "setServerTime", [int(time.time())])
