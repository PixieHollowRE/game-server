def returnPlacedItemsToStorage(air, avId: int) -> bool:
    """
    Unplace everything the fairy has put in their home.

    A placed item is marked by its `home` sub-doc and never leaves "Storage"
    (see FairiesHomeRealmAI), so dropping that sub-doc hands the item back to
    the fairy rather than destroying it.

    Leaves the garden alone, since that doesn't change when the fairy's house does.
    """
    result = air.mongoInterface.mongodb.fairies.update_one(
        {"_id": avId},
        {
            "$set": {"avatar.items.$[placed].location": "Storage"},
            "$unset": {"avatar.items.$[placed].home": ""}
        },
        array_filters=[{"placed.home.roomId": 1}]
    )

    return result.modified_count > 0

def clearPlacedHomeItems(air, avId: int) -> None:
    """
    Put every item the fairy has placed back into storage, realm or no realm.

    A home realm only exists while somebody is standing in it, so usually the
    owner is out shopping, nothing is generated, and the database write is the
    whole job. When this AI does happen to host their realm -- a visitor is in
    there while they shop -- take the furniture out of it too, so it goes away
    for whoever is watching instead of lingering until the realm empties.
    """
    realm = next(
        (realm for realm in getattr(air, "homeRealms", {}).values()
         if realm.ownerId == avId),
        None
    )

    if realm is not None:
        realm.clearHomeItems()
        return

    returnPlacedItemsToStorage(air, avId)
