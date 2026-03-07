"""
The Fairies Uber Distributed Object Globals server.
"""

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.PyDatagram import PyDatagram

from game.fairies.ai.FairiesAIMsgTypes import *
from game.fairies.distributed.FairiesGlobals import *

from game.otp.ai.AIDistrict import AIDistrict
from game.otp.uberdog.UberDog import UberDog

from game.fairies.uberdog.HolidayManagerUD import HolidayManagerUD


class FairiesUberDog(UberDog):
    notify = directNotify.newCategory("UberDog")

    def __init__(
            self, mdip, mdport, esip, esport, dcFilenames,
            serverId, minChannel, maxChannel):
        assert self.notify.debugStateCall(self)

        UberDog.__init__(
            self, mdip, mdport, esip, esport, dcFilenames,
            serverId, minChannel, maxChannel)

        self.districtInfo: dict[int, int] = {}

        self.generateObjectMap: dict[int, function] = {}

    def getGameDoId(self):
        return OTP_DO_ID_FAIRIES

    def createObjects(self):
        UberDog.createObjects(self)

        # Since we'll be generating objects to the State Server, we should
        # tell it to delete objects when this server goes down.
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.serverId, self.ourChannel, STATESERVER_SHARD_REST)
        datagram.addChannel(self.ourChannel)
        # schedule for execution on socket close
        self.addPostSocketClose(datagram)

        self.holidayManager = HolidayManagerUD(self)
        self.holidayManager.generateOtpObject(
            self.getGameDoId(), COMMUNITY_ALERTS_ALL,
            doId=self.allocateChannel())

        self.badgeManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_BADGE_MANAGER, "FairiesBadgeManager")
        self.realmGuardian = self.generateGlobalObject(OTP_DO_ID_REALM_GUARDIAN, "RealmGuardian")

    def handlePlayGame(self, msgType, di):
        # Handle Fairies specific message types before
        # calling the base class
        if msgType == DISTRICT_REGISTER:
            self.handleDistrictRegister(di)
        elif msgType == GENERATE_OBJECT_RESP:
            self.handleGenerateObjectResp(di)
        else:
            AIDistrict.handlePlayGame(self, msgType, di)

    def handleDistrictRegister(self, di):
        districtDoId = di.getUint32()
        sender = di.getUint32()

        self.districtInfo[districtDoId] = sender

    def remoteGenerateObject(self, aiChannel, objectType, callback):
        context = self.allocateContext()
        self.generateObjectMap[context] = callback

        dg = PyDatagram()
        dg.addServerHeader(aiChannel, self.ourChannel, GENERATE_OBJECT)
        dg.addUint32(context)
        dg.addUint8(objectType)

        self.send(dg)

    def handleGenerateObjectResp(self, di):
        context = di.getUint32()
        callback = self.generateObjectMap.get(context)
        if callback:
            del self.generateObjectMap[context]
            doId = di.getUint32()
            parentId = di.getUint32()
            zoneId = di.getUint32()
            callback(doId, parentId, zoneId)
        else:
            self.notify.warning("Ignoring unexpected context %d for GENERATE_OBJECT" % context)
