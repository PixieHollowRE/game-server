from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

HOUSING_ZONE_OFFSET = 1000000000

HOME_ZONE_AVAILABLE = 0
HOME_ZONE_UNAVAILABLE = 1
HOME_ZONE_POPULATION_LOCKED = 2

class RealmGuardianUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def homeTeleportRequest(self, avatarId) -> None:
        zoneId = avatarId + HOUSING_ZONE_OFFSET
        self.sendUpdateToAvatarId(avatarId, "homeTeleportResponse", [
            200000, # realmId
            zoneId, # zoneId
            HOME_ZONE_AVAILABLE, # status
            0 # pendingDecorationID
        ])
