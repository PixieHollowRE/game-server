from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

class DistributedMeadowGameAI(DistributedInstanceBaseAI):
    def __init__(self, air) -> None:
        super().__init__(air)

        self.gameId: int = 0
        self.minPlayers: int = 0
        self.maxPlayers: int = 0
        self.velvetRope: int = 0
        self.hotspotId: int = 0
        self.x: int = 0
        self.y: int = 0
        self.state: int = 0
        self.timeOutSecs: int = 0
        self.itemId: int = 0
        self.players: list[int] = []
        self.isSpawnedGame: int = 1

    def setGameInfo(self, gameId, minPlayers, maxPlayers, velvetRope, hotspotId):
        self.gameId = gameId
        self.minPlayers = minPlayers
        self.maxPlayers = maxPlayers
        self.velvetRope = velvetRope
        self.hotspotId = hotspotId

    def getGameInfo(self):
        return [self.gameId, self.minPlayers, self.maxPlayers, self.velvetRope, self.hotspotId]

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getPosition(self):
        return [self.x, self.y]

    def setGameState(self, state, timeOutSecs):
        self.state = state
        self.timeOutSecs = timeOutSecs

    def getGameState(self):
        return [self.state, self.timeOutSecs]

    def setItemId(self, itemId):
        self.itemId = itemId

    def getItemId(self):
        return self.itemId

    def setPlayers(self, players):
        self.players = players

    def getPlayers(self):
        return self.players

    def d_setPlayers(self):
        self.sendUpdate("setPlayers", [self.getPlayers()])

    def setIsSpawnedGame(self, spawned):
        self.isSpawnedGame = spawned

    def getIsSpawnedGame(self):
        return self.isSpawnedGame

    def joinRequest(self):
        avatarId = self.air.getAvatarIdFromSender()
        self.players.append(avatarId)
        self.d_setPlayers()
        self.sendUpdateToAvatarId(avatarId, "joinResponse", [0])
