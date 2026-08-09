HOUSING_ZONE_OFFSET = 1000000000

# Which room of a home realm something is in. A house and its garden share one
# realm and one zone, so this is the only thing that separates them -- both for
# placed furniture (DistributedHomeItem.setRoomID) and for where a fairy is
# standing (DistributedFairyPlayer.setRoomID).
#
# These must match MMOConstants.ROOM_TYPE_HOME / ROOM_TYPE_GARDEN in the client.
# Every client-side room test is an equality against one of these two values
# (see HomeController.onHomeItemGenerate and HomeItemNegotiator.selectForDecorate),
# so a third value is not "some other room" -- it is furniture that draws in the
# house but can never be selected, moved, or put back into storage.
ROOM_TYPE_HOME = 1
ROOM_TYPE_GARDEN = 2

VALID_ROOM_TYPES = (ROOM_TYPE_HOME, ROOM_TYPE_GARDEN)


def isValidRoomType(roomId: int) -> bool:
    return roomId in VALID_ROOM_TYPES
