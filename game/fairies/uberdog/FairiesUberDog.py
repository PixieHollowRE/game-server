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

    def getGameDoId(self):
        return OTP_DO_ID_FAIRIES

    def createObjects(self):
        # Since we'll be generating objects to the State Server, we should
        # tell it to delete objects when this server goes down.
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.serverId, self.ourChannel, STATESERVER_SHARD_REST)
        datagram.addChannel(self.ourChannel)
        # schedule for execution on socket close
        self.addPostSocketClose(datagram)

        holidayManager = HolidayManagerUD(self)
        holidayManager.generateOtpObject(
            self.getGameDoId(), OTP_ZONE_ID_DISTRICTS, # COMMUNITY_ALERTS_ALL
            doId=self.allocateChannel())

    def handlePlayGame(self, msgType, di):
        # Handle Fairies specific message types before
        # calling the base class
        AIDistrict.handlePlayGame(self, msgType, di)
