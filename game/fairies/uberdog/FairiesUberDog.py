"""
The Fairies Uber Distributed Object Globals server.
"""

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.PyDatagram import PyDatagram

from game.fairies.ai.FairiesAIMsgTypes import *
from game.fairies.distributed.FairiesGlobals import *

from game.otp.ai.AIDistrict import AIDistrict
from game.otp.uberdog.UberDog import UberDog

from game.fairies.distributed.MongoInterface import MongoInterface
from game.fairies.distributed.RealmPopulation import RealmPopulationRegistry

from game.fairies.uberdog.HolidayManagerUD import HolidayManagerUD


class FairiesUberDog(UberDog, RealmPopulationRegistry):
    notify = directNotify.newCategory("UberDog")

    def __init__(
            self, mdip, mdport, esip, esport, dcFilenames,
            serverId, minChannel, maxChannel):
        assert self.notify.debugStateCall(self)

        UberDog.__init__(
            self, mdip, mdport, esip, esport, dcFilenames,
            serverId, minChannel, maxChannel)

        RealmPopulationRegistry.__init__(self)

        self.mongoInterface = MongoInterface(self)

        # Maps a district's doId -> that district's AI channel. Populated as
        # districts register with us (SHARDMANAGER_ONLINE). The RealmGuardian
        # uses this to find which AI process to ask for a home realm.
        self.districtInfo = {}

        # Outstanding remoteGenerateObject requests, keyed by context.
        self.objectGenerateMap = {}

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
        self.inventoryManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_INVENTORY_MANAGER, "FairyInventoryMgr")
        self.petManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_PET_MANAGER, "PetMgr")
        self.leaderBoardManager = self.generateGlobalObject(OTP_DO_ID_LEADERBOARD_MANAGER, "LeaderBoardMgr")

        # Ask any districts that are already up to (re)announce themselves, in
        # case they started before us and their startup registration was lost.
        self.requestDistrictRegistrations()

    def handleConnect(self, msgType, di):
        # Districts broadcast their headcount on their own schedule, so if we
        # restarted one can arrive before we reach playGame. Record it rather
        # than let the base class log it as an unexpected message type.
        if msgType == REALM_POPULATION_UPDATE:
            self.handleRealmPopulationUpdate(di)
            return

        UberDog.handleConnect(self, msgType, di)

    def handlePlayGame(self, msgType, di):
        # Handle Fairies specific message types before
        # calling the base class
        if msgType == SHARDMANAGER_ONLINE:
            self.handleShardManagerOnline(di)
            return
        elif msgType == REALM_GENERATE_RESPONSE:
            self._handleRemoteGenerateResponse(di)
            return
        elif msgType == REALM_OCCUPANCY_UPDATE:
            self._handleRealmOccupancyUpdate(di)
            return
        elif msgType == REALM_MAIL_ARRIVED:
            self._handleRealmMailArrived(di)
            return
        elif msgType == REALM_POPULATION_UPDATE:
            # A district reporting its headcount, so the RealmGuardian can see
            # which shards still have room.
            self.handleRealmPopulationUpdate(di)
            return
        elif msgType == REALM_REGISTER_REQUEST:
            # Our own broadcast echoing back to us; only districts act on it.
            return

        AIDistrict.handlePlayGame(self, msgType, di)

    def _handleRealmOccupancyUpdate(self, di):
        avatarId = di.getUint32()
        ownerId = di.getUint32()
        # The home the reporting district AI believed the avatar was in. The
        # guardian checks it rather than trusting it -- see handleOccupancyUpdate.
        fromOwnerId = di.getUint32()
        if getattr(self, 'realmGuardian', None):
            self.realmGuardian.handleOccupancyUpdate(avatarId, ownerId, fromOwnerId)

    def _handleRealmMailArrived(self, di):
        recipientId = di.getUint32()
        typeId = di.getUint32()
        if getattr(self, 'realmGuardian', None):
            self.realmGuardian.handleMailArrived(recipientId, typeId)

    def requestDistrictRegistrations(self):
        # Broadcast to every district AI asking it to announce its channel.
        dg = PyDatagram()
        dg.addServerHeader(BROADCAST_MESSAGE_TO_ALL_AI, self.ourChannel, REALM_REGISTER_REQUEST)
        self.send(dg)

    def handleShardManagerOnline(self, di):
        # A district AI has come up and is telling us its channel so we can
        # route remote-generate requests (e.g. home realms) to it.
        districtId = di.getUint32()
        aiChannel = di.getUint64()
        self.districtInfo[districtId] = aiChannel
        self.notify.info("District %d registered (AI channel %d)" % (districtId, aiChannel))

        # If this district restarted, any home realms it was hosting are gone.
        if getattr(self, 'realmGuardian', None):
            self.realmGuardian.onDistrictRegistered(districtId)

    def remoteGenerateObject(self, aiChannel, objectType, ownerId, callback):
        """
        Ask the district AI at aiChannel to generate an object of the given
        type (see RealmGlobals.OBJECT_TYPE_*) belonging to ownerId, then invoke
        callback(doId, parentId, zoneId) once it reports back.
        """
        context = self.allocateContext()
        self.objectGenerateMap[context] = callback

        dg = PyDatagram()
        dg.addServerHeader(aiChannel, self.ourChannel, REALM_GENERATE_REQUEST)
        dg.addUint32(context)
        dg.addUint8(objectType)
        dg.addUint32(ownerId)
        self.send(dg)

    def _handleRemoteGenerateResponse(self, di):
        context = di.getUint32()
        doId = di.getUint32()
        parentId = di.getUint32()
        zoneId = di.getUint32()

        callback = self.objectGenerateMap.pop(context, None)
        if callback:
            callback(doId, parentId, zoneId)
        else:
            self.notify.warning(
                "Ignoring unexpected context %d for REALM_GENERATE_RESPONSE" % context)
