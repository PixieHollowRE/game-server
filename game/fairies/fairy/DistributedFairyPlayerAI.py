from datetime import datetime, timezone
import time
import random

from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.fairy.AuraMapping import AURA_MAPPING, SKIN_COLOR_MAPPING, WING_COLOR_MAPPING
from game.fairies.fairy.structs.RewardExt import RewardExt
from game.fairies.fairy.structs.MiscItem import MiscItem
from game.fairies.fairy.structs.LiteInvItemExt2 import LiteInvItemExt2
from game.fairies.fairy.structs.SavedOutfit import SavedOutfit

from game.fairies.badges import badge_events, badge_state
from game.fairies.daily.DailyChanceConstants import (
    Category,
    EXCLUDE_STORAGE,
    EXCLUDE_WARDROBE,
    FREE_ACORNS,
    MEMBER_ACORNS,
    SPIN_BADGE_ID_SET,
    SPIN_ROCK_ITEM_IDS,
)
from game.fairies.daily.DailyChancePool import draw_daily_spin
from game.fairies.daily.DailyChanceGrant import grant_prize
from game.fairies.daily.TimeUtils import get_period_start

from game.fairies.housing.HouseConstants import (
    HOUSING_ZONE_OFFSET, ROOM_TYPE_HOME, isValidRoomType)
from game.fairies.meadow import meadow_xml
from game.fairies.ai import ZoneConstants

# Mail types that light the client's HUD gift-box; written by the shopkeeper AI.
MAIL_STATUS_POSTCARD = 4
MAIL_STATUS_GIFTSET = 5

# Shop purchases by itemId (90003 = name change); the client sends no price.
GLOBAL_PURCHASE_ITEMS = {
    90003: MiscItem.unpackFromTuple((90003, 8006, 500, 200, 200)),
}

# Mirrors the client's SavedOutfits panel: MAX_OUTFIT_TABS(14) * 2 - 1 slots.
DEFAULT_MAX_OUTFIT_SLOTS = 1
MAX_OUTFIT_SLOTS = 27
OUTFIT_SLOTS_PER_PURCHASE = 2

# Charged from gold (the client's diamonds); mirrors SavedOutfits.SLOT_COST.
OUTFIT_SLOT_COST = 10

# The order the client sends invIds in and reads a SavedOutfit struct back in.
OUTFIT_SLOT_ORDER = ("head", "necklace", "shirt", "belt", "skirt", "wrist", "ankle", "shoes")

# The slots a fairy is always dressed in.
MANDATORY_OUTFIT_SLOTS = frozenset({"shirt", "skirt", "shoes"})
MANDATORY_SLOT_NUMBERS = frozenset(
    index + 1
    for index, slot in enumerate(OUTFIT_SLOT_ORDER)
    if slot in MANDATORY_OUTFIT_SLOTS
)

# Slot number -> the field that redraws it; equipping or dyeing must send one.
EQUIP_SLOT_FIELDS = {
    1: "setHeadItem",
    2: "setNecklace",
    3: "setChestItem",
    4: "setBelt",
    5: "setSkirt",
    6: "setWrist",
    7: "setAnkle",
    8: "setShoes",
}

# An empty LiteInvItemExt2 (invId, itemId, color1, color2, howAcquired).
EMPTY_LITE_INV_ITEM = [0, 0, 0, 0, 0]

# Off until PixiePower goes live; _grantPixiePower is wired but writes nothing.
PIXIE_POWER_ENABLED = False

# TODO: default should be 10 and max 240 once the PixiePower rules are settled.
DEFAULT_PIXIE_POWER = 100  # the setPixiePower default in fairy.dc

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ""
        self.DISLid: int = 0
        self.gold: int = 0
        self.access: int = 0
        self.level: int = 0
        self.experiencePoints: int = 0
        self.pixiePower: int = DEFAULT_PIXIE_POWER

        self.homeType: int = 0
        self.homeSubType: int = 0

        # 0 when not in a home; the RealmGuardian tears down the empty ones.
        self.currentHomeOwner: int = 0
        
        self.dailyChancePlayed: bool = False

        self.goldTradedToday: int = 0
        self.lastGoldTradeAt = None # date

        self._originalDNA = {}
        self.lastPoseStatus = -1

    def announceGenerate(self):
        self.air.incrementPopulation()
        self._reportRealmOverflow()

        # Fill in the missing information from the database (i.e. gold)
        self.air.fillInFairyPlayer(self)

        self.b_setHomeType(self._defaultHomeType())

        self.air.inventoryManager.avatarOnline(self.doId)

        self._sync_gold_trading_cap()

        self.sendUpdateToAvatarId(
            self.doId, "setGlobalPurchaseData", [list(GLOBAL_PURCHASE_ITEMS.values())]
        )

        NEW_LEVEL = 28

        if self.getLevel() != NEW_LEVEL:
            # TEMP: Set level at the request of Jessibee for the Test server.
            self.b_setLevel(NEW_LEVEL)

        # Pushed on generate: the client only pulls this at panel construction.
        self._pushSavedOutfitState()

        # An offline recipient never saw the live nudge, so light the box here.
        self._pushPendingMailStatus()

    def d_statusUpdateFromFairy(self, fromPlayerId: int, status: int) -> None:
        # 4/5 light the HUD gift-box; it clears when we next stand in our home.
        self.sendUpdateToAvatarId(self.doId, "statusUpdateFromFairy", [fromPlayerId, status])

    def _pushPendingMailStatus(self) -> None:
        latest = self.air.mongoInterface.mongodb.messages.find_one(
            {"recipient_id": self.doId,
             "type": {"$in": [MAIL_STATUS_POSTCARD, MAIL_STATUS_GIFTSET]}},
            sort=[("created", -1)],
        )
        if not latest:
            return

        senderId = (latest.get("sender") or {}).get("fairy_id", 0)
        self.d_statusUpdateFromFairy(senderId, latest["type"])

    def delete(self):
        """
        Tear down this copy of the avatar.

        A district hop deletes and rebuilds the avatar -- which is what flying
        between two houses does -- so the occupancy update names the home we
        think we are leaving. The guardian may already have seen us arrive
        somewhere else by then, and must not act on us if it has.
        """
        # TODO: Set a post-remove message in case of an AI crash.

        # Leave any home realm we were in so it can be torn down if now empty.
        if self.currentHomeOwner:
            self.air.sendRealmOccupancyUpdate(self.doId, 0, self.currentHomeOwner)
            self.currentHomeOwner = 0

        self.air.sendFriendManagerAccountOffline(self.DISLid)

        self.air.decrementPopulation()

        DistributedFairyBaseAI.delete(self)

    def setDISLname(self, DISLname: str) -> None:
        self.DISLname = DISLname

    def getDISLname(self) -> str:
        return self.DISLname

    def setDISLid(self, DISLid: int) -> None:
        self.air.sendFriendManagerAccountOnline(DISLid)

        self.DISLid = DISLid

    def getDISLid(self) -> int:
        return self.DISLid

    def setAccess(self, access: int) -> None:
        self.access = access

        if self.isPaid():
            self.sendUpdateToAvatarId(self.doId, "setAccess", [access])

    def getAccess(self) -> int:
        return self.access

    def isPaid(self) -> bool:
        return self.getAccess() == OTPGlobals.AccessFull

    def setDailyChancePlayed(self, played: int) -> None:
        self.dailyChancePlayed = played

    def getDailyChancePlayed(self) -> int:
        return self.dailyChancePlayed

    def d_setDailyChancePlayed(self, played: int) -> None:
        self.sendUpdate("setDailyChancePlayed", [played])

    def b_setDailyChancePlayed(self, played: int) -> None:
        self.dailyChancePlayed = played
        self.sendUpdate("setDailyChancePlayed", [played])

    def dailyChanceCanSpin(self) -> bool:
        doc = self.air.mongoInterface.mongodb.fairies.find_one({"_id": self.doId})
        last_spin = doc.get("dailyChanceLastSpin")

        if last_spin is None:
            return True

        # DB storage is tz unaware - make it aware
        last_spin_utc = last_spin.replace(tzinfo=timezone.utc)

        return get_period_start(last_spin_utc, "daily") != get_period_start(datetime.now(timezone.utc), "daily") 

    def recordDailyChanceSpin(self) -> None:
        # Store the timestamp in UTC
        self.air.mongoInterface.updateField(
            "fairies", "dailyChanceLastSpin", self.doId, datetime.now(timezone.utc)
        )
        self.b_setDailyChancePlayed(1)

    def setActualZoneId(self, zoneId) -> None:
        if zoneId == 50046: # Vidia's
            if self.dailyChanceCanSpin():
                self.b_setDailyChancePlayed(0)

        # Housing zones are ownerId + offset; anything else is not a home.
        homeOwner = zoneId - HOUSING_ZONE_OFFSET if zoneId >= HOUSING_ZONE_OFFSET else 0
        if homeOwner != self.currentHomeOwner:
            previousOwner = self.currentHomeOwner
            self.currentHomeOwner = homeOwner
            self.air.sendRealmOccupancyUpdate(self.doId, homeOwner, previousOwner)

        if badge_events.get_meadow_badge_for_zone(zoneId) is not None:
            self.air.badgeManager.d_exploreMeadow(self.doId, zoneId)

    def _dailyChanceExcludedBadges(self) -> set[int]:
        # Mr. Twitches postdates the client's mask, so trust our own badges.
        return badge_state.get_earned_badge_ids(self.air, self.doId, SPIN_BADGE_ID_SET)

    def _dailyChanceExcludedCategories(self, excludeMask: int) -> set[Category]:
        # Trusting the client is fine; a lie only wins an unusable prize.
        excluded = set()

        if excludeMask & EXCLUDE_WARDROBE:
            excluded.add(Category.WARDROBE)

        if excludeMask & EXCLUDE_STORAGE:
            excluded.add(Category.HOME)

        # Vidia's badges are Member-only; the manager would refuse to grant one.
        if not self.isPaid():
            excluded.add(Category.BADGE)

        return excluded

    def requestDailyChance(self, excludeMask: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        if avId != self.doId:
            self.notify.warning(
                f"requestDailyChance from {avId} but sender DO is {self.doId}"
            )
            return

        self.doDailyChance(excludeMask)

    def doDailyChance(self, excludeMask: int) -> None:
        """
        Spin Vidia's wheel and hand over whatever it lands on.

        Split out from requestDailyChance so the `daily-chance` magic word can
        reach it without having to look like a client message -- the sender
        check belongs to the client entry point, not to the spin itself.
        """
        avId = self.doId

        if not self.dailyChanceCanSpin():
            return

        prizes = draw_daily_spin(
            self.fairyDNA.gender,
            self._dailyChanceExcludedBadges(),
            self._dailyChanceExcludedCategories(excludeMask),
            MEMBER_ACORNS if self.isPaid() else FREE_ACORNS,
        )

        granted: list[RewardExt] = []
        rocksWon = 0

        for prize in prizes:
            success, reward = grant_prize(self.air, avId, prize)

            if not success:
                self.notify.warning(f"requestDailyChance: failed to grant item {prize.id} to {avId}")
                continue

            granted.append(reward)

            if prize.id in SPIN_ROCK_ITEM_IDS:
                rocksWon += 1

        self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [granted])

        if not granted:
            return

        self.recordDailyChanceSpin()

        # Counted per rock, so pulling three at once earns credit for three.
        self.air.badgeManager.d_accumulate(avId, badge_events.EVENT_PLAYED_DAILY_SPIN)

        if rocksWon:
            self.air.badgeManager.d_accumulate(avId, badge_events.EVENT_WON_ROCK, rocksWon)

    def _liteInvFromId(self, invId: int, itemsById: dict) -> LiteInvItemExt2:
        item = itemsById.get(invId)
        if not invId or item is None:
            return LiteInvItemExt2()

        return LiteInvItemExt2.unpackFromTuple((
            invId,
            item["item_id"],
            item.get("color1", 0),
            item.get("color2", 0),
            item.get("howAcquired", 0)
        ))

    def _equippedInvIdsBySlot(self, fairy: dict) -> dict:
        return {
            OUTFIT_SLOT_ORDER[item["slot"] - 1]: item["inv_id"]
            for item in fairy["avatar"]["items"]
            if item.get("location") == "Equipped"
            and 1 <= (item.get("slot") or 0) <= len(OUTFIT_SLOT_ORDER)
        }

    def _buildOutfitItems(self, invIds: tuple, fairy: dict) -> dict:
        """
        Snapshot the eight slots a saved outfit stores.

        The shop's save button (ShopPanel.saveOutfitToLookBook) sends 0 for
        every slot the player did not just buy, so a trinket run would save an
        outfit of bare accessories and undress the fairy when worn. Fall back to
        what she has on, the way the shop's own "wear it now" path does.

        A zero from the wardrobe is deliberate ("no necklace, thanks"), so only
        fall back when a mandatory slot arrives empty while she is wearing
        something there -- which only happens on the shop's partial path.
        """
        itemsById = {item["inv_id"]: item for item in fairy["avatar"]["items"]}
        wanted = dict(zip(OUTFIT_SLOT_ORDER, invIds))

        equipped = self._equippedInvIdsBySlot(fairy)
        if any(not wanted[slot] and equipped.get(slot) for slot in MANDATORY_OUTFIT_SLOTS):
            wanted = {
                slot: invId or equipped.get(slot, 0)
                for slot, invId in wanted.items()
            }

        return {
            slot: self._liteInvFromId(invId, itemsById).asTuple()
            for slot, invId in wanted.items()
        }

    def _savedOutfitToStruct(self, outfit: dict) -> SavedOutfit:
        items = outfit.get("items", {})
        return SavedOutfit.unpackFromTuple((
            outfit["outfitId"],
            *(
                LiteInvItemExt2.unpackFromTuple(items.get(slot, EMPTY_LITE_INV_ITEM))
                for slot in OUTFIT_SLOT_ORDER
            ),
        ))

    def _d_setSavedOutfits(self, outfits: list) -> None:
        payload = [self._savedOutfitToStruct(outfit).asTuple() for outfit in outfits]
        self.sendUpdateToAvatarId(self.doId, "setSavedOutfits", [payload])

    def _invalidateOutfitsForItem(self, invId: int) -> None:
        """
        Drop every saved outfit that references a donated-away item.

        An outfit stores a snapshot keyed by invId, so one naming an item the
        fairy no longer owns is unwearable. The donateConfirm dialog promises
        this ("You will lose this item and saved outfits with it!").
        """
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"savedOutfits": 1}
        )
        if not fairy:
            return

        outfits = fairy.get("savedOutfits", [])
        kept = [
            outfit for outfit in outfits
            if not any(item[0] == invId for item in outfit.get("items", {}).values())
        ]
        if len(kept) == len(outfits):
            return

        self.air.mongoInterface.updateField("fairies", "savedOutfits", self.doId, kept)
        self._d_setSavedOutfits(kept)

    def _pushSavedOutfitState(self) -> None:
        """
        Push the outfit state the client would otherwise only ever pull once.

        SavedOutfits reads maxOutfitSlots/savedOutfits when its panel is first
        constructed and caches them. After an AI crash the client rebuilds the
        player object empty and never re-asks, because the panel is not rebuilt:
        the book shows no outfits and every tab looks unpurchased. Generate runs
        on reconnect, so pushing here stands in for the missing pull.
        """
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"savedOutfits": 1, "maxOutfitSlots": 1}
        )
        maxSlots = (fairy or {}).get("maxOutfitSlots", DEFAULT_MAX_OUTFIT_SLOTS)
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [maxSlots])
        self._d_setSavedOutfits((fairy or {}).get("savedOutfits", []))

    def requestGetMaxOutfitSlots(self) -> None:
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"maxOutfitSlots": 1}
        )
        maxSlots = (fairy or {}).get("maxOutfitSlots", DEFAULT_MAX_OUTFIT_SLOTS)
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [maxSlots])

    def requestGetSavedOutfits(self) -> None:
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"savedOutfits": 1}
        )
        self._d_setSavedOutfits((fairy or {}).get("savedOutfits", []))

    def requestAddSavedOutfit(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        # _buildOutfitItems needs avatar.items to snapshot the eight slots.
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId},
            {"savedOutfits": 1, "maxOutfitSlots": 1, "avatar.items": 1}
        )
        if not fairy:
            return

        outfits = fairy.get("savedOutfits", [])
        maxSlots = fairy.get("maxOutfitSlots", DEFAULT_MAX_OUTFIT_SLOTS)

        # No free slot -- resync so the client drops its waiting-for-save state.
        if len(outfits) >= maxSlots:
            self._d_setSavedOutfits(outfits)
            return

        invIds = (headId, necklaceId, shirtId, beltId, skirtId, wristId, ankleId, shoesId)
        items = self._buildOutfitItems(invIds, fairy)

        outfits.append({"outfitId": self.air.mongoInterface.getNextDoId(), "items": items})
        self.air.mongoInterface.updateField("fairies", "savedOutfits", self.doId, outfits)
        self._d_setSavedOutfits(outfits)

    def requestUpdateSavedOutfit(self, outfitId: int, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        # _buildOutfitItems needs avatar.items to snapshot the eight slots.
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"savedOutfits": 1, "avatar.items": 1}
        )
        if not fairy:
            return

        outfits = fairy.get("savedOutfits", [])
        outfit = next((o for o in outfits if o["outfitId"] == outfitId), None)
        if outfit is None:
            self._d_setSavedOutfits(outfits)
            return

        invIds = (headId, necklaceId, shirtId, beltId, skirtId, wristId, ankleId, shoesId)
        outfit["items"] = self._buildOutfitItems(invIds, fairy)

        self.air.mongoInterface.updateField("fairies", "savedOutfits", self.doId, outfits)
        self._d_setSavedOutfits(outfits)

    def requestRemoveSavedOutfits(self, outfitIds: list) -> None:
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"savedOutfits": 1}
        )
        if not fairy:
            return

        # outfitIds is a LongType[]; each struct arrives as (longVal,).
        toRemove = {longType[0] for longType in outfitIds}
        outfits = [o for o in fairy.get("savedOutfits", []) if o["outfitId"] not in toRemove]

        self.air.mongoInterface.updateField("fairies", "savedOutfits", self.doId, outfits)
        self._d_setSavedOutfits(outfits)

    def requestSendSavedOutfitSlotPurchaseRequest(self) -> None:
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId}, {"maxOutfitSlots": 1}
        )
        if not fairy:
            return

        maxSlots = fairy.get("maxOutfitSlots", DEFAULT_MAX_OUTFIT_SLOTS)
        if maxSlots >= MAX_OUTFIT_SLOTS:
            return

        # takeGold charges nothing if the fairy can't afford the upgrade.
        if not self.takeGold(OUTFIT_SLOT_COST):
            return

        maxSlots = min(maxSlots + OUTFIT_SLOTS_PER_PURCHASE, MAX_OUTFIT_SLOTS)
        self.air.mongoInterface.updateField("fairies", "maxOutfitSlots", self.doId, maxSlots)
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [maxSlots])

    def d_refreshEquippedItem(self, invId: int) -> bool:
        """
        Redraw one item the fairy is wearing, after its colors changed.

        Does nothing (and says so) for an item that isn't equipped: a wardrobe
        or storage entry has nothing on the avatar to redraw, and shows its new
        colors the next time the inventory panel reads it.
        """
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {
                "_id": self.doId,
                "avatar.items": {
                    "$elemMatch": {"inv_id": invId, "location": "Equipped"}
                },
            },
            {"avatar.items.$": 1},
        )

        if not fairy:
            return False

        items = fairy.get("avatar", {}).get("items")

        if not items:
            return False

        item = items[0]
        field = EQUIP_SLOT_FIELDS.get(item.get("slot"))

        if not field:
            return False

        self.sendUpdate(field, [[invId, item["item_id"], item["color1"], item["color2"]]])
        self.redrawFairy()

        return True

    def setOutfitDB(self, headId: int, necklaceId: int, shirtId: int, beltId: int, skirtId: int, wristId: int, ankleId: int, shoesId: int) -> None:
        SLOT_METHODS = EQUIP_SLOT_FIELDS

        EMPTY_LITE_INV = [0, 0, 0, 0]

        desiredOutfit = {
            1: headId, 2: necklaceId, 3: shirtId, 4: beltId,
            5: skirtId, 6: wristId, 7: ankleId, 8: shoesId
        }
        equippedIds = {invId: slot for slot, invId in desiredOutfit.items() if invId != 0}
        filledSlots = set(equippedIds.values())
        keepSlots = {
            slot for slot, invId in desiredOutfit.items()
            if not invId and slot in MANDATORY_SLOT_NUMBERS
        }

        table = self.air.mongoInterface.mongodb.fairies

        # Ask Mongo for the few items involved, not a thousand-entry wardrobe.
        rows = list(table.aggregate([
            {"$match": {"_id": self.doId}},
            {"$project": {
                "items": {
                    "$filter": {
                        "input": {"$ifNull": ["$avatar.items", []]},
                        "as": "item",
                        "cond": {
                            "$or": [
                                {"$eq": ["$$item.location", "Equipped"]},
                                {"$in": ["$$item.inv_id", list(equippedIds)]},
                            ]
                        },
                    }
                }
            }},
        ]))

        if not rows:
            return

        # Positional updates: $set-ing the array rewrites the whole document.
        setOps = {}
        arrayFilters = []

        def stage(invId: int, location: str, slot: int) -> None:
            alias = f"i{len(arrayFilters)}"
            setOps[f"avatar.items.$[{alias}].location"] = location
            setOps[f"avatar.items.$[{alias}].slot"] = slot
            arrayFilters.append({f"{alias}.inv_id": invId})

        for item in rows[0].get("items", []):
            invId = item["inv_id"]

            if invId in equippedIds:
                slot = equippedIds[invId]

                if item["location"] == "Equipped" and item["slot"] == slot:
                    continue

                stage(invId, "Equipped", slot)
                payload = [invId, item["item_id"], item["color1"], item["color2"]]
                self.sendUpdate(SLOT_METHODS[slot], [payload])

            elif item["location"] == "Equipped":
                oldSlot = item["slot"]

                if oldSlot in keepSlots:
                    continue

                stage(invId, "Wardrobe", 0)

                if oldSlot in SLOT_METHODS and oldSlot not in filledSlots:
                    self.sendUpdate(SLOT_METHODS[oldSlot], [EMPTY_LITE_INV])

        if setOps:
            table.update_one(
                {"_id": self.doId},
                {"$set": setOps},
                array_filters=arrayFilters
            )

            self.redrawFairy()

    def setHotspotTriggered(self, tagId, hotspotFrame) -> None:
        """
        Play a shared meadow hotspot for everyone in the zone.

        The client keys hotspots by tagId rather than the config's `id`, and a
        shared one plays for nobody -- not even the fairy who clicked it --
        until the server sends a frame back. A full-play hotspot gets -1, the
        client's "run it from the start" path; a keyframe one gets the clicker's
        own frame, so everyone plays on from where they were. The config's
        serverParm is ignored on purpose -- meadow_xml's docstring has the why.
        """
        if not (meadow := self.air.zoneToMeadow.get(self.zoneId)):
            return

        hotspot = meadow_xml.getHotspot(self.zoneId, tagId)

        if hotspot is None:
            self.notify.warning(
                f"setHotspotTriggered from {self.doId} for unknown hotspot "
                f"{tagId} in zone {self.zoneId}"
            )
            return

        if not hotspot.shared:
            # Unshared hotspots are client-side; no honest client sends this.
            self.notify.warning(
                f"setHotspotTriggered from {self.doId} for unshared hotspot "
                f"{tagId} (id {hotspot.hotspotId}) in zone {self.zoneId}"
            )
            return

        frame = meadow_xml.PLAY_FROM_START if hotspot.playsFull else hotspotFrame

        self.notify.debug(
            f"setHotspotTriggered: {self.doId} hit hotspot {tagId} "
            f"(id {hotspot.hotspotId}) in zone {self.zoneId} at frame "
            f"{hotspotFrame}, sending {frame}"
        )

        meadow.d_setHotspotFrame(tagId, frame)

        # The client doesn't read <resets>, so we put the cleared ones back.
        for resetTagId, keyframe in hotspot.resets:
            if meadow_xml.getHotspot(self.zoneId, resetTagId) is None:
                self.notify.warning(
                    f"hotspot {tagId} in zone {self.zoneId} resets hotspot "
                    f"{resetTagId}, which isn't live"
                )
                continue

            # Snap and hold: a reset is a state change, not an animation.
            meadow.d_setHotspotFrame(resetTagId, meadow_xml.PLAY_AT_OFFSET + keyframe)

    def setGold(self, gold: int) -> None:
        self.gold = gold

    def getGold(self) -> int:
        return self.gold

    def d_setGold(self, gold: int) -> None:
        self.sendUpdate("setGold", [gold])

    def d_setPouch(self, pouch: list) -> None:
        self.sendUpdateToAvatarId(self.doId, "setPouch", [pouch])

    def d_syncPouchAfterChanges(self) -> None:
        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def b_setGold(self, gold: int) -> None:
        self.setGold(gold)
        self.d_setGold(gold)

    def addGold(self, deltaGold: int) -> None:
        self.b_setGold(deltaGold + self.getGold())

    def takeGold(self, deltaGold: int) -> bool:
        totalGold = self.gold

        if deltaGold > totalGold:
            return False

        self.b_setGold(self.gold - deltaGold)

        return True
    
    def requestDailyGoldTradeCapData(self) -> None:
        self._sync_gold_trading_cap()

    def _refresh_gold_trading(self) -> None:
        doc = self.air.mongoInterface.mongodb.fairies.find_one({"_id": self.doId})
        last_trade = doc.get("lastGoldTradeAt")
        self.goldTradedToday = doc.get("goldTradedToday")

        if last_trade is None:
            return

        # DB storage is tz unaware - make it aware
        last_trade_utc = last_trade.replace(tzinfo=timezone.utc)

        if get_period_start(last_trade_utc, "daily") != get_period_start(datetime.now(timezone.utc), "daily"):
            self.goldTradedToday = 0
            self._save_gold_trading()

    def _save_gold_trading(self) -> None:
        self.air.mongoInterface.updateFields(
            "fairies",
            {
                "goldTradedToday": self.goldTradedToday,
                "lastGoldTradeAt": self.lastGoldTradeAt,
            },
            self.doId,
        )
    
    def _sync_gold_trading_cap(self) -> None:
        self._refresh_gold_trading()
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [200])
        self.sendUpdateToAvatarId(self.doId, "setAmountGoldTradedForToday", [self.goldTradedToday])

    def tradeGoldForItem(self, amountToGive: int, invItemToGet: int, amountToGet: int) -> None:
        if self.takeGold(amountToGive):
            if not self.air.inventoryManager.addIngredientsToPouch(self.doId, invItemToGet, amountToGet, -1):
                self.notify.warning("Failed to add ingredient %d to pouch!" % (invItemToGet))
                return

            # Sent twice: onCheckForGiveGetUpdates only fires above one call.
            pouch = self.air.inventoryManager.getPouch(self.doId)
            self.d_setPouch(pouch)
            self.d_setPouch(pouch)

    def tradeItemForGold(self, invItemToGive: int, amountToGive: int, amountToGet: int) -> None:
        self._refresh_gold_trading()

        gold_remaining = 200 - self.goldTradedToday
        if gold_remaining <= 0 or amountToGet <= 0 or amountToGet > gold_remaining:
            self._sync_gold_trading_cap()
            return

        if not self.air.inventoryManager.removeIngredientsFromPouch(self.doId, invItemToGive, amountToGive):
            print("tradeItem - Couldn't Remove Ingredients??")
            return

        self.addGold(amountToGet)
        self.goldTradedToday += amountToGet
        self.lastGoldTradeAt = datetime.now(timezone.utc)
        self._save_gold_trading()
        self._sync_gold_trading_cap()
        # Sent twice: onCheckForGiveGetUpdates only fires above one call.
        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def tradeItem(self, invItemToGive: int, amountToGive: int, invItemToGet: int, amountToGet: int) -> None:
        if not self.air.inventoryManager.removeIngredientsFromPouch(self.doId, invItemToGive, amountToGive):
            print("tradeItemForGold - Couldn't Remove Ingredients??")
            return

        if not self.air.inventoryManager.addIngredientsToPouch(self.doId, invItemToGet, amountToGet, -1):
            self.notify.warning("Failed to add ingredient %d to pouch!" % (invItemToGet))
            return

        # Sent twice: onCheckForGiveGetUpdates only fires above one call.
        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def auraRemover(self, task):
        self.sendUpdate("setAura", [0])

    def invisRemover(self, task):
        self.sendUpdate("setRenderEffects", [0])
        self.sendUpdate("setRedraw", [1])

    def _getSweetType(self, itemId):
        """Determine which kind of silly sweet this item is."""
        if itemId == 22525:
            return "invisible"
        if itemId in AURA_MAPPING:
            return "aura"
        if itemId in SKIN_COLOR_MAPPING:
            return "skin"
        if itemId in WING_COLOR_MAPPING:
            return "wing"
        return None

    def _handleAuraSweet(self, itemId):
        aura = AURA_MAPPING[itemId]
        # A list means the sweet grants one of several auras at random.
        aura_id = random.choice(aura) if isinstance(aura, list) else aura
        self.sendUpdate("setAura", [aura_id])

        taskMgr.remove(f"AuraRemover-{self.doId}")
        taskMgr.doMethodLater(60, self.auraRemover, f"AuraRemover-{self.doId}")

    def _handleSkinSweet(self, itemId):
        color = SKIN_COLOR_MAPPING[itemId]
        self._applyDNAColor(color, slotIndex=12)

    def _handleWingSweet(self, itemId):
        color = WING_COLOR_MAPPING[itemId]
        self._applyDNAColor(color, slotIndex=13)

    def _handleInvisibleSweet(self, _):
        self.sendUpdate("setRenderEffects", [1])
        self.redrawFairy()

        taskMgr.remove(f"InvisRemover-{self.doId}")
        taskMgr.doMethodLater(60, self.invisRemover, f"InvisRemover-{self.doId}")

    def _cancelColorSweet(self, slotIndex):
        taskMgr.remove(f"DNARestore-{self.doId}-{slotIndex}")
        taskMgr.remove(f"ColorCycle-{self.doId}-{slotIndex}")

    def _restoreDNA(self, slotIndex):
        taskMgr.remove(f"ColorCycle-{self.doId}-{slotIndex}")
        if slotIndex not in self._originalDNA:
            return  # already restored, nothing to do
        dna = list(self.getFairyDNA())
        dna[slotIndex] = self._originalDNA[slotIndex]
        self.b_setFairyDNA(tuple(dna))
        self.redrawFairy()
        del self._originalDNA[slotIndex]

    def _restoreDNATask(self, task):
        if not self.isDeleted() and task.slotIndex in self._originalDNA:
            self._restoreDNA(task.slotIndex)
        return task.done

    def _runColorCycleTask(self, task):
        if not self.isDeleted():
            self._applyColorStep(task.colors[task.cycleIndex], task.slotIndex)
            task.cycleIndex = (task.cycleIndex + 1) % len(task.colors)
        return task.again

    def _applyDNAColor(self, color, slotIndex):
        if isinstance(color, list):
            self._scheduleCyclingColors(color, slotIndex)
            return

        restore_task_name = f"DNARestore-{self.doId}-{slotIndex}"

        if not taskMgr.hasTaskNamed(restore_task_name):
            self._originalDNA[slotIndex] = self.getFairyDNA()[slotIndex]

        self._cancelColorSweet(slotIndex)

        dna = list(self.getFairyDNA())
        dna[slotIndex] = color
        self.b_setFairyDNA(tuple(dna))
        self.redrawFairy()

        restore_task = taskMgr.doMethodLater(60, self._restoreDNATask, restore_task_name)
        restore_task.slotIndex = slotIndex

    def _applyColorStep(self, color, slotIndex):
        """Single color application step, used by cycling tasks."""
        dna = list(self.getFairyDNA())
        dna[slotIndex] = color
        self.b_setFairyDNA(tuple(dna))
        self.redrawFairy()

    def _runColorCycle(self, colors, slotIndex, cycleIndex=0):
        self._applyColorStep(colors[cycleIndex], slotIndex)

        cycle_task = taskMgr.doMethodLater(5, self._runColorCycleTask, f"ColorCycle-{self.doId}-{slotIndex}")
        cycle_task.colors = colors
        cycle_task.slotIndex = slotIndex
        cycle_task.cycleIndex = (cycleIndex + 1) % len(colors)

    def _scheduleCyclingColors(self, colors, slotIndex):
        restore_task_name = f"DNARestore-{self.doId}-{slotIndex}"

        if not taskMgr.hasTaskNamed(restore_task_name):
            self._originalDNA[slotIndex] = self.getFairyDNA()[slotIndex]

        self._cancelColorSweet(slotIndex)

        self._runColorCycle(colors, slotIndex, cycleIndex=0)

        restore_task = taskMgr.doMethodLater(60, self._restoreDNATask, restore_task_name)
        restore_task.slotIndex = slotIndex

    def consumePouchItem(self, itemId, amount) -> None:
        baked = BAKED_ITEMS.get(itemId)
        if not baked:
            return

        if baked["bakedType"] == "sillysweet":
            sweet_type = self._getSweetType(itemId)

            if sweet_type is None:
                print(f"ITEM MISSING FROM ALL SWEET MAPPINGS: {itemId}")
                return

            # A new sweet type only needs a matching _handle<Type>Sweet method.
            handler = getattr(self, f"_handle{sweet_type.capitalize()}Sweet")
            handler(itemId)

        elif baked["bakedType"] in ("cookie", "cupcake"):
            # Stubbed while PIXIE_POWER_ENABLED is False; see _grantPixiePower.
            self._grantPixiePower(baked["pixiePower"])

        self.sendUpdate("setItemEvent", [itemId, amount, 0, 0])
        self.air.inventoryManager.removeIngredientsFromPouch(self.doId, itemId, amount)

        pouch = self.air.inventoryManager.getPouch(self.doId)
        self.d_setPouch(pouch)
        self.d_setPouch(pouch)

    def redrawFairy(self) -> None:
        self.sendUpdate("setRedraw", [1])

    def setLevel(self, level: int) -> None:
        self.level = level

    def d_setLevel(self, level: int) -> None:
        self.sendUpdate("setLevel", [level])

    def b_setLevel(self, level: int) -> None:
        self.setLevel(level)
        self.d_setLevel(level)

    def getLevel(self) -> int:
        return self.level

    def setExperiencePoints(self, experiencePoints: int) -> None:
        self.experiencePoints = experiencePoints

    def d_setExperiencePoints(self, experiencePoints: int) -> None:
        self.sendUpdate("setExperiencePoints", [experiencePoints])

    def b_setExperiencePoints(self, experiencePoints: int) -> None:
        self.setExperiencePoints(experiencePoints)
        self.d_setExperiencePoints(experiencePoints)

    def getExperiencePoints(self) -> int:
        return self.experiencePoints

    def d_setMute(self, mute: int) -> None:
        # A courtesy, not a gag: it grays their input; setTalk still flows.
        self.sendUpdateToAvatarId(self.doId, "setMute", [mute])

    def setPixiePower(self, pixiePower: int) -> None:
        self.pixiePower = pixiePower

    def d_setPixiePower(self, pixiePower: int) -> None:
        self.sendUpdate("setPixiePower", [pixiePower])

    def b_setPixiePower(self, pixiePower: int) -> None:
        self.setPixiePower(pixiePower)
        self.d_setPixiePower(pixiePower)

    def getPixiePower(self) -> int:
        return self.pixiePower

    def _grantPixiePower(self, amount: int) -> None:
        """Restore pixie power from eating a cookie or cupcake.

        Stubbed: while PIXIE_POWER_ENABLED is False this works out the intended
        new total but neither persists nor broadcasts it, so behavior is
        unchanged. Everything else is wired, so enabling the economy later is
        just flipping the flag.
        """
        # TODO: clamp to the real maximum once the PixiePower rules are settled.
        newPower = self.getPixiePower() + amount

        if not PIXIE_POWER_ENABLED:
            return

        self.b_setPixiePower(newPower)

    def setHomeType(self, homeType: int, homeSubType: int = 0) -> None:
        self.homeType = homeType
        self.homeSubType = homeSubType

    def getHomeType(self) -> int:
        return self.homeType

    def d_setHomeType(self, homeType: int, homeSubType: int = 0) -> None:
        self.sendUpdateToAvatarId(self.doId, "setHomeType", [homeType, homeSubType])

    def b_setHomeType(self, homeType: int, homeSubType: int = 0) -> None:
        self.setHomeType(homeType, homeSubType)
        self.d_setHomeType(homeType, homeSubType)

    def _defaultHomeType(self) -> int:
        # Falls back to the fairy's talent until the player picks a home type.
        doc = self.air.mongoInterface.mongodb.fairies.find_one({"_id": self.doId})
        if doc:
            stored = doc.get("homeType")
            if stored is not None:
                return stored
            talent = doc.get("talent")
            if talent is not None:
                return talent
        return self.fairyDNA.talent

    def requestFairyInfo(self, fairyId: int, unk: int) -> None:
        from game.fairies.ai.DatabaseObject import DatabaseObject

        from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI

        def gotFairyLocation(doId: int, parentId: int, zoneId: int) -> None:
            if fairyId != doId:
                self.notify.warning(f"Got unexpected location for doId {doId}, was expecting {fairyId}!")
                return

            DISLid = fairy.getDISLid()
            fairyName = fairy.getName()
            DISLname = fairy.getDISLname()
            fairyDNA = fairy.fairyDNA.asTuple()
            fairyAccess = fairy.getAccess()
            fairyLevel = fairy.getLevel()

            # TODO: Implement this
            place: int = 0

            self.sendUpdateToAvatarId(self.doId, "responseFairyInfo", [[
                fairyId,
                DISLid,
                parentId,
                zoneId,
                fairyName,
                DISLname,
                fairyDNA[0], # talent
                fairyAccess,
                fairyLevel,
                place
            ]])

        fairy = self.air.getDo(fairyId)

        if fairy:
            # Present on this shard -- no need to ask the OTP server.
            gotFairyLocation(fairyId, fairy.parentId, fairy.zoneId)
            return

        def fieldsCallback(db: DatabaseObject, retCode: int) -> None:
            nonlocal fairy

            if retCode != 0:
                return

            fairy = DistributedFairyPlayerAI(self.air)

            db.fillin(fairy, db.dclass)

            self.air.getObjectLocation(fairyId, gotFairyLocation)

        # Not on this shard -- read their fields out of the database.
        gotFairyEvent = self.air.uniqueName(f"gotFairy-{fairyId}")
        self.acceptOnce(gotFairyEvent, fieldsCallback)

        db = DatabaseObject(self.air, fairyId)
        db.doneEvent = gotFairyEvent
        db.dclass = self.air.dclassesByName[self.__class__.__name__]
        db.getFields(["setDISLid", "setName", "setDISLname", "setFairyDNA", "setAccess", "setLevel"])

    def ignoresRealmCapacity(self) -> bool:
        # Overridden by the GM AI; the client exempts GMs from the same checks.
        return False

    def isRealmCapacityBlocked(self, parentId: int) -> bool:
        """
        Should this fairy be kept out of realm `parentId` because it is full?

        Only ever true for a *different* realm that the cluster has reported a
        FULL headcount for. Home realms are not districts and never answer yes
        here -- their cap lives in the RealmGuardian.
        """
        if parentId == self.parentId:
            # Already in that realm; capacity cannot be the reason to refuse.
            return False

        if self.ignoresRealmCapacity():
            return False

        return self.air.isRealmFull(parentId)

    def _reportRealmOverflow(self) -> None:
        """
        Log an arrival into an already-full realm.

        Nothing here can turn a client away: the client drives its own
        setLocation and the DC has no "go somewhere else" message to send.
        Realms are held under their cap by the request-time checks (fly-to-
        fairy, home teleport) and the client's shard chooser, so an overflow
        means one of those was bypassed and should not pass silently.
        """
        if self.ignoresRealmCapacity():
            return

        # We are already counted, so compare the headcount from just before.
        if self.air.getPopulation() - 1 < self.air.getRealmCapacity():
            return

        self.air.writeServerEvent(
            'realm-overflow', self.doId,
            '%s|%s' % (self.air.districtId, self.air.getPopulation()))

    def teleportRequestTo(self, fairyId: int) -> None:
        from game.fairies.ai.DatabaseObject import DatabaseObject

        from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI

        def sendResponse(parentId: int, zoneId: int, roomId: int) -> None:
            """
            Answer a fly-to request, saying where the target is and if they can
            be reached.

            An activity zone (minigame, party game, quiet meadow, home preview)
            can never load a peer, so the arriving client would hang on the
            loading screen -- report those as unavailable instead.

            roomId is the target's room type. A home and its garden share one
            zone, so it is the only thing that drops the arriving fairy in the
            garden rather than the house, and it must never be anything else:
            the client feeds it into its own dispatchRoomID, so a bogus value
            gets stamped on everything that fairy places until they next fly.
            """
            available: bool = not ZoneConstants.isUnflyableActivityZone(zoneId)

            if available and self.isRealmCapacityBlocked(parentId):
                # The shard chooser grays full realms out; this catches leaks.
                self.notify.debug(
                    "Refusing to fly %d to %d: realm %d is full (%d)"
                    % (self.doId, fairyId, parentId,
                       self.air.getRealmPopulation(parentId)))
                available = False

            if not isValidRoomType(roomId):
                self.notify.warning(
                    "teleportRequestTo: %s reported room %r, reporting the house"
                    % (fairyId, roomId))
                roomId = ROOM_TYPE_HOME

            self.sendUpdateToAvatarId(self.doId, "teleportResponse", [
                fairyId,
                available,
                parentId,
                zoneId,
                roomId
            ])

        fairy = self.air.getDo(fairyId)

        if fairy:
            # Present on this shard -- read both off the live object.
            sendResponse(fairy.parentId, fairy.zoneId, fairy.roomID)
            return

        # The room type lives on the object, not in the OTP location record.
        def gotRoomID(db: DatabaseObject, retCode: int) -> None:
            roomId: int = ROOM_TYPE_HOME
            if retCode == 0:
                remoteFairy = DistributedFairyPlayerAI(self.air)
                db.fillin(remoteFairy, db.dclass)
                roomId = remoteFairy.roomID

            def gotFairyLocation(doId: int, parentId: int, zoneId: int) -> None:
                if fairyId != doId:
                    self.notify.warning(f"Got unexpected location for doId {doId}, was expecting {fairyId}!")
                    return

                sendResponse(parentId, zoneId, roomId)

            self.air.getObjectLocation(fairyId, gotFairyLocation)

        gotRoomEvent = self.air.uniqueName(f"gotRoomID-{fairyId}")
        self.acceptOnce(gotRoomEvent, gotRoomID)

        db = DatabaseObject(self.air, fairyId)
        db.doneEvent = gotRoomEvent
        db.dclass = self.air.dclassesByName[self.__class__.__name__]
        db.getFields(["setRoomID"])

    def setWhisperSCEmoteTo(self, toId: int, emoteId: int) -> None:
        channelId = self.GetPuppetConnectionChannel(toId)

        fromId = self.doId

        self.air.sendUpdateToChannelFrom(self, channelId, "setWhisperSCEmoteFrom", fromId, [fromId, emoteId])

    def removeFromInventory(self, invId, itemId):
        """
        Drop a donated item and echo the removal on the right client list.

        Storage and wardrobe items share avatar.items, so the item's location
        picks the echo: storageRemove for Storage, wardrobeRemove for Wardrobe
        and Equipped. The wrong one leaves a stale entry in the client's model
        and skips its donate confirmation (clearDonate), so read the location
        before pulling the item.
        """
        item = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId, "avatar.items.inv_id": invId},
            {"avatar.items.$": 1}
        )

        self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": self.doId},
                {
                    "$pull": {
                        "avatar.items": {
                            "inv_id": invId
                        }
                    }
                }
        )

        location = None
        if item and item.get("avatar", {}).get("items"):
            location = item["avatar"]["items"][0].get("location")

        if location == "Storage":
            field = "storageRemove"
            donationEvent = badge_events.EVENT_DONATE_STORAGE_ITEM
        else:
            field = "wardrobeRemove"
            donationEvent = badge_events.EVENT_DONATE_WARDROBE_ITEM

        self.air.inventoryManager.sendUpdateToAvatarId(self.doId, field, [0, invId])

        # The donate confirmation promises saved outfits go with the item.
        self._invalidateOutfitsForItem(invId)

        # Donating is the only caller: one call, one item to the community.
        self.air.badgeManager.d_accumulate(self.doId, donationEvent)

    def requestGlobalPurchase(self, item):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.doId:
            self.notify.warning(
                f"requestGlobalPurchase from {avId} but sender DO is {self.doId}"
            )
            return

        # The client sends {itemId, amount} and never a price; we look it up.
        try:
            itemId, amount = item[0]
        except (IndexError, TypeError, ValueError):
            self.air.writeServerEvent(
                'suspicious', self.doId,
                'malformed requestGlobalPurchase item: %r' % (item,)
            )
            self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [0])
            return

        purchase = GLOBAL_PURCHASE_ITEMS.get(itemId)
        if purchase is None or amount < 1:
            self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [0])
            return

        # The client always displays goldPrice, so charge that to stay in sync.
        cost = purchase.goldPrice * amount
        if not self.takeGold(cost):
            self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [0])
            return

        self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [1])

    def requestSendUpdateFairyName(self, name):
        """
        Rename the fairy, live for the whole zone and persisted to Mongo.

        setName is `broadcast db ownrecv`, so one call does both. It does not
        reach the pre-game loading screen, which stays stale until the next
        login: that art belongs to the login/container shell, which caches the
        fairy list from web-api and never subscribes to this DO. Refreshing it
        live would take a client edit.
        """
        # A last-name-only pick arrives as " Bellbreeze" -- gap and all.
        name = " ".join(name.split())
        if not name:
            return

        self.b_setName(name)
        self.sendUpdateToAvatarId(self.doId, "setRedraw", [1])

    def setStatus(self, location_status, pose_status, holding_status, afk_status):
        if pose_status == 8:
            if self.lastPoseStatus not in (8,10):
                pose_status = random.choice([8, 10])
            else:
                pose_status = self.lastPoseStatus
        
        self.lastPoseStatus = pose_status
        self.sendUpdate("setStatus", [location_status, pose_status, holding_status, afk_status])
