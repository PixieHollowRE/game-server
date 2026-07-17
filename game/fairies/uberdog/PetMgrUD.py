from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

EMPTY_PET_DNA = [0, 0, 0, 0]
EMPTY_PET_DETAIL = [0, 0, 0, 0, 0, 0, 0, 0, 0]

class PetMgrUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def petProfileRequest(self, avatarId: int) -> None:
        # avatarId is the fairy whose profile is being viewed, not the viewer, so the
        # response has to go back to the sender. Profile.onGotPetInfo ignores a response
        # whose fairyId isn't the profile it has open, so the payload stays avatarId.
        requesterId = self.air.getAvatarIdFromSender()

        self.sendUpdateToAvatarId(
            requesterId, "petProfileResponse",
            [avatarId, EMPTY_PET_DNA, EMPTY_PET_DETAIL]
        )
