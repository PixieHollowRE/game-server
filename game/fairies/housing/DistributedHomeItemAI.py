from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI


class DistributedHomeItemAI(DistributedObjectAI):
    """
    AI half of the client's DistributedHomeItem - a single piece of furniture
    placed in a fairy's home or garden.

    These are generated inside a FairiesHomeRealm (parented to the realm at the
    owner's housing zone) so every client that enters the realm sees the owner's
    furniture. The placement is persisted on the owner's item in avatar.items
    as a `home` sub-doc; the item itself stays in "Storage" so the client keeps
    its return-to-storage flow. See FairiesHomeRealmAI.
    """
    notify = directNotify.newCategory("DistributedHomeItemAI")

    def __init__(self, air, ownerId, invId, itemId, colorIds,
                 x, y, depth, flip, scale, roomId):
        DistributedObjectAI.__init__(self, air)

        self.ownerId = ownerId
        self.invId = invId
        self.itemId = itemId
        self.colorIds = colorIds
        self.x = x
        self.y = y
        self.depth = depth
        self.flip = flip
        self.scale = scale
        self.roomId = roomId

    def getItemID(self):
        return self.itemId

    def getInventoryID(self):
        return self.invId

    def getColorIDs(self):
        return self.colorIds

    def getPosition(self):
        return (self.x, self.y, self.depth)

    def getFlip(self):
        return self.flip

    def getScale(self):
        return self.scale

    def getRoomID(self):
        return self.roomId

    def setHomeManagerDOID(self, doId):
        pass

    def updatePlacement(self, x, y, depth, flip, scale, roomId):
        # Re-sync placement without regenerating. The client re-sends
        # addHomeObject for anything missing from its _serverItems map (it
        # clears that map when it teleports back into the home), so we can be
        # told about a placement we already have.
        self._applyPlacement(x, y, depth, flip, scale, roomId)

    def requestItemChange(self, x, y, depth, flip, scale):
        # The client moved/flipped/resized the item.
        if self._applyPlacement(x, y, depth, flip, scale, self.roomId):
            self._persistPlacement()

    def _applyPlacement(self, x, y, depth, flip, scale, roomId):
        """
        Store a new placement and mirror it back out over the network. Returns
        whether anything actually changed.

        The broadcast is what tells the client the change took: its copy of this
        object is what it diffs against on every sync pass, so without this it
        keeps the values it was generated with -- it re-sends the same change
        forever, and rebuilds the item at the stale placement whenever it
        switches rooms.
        """
        if (x, y, depth, flip, scale, roomId) == (
                self.x, self.y, self.depth, self.flip, self.scale, self.roomId):
            return False

        moved = (x, y, depth) != (self.x, self.y, self.depth)
        flipped = flip != self.flip
        resized = scale != self.scale
        changedRoom = roomId != self.roomId

        self.x = x
        self.y = y
        self.depth = depth
        self.flip = flip
        self.scale = scale
        self.roomId = roomId

        if moved:
            self.sendUpdate("setPosition", [x, y, depth])
        if flipped:
            self.sendUpdate("setFlip", [flip])
        if resized:
            self.sendUpdate("setScale", [scale])
        if changedRoom:
            self.sendUpdate("setRoomID", [roomId])

        return True

    def _persistPlacement(self):
        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": self.ownerId, "avatar.items.inv_id": self.invId},
            {"$set": {
                "avatar.items.$.home.x": self.x,
                "avatar.items.$.home.y": self.y,
                "avatar.items.$.home.depth": self.depth,
                "avatar.items.$.home.flip": self.flip,
                "avatar.items.$.home.scale": self.scale,
                "avatar.items.$.home.roomId": self.roomId
            }}
        )
