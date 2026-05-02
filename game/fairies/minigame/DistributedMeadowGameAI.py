from game.fairies.instance.DistributedInstanceBaseAI import DistributedInstanceBaseAI

MEADOW_GAME_JOIN_RESPONSE_ACCEPTED = 0
MEADOW_GAME_JOIN_RESPONSE_GAMEON_FULL = 1
MEADOW_GAME_JOIN_RESPONSE_DUPLICATE = 2
MEADOW_GAME_JOIN_RESPONSE_MEMBER_ONLY = 3

MEADOW_GAME_STATE_GROUPING = 0
MEADOW_GAME_STATE_INIT = 1
MEADOW_GAME_STATE_PLAY = 2
MEADOW_GAME_STATE_RESET = 3

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

    def d_setGameState(self):
        self.sendUpdate("setGameState", self.getGameState())

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

    def joinRequest(self, avatarId):
        avatar = self.air.doId2do.get(avatarId)

        if avatar is None:
            self.notify.warning(f"No avatar present on AI for joinRequest: {avatarId}")
            return

        addedPlayer = False

        if len(self.players) >= self.maxPlayers:
            responseCode = MEADOW_GAME_JOIN_RESPONSE_GAMEON_FULL
        elif self.velvetRope and not avatar.isPaid():
            responseCode = MEADOW_GAME_JOIN_RESPONSE_MEMBER_ONLY
        else:
            responseCode = MEADOW_GAME_JOIN_RESPONSE_ACCEPTED

            self.players.append(avatarId)
            addedPlayer = True
            self.d_setPlayers()

        self.sendUpdateToAvatarId(avatarId, "joinResponse", [responseCode])

        if addedPlayer and len(self.players) >= self.maxPlayers and self.state != MEADOW_GAME_STATE_PLAY:
            self.setGameState(MEADOW_GAME_STATE_PLAY, 0)
            self.d_setGameState()
