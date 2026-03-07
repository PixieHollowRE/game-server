from direct.directnotify.DirectNotifyGlobal import directNotify

from game.otp.distributed.DistributedDistrictAI import DistributedDistrictAI

import time

class FairiesHomeRealmAI(DistributedDistrictAI):
    notify = directNotify.newCategory("FairiesHomeRealmAI")

    def __init__(self, air, name="untitled"):
        DistributedDistrictAI.__init__(self, air, name)

    def generate(self):
        DistributedDistrictAI.generate(self)

    def delete(self):
        DistributedDistrictAI.delete(self)

    def setServerTime(self, refresh):
        if refresh:
            # NOTE: Panda3D globalClockDelta doesn't seem to work for this.
            self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), "setServerTime", [int(time.time())])
