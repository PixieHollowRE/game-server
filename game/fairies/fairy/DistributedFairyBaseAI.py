from collections.abc import Sequence

from direct.distributed.DistributedObjectAI import DistributedObjectAI

from game.fairies.fairy.structs.FairyDNA import FairyDNA
from game.fairies.fairy.structs.FairyPose import FairyPose

from game.fairies.fairy.structs.LiteInvItemExt import LiteInvItemExt

from game.fairies.housing.HouseConstants import ROOM_TYPE_HOME, isValidRoomType

class DistributedFairyBaseAI(DistributedObjectAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.name: str = ""

        self.position: tuple[int, int] = (0, 0)
        self.rotation: int = 0

        self.fairyDNA: FairyDNA = FairyDNA()

        self.fairyPose: FairyPose = FairyPose()

        self.headItem: LiteInvItemExt = LiteInvItemExt()
        self.necklace: LiteInvItemExt = LiteInvItemExt()
        self.chestItem: LiteInvItemExt = LiteInvItemExt()
        self.belt: LiteInvItemExt = LiteInvItemExt()
        self.skirt: LiteInvItemExt = LiteInvItemExt()
        self.wrist: LiteInvItemExt = LiteInvItemExt()
        self.ankle: LiteInvItemExt = LiteInvItemExt()
        self.shoes: LiteInvItemExt = LiteInvItemExt()

        # Default to the house rather than 0. setRoomID is declared `db`, but
        # nothing persists it (it is absent from APIDatabase.lua's Api2Field and
        # from the web-api Fairy schema), so a fairy generates with the DC
        # default and stays there until their client reports a room. 0 is not a
        # room the client recognises, and teleportRequestTo hands this value
        # straight to an arriving client, which adopts it as its own roomID making
        # anything that fairy then places unreachable.
        self.roomID: int = ROOM_TYPE_HOME

    def setName(self, name: str) -> None:
        self.name = name

    def d_setName(self, name: str) -> None:
        self.sendUpdate("setName", [name])

    def b_setName(self, name: str) -> None:
        self.setName(name)
        self.d_setName(name)

    def getName(self) -> str:
        return self.name

    def setPosition(self, x: int, y: int) -> None:
        self.position = (x, y)

    def getPosition(self) -> tuple[int, int]:
        return self.position

    def setRotation(self, rotation: int) -> None:
        self.rotation = rotation

    def getRotation(self) -> int:
        return self.rotation

    def setFairyDNA(self, fairyDNA: Sequence[int]) -> None:
        self.fairyDNA = FairyDNA.unpackFromTuple(fairyDNA)

    def d_setFairyDNA(self, fairyDNA: Sequence[int]):
        self.sendUpdate("setFairyDNA", [fairyDNA])

    def b_setFairyDNA(self, fairyDNA: Sequence[int]):
        self.setFairyDNA(fairyDNA)
        self.d_setFairyDNA(fairyDNA)

    def getFairyDNA(self) -> tuple[int, ...]:
        return self.fairyDNA.asTuple()

    def setFairyPose(self, fairyPose: Sequence[int]) -> None:
        self.fairyPose = FairyPose.unpackFromTuple(fairyPose)

    def getFairyPose(self) -> tuple[int, ...]:
        return self.fairyPose.asTuple()

    def setHeadItem(self, item: Sequence[int]) -> None:
        self.headItem = LiteInvItemExt.unpackFromTuple(item)

    def getHeadItem(self) -> tuple[int, ...]:
        return self.headItem.asTuple()

    def setNecklace(self, item: Sequence[int]) -> None:
        self.necklace = LiteInvItemExt.unpackFromTuple(item)

    def getNecklace(self) -> tuple[int, ...]:
        return self.necklace.asTuple()

    def setChestItem(self, item: Sequence[int]) -> None:
        self.chestItem = LiteInvItemExt.unpackFromTuple(item)

    def getChestItem(self) -> tuple[int, ...]:
        return self.chestItem.asTuple()

    def setBelt(self, item: Sequence[int]) -> None:
        self.belt = LiteInvItemExt.unpackFromTuple(item)

    def getBelt(self) -> tuple[int, ...]:
        return self.belt.asTuple()

    def setSkirt(self, item: Sequence[int]) -> None:
        self.skirt = LiteInvItemExt.unpackFromTuple(item)

    def getSkirt(self) -> tuple[int, ...]:
        return self.skirt.asTuple()

    def setWrist(self, item: Sequence[int]) -> None:
        self.wrist = LiteInvItemExt.unpackFromTuple(item)

    def getWrist(self) -> tuple[int, ...]:
        return self.wrist.asTuple()

    def setAnkle(self, item: Sequence[int]) -> None:
        self.ankle = LiteInvItemExt.unpackFromTuple(item)

    def getAnkle(self) -> tuple[int, ...]:
        return self.ankle.asTuple()

    def setShoes(self, item: Sequence[int]) -> None:
        self.shoes = LiteInvItemExt.unpackFromTuple(item)

    def getShoes(self) -> tuple[int, ...]:
        return self.shoes.asTuple()

    def setRoomID(self, roomID: int) -> None:
        # Now airecv, so this arrives from the owning client on every room
        # change. Only the two real rooms are worth recording -- keep the last
        # good value rather than let a bad one propagate to anyone who flies here.
        if not isValidRoomType(roomID):
            # 0 is the DC default and arrives on every generate, because nothing
            # actually persists this field: it is declared `db`, but it is in
            # neither APIDatabase.lua's Api2Field nor the web-api Fairy schema,
            # so the stored value is always absent. Expected, not worth a warning.
            if roomID:
                self.notify.warning(
                    "setRoomID(%r) for %s is not a room, ignoring"
                    % (roomID, self.doId))
            return

        self.roomID = roomID

    def getRoomID(self) -> int:
        return self.roomID
