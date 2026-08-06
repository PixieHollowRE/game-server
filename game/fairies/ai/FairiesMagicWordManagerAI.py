from direct.distributed.DistributedObjectAI import DistributedObjectAI

from game.fairies.fairy.DistributedFairyGMAI import DistributedFairyGMAI
from game.fairies.magicwords import commands  # noqa: F401 -- fills the registry
from game.fairies.magicwords.registry import MagicWordError, dispatch


class FairiesMagicWordManagerAI(DistributedObjectAI):
    """
    The server end of the client's LiveMod developer console.

    setMagicWord is `clsend`, so anything with a socket can call it. The avatar
    class is what says who is allowed to: FairyClient.lua activates a staff login
    as DistributedFairyGM and everyone else as DistributedFairyPlayer, so a
    non-GM asking for a magic word is a modified client and is refused here.
    """

    notify = directNotify.newCategory("FairiesMagicWordManagerAI")

    def __init__(self, air) -> None:
        super().__init__(air)

        self.identifier: int = 0

    def setMagicWord(self, magicWord: str, avId: int, zoneId: int, signature: str):
        senderId = self.air.getAvatarIdFromSender()

        # avId is whatever the client put in the message; the sender channel is
        # not. Anywhere they disagree, someone is asking us to act as another
        # fairy, so the sender wins and the attempt is logged.
        if senderId != avId:
            self.notify.warning(
                f"setMagicWord from {senderId} claiming to be {avId}: {magicWord!r}"
            )

        av = self.air.doId2do.get(senderId)

        if not av:
            self.notify.warning(f"setMagicWord from unknown avatar {senderId}")
            return

        if not isinstance(av, DistributedFairyGMAI):
            self.notify.warning(
                f"setMagicWord from non-GM {senderId} ({av.getName()!r}): {magicWord!r}"
            )
            return

        self.notify.info(f"magic word from {senderId}: {magicWord!r}")

        try:
            response = dispatch(self.air, av, magicWord, zoneId)
        except MagicWordError as e:
            response = f"error: {e}"
            self.notify.warning(f"magic word {magicWord!r} from {senderId}: {e}")

        # The client only writes this to its debug log, so it is a status line
        # for whoever is watching the console rather than anything the game
        # reacts to.
        self.sendUpdateToAvatarId(senderId, "setMagicWordResponse", [response])

    def setID(self, identifier: int) -> None:
        self.identifier = identifier

    def getID(self) -> int:
        return self.identifier
