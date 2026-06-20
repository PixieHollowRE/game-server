from direct.directnotify import DirectNotifyGlobal

from game.otp.otpbase import OTPGlobals

from .DistributedFairyBaseAI import DistributedFairyBaseAI
from game.fairies.ai.BakingAssets import BAKED_ITEMS
from game.fairies.fairy.AuraMapping import AURA_MAPPING, SKIN_COLOR_MAPPING, WING_COLOR_MAPPING
from game.fairies.fairy.structs.MiscItem import MiscItem

from game.fairies.daily.DailyChanceData import (
    DEV_TEST_PRIZE,
    owned_spin_badge_exclude_mask,
    roll_rewards,
)
from game.fairies.daily.DailyChanceEligibility import (
    can_spin_today,
    current_spin_day,
    played_flag_for_client,
)
from game.fairies.daily.DailyChanceGrant import get_earned_spin_badge_ids, grant_prize
from game.fairies.stats.GameStatsService import apply_daily_spin
from game.fairies.daily.DailyGoldTradeEligibility import (
    DAILY_GOLD_TRADE_CAP,
    refresh_gold_trade_window,
)
from game.fairies.badges.MoreOptions import (
    MORE_OPTIONS_EMPTY,
    normalize_more_options,
    persist_more_options,
)
from game.fairies.badges.MeadowExplorerBadgeRegistry import ALL_EXPLORER_ZONE_IDS
from game.fairies.outfits.SavedOutfitService import (
    SAVED_OUTFIT_SLOT_ITEM_ID,
    add_saved_outfit,
    extract_outfit_ids,
    get_max_outfit_slots,
    get_outfit_slot_price,
    load_saved_outfit_doc,
    lookup_item_for_equip,
    pack_saved_outfits_for_client,
    purchase_outfit_slot,
    remove_saved_outfits,
    resolve_monotonic_max_outfit_slots,
    update_saved_outfit,
)
# Matches client MMOConstants.HOTSPOT_PLAY_AT_OFFSET — frame > offset snaps without play().
HOTSPOT_PLAY_AT_OFFSET = 8000
CBH_TTT_RESET_FRAME = HOTSPOT_PLAY_AT_OFFSET + 1  # keyframe 1 → empty cell

notify = DirectNotifyGlobal.directNotify.newCategory("DistributedFairyPlayerAI")

DAILY_CHANCE_GRANTS_ENABLED = True
DAILY_CHANCE_ONCE_PER_DAY_ENABLED = True

OUTFIT_MAX_DEBOUNCE_SEC = 0.2
OUTFIT_PURCHASE_FOLLOWUP_SEC = 0.35

class DistributedFairyPlayerAI(DistributedFairyBaseAI):
    def __init__(self, air) -> None:
        DistributedFairyBaseAI.__init__(self, air)

        self.DISLname: str = ""
        self.DISLid: int = 0
        self.gold: int = 0
        self.access: int = 0
        self.level: int = 0
        self.dailyChancePlayed: int = 0
        self.dailyChanceLastSpinDay: int = 0
        self.amountGoldTradedToday: int = 0
        self.goldTradeResetAt: int = 0
        self.moreOptions: str = MORE_OPTIONS_EMPTY

        self._originalDNA = {}
        self._outfitSlotsClientMax: int | None = None
        self._outfitSlotSeq: int = 0

    def announceGenerate(self):
        self.air.incrementPopulation()

        # Fill in the missing information from the database (i.e. gold)
        self.air.fillInFairyPlayer(self)

        if not DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._sync_daily_chance_not_played_for_client()

        self.air.inventoryManager.avatarOnline(self.doId)

        self._sync_daily_gold_trade_cap()

        self._sync_saved_outfits_to_client(force_max=True)
        self._send_global_purchase_data()

    def delete(self):
        from game.fairies.uberdog.leaderboard.leaderboard_panel import clear_panel_session

        self._cancel_outfit_slot_tasks()
        clear_panel_session(self.doId)

        self.air.decrementPopulation()

        DistributedFairyBaseAI.delete(self)

    def setLocation(self, parentId, zoneId):
        old_zone = self.zoneId
        super().setLocation(parentId, zoneId)
        if zoneId and zoneId != old_zone:
            self._sync_zone_peer_profile_state()

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

    def setDailyChanceLastSpinDay(self, spin_day: int) -> None:
        self.dailyChanceLastSpinDay = int(spin_day)
        if DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._sync_daily_chance_played_from_spin_day()

    def getDailyChanceLastSpinDay(self) -> int:
        return self.dailyChanceLastSpinDay

    def _sync_daily_chance_played_from_spin_day(self) -> None:
        played = played_flag_for_client(self.getDailyChanceLastSpinDay())
        self.setDailyChancePlayed(played)
        self.d_setDailyChancePlayed(played)

    def _record_daily_chance_spin(self) -> None:
        if not DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            return

        spin_day = current_spin_day()
        self.setDailyChanceLastSpinDay(spin_day)
        self.air.mongoInterface.updateField(
            "fairies", "dailyChanceLastSpinDay", self.doId, spin_day
        )

    def _sync_daily_chance_not_played_for_client(self) -> None:
        self.setDailyChancePlayed(0)
        self.d_setDailyChancePlayed(0)

    def requestDailyChance(self, excludeMask: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        if avId != self.doId:
            self.notify.warning(
                f"requestDailyChance from {avId} but sender DO is {self.doId}"
            )
            return

        if DAILY_CHANCE_ONCE_PER_DAY_ENABLED and not can_spin_today(
            self.getDailyChanceLastSpinDay()
        ):
            self._sync_daily_chance_played_from_spin_day()
            self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [[]])
            return

        if not DAILY_CHANCE_GRANTS_ENABLED:
            self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [[]])
            return

        avatar_gender = self.fairyDNA.gender
        earned_spin_badges = get_earned_spin_badge_ids(self.air, avId)
        effective_mask = excludeMask | owned_spin_badge_exclude_mask(earned_spin_badges)
        prizes = roll_rewards(effective_mask, self.isPaid(), avatar_gender)
        if not prizes:
            prizes = [DEV_TEST_PRIZE]

        granted: list[tuple[int, int, int, int]] = []
        granted_prizes = []
        for prize in prizes:
            if grant_prize(self.air, avId, self, prize):
                granted.append(prize.as_reward_ext())
                granted_prizes.append(prize)
            else:
                self.notify.warning(
                    f"requestDailyChance: failed to grant item {prize.item_id} to {avId}"
                )

        if not granted and prizes:
            self.notify.warning(
                f"requestDailyChance: no grants applied for {avId}, "
                f"prizes={[p.item_id for p in prizes]}"
            )

        self.sendUpdateToAvatarId(avId, "setDailyChanceReward", [granted])

        badge_manager = getattr(self.air, "badgeManager", None)
        inventory_manager = getattr(self.air, "inventoryManager", None)
        if badge_manager is not None and inventory_manager is not None:
            apply_daily_spin(
                badge_manager,
                inventory_manager,
                avId,
                granted_prizes,
            )

        if DAILY_CHANCE_ONCE_PER_DAY_ENABLED:
            self._record_daily_chance_spin()
        else:
            self._sync_daily_chance_not_played_for_client()

    def requestDailyGoldTradeCapData(self) -> None:
        self._sync_daily_gold_trade_cap()

    def _refresh_gold_trade_window(self) -> None:
        amount, reset_at = refresh_gold_trade_window(
            self.amountGoldTradedToday,
            self.goldTradeResetAt,
        )
        if amount != self.amountGoldTradedToday or reset_at != self.goldTradeResetAt:
            self.amountGoldTradedToday = amount
            self.goldTradeResetAt = reset_at
            self._persist_gold_trade_state()

    def _persist_gold_trade_state(self) -> None:
        self.air.mongoInterface.updateFields(
            "fairies",
            {
                "amountGoldTradedToday": self.amountGoldTradedToday,
                "goldTradeResetAt": self.goldTradeResetAt,
            },
            self.doId,
        )

    def _sync_daily_gold_trade_cap(self) -> None:
        self._refresh_gold_trade_window()
        self.sendUpdateToAvatarId(self.doId, "setDailyGoldTradeCap", [DAILY_GOLD_TRADE_CAP])
        self.sendUpdateToAvatarId(
            self.doId, "setAmountGoldTradedForToday", [self.amountGoldTradedToday]
        )

    def _send_saved_outfits_list(self, doc: dict | None = None) -> None:
        if doc is None:
            doc = load_saved_outfit_doc(self.air, self.doId)
        self.sendUpdateToAvatarId(
            self.doId,
            "setSavedOutfits",
            [pack_saved_outfits_for_client(doc)],
        )

    def _outfit_slot_task_name(self, suffix: str) -> str:
        return f"outfitSlot-{suffix}-{self.doId}"

    def _cancel_outfit_slot_tasks(self) -> None:
        taskMgr.remove(self._outfit_slot_task_name("debounce"))
        taskMgr.remove(self._outfit_slot_task_name("followup"))

    def _schedule_debounced_max_sync(self) -> None:
        task_name = self._outfit_slot_task_name("debounce")
        taskMgr.remove(task_name)
        taskMgr.doMethodLater(
            OUTFIT_MAX_DEBOUNCE_SEC,
            self._debounced_max_sync_task,
            task_name,
        )

    def _debounced_max_sync_task(self, task) -> None:
        self._send_max_outfit_slots(reason="debounced_get_max")

    def _schedule_purchase_followup_resync(self) -> None:
        task_name = self._outfit_slot_task_name("followup")
        taskMgr.remove(task_name)
        taskMgr.doMethodLater(
            OUTFIT_PURCHASE_FOLLOWUP_SEC,
            self._purchase_followup_resync_task,
            task_name,
        )

    def _purchase_followup_resync_task(self, task) -> None:
        self._send_max_outfit_slots(force=True, reason="purchase_followup")

    def _send_max_outfit_slots(
        self,
        doc: dict | None = None,
        *,
        force: bool = False,
        reason: str = "unspecified",
    ) -> int:
        if doc is None:
            doc = load_saved_outfit_doc(self.air, self.doId)
        mongo_max = get_max_outfit_slots(doc)
        send_max, suppressed = resolve_monotonic_max_outfit_slots(
            mongo_max,
            self._outfitSlotsClientMax,
            force=force,
        )
        self._outfitSlotSeq += 1
        seq = self._outfitSlotSeq
        highwater_before = self._outfitSlotsClientMax
        if suppressed:
            notify.info(
                "suppressed stale maxOutfitSlots avId=%s mongo=%s highwater=%s reason=%s seq=%s"
                % (self.doId, mongo_max, highwater_before, reason, seq)
            )
        self._outfitSlotsClientMax = send_max
        self.sendUpdateToAvatarId(self.doId, "setMaxOutfitSlots", [send_max])
        return send_max

    def _sync_saved_outfits_to_client(self, *, force_max: bool = False) -> None:
        doc = load_saved_outfit_doc(self.air, self.doId)
        reason = "login_sync" if force_max else "full_sync"
        self._send_max_outfit_slots(doc, force=force_max, reason=reason)
        self._send_saved_outfits_list(doc)

    def _send_global_purchase_data(self) -> None:
        doc = load_saved_outfit_doc(self.air, self.doId)
        price = get_outfit_slot_price(get_max_outfit_slots(doc))
        outfit_slot = MiscItem.unpackFromTuple(
            (SAVED_OUTFIT_SLOT_ITEM_ID, 8499, price, price, price)
        )
        name_change = MiscItem.unpackFromTuple((90003, 8006, 500, 200, 200))
        self.sendUpdateToAvatarId(
            self.doId,
            "setGlobalPurchaseData",
            [[outfit_slot, name_change]],
        )

    def _handle_outfit_slot_purchase(self) -> None:
        self._cancel_outfit_slot_tasks()
        new_max = purchase_outfit_slot(self.air, self.doId, self)
        if new_max is None:
            notify.warning(
                "outfit slot purchase failed avId=%s gold=%s"
                % (self.doId, self.getGold())
            )
            self._send_max_outfit_slots(force=True, reason="purchase_fail_resync")
            self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [0])
            return

        notify.info("outfit slot purchase ok avId=%s newMax=%s" % (self.doId, new_max))
        self._send_max_outfit_slots(force=True, reason="purchase_ok")
        self._send_saved_outfits_list()
        self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [1])
        self._send_global_purchase_data()

    def requestGetMaxOutfitSlots(self) -> None:
        self._cancel_outfit_slot_tasks()
        notify.info(
            "requestGetMaxOutfitSlots avId=%s highwater=%s"
            % (self.doId, self._outfitSlotsClientMax)
        )
        # Panel refreshOutfits() waits for setMaxOutfitSlots before it can display.
        self._send_max_outfit_slots(reason="get_max")

    def requestGetSavedOutfits(self) -> None:
        notify.info("requestGetSavedOutfits avId=%s" % self.doId)
        self._send_saved_outfits_list()

    def requestAddSavedOutfit(
        self,
        headId: int,
        necklaceId: int,
        shirtId: int,
        beltId: int,
        skirtId: int,
        wristId: int,
        ankleId: int,
        shoesId: int,
    ) -> None:
        inv_ids = [headId, necklaceId, shirtId, beltId, skirtId, wristId, ankleId, shoesId]
        notify.info(
            "requestAddSavedOutfit avId=%s invIds=%s" % (self.doId, inv_ids)
        )
        result, failure = add_saved_outfit(self.air, self.doId, inv_ids, player=self)
        if result is None:
            notify.warning(
                "requestAddSavedOutfit failed avId=%s reason=%s invIds=%s"
                % (self.doId, failure, inv_ids)
            )
            return

        notify.info(
            "requestAddSavedOutfit ok avId=%s outfitCount=%s"
            % (self.doId, len(result["savedOutfits"]))
        )
        self._send_saved_outfits_list(result)

    def requestUpdateSavedOutfit(
        self,
        outfitId: int,
        headId: int,
        necklaceId: int,
        shirtId: int,
        beltId: int,
        skirtId: int,
        wristId: int,
        ankleId: int,
        shoesId: int,
    ) -> None:
        inv_ids = [headId, necklaceId, shirtId, beltId, skirtId, wristId, ankleId, shoesId]
        notify.info(
            "requestUpdateSavedOutfit avId=%s outfitId=%s invIds=%s"
            % (self.doId, outfitId, inv_ids)
        )
        result, failure = update_saved_outfit(
            self.air, self.doId, outfitId, inv_ids, player=self
        )
        if result is None:
            notify.warning(
                "requestUpdateSavedOutfit failed avId=%s outfitId=%s reason=%s invIds=%s"
                % (self.doId, outfitId, failure, inv_ids)
            )
            return

        notify.info(
            "requestUpdateSavedOutfit ok avId=%s outfitId=%s" % (self.doId, outfitId)
        )
        self._send_saved_outfits_list(result)

    def requestRemoveSavedOutfits(self, outfitIds) -> None:
        ids = extract_outfit_ids(outfitIds)
        notify.info(
            "requestRemoveSavedOutfits avId=%s raw=%s parsed=%s"
            % (self.doId, outfitIds, ids)
        )
        if not ids:
            notify.warning(
                "requestRemoveSavedOutfits empty id list avId=%s raw=%s"
                % (self.doId, outfitIds)
            )
            return

        result = remove_saved_outfits(self.air, self.doId, ids)
        notify.info(
            "requestRemoveSavedOutfits ok avId=%s remaining=%s"
            % (self.doId, len(result["savedOutfits"]))
        )
        self._send_saved_outfits_list(result)

    def requestSendSavedOutfitSlotPurchaseRequest(self) -> None:
        notify.info(
            "requestSendSavedOutfitSlotPurchaseRequest avId=%s highwater=%s gold=%s"
            % (self.doId, self._outfitSlotsClientMax, self.getGold())
        )
        self._handle_outfit_slot_purchase()

    def requestGlobablPurchaseData(self) -> None:
        self._send_global_purchase_data()

    def setOutfitDB(
        self,
        headId: int,
        necklaceId: int,
        shirtId: int,
        beltId: int,
        skirtId: int,
        wristId: int,
        ankleId: int,
        shoesId: int,
    ) -> None:
        SLOT_METHODS = {
            1: "setHeadItem",
            2: "setNecklace",
            3: "setChestItem",
            4: "setBelt",
            5: "setSkirt",
            6: "setWrist",
            7: "setAnkle",
            8: "setShoes",
        }

        EMPTY_LITE_INV = [0, 0, 0, 0]

        desiredOutfit = {
            1: headId,
            2: necklaceId,
            3: shirtId,
            4: beltId,
            5: skirtId,
            6: wristId,
            7: ankleId,
            8: shoesId,
        }
        equippedIds = {invId: slot for slot, invId in desiredOutfit.items() if invId != 0}
        filledSlots = set(equippedIds.values())

        notify.info(
            "setOutfitDB avId=%s invIds=%s" % (self.doId, list(desiredOutfit.values()))
        )

        table = self.air.mongoInterface.mongodb.fairies
        fairy = table.find_one({"_id": self.doId})

        if not fairy:
            return

        dirty = False
        equipped_from_mongo: set[int] = set()

        for item in fairy["avatar"]["items"]:
            invId = item["inv_id"]

            if invId in equippedIds:
                slot = equippedIds[invId]
                changed = item["location"] != "Equipped" or item["slot"] != slot
                item["location"] = "Equipped"
                item["slot"] = slot
                equipped_from_mongo.add(slot)

                if changed:
                    dirty = True
                    payload = [invId, item["item_id"], item["color1"], item["color2"]]
                    self.sendUpdate(SLOT_METHODS[slot], [payload])

            elif item["location"] == "Equipped":
                oldSlot = item["slot"]
                item["location"] = "Wardrobe"
                item["slot"] = 0
                dirty = True

                if oldSlot in SLOT_METHODS and oldSlot not in filledSlots:
                    self.sendUpdate(SLOT_METHODS[oldSlot], [EMPTY_LITE_INV])

        for slot, inv_id in desiredOutfit.items():
            if not inv_id or slot in equipped_from_mongo:
                continue
            lookup = lookup_item_for_equip(self.air, self.doId, inv_id)
            if lookup is None:
                notify.warning(
                    "setOutfitDB missing item avId=%s slot=%s invId=%s"
                    % (self.doId, slot, inv_id)
                )
                continue
            payload = [
                inv_id,
                lookup["item_id"],
                lookup["color1"],
                lookup["color2"],
            ]
            self.sendUpdate(SLOT_METHODS[slot], [payload])
            dirty = True

        if dirty:
            table.update_one(
                {"_id": self.doId},
                {"$set": {"avatar.items": fairy["avatar"]["items"]}},
            )

            self.redrawFairy()

    def setHotspotTriggered(self, hotspotId, hotspotFrame) -> None:
        if not (meadow := self.air.zoneToMeadow.get(self.zoneId)):
            return

        if self.zoneId == 100 and hotspotId in (0, 10): # CBH TTT Reset
            for id in range(hotspotId + 1, hotspotId + 10):
                meadow.sendUpdate("setHotspotFrame", [id, CBH_TTT_RESET_FRAME])
            hotspotFrame = CBH_TTT_RESET_FRAME

        meadow.sendUpdate("setHotspotFrame", [hotspotId, hotspotFrame])

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

    def setMoreOptions(self, options: str) -> None:
        options = normalize_more_options(options)
        self.moreOptions = options
        persist_more_options(self.air, self.doId, options)
        self.d_setMoreOptions(options)

    def getMoreOptions(self) -> str:
        return self.moreOptions

    def d_setMoreOptions(self, options: str) -> None:
        self.sendUpdate("setMoreOptions", [options])

    def addGold(self, deltaGold: int) -> None:
        self.b_setGold(deltaGold + self.getGold())

    def takeGold(self, deltaGold: int) -> bool:
        totalGold = self.gold

        if deltaGold > totalGold:
            return False

        self.b_setGold(self.gold - deltaGold)

        return True

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
        self._refresh_gold_trade_window()

        remaining = DAILY_GOLD_TRADE_CAP - self.amountGoldTradedToday
        if remaining <= 0 or amountToGet <= 0 or amountToGet > remaining:
            self._sync_daily_gold_trade_cap()
            return

        if not self.air.inventoryManager.removeIngredientsFromPouch(self.doId, invItemToGive, amountToGive):
            print("tradeItem - Couldn't Remove Ingredients??")
            return

        self.addGold(amountToGet)
        self.amountGoldTradedToday += amountToGet
        self._persist_gold_trade_state()
        self._sync_daily_gold_trade_cap()
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

    def donateItem(self, itemId: int, amount: int) -> None:
        if amount <= 0:
            return

        if not self.air.inventoryManager.removeIngredientsFromPouch(self.doId, itemId, amount):
            self.notify.debug(
                f"donateItem failed avId={self.doId} itemId={itemId} amount={amount}"
            )
            return

        self.d_syncPouchAfterChanges()

    def auraRemover(self, task):
        self.sendUpdateToAvatarId(self.doId, "setAura", [0])

    def invisRemover(self, task):
        self.sendUpdateToAvatarId(self.doId, "setRenderEffects", [0])
        self.sendUpdateToAvatarId(self.doId, "setRedraw", [1])

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
        aura_id = AURA_MAPPING[itemId]
        self.sendUpdateToAvatarId(self.doId, "setAura", [aura_id])

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
        self.sendUpdateToAvatarId(self.doId, "setRenderEffects", [1])
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

        self.sendUpdateToAvatarId(self.doId, "setItemEvent", [itemId, amount, 0, 0])
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
        old_level = self.getLevel()
        self.setLevel(level)
        self.d_setLevel(level)
        if level != old_level:
            self._invalidate_peer_level_pushed_for_avatar(self.doId, old_level)
            if self.zoneId:
                self._sync_zone_peer_profile_state(include_level=True)

    def publish_loaded_level(self, level: int | None = None) -> None:
        """Apply Mongo talent level to AI state and the owner client.

        Peer meadow clients receive talent level lazily (requestFairyInfo or a
        real b_setLevel), not on zone enter — targeted setLevel triggers the
        client level-up animation on every fairy in view.
        """
        if level is None:
            level = self.getLevel()
        level = int(level or 0)
        if level <= 0:
            return

        if self.getLevel() != level:
            self.setLevel(level)

        self.sendUpdateToAvatarId(self.doId, "setLevel", [level])

    def getLevel(self) -> int:
        return self.level

    def _invalidate_peer_level_pushed_for_avatar(
        self, avatar_id: int, level: int | None = None
    ) -> None:
        pushed = getattr(self.air, "peerLevelPushed", None)
        if not pushed:
            return
        if level is None:
            stale = [key for key in pushed if key[1] == avatar_id]
        else:
            stale = [key for key in pushed if key[1] == avatar_id and key[2] == level]
        for key in stale:
            pushed.discard(key)

    def _clear_peer_level_pushed_for_viewer(self, viewer_id: int) -> None:
        pushed = getattr(self.air, "peerLevelPushed", None)
        if not pushed:
            return
        for key in [entry for entry in pushed if entry[0] == viewer_id]:
            pushed.discard(key)

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
            fairyLevel = self._peer_talent_level_for_profile(fairy)

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
            self._push_access_to_avatar(self.doId, fairy)
            self._push_peer_more_options_to_avatar(self.doId, fairy)
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

    def teleportRequestTo(self, fairyId: int) -> None:
        def gotFairyLocation(doId: int, parentId: int, zoneId: int) -> None:
            if fairyId != doId:
                self.notify.warning(f"Got unexpected location for doId {doId}, was expecting {fairyId}!")
                return

            # TODO: Implement these
            available: bool = True
            roomId: int = 0

            self.sendUpdateToAvatarId(self.doId, "teleportResponse", [
                fairyId,
                available,
                parentId,
                zoneId,
                roomId
            ])

        fairy = self.air.getDo(fairyId)

        if fairy:
            # This fairy is present on this shard, no need to query location from OTP server.
            gotFairyLocation(fairyId, fairy.parentId, fairy.zoneId)
            return

        # Dispatch a request to the OTP server to find out where this fairy is.
        self.air.getObjectLocation(fairyId, gotFairyLocation)

    def setWhisperSCEmoteTo(self, toId: int, emoteId: int) -> None:
        channelId = self.GetPuppetConnectionChannel(toId)

        fromId = self.doId

        self.air.sendUpdateToChannelFrom(self, channelId, "setWhisperSCEmoteFrom", fromId, [fromId, emoteId])

    def removeFromInventory(self, invId, itemId):
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"_id": self.doId, "avatar.items.inv_id": invId},
            {"avatar.items.$": 1},
        )
        if not fairy or not fairy.get("avatar", {}).get("items"):
            return

        location = fairy["avatar"]["items"][0].get("location") or ""
        track_key = None
        if location in ("Wardrobe", "Equipped"):
            track_key = "wardrobe"
        elif location == "Storage":
            track_key = "storage"
        else:
            return

        result = self.air.mongoInterface.mongodb.fairies.update_one(
            {"_id": self.doId},
            {
                "$pull": {
                    "avatar.items": {
                        "inv_id": invId
                    }
                }
            },
        )
        if result.modified_count == 0:
            return

        if track_key == "storage":
            self.air.inventoryManager.sendUpdateToAvatarId(
                self.doId, "storageRemove", [0, invId]
            )
        else:
            self.air.inventoryManager.sendUpdateToAvatarId(
                self.doId, "wardrobeRemove", [0, invId]
            )

        badge_manager = getattr(self.air, "badgeManager", None)
        if badge_manager is not None:
            badge_manager.applyLeafJournalDonation(self.doId, track_key, 1)

    def requestGlobalPurchase(self, item):
        glblp_id, _qty = item[0]

        if glblp_id == SAVED_OUTFIT_SLOT_ITEM_ID:
            notify.info(
                "requestGlobalPurchase outfit slot avId=%s qty=%s"
                % (self.doId, _qty)
            )
            self._handle_outfit_slot_purchase()
            return

        if not self.takeGold(_qty):
            self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [0])
            return

        self.sendUpdateToAvatarId(self.doId, "setGlobalPurchase", [1])

    def requestSendUpdateFairyName(self, name):
        self.b_setName(name)
        self.sendUpdateToAvatarId(self.doId, "setRedraw", [1])

    def setTeleportComplete(self) -> None:
        av_id = self.air.getAvatarIdFromSender()
        if av_id != self.doId:
            self.notify.warning(
                f"setTeleportComplete from {av_id} but sender DO is {self.doId}"
            )
            return

        badge_manager = getattr(self.air, "badgeManager", None)
        if badge_manager is not None:
            badge_manager.applyMeadowVisit(self.doId, self.zoneId)

        if self.zoneId in ALL_EXPLORER_ZONE_IDS:
            self.sendUpdate("setLastMeadow", [self.zoneId])

        self._sync_zone_peer_profile_state()

    def _peer_talent_level_for_profile(self, peer) -> int:
        """Return talent level for profile/responseFairyInfo without setLevel push."""
        if not isinstance(peer, DistributedFairyPlayerAI):
            return 0

        level = peer.getLevel()
        if level > 0:
            return level

        docs = self.air.mongoInterface.retrieveDocs(
            "fairies", peer.doId, queryField="_id"
        )
        doc = docs[0] if docs else {}
        mongo_level = int(doc.get("level") or 0)
        if mongo_level > 0:
            peer.setLevel(mongo_level)
        return mongo_level

    def _push_access_to_avatar(self, viewer_id: int, peer) -> None:
        if viewer_id <= 0 or not isinstance(peer, DistributedFairyPlayerAI):
            return
        peer.sendUpdateToAvatarId(viewer_id, "setAccess", [peer.getAccess()])

    def _push_level_to_avatar(self, viewer_id: int, peer) -> None:
        if viewer_id <= 0 or not isinstance(peer, DistributedFairyPlayerAI):
            return

        level = peer.getLevel()
        if level <= 0:
            return

        pushed = getattr(self.air, "peerLevelPushed", None)
        if pushed is None:
            pushed = set()
            self.air.peerLevelPushed = pushed

        key = (viewer_id, peer.doId, level)
        if key in pushed:
            return

        peer.sendUpdateToAvatarId(viewer_id, "setLevel", [level])
        pushed.add(key)

    def _push_peer_more_options_to_avatar(self, viewer_id: int, peer) -> None:
        if viewer_id <= 0 or not isinstance(peer, DistributedFairyPlayerAI):
            return
        options = peer.getMoreOptions() or MORE_OPTIONS_EMPTY
        peer.sendUpdateToAvatarId(viewer_id, "setMoreOptions", [options])

    def _zone_fairy_peers(self) -> list:
        peers = []
        zone_map = getattr(self.air, "zoneToMeadow", None)
        my_meadow = zone_map.get(self.zoneId) if zone_map else None
        for do in self.air.doId2do.values():
            if do is self or not isinstance(do, DistributedFairyPlayerAI):
                continue
            if do.zoneId == self.zoneId:
                peers.append(do)
                continue
            if my_meadow is not None and zone_map.get(do.zoneId) is my_meadow:
                peers.append(do)
        return peers

    def _sync_zone_peer_profile_state(self, include_level: bool = False) -> None:
        """Push meadow profile fields to zone peers (setAccess, setMoreOptions).

        Client DC fields are ownrecv-only; targeted updates let other players
        open profiles with correct badge tab visibility (velvetRope).

        setLevel is omitted by default because the client plays the level-up
        animation on every post-generate setLevel. Push levels only on actual
        level changes (include_level=True) or via requestFairyInfo.
        """
        if not self.zoneId:
            return

        options = self.getMoreOptions() or MORE_OPTIONS_EMPTY
        viewer_id = self.doId
        for peer in self._zone_fairy_peers():
            self._push_peer_more_options_to_avatar(viewer_id, peer)
            peer.sendUpdateToAvatarId(viewer_id, "setMoreOptions", [options])
            self._push_access_to_avatar(self.doId, peer)
            self._push_access_to_avatar(peer.doId, self)
            if include_level:
                self._push_level_to_avatar(self.doId, peer)
                self._push_level_to_avatar(peer.doId, self)
