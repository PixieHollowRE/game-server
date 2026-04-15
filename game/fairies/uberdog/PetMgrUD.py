from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

EMPTY_PET_DNA = [0, 0, 0, 0]
EMPTY_PET_DETAIL = [0, 0, 0, 0, 0, 0, 0, 0, 0]

class PetMgrUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def petProfileRequest(self, avatarId: int) -> None:
        self.sendUpdateToAvatarId(
            avatarId, "petProfileResponse",
            [avatarId, EMPTY_PET_DNA, EMPTY_PET_DETAIL]
        )
