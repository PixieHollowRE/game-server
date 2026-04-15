from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedSpawnStackAI(DistributedObjectAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.itemID: int = 0
        self.name: str = ""
        self.posX: int = 0
        self.posY: int = 0
        self.colorIDs: list[int] = []
        self.itemCount: int = 0
        self.servingSize: int = 0

    def setItemID(self, itemID: int) -> None:
        self.itemID = itemID

    def getItemID(self) -> int:
        return self.itemID

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def setPosition(self, x: int, y: int) -> None:
        self.posX = x
        self.posY = y

    def getPosition(self) -> tuple[int, int]:
        return self.posX, self.posY

    def setColorIDs(self, colorIDs: list[int]) -> None:
        self.colorIDs = colorIDs

    def getColorIDs(self) -> list[int]:
        return self.colorIDs

    def setItemCount(self, itemCount: int) -> None:
        self.itemCount = itemCount

    def getItemCount(self) -> int:
        return self.itemCount

    def setServingSize(self, servingSize: int) -> None:
        self.servingSize = servingSize

    def getServingSize(self) -> int:
        return self.servingSize

    def setEligible(self, bogus: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        self.sendUpdateToAvatarId(avId, "setEligible", [1])

    def setCollectRequest(self, bogus: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setCollectRequest: {avId}")
            return

        itemID, itemCount, itemSlot = self.getItemID(), self.getItemCount(), -1

        if self.air.inventoryManager.addIngredientsToPouch(avId, itemID, itemCount, itemSlot):
            avatar.d_setPouch(self.air.inventoryManager.getPouch(avId))
