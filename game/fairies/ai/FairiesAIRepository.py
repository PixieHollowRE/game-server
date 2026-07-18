from typing import Dict, List

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from game.fairies.ai.FairiesAIMsgTypes import *
from game.fairies.ai.DatabaseObject import DatabaseObject
from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI
from game.fairies.distributed.FairiesRealmAI import FairiesRealmAI
from game.fairies.distributed.FairiesGlobals import *
from game.fairies.distributed.RealmGlobals import OBJECT_TYPE_REALM
from game.fairies.housing.FairiesHomeRealmAI import FairiesHomeRealmAI
from game.fairies.distributed.MongoInterface import MongoInterface
from game.fairies.meadow.DistributedMeadowAI import DistributedMeadowAI
from game.fairies.meadow.IngredientSpawnMgrAI import IngredientSpawnMgrAI
from game.fairies.minigame import MinigameConstants
from game.fairies.minigame.DistributedTalentMinigameAI import DistributedTalentMinigameAI
from game.fairies.minigame.DistributedCraftingMinigameAI import DistributedCraftingMinigameAI
from game.fairies.gateway.DistributedGatewayAI import DistributedGatewayAI
from game.fairies.gateway.GatewayConstants import GATEWAYS, get_gateway_name
from game.fairies.fairy.npc.DistributedFairyQuestNPCAI import DistributedFairyQuestNPCAI
from game.fairies.fairy.npc.DistributedFairyShopkeeperNPCAI import DistributedFairyShopkeeperNPCAI
from game.fairies.minigame.DistributedMatchGameAI import DistributedMatchGameAI
from game.fairies.fairy import FamousFairyData
from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesMagicWordManagerAI import FairiesMagicWordManagerAI
from game.fairies.ai.PetMgrAI import PetMgrAI
from game.fairies.shop.data import SHOPS
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

        # Home realms this district AI is currently hosting, keyed by doId.
        # The RealmGuardian asks us to spawn these on demand.
        self.homeRealms: Dict[int, FairiesHomeRealmAI] = {}

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
        if msgType == REALM_GENERATE_REQUEST:
            self._handleRemoteGenerateRequest(di)
            return
        elif msgType == REALM_REGISTER_REQUEST:
            # The RealmGuardian (re)started and wants us to announce ourselves.
            self.registerWithRealmGuardian()
            return
        elif msgType == REALM_DELETE_REQUEST:
            self._handleRealmDeleteRequest(di)
            return

        AIDistrict.handlePlayGame(self, msgType, di)

    def sendRealmOccupancyUpdate(self, avatarId, ownerId):
        # Tell the RealmGuardian an avatar entered (ownerId != 0) or left
        # (ownerId == 0) a home realm, so it can tear down empty ones.
        dg = PyDatagram()
        dg.addServerHeader(OTP_DO_ID_REALM_GUARDIAN, self.ourChannel, REALM_OCCUPANCY_UPDATE)
        dg.addUint32(avatarId)
        dg.addUint32(ownerId)
        self.send(dg)

    def _handleRealmDeleteRequest(self, di):
        realmId = di.getUint32()
        realm = self.homeRealms.pop(realmId, None)
        if realm is not None:
            realm.requestDelete()
            self.notify.info("Deleted home realm %d" % realmId)

    def registerWithRealmGuardian(self):
        # Tell the RealmGuardian uberdog our district doId and AI channel so it
        # can route home-realm generate requests back to this process.
        dg = PyDatagram()
        dg.addServerHeader(OTP_DO_ID_REALM_GUARDIAN, self.ourChannel, SHARDMANAGER_ONLINE)
        dg.addUint32(self.districtId)
        dg.addChannel(self.ourChannel)
        self.send(dg)

    def _handleRemoteGenerateRequest(self, di):
        context = di.getUint32()
        objectType = di.getUint8()
        ownerId = di.getUint32()
        sender = self.getMsgSender()

        doId, parentId, zoneId = self.createRemoteObject(objectType, ownerId)

        dg = PyDatagram()
        dg.addServerHeader(sender, self.ourChannel, REALM_GENERATE_RESPONSE)
        dg.addUint32(context)
        dg.addUint32(doId)
        dg.addUint32(parentId)
        dg.addUint32(zoneId)
        self.send(dg)

    def createRemoteObject(self, objectType, ownerId):
        # Generate an object requested remotely by the RealmGuardian and return
        # (doId, parentId, zoneId). Home realms are district-siblings, so they
        # live under OTP_DO_ID_FAIRIES / OTP_ZONE_ID_DISTRICTS like a shard.
        if objectType == OBJECT_TYPE_REALM:
            realm = FairiesHomeRealmAI(self, ownerId)
            realm.generateOtpObject(
                OTP_DO_ID_FAIRIES, OTP_ZONE_ID_DISTRICTS,
                doId=self.allocateChannel())
            self.setAIReceiver(realm.getDoId(), self.ourChannel)
            realm.b_setAvailable(1)

            # Populate the realm with the owner's saved furniture.
            realm.loadHomeItems()

            self.homeRealms[realm.getDoId()] = realm
            self.notify.info(
                "Generated home realm %d for owner %d" % (realm.getDoId(), ownerId))
            return realm.getDoId(), OTP_DO_ID_FAIRIES, OTP_ZONE_ID_DISTRICTS

        self.notify.warning("createRemoteObject: unknown object type %s" % objectType)
        return 0, 0, 0

    def createObjects(self):
        self.district = FairiesRealmAI(self, self.districtName)
        self.district.generateOtpObject(
                OTP_DO_ID_FAIRIES, OTP_ZONE_ID_DISTRICTS,
                doId=self.districtId)

        self.setAIReceiver(self.district.getDoId(), self.ourChannel)

        # Two For Tea (gameId 13072) — the Tearoom has four 2-player tables that
        # all share hotspot id 27625 in the meadow XML, distinguished only by
        # tagId (7/8/9/10). The client keys each game object by the hotspot's
        # tagId (it calls activateMeadowGameLauncher(gameId, tagId) and
        # getMeadowGameByHotSpotId(tagId)), which maps to the game's hotspotId
        # field, so we spawn one independent instance per table with its
        # hotspotId set to that tagId. Positions mirror the hotspot x/y.
        # for tagId, x, y in ((7, 196, 375), (8, 364, 363), (9, 818, 361), (10, 975, 375)):
            # table = DistributedMatchGameAI(self)
            # table.setGameInfo(13072, 2, 2, 0, tagId)
            # table.setPosition(x, y)
            # table.generateWithRequired(ZoneConstants.THE_TEAROOM)

        for zoneId in ZoneConstants.GAMES_ZONE_LIST:
            minigame = DistributedTalentMinigameAI(self)
            minigame.setGameID(MinigameConstants.getGameIdForZone(zoneId))
            minigame.generateWithRequired(zoneId)

        for zoneId in ZoneConstants.CRAFTING_ZONE_LIST:
            crafting = DistributedCraftingMinigameAI(self)
            if zoneId in (ZoneConstants.MENDYS_TAILORING, ZoneConstants.BOBBINS_TAILORING):
                crafting.setProfessionID(MinigameConstants.CRAFT_TYPE_TAILORING)
            elif zoneId == ZoneConstants.DULCIES_BAKING:
                crafting.setProfessionID(MinigameConstants.CRAFT_TYPE_BAKING)
            else:  # COPPERS_TINKERING
                crafting.setProfessionID(MinigameConstants.CRAFT_TYPE_TINKERING)
            crafting.generateWithRequired(zoneId)

        for zoneId in ZoneConstants.SHOPS_ZONE_LIST + ZoneConstants.MEADOW_ZONES_LIST:
            meadow = DistributedMeadowAI(self)
            meadow.generateWithRequired(zoneId)
            self.zoneToMeadow[zoneId] = meadow

        for zoneId, gateways in GATEWAYS.items():
            for gw in gateways:
                gate = DistributedGatewayAI(self)
                gate.setName(get_gateway_name(gw["name"]))
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
        self.leaderBoardManager = self.generateGlobalObject(OTP_DO_ID_LEADERBOARD_MANAGER, "LeaderBoardMgr")

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

        # Announce ourselves to the RealmGuardian so it can spawn home realms
        # in this district AI process on demand.
        self.registerWithRealmGuardian()

        self.notify.info("Ready!")

    def updateShard(self):
        if self.isProdServer():
            # This is the production server.
            # Send our population update.
            self.sendPopulation()

        # Update the population on the district (realm) as well.
        self.district.updatePopulationLevel()

    def sendFriendManagerAccountOnline(self, accountId):
        dg = PyDatagram()
        dg.addServerHeader(OTP_DO_ID_PLAYER_FRIENDS_MANAGER, self.ourChannel, FRIENDMANAGER_ACCOUNT_ONLINE)
        dg.addUint32(accountId)
        self.send(dg)

    def sendFriendManagerAccountOffline(self, accountId):
        dg = PyDatagram()
        dg.addServerHeader(OTP_DO_ID_PLAYER_FRIENDS_MANAGER, self.ourChannel, FRIENDMANAGER_ACCOUNT_OFFLINE)
        dg.addUint32(accountId)
        self.send(dg)

    def fillInFairyPlayer(self, fairyPlayer) -> None:
        dbo = DatabaseObject(self, fairyPlayer.doId)
        # Add more fields if needed. (Good spot to look if the field you want
        # is an ownrequired field, but no required or ram.)
        dbo.readObject(fairyPlayer, ["setGold"])

        fairyPlayer.b_setDailyChancePlayed(0 if fairyPlayer.dailyChanceCanSpin() else 1)

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
