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

# Post Office mail types that light the HUD "you've got a package" gift-box next
# to the house button (client GameButtons.onShowHomeItem keys off
# statusUpdateFromFairy being 4 or 5). Mirror the message `type` written by the
# shopkeeper AI: 4 = postcards, 5 = gift sets.
MAIL_STATUS_POSTCARD = 4
MAIL_STATUS_GIFTSET = 5

# Global purchases the client can make from the shop panel, keyed by itemId. The
# client only ever sends {itemId, amount} up (see GlobalShopPurchase); the server
# is the price authority, so we keep the MiscItem here and charge from it.
#   90003 = avatar name change (MMOConstants.AVATAR_NAME_UPDATE_ID)
GLOBAL_PURCHASE_ITEMS = {
    90003: MiscItem.unpackFromTuple((90003, 8006, 500, 200, 200)),
}

# Saved outfits. Every fairy starts with one slot and can buy more, two at a
# time (a "tab" in the client's SavedOutfits panel holds two outfits). The cap
# and per-purchase step mirror the client: MAX_OUTFIT_TABS(14) * 2 - 1 slots,
# and SLOT_COST pixie diamonds per upgrade.
DEFAULT_MAX_OUTFIT_SLOTS = 1
MAX_OUTFIT_SLOTS = 27
OUTFIT_SLOTS_PER_PURCHASE = 2

# Flat cost per slot upgrade, charged from `gold` (what the client calls
# diamonds). Must stay in sync with the client's hardcoded
# SavedOutfits.SLOT_COST = 10, since the client both labels the dialog and gates
# affordability on that number.
OUTFIT_SLOT_COST = 10

# The eight equipment slots, in the order the client sends the invIds for
# add/update and reads them back in a SavedOutfit struct (see setOutfitDB).
OUTFIT_SLOT_ORDER = ("head", "necklace", "shirt", "belt", "skirt", "wrist", "ankle", "shoes")

# The slots a fairy is always dressed in.
MANDATORY_OUTFIT_SLOTS = frozenset({"shirt", "skirt", "shoes"})
MANDATORY_SLOT_NUMBERS = frozenset(
    index + 1
    for index, slot in enumerate(OUTFIT_SLOT_ORDER)
    if slot in MANDATORY_OUTFIT_SLOTS
)

# Stored slot number -> the DC field that redraws that slot on every client
# watching. Anything that changes what is worn (equipping, dyeing) has to send
# the matching one or the fairy keeps wearing the old thing.
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

# Master switch for the pixie-power economy (cookies/cupcakes restoring power).
# PixiePower is a fixed value in-game today, so the grant path (_grantPixiePower)
# is fully wired but does not persist/broadcast while this is False. Flip to True
# once PixiePower goes live — no other code change is needed to enable it.
PIXIE_POWER_ENABLED = False

# Pixie power the setPixiePower DC field is born with (see fairy.dc: default 100).
# TODO: Change this later once everything works right - Default should be 10, Max 240.
DEFAULT_PIXIE_POWER = 100

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

        # Owner of the home realm this avatar is currently in (0 = not in a
        # home). Tracked so the RealmGuardian can tear down empty realms.
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

        # The client only pulls saved-outfit state once (on panel construction),
        # so push it on generate to survive a crash + reconnect. See
        # _pushSavedOutfitState.
        self._pushSavedOutfitState()

        # Light the HUD gift-box if Post Office mail is waiting. Same reconnect
        # reasoning: the client only reacts to statusUpdateFromFairy, and an
        # offline recipient never saw the live nudge, so push it on generate.
        self._pushPendingMailStatus()

    def d_statusUpdateFromFairy(self, fromPlayerId: int, status: int) -> None:
        # Tell our own client someone left us Post Office mail. status 4/5 lights
        # the HUD gift-box (GameButtons.onShowHomeItem); it clears to 0 when we
        # next stand in our home.
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
        # TODO: Set a post-remove message in case of an AI crash.

        # Leave any home realm we were in so it can be torn down if now empty.
        #
        # This copy of the avatar is also deleted when it migrates to another
        # district AI -- which is exactly what flying from one house to another
        # usually does -- so name the home we think we are leaving. By the time
        # the guardian reads this the fairy may already have been reported as
        # having arrived somewhere else, and it must not act on us then.
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

        # Track home-realm occupancy. Housing zones are ownerId + offset; 
        # anything else means we're not in a home.
        homeOwner = zoneId - HOUSING_ZONE_OFFSET if zoneId >= HOUSING_ZONE_OFFSET else 0
        if homeOwner != self.currentHomeOwner:
            previousOwner = self.currentHomeOwner
            self.currentHomeOwner = homeOwner
            self.air.sendRealmOccupancyUpdate(self.doId, homeOwner, previousOwner)

        if badge_events.get_meadow_badge_for_zone(zoneId) is not None:
            self.air.badgeManager.d_exploreMeadow(self.doId, zoneId)

    def _dailyChanceExcludedBadges(self) -> set[int]:
        # Never offer a badge the fairy already has. The client sends bits for
        # two of the three, but has none for Mr. Twitches, who was added after
        # it shipped -- so read the fairy's own badges rather than trust a mask
        # that cannot describe all of them anyway.
        return badge_state.get_earned_badge_ids(self.air, self.doId, SPIN_BADGE_ID_SET)

    def _dailyChanceExcludedCategories(self, excludeMask: int) -> set[Category]:
        # The wardrobe and storage bits say if there is nowhere to put that kind of
        # prize. Taking the client's word here is fine. The worst a lie can do
        # is win someone a prize they have no room for
        excluded = set()

        if excludeMask & EXCLUDE_WARDROBE:
            excluded.add(Category.WARDROBE)

        if excludeMask & EXCLUDE_STORAGE:
            excluded.add(Category.HOME)

        # Every badge on Vidia's page is Member-only, so a free fairy drawing one
        # would win a prize the badge manager then refuses to hand over.
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

        # The rocks are counted per rock, so a member pulling three at once gets credit for three.
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
        itemsById = {item["inv_id"]: item for item in fairy["avatar"]["items"]}
        wanted = dict(zip(OUTFIT_SLOT_ORDER, invIds))

        # The shop's save-outfit button (ShopPanel.saveOutfitToLookBook) fills in
        # only the slots the player just bought and sends 0 for all the rest, so
        # a Post Office trinket run saves an outfit of bare accessories -- and
        # wearing it later undresses the fairy, since SavedOutfits.onWearOutfit
        # hands those zeros straight to setOutfitDB. The shop's own "wear it now"
        # path doesn't have the hole (getUpdatedInvIdForDB falls back to what the
        # fairy has on for every slot it didn't buy), so do the same here: the
        # saved outfit becomes the whole look, not just the receipt.
        #
        # A zero from the wardrobe *is* deliberate ("no necklace, thanks"), so
        # only reach for the fallback when a slot the fairy can't go without came
        # in empty while she is in fact wearing something there. That never
        # happens on the wardrobe path, only on the shop's partial one.
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
        # A saved outfit stores a snapshot of each slot's item, keyed by invId
        # (index 0 of the stored LiteInvItemExt2 tuple). When the underlying item
        # is donated away, any outfit referencing it is no longer wearable, so we
        # drop the whole outfit -- the donateConfirm dialog warns the player of
        # exactly this ("You will lose this item and saved outfits with it!").
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
        # The client's SavedOutfits panel fetches maxOutfitSlots/savedOutfits
        # exactly once -- when it's first constructed (SavedOutfits.refreshOutfits,
        # called from the panel's one-time init) -- and caches them on the
        # DistributedFairyPlayer. After an AI crash + reconnect the client rebuilds
        # that player object empty (savedOutfits=null, maxOutfitSlots=-1) but never
        # re-requests, because the panel isn't reconstructed. The book then shows
        # no outfits and every tab looks unpurchased (and buying does nothing,
        # since we're really already at the slot cap). Push the state on generate
        # (which also runs on reconnect) so the freshly (re)generated client
        # object is populated without needing a request, mirroring the pull.
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

        # No free slot -- just resync so the client leaves its "waiting for save"
        # state. The client is meant to buy a slot before it gets here.
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

        # outfitIds is a LongType[]; each struct arrives as a one-tuple (longVal,).
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

        # takeGold is the diamond balance from the client's point of view; it
        # fails (and charges nothing) if the fairy can't afford the upgrade.
        if not self.takeGold(OUTFIT_SLOT_COST):
            return

        maxSlots = min(maxSlots + OUTFIT_SLOTS_PER_PURCHASE, MAX_OUTFIT_SLOTS)
        self.air.mongoInterface.updateField("fairies", "maxOutfitSlots", self.doId, maxSlots)
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [maxSlots])

    def d_refreshEquippedItem(self, invId: int) -> bool:
        """
        Redraw one item the fairy is wearing, after its colours changed.

        Does nothing (and says so) for an item that isn't equipped: a wardrobe
        or storage entry has nothing on the avatar to redraw, and shows its new
        colours the next time the inventory panel reads it.
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

        # Only two kinds of item can change here: one the client asked us to put
        # on, and one that is on right now (and may have to come off). The rest
        # of the wardrobe -- most of a thousand-odd entries, for the players who
        # notice this -- is untouched, so ask Mongo for just those few instead of
        # dragging the whole document back to filter it in Python.
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

        # Stage each change as its own positional update rather than $set-ing
        # avatar.items wholesale: writing the array back makes Mongo rewrite the
        # entire document -- and the oplog carry a copy of it -- on every single
        # outfit change, to move at most sixteen items between two locations.
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
        # The client keys hotspots by tagId, not by the config's `id`, and sends
        # its own current frame along. A shared hotspot plays for nobody -- not
        # even the fairy who clicked it -- until we send a frame back.
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
            # Unshared hotspots are handled entirely client-side, so this can't
            # come from an honest client.
            self.notify.warning(
                f"setHotspotTriggered from {self.doId} for unshared hotspot "
                f"{tagId} (id {hotspot.hotspotId}) in zone {self.zoneId}"
            )
            return

        # A full-play hotspot gets -1, which is the client's "run the whole
        # animation from the start" path; a keyframe one gets the clicker's own
        # frame back, so everyone plays on from where they were. The config's
        # serverParm looks like it should decide this instead and is ignored on
        # purpose -- meadow_xml's docstring has the why, and the why for -1.
        frame = meadow_xml.PLAY_FROM_START if hotspot.playsFull else hotspotFrame

        self.notify.debug(
            f"setHotspotTriggered: {self.doId} hit hotspot {tagId} "
            f"(id {hotspot.hotspotId}) in zone {self.zoneId} at frame "
            f"{hotspotFrame}, sending {frame}"
        )

        meadow.d_setHotspotFrame(tagId, frame)

        # Some hotspots are a button for clearing other hotspots -- the
        # tic-tac-toe eraser and its nine squares. The client doesn't read
        # <resets>, so the squares only go back if we put them back.
        for resetTagId, keyframe in hotspot.resets:
            if meadow_xml.getHotspot(self.zoneId, resetTagId) is None:
                self.notify.warning(
                    f"hotspot {tagId} in zone {self.zoneId} resets hotspot "
                    f"{resetTagId}, which isn't live"
                )
                continue

            # Snap-and-hold rather than play-on: a reset is a state change, not
            # an animation, and the mark should just be gone.
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

            # Apparently setPouch has to be sent back to the client twice here because `onCheckForGiveGetUpdates`
            # only fires if pouchUpdateCalls is greater than 1
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
        # Apparently setPouch has to be sent back to the client twice here because `onCheckForGiveGetUpdates`
        # only fires if pouchUpdateCalls is greater than 1
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

        # Apparently setPouch has to be sent back to the client twice here because `onCheckForGiveGetUpdates`
        # only fires if pouchUpdateCalls is greater than 1
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
        # A list means the sweet randomly grants one of several auras
        # (e.g. 22587/22588 grow or shrink, a nod to Alice in Wonderland).
        aura_id = random.choice(aura) if isinstance(aura, list) else aura
        self.sendUpdate("setAura", [aura_id])

        # Cancel any existing aura timer and start fresh
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

            # Calls _handleAuraSweet, _handleSkinSweet, or _handleWingSweet
            # depending on sweet_type. Add new types by adding a matching method.
            handler = getattr(self, f"_handle{sweet_type.capitalize()}Sweet")
            handler(itemId)

        elif baked["bakedType"] in ("cookie", "cupcake"):
            # Cookies and cupcakes restore pixie power. Stubbed for now — see
            # _grantPixiePower / PIXIE_POWER_ENABLED — since PixiePower is a
            # fixed value in-game today.
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
        # Owner-directed: the only thing that reacts is the muted fairy's own
        # ChatManager, which greys their chat input out. Nothing on this server
        # drops their setTalk, so this is a client-side courtesy and not a gag --
        # see game/fairies/magicwords/commands/moderation.py.
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

        Stubbed: while PIXIE_POWER_ENABLED is False this computes the intended
        new total but does not persist or broadcast it, so behaviour is
        unchanged. The dispatch and plumbing are in place so enabling the
        economy later is just flipping the flag.
        """
        # TODO: clamp to the real in-game maximum once PixiePower rules are
        # confirmed (the DC default is 100, but cookies grant well past that).
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
        # home_type_id defaults to the fairy's talent until they change it.
        # A stored homeType (once the player changes it) takes precedence.
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
            # This fairy is present on this shard, no need to query location from OTP server.
            gotFairyLocation(fairyId, fairy.parentId, fairy.zoneId)
            return

        def fieldsCallback(db: DatabaseObject, retCode: int) -> None:
            nonlocal fairy

            if retCode != 0:
                return

            fairy = DistributedFairyPlayerAI(self.air)

            db.fillin(fairy, db.dclass)

            # Dispatch a request to the OTP server to find out where this fairy is.
            self.air.getObjectLocation(fairyId, gotFairyLocation)

        # Query the fairy for data since they are not present on this shard:
        gotFairyEvent = self.air.uniqueName(f"gotFairy-{fairyId}")
        self.acceptOnce(gotFairyEvent, fieldsCallback)

        db = DatabaseObject(self.air, fairyId)
        db.doneEvent = gotFairyEvent
        db.dclass = self.air.dclassesByName[self.__class__.__name__]
        db.getFields(["setDISLid", "setName", "setDISLname", "setFairyDNA", "setAccess", "setLevel"])

    def ignoresRealmCapacity(self) -> bool:
        # Overridden by DistributedFairyGMAI. The client exempts GMs from the
        # shard chooser's full-realm greyout and from the home population lock,
        # so the server has to let them past its own checks too.
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
        # Nothing here can turn a client away: the client drives its own
        # setLocation and the DC has no "go somewhere else" message for us to
        # send. Realms are kept under their cap by the request-time checks
        # (fly-to-fairy, home teleport) plus the client's shard chooser, so an
        # arrival into an already-full realm means one of those was bypassed.
        # Log it rather than let the overflow pass silently.
        if self.ignoresRealmCapacity():
            return

        # We have already counted ourselves, so compare the headcount as it was
        # immediately before we arrived.
        if self.air.getPopulation() - 1 < self.air.getRealmCapacity():
            return

        self.air.writeServerEvent(
            'realm-overflow', self.doId,
            '%s|%s' % (self.air.districtId, self.air.getPopulation()))

    def teleportRequestTo(self, fairyId: int) -> None:
        from game.fairies.ai.DatabaseObject import DatabaseObject

        from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI

        def sendResponse(parentId: int, zoneId: int, roomId: int) -> None:
            # A fairy in an activity zone (talent/crafting minigame, multiplayer
            # party game, quest/quiet meadow, or home preview) can't be flown to
            # -- the client would set interest on a zone it can never load a peer
            # into, hanging forever on the loading screen. Report them as
            # unavailable so the client shows a graceful teleport-failed instead.
            available: bool = not ZoneConstants.isUnflyableActivityZone(zoneId)

            if available and self.isRealmCapacityBlocked(parentId):
                # The target is in a different realm that is already FULL. The
                # shard chooser greys full realms out client-side; without this
                # check, flying to a friend walked straight past that and
                # overfilled the shard anyway.
                self.notify.debug(
                    "Refusing to fly %d to %d: realm %d is full (%d)"
                    % (self.doId, fairyId, parentId,
                       self.air.getRealmPopulation(parentId)))
                available = False

            # roomId is the target's room type (ROOM_TYPE_HOME / ROOM_TYPE_GARDEN).
            # A home and its garden share the same zone, so this is the only thing
            # that tells the client to drop the arriving fairy in the garden rather
            # than the house.
            #
            # Never report anything else. The arriving client does not just read
            # this to pick a room -- teleportResponse feeds it into its own
            # dispatchRoomID, so it becomes that fairy's roomID, and anything they
            # place before their next teleport is stamped with it. A value that is
            # neither room produces furniture that draws in the house but can never
            # be selected or returned to storage.
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
            # Present on this shard: read location and room type straight off the
            # live object, no need to query the OTP server or database.
            sendResponse(fairy.parentId, fairy.zoneId, fairy.roomID)
            return

        # Not on this shard. The room type lives on the object (not in the OTP
        # location record), so pull the persisted setRoomID from the database
        # first, then ask the OTP server where the fairy currently is.
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
        # Donating an item (StorageInventoryEntry.donate / WardrobeInventoryEntry.donate)
        # both land here -- storage and wardrobe items share avatar.items. We must
        # echo the removal on the matching client list: storageRemove for Storage
        # items, wardrobeRemove for Wardrobe/Equipped. Sending the wrong one leaves
        # a stale entry in the client's inventory model and skips its donate
        # confirmation (clearDonate). Read the location before pulling.
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

        # The item is gone from inventory, so invalidate any saved outfit that
        # still references it (the client's donate confirmation promises this).
        self._invalidateOutfitsForItem(invId)

        # Donating is the only thing that reaches removeFromInventory (both
        # StorageInventoryEntry.donate and WardrobeInventoryEntry.donate), so each
        # call is one item given to the community -- advance the donation ladder.
        self.air.badgeManager.d_accumulate(self.doId, donationEvent)

    def requestGlobalPurchase(self, item):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.doId:
            self.notify.warning(
                f"requestGlobalPurchase from {avId} but sender DO is {self.doId}"
            )
            return

        # GlobalPurchaseItem is {itemId, amount}; the client hardcodes amount to 1
        # and never sends a price -- we look the price up ourselves.
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
        # setName is `broadcast db ownrecv`, so this updates every client in the
        # zone live and persists to Mongo via the DBSS bridge.
        #
        # Known limitation (client-side, not fixable from here): the name on the
        # pre-game loading screen stays stale until the next login. That art is
        # rendered by the login/container shell (login.swf / container.swf), a
        # separate SWF that caches the fairy list from web-api at login and never
        # subscribes to this DO -- so it never hears setName. It self-heals on
        # reload once web-api returns the persisted name. Refreshing it live would
        # require a client edit (e.g. mmo.swf pushing the name to the shell).
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
