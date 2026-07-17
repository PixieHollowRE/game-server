from direct.directnotify.DirectNotifyGlobal import directNotify

from game.otp.distributed.DistributedDistrictAI import DistributedDistrictAI

from game.fairies.housing.HouseConstants import HOUSING_ZONE_OFFSET
from game.fairies.housing.DistributedHomeItemAI import DistributedHomeItemAI
from game.fairies.housing.HomeItems import returnPlacedItemsToStorage


class FairiesHomeRealmAI(DistributedDistrictAI):
    """
    AI half of the client's FairiesHomeRealm (dclass FairiesHomeRealm :
    DistributedDistrict).

    Player housing lives in its own realms rather than in the shared meadow
    districts. The RealmGuardian uberdog asks a district AI process to spawn one
    of these on demand (see FairiesAIRepository.createRemoteObject) and tears it
    back down once it is empty.

    A home realm belongs to one owner. When it spawns, it loads that owner's
    placed furniture and generates a DistributedHomeItem for each, parented to
    the realm in the owner's housing zone, so anyone who enters sees the home.
    """
    notify = directNotify.newCategory("FairiesHomeRealmAI")

    def __init__(self, air, ownerId, name="Home Realm"):
        DistributedDistrictAI.__init__(self, air, name)

        self.ownerId = ownerId
        # Everything in a home realm lives in the owner's housing zone.
        self.ownerZone = ownerId + HOUSING_ZONE_OFFSET
        # inv_id -> DistributedHomeItemAI currently generated in this realm.
        self.homeItems = {}

    def _fairies(self):
        return self.air.mongoInterface.mongodb.fairies

    def loadHomeItems(self):
        # Generate a DistributedHomeItem for each piece of furniture the owner
        # has placed. Called right after the realm is generated.
        fairy = self._fairies().find_one({"_id": self.ownerId})
        if not fairy:
            return

        for item in fairy.get("avatar", {}).get("items", []):
            # A placed item is marked by its `home` sub-doc; it stays in
            # "Storage" so the client keeps its return-to-storage flow.
            if item.get("home"):
                self._generateHomeItem(item)

    def _generateHomeItem(self, item):
        home = item["home"]
        # Only send non-zero dye colors. A stored 0 means "undyed", and the
        # client resolves the item's default colours itself - if we sent 0 it
        # would override those defaults and the item would render colourless.
        colorIds = [c for c in (item.get("color1", 0), item.get("color2", 0)) if c]

        homeItem = DistributedHomeItemAI(
            self.air, self.ownerId,
            invId=item["inv_id"],
            itemId=item["item_id"],
            colorIds=colorIds,
            x=home["x"], y=home["y"], depth=home["depth"],
            flip=home["flip"], scale=home["scale"], roomId=home["roomId"])

        # Parent to the realm (not the district) in the owner's housing zone.
        self.air.generateWithRequired(homeItem, self.getDoId(), self.ownerZone)
        self.homeItems[item["inv_id"]] = homeItem
        return homeItem

    def addHomeObject(self, invId, x, y, depth, flip, roomId, scale):
        # The client placed a storage item in the home. Record the placement on
        # the item via a `home` sub-doc, but keep it in "Storage" - the item
        # stays in the player's inventory so it can be returned to storage.
        self._fairies().update_one(
            {"_id": self.ownerId, "avatar.items.inv_id": invId},
            {"$set": {
                "avatar.items.$.home": {
                    "roomId": roomId, "x": x, "y": y,
                    "depth": depth, "flip": flip, "scale": scale
                }
            }})

        homeItem = self.homeItems.get(invId)
        if homeItem is not None:
            # We already have this one. This is the client re-syncing after a
            # room switch, and it may carry a newer position than the object
            # holds, so apply it rather than dropping it.
            homeItem.updatePlacement(x, y, depth, flip, scale, roomId)
            return

        result = self._fairies().find_one(
            {"_id": self.ownerId, "avatar.items.inv_id": invId},
            {"avatar.items.$": 1})
        if not result or not result.get("avatar", {}).get("items"):
            self.notify.warning(
                "addHomeObject: item %s not found for owner %s" % (invId, self.ownerId))
            return

        self._generateHomeItem(result["avatar"]["items"][0])

    def removeHomeObject(self, invId, doId):
        # The client took a placed item back into storage.
        self._fairies().update_one(
            {"_id": self.ownerId, "avatar.items.inv_id": invId},
            {"$set": {"avatar.items.$.location": "Storage"},
             "$unset": {"avatar.items.$.home": ""}})

        homeItem = self.homeItems.pop(invId, None)
        if homeItem is not None:
            homeItem.requestDelete()

    def clearHomeItems(self):
        returnPlacedItemsToStorage(self.air, self.ownerId)

        for homeItem in list(self.homeItems.values()):
            homeItem.requestDelete()
        self.homeItems.clear()

    def delete(self):
        # Clean up our generated furniture with the realm.
        for homeItem in list(self.homeItems.values()):
            homeItem.requestDelete()
        self.homeItems.clear()
        DistributedDistrictAI.delete(self)

    def setParentingRules(self, style, rule):
        pass

    def createHomeRequest(self, avatarId):
        pass

    def removeHomeHotspotObject(self, tagId):
        pass

    def setServerTime(self, time):
        pass

    def setPetState(self, avatarId, state):
        pass

    def requestDropGame(self, inventoryId, itemId, quantity, x, y,
                        dropType, dropSubType, dropChance, seed):
        pass

    def bootRequest(self, avatarId):
        # The home owner clicked "boot" on a visitor's profile in their home
        # (client Profile.onConfirmBoot -> FairiesHomeRealm.dispatchBootRequest).
        # bootRequest is clsend, so anyone in the realm could send it -- only the
        # owner of this home is allowed to eject someone, so drop anyone else.
        senderId = self.air.getAvatarIdFromSender()
        if senderId != self.ownerId:
            self.notify.warning(
                "bootRequest for %s in %s's home from %s, not the owner - ignoring"
                % (avatarId, self.ownerId, senderId))
            return

        # An owner booting themselves would just fling them out of their own
        # home; nothing to do.
        if avatarId == self.ownerId:
            return

        # Tell the booted fairy's own client it was ejected from this housing
        # zone. DistributedFairyPlayer.bootedFromZone flies the local player back
        # to the last meadow and remembers the zone so it can't come straight
        # back in. bootedFromZone lives on DistributedFairyPlayer (not on this
        # realm), so address the update at the target's object and route it to
        # that player's client connection channel directly.
        self.air.sendUpdateToDoId(
            "DistributedFairyPlayer", "bootedFromZone", avatarId,
            [self.ownerZone],
            channelId=self.GetPuppetConnectionChannel(avatarId))
