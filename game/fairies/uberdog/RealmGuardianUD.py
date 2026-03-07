from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

from game.fairies.distributed.FairiesGlobals import OBJECT_TYPE_REALM

HOUSING_ZONE_OFFSET = 1000000000

HOME_ZONE_AVAILABLE = 0
HOME_ZONE_UNAVAILABLE = 1
HOME_ZONE_POPULATION_LOCKED = 2

class RealmGuardianUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def homeTeleportRequest(self, avatarId: int) -> None:
        def gotAvatarLocation(doId: int, parentId: int, zoneId: int) -> None:
            # Get the AI channel of the avatar's district:
            districtChannel = self.air.districtInfo[parentId]
            if not districtChannel:
                self.notify.warning("No districtChannel")
                return

            def gotRealm(doId: int, parentId: int, zoneId: int) -> None:
                self.sendUpdateToAvatarId(avatarId, "homeTeleportResponse", [
                    doId, # realmId
                    avatarId + HOUSING_ZONE_OFFSET, # zoneId
                    HOME_ZONE_AVAILABLE, # status
                    0 # pendingDecorationID
                ])

            self.air.remoteGenerateObject(districtChannel, OBJECT_TYPE_REALM, gotRealm)

        self.air.getObjectLocation(avatarId, gotAvatarLocation)
