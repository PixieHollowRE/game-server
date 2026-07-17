from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import PyDatagram

from game.fairies.distributed.RealmGlobals import OBJECT_TYPE_REALM
from game.fairies.ai.FairiesAIMsgTypes import REALM_DELETE_REQUEST

HOUSING_ZONE_OFFSET = 1000000000

HOME_ZONE_AVAILABLE = 0
HOME_ZONE_UNAVAILABLE = 1
HOME_ZONE_POPULATION_LOCKED = 2

class RealmGuardianUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

        # owner avatarId -> their active home realm doId. A home and its garden
        # share one realm (the client just switches rooms), and visitors share
        # the owner's realm, so there is at most one realm per owner.
        self.ownerToRealm: dict[int, int] = {}
        # realm doId -> owner avatarId (reverse of ownerToRealm)
        self.realmToOwner: dict[int, int] = {}
        # realm doId -> id of the district AI hosting it
        self.realmToDistrict: dict[int, int] = {}
        # realm doId -> set of avatarIds currently inside it
        self.realmOccupants: dict[int, set] = {}
        # avatarId -> the realm doId they are currently in
        self.avatarRealm: dict[int, int] = {}

    def homeTeleportRequest(self, ownerId: int) -> None:
        # ownerId identifies whose home/garden is being entered. The requester
        # (the fairy we reply to) is the sender: the owner for your own home, or
        # a visitor for someone else's.
        requesterId = self.air.getAvatarIdFromSender()

        existingRealm = self.ownerToRealm.get(ownerId)
        if existingRealm is not None:
            self._sendHomeTeleportResponse(requesterId, ownerId, existingRealm)
            return

        # Home realms are global district-siblings visible to every client, so
        # any online district AI can host one. We don't need the owner (who may
        # be offline) or the requester to be in a normal shard.
        districtId = self._pickDistrict(ownerId)
        if districtId is None:
            self.notify.warning(
                "homeTeleportRequest: no district AI available to host a realm "
                "for owner %s" % ownerId)
            return

        def gotRealm(realmId: int, realmParentId: int, realmZoneId: int) -> None:
            self.ownerToRealm[ownerId] = realmId
            self.realmToOwner[realmId] = ownerId
            self.realmToDistrict[realmId] = districtId
            self.realmOccupants[realmId] = set()
            self._sendHomeTeleportResponse(requesterId, ownerId, realmId)

        self.air.remoteGenerateObject(
            self.air.districtInfo[districtId], OBJECT_TYPE_REALM, ownerId, gotRealm)

    def _pickDistrict(self, ownerId: int):
        # Spread home realms across the available districts, stable per owner.
        districtIds = list(self.air.districtInfo.keys())
        if not districtIds:
            return None
        return districtIds[ownerId % len(districtIds)]

    def _sendHomeTeleportResponse(self, requesterId: int, ownerId: int, realmId: int) -> None:
        # The home lives in the OWNER's zone within the realm, so a visitor is
        # sent to ownerId's zone (not their own).
        self.sendUpdateToAvatarId(requesterId, "homeTeleportResponse", [
            realmId,                        # realmId
            ownerId + HOUSING_ZONE_OFFSET,  # zoneId (the owner's home zone)
            HOME_ZONE_AVAILABLE,            # status
            0                               # pendingDecorationID
        ])

    # --- Occupancy tracking + teardown ---

    def handleOccupancyUpdate(self, avatarId: int, ownerId: int) -> None:
        # Move the avatar out of whatever realm they were previously in, tearing
        # that realm down if it just became empty.
        prevRealm = self.avatarRealm.pop(avatarId, None)
        if prevRealm is not None:
            occupants = self.realmOccupants.get(prevRealm)
            if occupants is not None:
                occupants.discard(avatarId)
                if not occupants:
                    self._teardownRealm(prevRealm)

        # ownerId == 0 means the avatar is no longer in any home (left the
        # housing zone entirely, or disconnected).
        if ownerId:
            realmId = self.ownerToRealm.get(ownerId)
            if realmId is not None:
                self.realmOccupants.setdefault(realmId, set()).add(avatarId)
                self.avatarRealm[avatarId] = realmId

    def _teardownRealm(self, realmId: int) -> None:
        districtId = self.realmToDistrict.pop(realmId, None)
        ownerId = self.realmToOwner.pop(realmId, None)
        self.realmOccupants.pop(realmId, None)
        if ownerId is not None:
            self.ownerToRealm.pop(ownerId, None)

        if districtId is not None:
            districtChannel = self.air.districtInfo.get(districtId)
            if districtChannel:
                dg = PyDatagram()
                dg.addServerHeader(districtChannel, self.air.ourChannel, REALM_DELETE_REQUEST)
                dg.addUint32(realmId)
                self.air.send(dg)

        self.notify.info("Tore down empty home realm %d" % realmId)

    def onDistrictRegistered(self, districtId: int) -> None:
        # A district AI (re)registered. If it restarted, every realm we thought
        # it was hosting is gone, so drop our bookkeeping for them; they'll be
        # respawned fresh on the next request. This is what protects reconnects
        # after an AI crash from being handed a dead realm.
        staleRealms = [realmId for realmId, d in self.realmToDistrict.items()
                       if d == districtId]
        for realmId in staleRealms:
            ownerId = self.realmToOwner.pop(realmId, None)
            self.realmToDistrict.pop(realmId, None)
            occupants = self.realmOccupants.pop(realmId, set())
            if ownerId is not None:
                self.ownerToRealm.pop(ownerId, None)
            for avatarId in occupants:
                self.avatarRealm.pop(avatarId, None)
            self.notify.info(
                "Dropped stale home realm %d after district %d re-registered"
                % (realmId, districtId))
