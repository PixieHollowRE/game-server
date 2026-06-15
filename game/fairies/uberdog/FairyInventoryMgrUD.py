from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.showbase.PythonUtil import describeException

from game.fairies.stats.GameStatsService import sync_game_stats_to_client

notify = DirectNotifyGlobal.directNotify.newCategory("FairyInventoryMgrUD")


def _item_inv_ext(item: dict) -> list:
    return [
        int(item.get("inv_id") or 0),
        int(item.get("item_id") or 0),
        int(item.get("slot") or 0),
        int(item.get("createdById") or 0),
        str(item.get("createdByName") or ""),
        int(item.get("giftedById") or 0),
        str(item.get("giftedByName") or ""),
        int(item.get("quality") or 0),
        int(item.get("color1") or 0),
        int(item.get("color2") or 0),
        int(item.get("howAcquired") or 0),
    ]


class FairyInventoryMgrUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def announceGenerate(self) -> None:
        DistributedObjectGlobalUD.announceGenerate(self)

        self.accept("avatarOnline", self.avatarOnline)

    def avatarOnline(self, avatarId, avatarType) -> None:
        # avatarType is unused, but it is sent over the messenger anyways.
        try:
            docs = self.air.mongoInterface.retrieveDocs("fairies", avatarId, "_id")
            if not docs:
                notify.warning(f"avatarOnline: no fairy document for avId={avatarId}")
                return

            fairy = docs[0]
            avatar = fairy.get("avatar")
            if not avatar:
                notify.warning(f"avatarOnline: fairy {avatarId} missing avatar subdocument")
                return

            items = avatar.get("items")
            if not isinstance(items, list):
                notify.warning(f"avatarOnline: fairy {avatarId} avatar.items is not a list")
                return

            wardrobe_sent = 0
            storage_sent = 0
            skipped_location = 0

            for item in items:
                if not isinstance(item, dict):
                    skipped_location += 1
                    continue

                location = item.get("location") or ""
                if location in ("Wardrobe", "Equipped"):
                    field_name = "wardrobeItem"
                    wardrobe_sent += 1
                elif location == "Storage":
                    field_name = "storageItem"
                    storage_sent += 1
                else:
                    skipped_location += 1
                    continue

                self.sendUpdateToAvatarId(avatarId, field_name, [
                    int(item.get("item_id") or 0),
                    _item_inv_ext(item),
                ])

            notify.info(
                f"avatarOnline inventory sync avId={avatarId} "
                f"wardrobe={wardrobe_sent} storage={storage_sent} "
                f"skipped={skipped_location}"
            )

            sync_game_stats_to_client(self, avatarId)
        except Exception:
            notify.warning(
                f"avatarOnline inventory sync failed for avId={avatarId}: "
                f"{describeException()}"
            )

    def setStorageSlot(self, invId, slot) -> None:
        av_id = self.air.getAvatarIdFromSender()
        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": av_id, "avatar.items.inv_id": invId},
            {"$set": {"avatar.items.$.slot": slot}},
        )

    def setWardrobeSlot(self, invId, slot) -> None:
        av_id = self.air.getAvatarIdFromSender()
        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": av_id, "avatar.items.inv_id": invId},
            {"$set": {"avatar.items.$.slot": slot}},
        )
