from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import PyDatagram
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.distributed.RealmGlobals import OBJECT_TYPE_REALM
from game.fairies.ai.FairiesAIMsgTypes import REALM_DELETE_REQUEST, REALM_MAIL_DELIVERED

HOUSING_ZONE_OFFSET = 1000000000

HOME_ZONE_AVAILABLE = 0
HOME_ZONE_UNAVAILABLE = 1
HOME_ZONE_POPULATION_LOCKED = 2

# Fairies allowed inside one home realm (house + garden together) at a time,
# unless home-realm-max-occupants says otherwise. 0 disables the cap.
DEFAULT_MAX_HOME_OCCUPANTS = 30

# How long an empty home realm is kept alive before it is torn down.
#
# The realm doId is the parent the arriving client sets interest on, so deleting
# one mid-teleport leaves that client waiting forever for an interest reply the
# state server will never send -- and the client's TeleportIn state has no
# timeout, so it never recovers. A grace period means a realm that empties for a
# moment (everyone leaving at once, bookkeeping arriving out of order) is reused
# rather than destroyed and immediately respawned.
DEFAULT_TEARDOWN_GRACE_SECS = 30

# How long a fairy who has been handed a realm is held as an incoming occupant
# before we assume the teleport was abandoned. Long enough to cover a slow
# client's asset load, short enough that a cancelled flight does not hold a slot
# against the occupancy cap for long.
DEFAULT_RESERVATION_SECS = 60

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
        # realm doId -> set of avatarIds who have reported arriving in it
        self.realmOccupants: dict[int, set] = {}
        # realm doId -> set of avatarIds we have promised a place to but who
        # have not arrived yet. A fairy is only reported as an occupant once
        # they land, which is a whole loading screen after we answer their
        # request, so until then nothing else would stop the realm being torn
        # down under them or another visitor taking the last slot.
        self.realmReservations: dict[int, set] = {}
        # avatarId -> the realm doId they are currently in
        self.avatarRealm: dict[int, int] = {}

    def homeTeleportRequest(self, ownerId: int) -> None:
        # ownerId identifies whose home/garden is being entered. The requester
        # (the fairy we reply to) is the sender: the owner for your own home, or
        # a visitor for someone else's.
        requesterId = self.air.getAvatarIdFromSender()

        existingRealm = self.ownerToRealm.get(ownerId)
        if existingRealm is not None:
            self._sendHomeTeleportResponse(
                requesterId, ownerId, existingRealm,
                self._homeStatusFor(requesterId, ownerId, existingRealm))
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
            # A realm we just spawned is empty, so the requester always fits.
            self._sendHomeTeleportResponse(
                requesterId, ownerId, realmId, HOME_ZONE_AVAILABLE)

        self.air.remoteGenerateObject(
            self.air.districtInfo[districtId], OBJECT_TYPE_REALM, ownerId, gotRealm)

    def _maxHomeOccupants(self) -> int:
        return config.GetInt("home-realm-max-occupants", DEFAULT_MAX_HOME_OCCUPANTS)

    def _teardownGraceSecs(self) -> int:
        return config.GetInt("home-realm-teardown-grace", DEFAULT_TEARDOWN_GRACE_SECS)

    def _reservationSecs(self) -> int:
        return config.GetInt("home-realm-reservation-timeout", DEFAULT_RESERVATION_SECS)

    def _realmHeadcount(self, realmId: int) -> int:
        # Fairies on their way in count against the cap too, otherwise a popular
        # house lets in far more than the limit while they are all still loading.
        return (len(self.realmOccupants.get(realmId, ()))
                + len(self.realmReservations.get(realmId, ())))

    def _realmIsEmpty(self, realmId: int) -> bool:
        return not self._realmHeadcount(realmId)

    def _homeStatusFor(self, requesterId: int, ownerId: int, realmId: int) -> int:
        # Decide whether one more fairy fits in this home realm. A house and its
        # garden share the realm, so this is a single cap across both rooms.
        maxOccupants = self._maxHomeOccupants()
        if maxOccupants <= 0:
            return HOME_ZONE_AVAILABLE

        if requesterId == ownerId:
            # You can always get into your own home. (The client believes this
            # too and ignores the lock for its own home/garden, so refusing
            # here would only produce a pointless failure message.)
            return HOME_ZONE_AVAILABLE

        if (requesterId in self.realmOccupants.get(realmId, ())
                or requesterId in self.realmReservations.get(realmId, ())):
            # Already inside, or already on their way: hopping between the house
            # and the garden re-sends homeTeleportRequest, and that must not be
            # turned away by a cap the requester is themselves part of.
            return HOME_ZONE_AVAILABLE

        if self._realmHeadcount(realmId) < maxOccupants:
            return HOME_ZONE_AVAILABLE

        return HOME_ZONE_POPULATION_LOCKED

    def _pickDistrict(self, ownerId: int):
        # Spread home realms across the available districts, stable per owner.
        # Skip districts that are already FULL: everyone who visits a home realm
        # is generated on -- and counted against -- whichever district AI hosts
        # it, so parking one on a full shard just pushes it further over.
        districtIds = list(self.air.districtInfo.keys())
        if not districtIds:
            return None

        roomy = [districtId for districtId in districtIds
                 if not self.air.isRealmFull(districtId)]
        if roomy:
            return roomy[ownerId % len(roomy)]

        # Every district is full. The owner still needs somewhere to live, so
        # fall back to the least crowded one rather than refusing outright.
        return min(districtIds, key=self.air.getRealmPopulation)

    def _sendHomeTeleportResponse(self, requesterId: int, ownerId: int, realmId: int,
                                  status: int) -> None:
        # The home lives in the OWNER's zone within the realm, so a visitor is
        # sent to ownerId's zone (not their own).
        #
        # realmId/zoneId are sent even when status is HOME_ZONE_POPULATION_LOCKED:
        # the client overrides the lock for GMs and for someone already standing
        # in that exact realm+zone, and needs a real destination in those cases.
        # Those overrides are also why the reservation below is taken whatever
        # the status is -- we have handed out a realm that the client may well
        # fly into, and it has to survive until they get there.
        self._reserveRealm(realmId, requesterId)

        self.sendUpdateToAvatarId(requesterId, "homeTeleportResponse", [
            realmId,                        # realmId
            ownerId + HOUSING_ZONE_OFFSET,  # zoneId (the owner's home zone)
            status,                         # status
            0                               # pendingDecorationID
        ])

    # --- Post Office mail ---

    def handleMailArrived(self, recipientId: int, typeId: int) -> None:
        # A district AI wrote Post Office mail for `recipientId`. If that fairy's
        # home realm is up right now, tell the district hosting it to put the
        # mailbox out -- the realm only reads the message count at generate, so
        # a recipient standing in their own home would otherwise not see it.
        realmId = self.ownerToRealm.get(recipientId)
        if realmId is None:
            # No realm up: nothing to update. Whoever next enters this fairy's
            # home spawns a fresh realm, and loadPostOfficeSurprises picks the
            # mail up from Mongo then.
            return

        districtId = self.realmToDistrict.get(realmId)
        districtChannel = (self.air.districtInfo.get(districtId)
                           if districtId is not None else None)
        if not districtChannel:
            self.notify.warning(
                "handleMailArrived: no district channel for realm %s (owner %s)"
                % (realmId, recipientId))
            return

        dg = PyDatagram()
        dg.addServerHeader(districtChannel, self.air.ourChannel, REALM_MAIL_DELIVERED)
        dg.addUint32(realmId)
        dg.addUint32(typeId)
        self.air.send(dg)

    # --- Reservations (fairies on their way in) ---

    def _reservationTaskName(self, realmId: int, avatarId: int) -> str:
        return "RealmReservation-%d-%d" % (realmId, avatarId)

    def _reserveRealm(self, realmId: int, avatarId: int) -> None:
        # Hold a place in this realm for a fairy we have just pointed at it.
        if self.avatarRealm.get(avatarId) == realmId:
            # Already inside -- switching between the house and the garden
            # re-sends homeTeleportRequest. Nothing to hold.
            return

        self._cancelTeardown(realmId)
        self.realmReservations.setdefault(realmId, set()).add(avatarId)

        taskMgr.remove(self._reservationTaskName(realmId, avatarId))
        taskMgr.doMethodLater(
            self._reservationSecs(), self._reservationExpiredTask,
            self._reservationTaskName(realmId, avatarId),
            extraArgs=[realmId, avatarId])

    def _dropReservation(self, realmId: int, avatarId: int) -> None:
        reservations = self.realmReservations.get(realmId)
        if reservations is None:
            return

        reservations.discard(avatarId)
        if not reservations:
            self.realmReservations.pop(realmId, None)

    def _clearReservation(self, realmId: int, avatarId: int) -> None:
        taskMgr.remove(self._reservationTaskName(realmId, avatarId))
        self._dropReservation(realmId, avatarId)

    def _reservationExpiredTask(self, realmId: int, avatarId: int) -> int:
        # They never arrived: the teleport was cancelled, rejected client-side,
        # or the client dropped on the loading screen. Give the slot back, and
        # reclaim the realm if that leaves nobody in it -- a realm spawned for a
        # flight that never completed would otherwise sit there forever.
        self._dropReservation(realmId, avatarId)

        if self._realmIsEmpty(realmId):
            self.notify.info(
                "Reservation for %d in realm %d expired unused" % (avatarId, realmId))
            self._scheduleTeardown(realmId)

        return Task.done

    # --- Occupancy tracking + teardown ---

    def handleOccupancyUpdate(self, avatarId: int, ownerId: int,
                              fromOwnerId: int = 0) -> None:
        """
        An avatar moved out of `fromOwnerId`'s home and into `ownerId`'s, where
        0 means "no home" on either side.

        `fromOwnerId` is the home the *reporting district AI* believed the avatar
        was in, and it has to be checked rather than trusted. Entering a home
        realm hosted by a different district AI process migrates the avatar
        object between processes: the old process deletes its copy and reports a
        departure, the new one reports the arrival, and the two race. A departure
        that lands after the arrival used to empty the realm the fairy had just
        flown into and tear it down under them -- which, since the realm doId is
        the parent their client sets interest on, hung them on the loading
        screen forever. So a departure only counts if the avatar is still where
        the reporter thought they were.
        """
        if fromOwnerId:
            currentRealm = self.avatarRealm.get(avatarId)
            leavingRealm = self.ownerToRealm.get(fromOwnerId)

            if currentRealm is not None and currentRealm == leavingRealm:
                self._removeOccupant(avatarId, currentRealm)
            elif currentRealm is not None:
                self.notify.debug(
                    "Ignoring stale departure from owner %s for avatar %s, who "
                    "is in realm %s now" % (fromOwnerId, avatarId, currentRealm))

        # ownerId == 0 means the avatar is no longer in any home (left the
        # housing zone entirely, or disconnected).
        if not ownerId:
            return

        realmId = self.ownerToRealm.get(ownerId)

        # An avatar can only be in one realm, so an arrival is also proof they
        # left wherever we had them before. This is the safety net for a
        # migrated AI copy that reports an arrival it believes to be the
        # fairy's first (fromOwnerId 0) because it was generated after the
        # client sent its zone. It has to run even when there is no realm to
        # join, or the realm they came from would never empty.
        currentRealm = self.avatarRealm.get(avatarId)
        if currentRealm is not None and currentRealm != realmId:
            self._removeOccupant(avatarId, currentRealm)

        if realmId is None:
            # No realm up for that home, so there is nothing to join. The client
            # is answered with one before it ever gets here, so this means the
            # realm went away underneath them.
            self.notify.warning(
                "Avatar %s reported arriving in %s's home, which has no realm"
                % (avatarId, ownerId))
            return

        self._clearReservation(realmId, avatarId)
        self._cancelTeardown(realmId)
        self.realmOccupants.setdefault(realmId, set()).add(avatarId)
        self.avatarRealm[avatarId] = realmId

    def _removeOccupant(self, avatarId: int, realmId: int) -> None:
        if self.avatarRealm.get(avatarId) == realmId:
            self.avatarRealm.pop(avatarId, None)

        self._clearReservation(realmId, avatarId)

        occupants = self.realmOccupants.get(realmId)
        if occupants is not None:
            occupants.discard(avatarId)

        if self._realmIsEmpty(realmId):
            self._scheduleTeardown(realmId)

    def _teardownTaskName(self, realmId: int) -> str:
        return "RealmTeardown-%d" % realmId

    def _scheduleTeardown(self, realmId: int) -> None:
        if realmId not in self.realmToOwner:
            # Already gone.
            return

        # Restarting the timer rather than stacking one keeps an emptied realm
        # alive for the full grace period after the *last* fairy left.
        taskMgr.remove(self._teardownTaskName(realmId))
        taskMgr.doMethodLater(
            self._teardownGraceSecs(), self._teardownTask,
            self._teardownTaskName(realmId), extraArgs=[realmId])

    def _cancelTeardown(self, realmId: int) -> None:
        taskMgr.remove(self._teardownTaskName(realmId))

    def _teardownTask(self, realmId: int) -> int:
        if not self._realmIsEmpty(realmId):
            # Somebody moved back in during the grace period.
            return Task.done

        self._teardownRealm(realmId)
        return Task.done

    def _teardownRealm(self, realmId: int) -> None:
        taskMgr.remove(self._teardownTaskName(realmId))
        for avatarId in list(self.realmReservations.get(realmId, ())):
            self._clearReservation(realmId, avatarId)

        districtId = self.realmToDistrict.pop(realmId, None)
        ownerId = self.realmToOwner.pop(realmId, None)
        self.realmOccupants.pop(realmId, None)
        self.realmReservations.pop(realmId, None)
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
            self._cancelTeardown(realmId)
            for avatarId in list(self.realmReservations.get(realmId, ())):
                self._clearReservation(realmId, avatarId)

            ownerId = self.realmToOwner.pop(realmId, None)
            self.realmToDistrict.pop(realmId, None)
            occupants = self.realmOccupants.pop(realmId, set())
            self.realmReservations.pop(realmId, None)
            if ownerId is not None:
                self.ownerToRealm.pop(ownerId, None)
            for avatarId in occupants:
                self.avatarRealm.pop(avatarId, None)
            self.notify.info(
                "Dropped stale home realm %d after district %d re-registered"
                % (realmId, districtId))
