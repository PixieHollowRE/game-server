from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedHomeAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.address: str = "1234CatepillerCorral"

        self.unlockedRooms: int = 0

    def setAddress(self, address: str) -> None:
        self.address = address

    def setUnlockedRooms(self, unlockedRooms: int) -> None:
        self.unlockedRooms = unlockedRooms

    def getAddress(self) -> str:
        return self.address

    def getUnlockedRooms(self) -> int:
        return self.unlockedRooms
