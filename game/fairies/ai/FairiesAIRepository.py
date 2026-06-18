from typing import Dict, List

from direct.directnotify import DirectNotifyGlobal
from game.fairies.ai.FairiesAIMsgTypes import *
from game.fairies.ai.DatabaseObject import DatabaseObject
from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI
from game.fairies.distributed.FairiesRealmAI import FairiesRealmAI
from game.fairies.distributed.FairiesGlobals import *
from game.fairies.distributed.MongoInterface import MongoInterface
from game.fairies.meadow.DistributedMeadowAI import DistributedMeadowAI
from game.fairies.meadow.IngredientSpawnMgrAI import IngredientSpawnMgrAI
from game.fairies.minigame import MinigameConstants
from game.fairies.minigame.DistributedTalentMinigameAI import DistributedTalentMinigameAI
from game.fairies.minigame.DistributedCraftingMinigameAI import DistributedCraftingMinigameAI
from game.fairies.gateway.DistributedGatewayAI import DistributedGatewayAI
from game.fairies.gateway.GatewayConstants import GATEWAYS
from game.fairies.fairy.npc.DistributedFairyQuestNPCAI import DistributedFairyQuestNPCAI
from game.fairies.fairy.npc.DistributedFairyShopkeeperNPCAI import DistributedFairyShopkeeperNPCAI
from game.fairies.minigame.DistributedMatchGameAI import DistributedMatchGameAI
from game.fairies.fairy import FamousFairyData
from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesMagicWordManagerAI import FairiesMagicWordManagerAI
from game.fairies.ai.PetMgrAI import PetMgrAI
from game.fairies.badges.MoreOptions import (
    normalize_more_options,
    parse_favorite_badge_from_more_options,
    persist_more_options,
    repair_more_options,
)
from game.fairies.shop.ShopData import SHOPS
from game.otp.ai.AIDistrict import AIDistrict
from game.otp.server.ServerBase import ServerBase
from game.otp.server.ServerGlobals import PIXIE_HOLLOW
from game.fairies.fairy.npc.QuestZoneData import QUEST_ZONES


class FairiesAIRepository(AIDistrict, ServerBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("FairiesAIRepository")

    def __init__(self, *args, **kw):
        AIDistrict.__init__(self, *args, **kw)
        ServerBase.__init__(self)

        self.mongoInterface = MongoInterface(self)

        self.staffMembers: List[int] = []
        self.accountMap: Dict[int, str] = {}
        self.zoneToMeadow: Dict[int, DistributedMeadowAI] = {}

    def getGameDoId(self):
        return OTP_DO_ID_FAIRIES

    def getMinDynamicZone(self):
        # Override this to return the minimum allowable value for a
        # dynamically-allocated zone id.
        return DynamicZonesBegin

    def getMaxDynamicZone(self):
        # Override this to return the maximum allowable value for a
        # dynamically-allocated zone id.

        # Note that each zone requires the use of the channel derived
        # by self.districtId + zoneId.  Thus, we cannot have any zones
        # greater than or equal to self.minChannel - self.districtId,
        # which is our first allocated doId.
        return min(self.minChannel - self.districtId, DynamicZonesEnd) - 1

    def handlePlayGame(self, msgType, di):
        AIDistrict.handlePlayGame(self, msgType, di)

    def createObjects(self):
        self.district = FairiesRealmAI(self, self.districtName)
        self.district.generateOtpObject(
                OTP_DO_ID_FAIRIES, OTP_ZONE_ID_DISTRICTS,
                doId=self.districtId)

        self.setAIReceiver(self.district.getDoId(), self.ourChannel)

        twofortea = DistributedMatchGameAI(self)
        twofortea.setGameInfo(13072, 2, 2, 0, 9)
        twofortea.generateWithRequired(ZoneConstants.THE_TEAROOM)

        for zoneId in ZoneConstants.GAMES_ZONE_LIST:
            minigame = DistributedTalentMinigameAI(self)
            minigame.setGameID(MinigameConstants.getGameIdForZone(zoneId))
            minigame.generateWithRequired(zoneId)

        for zoneId in ZoneConstants.CRAFTING_ZONE_LIST:
            crafting = DistributedCraftingMinigameAI(self)
            if zoneId in (ZoneConstants.MENDYS_TAILORING, ZoneConstants.BOBBINS_TAILORING):
                crafting.setProfessionID(0)
            elif zoneId == ZoneConstants.DULCIES_BAKING:
                crafting.setProfessionID(1)
            else:
                crafting.setProfessionID(2) # Tinkering
            crafting.generateWithRequired(zoneId)

        for zoneId in ZoneConstants.SHOPS_ZONE_LIST + ZoneConstants.MEADOW_ZONES_LIST:
            meadow = DistributedMeadowAI(self)
            meadow.generateWithRequired(zoneId)
            self.zoneToMeadow[zoneId] = meadow

        for zoneId, gateways in GATEWAYS.items():
            for gw in gateways:
                gate = DistributedGatewayAI(self)
                gate.setName(gw["name"])
                gate.setPosition(*gw["position"])
                gate.setTargetLocationName(gw["targetLocationName"])
                gate.setTargetZoneID(gw["targetZoneID"])

                if rewardList := gw.get("rewardList"):
                    gate.setRewardList(rewardList)

                gate.generateWithRequired(zoneId)

        self.ingredientSpawnMgr = IngredientSpawnMgrAI(self)
        self.ingredientSpawnMgr.start()

        # DistributedFairyQuestNPC testing
        for qzone in QUEST_ZONES:
            qgiver_ai = DistributedFairyQuestNPCAI(self)
            qzone.generate_quest_zone(qgiver_ai)

        for shop in SHOPS:
            shop_ai = DistributedFairyShopkeeperNPCAI(self)
            shop.generate_shop(shop_ai)

        self.badgeManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_BADGE_MANAGER, "FairiesBadgeManager")
        self.inventoryManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_INVENTORY_MANAGER, "FairyInventoryMgr")
        self.petManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_PET_MANAGER, "PetMgr")
        self.leaderboardManager = self.generateGlobalObject(
            OTP_DO_ID_FAIRIES_LEADERBOARD_MANAGER, "LeaderBoardMgr"
        )

        # The Magic Word Manager
        self.magicWordManager = FairiesMagicWordManagerAI(self)
        self.magicWordManager.generateOtpObject(
            self.districtId, COMMUNITY_ALERTS_ALL,
            doId=self.allocateChannel())

        # mark district as avaliable
        self.district.b_setAvailable(1)

        if self.isProdServer():
            # Register us with the API server
            self.sendPopulation()

        self.notify.info("Ready!")

    def updateShard(self):
        if self.isProdServer():
            # This is the production server.
            # Send our population update.
            self.sendPopulation()

        # Update the population on the district (realm) as well.
        self.district.updatePopulationLevel()

    def fillInFairyPlayer(self, fairyPlayer) -> None:
        dbo = DatabaseObject(self, fairyPlayer.doId)
        # Add more fields if needed. (Good spot to look if the field you want
        # is an ownrequired field, but no required or ram.)
        dbo.readObject(fairyPlayer, ["setGold"])

        docs = self.mongoInterface.retrieveDocs(
            "fairies", fairyPlayer.doId, queryField="_id"
        )
        doc = docs[0] if docs else {}
        spin_day = int(doc.get("dailyChanceLastSpinDay") or 0)
        fairyPlayer.setDailyChanceLastSpinDay(spin_day)

        fairyPlayer.amountGoldTradedToday = int(doc.get("amountGoldTradedToday") or 0)
        fairyPlayer.goldTradeResetAt = int(doc.get("goldTradeResetAt") or 0)
        fairyPlayer._refresh_gold_trade_window()

        earned_badge_ids = {
            int(entry["badgeId"]) for entry in (doc.get("earnedBadges") or [])
        }
        raw_more_options = doc.get("moreOptions") or ""
        more_options = normalize_more_options(raw_more_options)
        more_options = repair_more_options(
            more_options,
            favorite_badge_id=int(doc.get("favoriteBadgeId") or 0),
            earned_badge_ids=earned_badge_ids,
        )
        if (
            more_options != normalize_more_options(raw_more_options)
            or parse_favorite_badge_from_more_options(more_options)
            != int(doc.get("favoriteBadgeId") or 0)
        ):
            persist_more_options(fairyPlayer.air, fairyPlayer.doId, more_options)

        fairyPlayer.moreOptions = more_options
        fairyPlayer.d_setMoreOptions(more_options)

        mongo_level = int(doc.get("level") or 0)
        fairyPlayer.publish_loaded_level(mongo_level)

    def readFairyPlayer(self, fairyPlayerId, fields = None, doneEvent = '') -> DistributedFairyPlayerAI:
        dbo = DatabaseObject(self, fairyPlayerId, doneEvent)
        return dbo.readFairyPlayer(fields)

    def sendPopulation(self):
        data = {
            'token': config.GetString('api-token'),
            'population': self.getPopulation(),
            'serverType': PIXIE_HOLLOW,
            'shardName': self.districtName,
            'shardId': self.districtId
        }

        headers = {
            'User-Agent': 'Sunrise Games - FairiesAIRepository'
        }

        try:
            requests.post('https://api.sunrise.games/api/setPopulation', json=data, headers=headers)
        except:
            self.notify.warning('Failed to send district population!')

    def incrementPopulation(self):
        AIDistrict.incrementPopulation(self)
        self.updateShard()

    def decrementPopulation(self):
        AIDistrict.decrementPopulation(self)
        self.updateShard()

    def setAllowModerationActions(self, accountId: int, accountType: str) -> None:
        if accountId not in self.staffMembers:
            self.staffMembers.append(accountId)
            self.accountMap[accountId] = accountType
