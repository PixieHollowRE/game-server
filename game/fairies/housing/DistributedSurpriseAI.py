from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI

SURPRISE_CLOSED = 0
SURPRISE_OPEN = 1

TYPE_POST_OFFICE_POSTCARDS = 4
TYPE_POST_OFFICE_GIFT_SETS = 5

SURPRISE_ITEM_ID_BY_TYPE = {
    TYPE_POST_OFFICE_POSTCARDS: 28503,
    TYPE_POST_OFFICE_GIFT_SETS: 28504,
}


class DistributedSurpriseAI(DistributedObjectAI):
    """
    AI half of the client's DistributedSurprise (dclass 74). Currently only used
    for the home Post Office: when a fairy has postcards or gift sets waiting, one
    of these is generated in their home realm (see FairiesHomeRealmAI) so the
    owner sees the mailbox, opens it, and the client fetches/deletes the waiting
    mail via web-api (FairiesMessageArchiveRequest / FairiesDeleteMessageRequest).

    The item/postcard data does not travel through this object -- the client pulls
    it over HTTP. This object only carries the mailbox's placement and its
    open/closed state, and drives the open animation.
    """
    notify = directNotify.newCategory("DistributedSurpriseAI")

    def __init__(self, air, typeId, x, y, itemId=None, restricted=0):
        DistributedObjectAI.__init__(self, air)

        self.typeId = typeId
        self.x = x
        self.y = y
        # Each surprise type has a fixed art item; callers may override.
        self.itemId = itemId if itemId is not None else SURPRISE_ITEM_ID_BY_TYPE.get(typeId, 0)
        self.restricted = restricted
        self.state = SURPRISE_CLOSED

    def getItemId(self):
        return self.itemId

    def getTypeId(self):
        return self.typeId

    def getTypeData(self):
        # The panels fetch their real contents over HTTP, so no per-item payload
        # rides along here.
        return []

    def getPosition(self):
        return (self.x, self.y)

    def getRestricted(self):
        return self.restricted

    def getState(self):
        return self.state

    def b_setState(self, state):
        self.state = state
        self.sendUpdate("setState", [state])

    def openRequest(self, surpriseSet):
        # The home owner triggered the closed mailbox. Opening it tells the client
        # to play the animation and open the archive panel. `surpriseSet` is the
        # client's BOGUS_SET sentinel and is unused.
        if self.state == SURPRISE_CLOSED:
            self.b_setState(SURPRISE_OPEN)

    def openComplete(self, surpriseSet):
        # The owner finished viewing (and deleting) all their mail. The messages
        # themselves were already removed via FairiesDeleteMessageRequest, so all
        # that's left is to take the mailbox away until new mail arrives.
        self.requestDelete()
