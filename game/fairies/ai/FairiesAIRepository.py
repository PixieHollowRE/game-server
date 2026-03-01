from typing import Dict, List

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from game.fairies.ai.FairiesAIMsgTypes import *
from game.fairies.ai.DatabaseObject import DatabaseObject
from game.fairies.fairy.DistributedFairyPlayerAI import DistributedFairyPlayerAI
from game.fairies.distributed.FairiesRealmAI import FairiesRealmAI
from game.fairies.distributed.FairiesGlobals import *
from game.fairies.distributed.MongoInterface import MongoInterface
from game.fairies.meadow.DistributedMeadowAI import DistributedMeadowAI
from game.fairies.minigame import MinigameConstants
from game.fairies.minigame.DistributedTalentMinigameAI import DistributedTalentMinigameAI
from game.fairies.gateway.DistributedGatewayAI import DistributedGatewayAI
from game.fairies.gateway.GatewayConstants import GATEWAYS
from game.fairies.fairy.npc.DistributedFairyQuestNPCAI import DistributedFairyQuestNPCAI
from game.fairies.fairy.npc.DistributedFairyShopkeeperNPCAI import DistributedFairyShopkeeperNPCAI
from game.fairies.fairy import FamousFairyData
from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesMagicWordManagerAI import FairiesMagicWordManagerAI
from game.fairies.shop.ShopConstants import SHOPS
from game.fairies.shop.ShopData import SHOPDATA
from game.otp.ai.AIDistrict import AIDistrict
from game.otp.server.ServerBase import ServerBase
from game.otp.server.ServerGlobals import PIXIE_HOLLOW


class FairiesAIRepository(AIDistrict, ServerBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("FairiesAIRepository")

    def __init__(self, *args, **kw):
        AIDistrict.__init__(self, *args, **kw)
        ServerBase.__init__(self)

        self.mongoInterface = MongoInterface(self)

        self.staffMembers: List[int] = []
        self.accountMap: Dict[int, str] = {}

        for dclassName in self.dclassesByName:
            dclass = self.dclassesByName[dclassName]

            if not dclass.isStruct():
                print(dclass.getName(), dclass.getNumber())

        print(self.dclassesByName["DistributedFairyBase"].getFieldByName("setName"))

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

        for zoneId in ZoneConstants.GAMES_ZONE_LIST:
            minigame = DistributedTalentMinigameAI(self)
            minigame.setGameID(MinigameConstants.getGameIdForZone(zoneId))
            minigame.generateWithRequired(zoneId)

        for zoneId in ZoneConstants.SHOPS_ZONE_LIST + ZoneConstants.MEADOW_ZONES_LIST:
            meadow = DistributedMeadowAI(self)
            meadow.generateWithRequired(zoneId)

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

        # DistributedFairyQuestNPC testing
        tutorialTerence = DistributedFairyQuestNPCAI(self)
        tutorialTerence.setName(str(FamousFairyData.TERENCE_DO_ID))
        tutorialTerence.setFairyDNA(FamousFairyData.TERENCE_DNA)
        tutorialTerence.setFamousFairyId(FamousFairyData.FAMOUS_FAIRY_TERENCE)
        tutorialTerence.setQuestGiverId(FamousFairyData.TERENCE_DO_ID)
        tutorialTerence.setRoomID(1)
        tutorialTerence.generateWithRequired(ZoneConstants.PIXIE_DUST_MILL)

        tinkerbellQuest = DistributedFairyQuestNPCAI(self)
        tinkerbellQuest.setName(str(FamousFairyData.TINKERBELL_DO_ID))
        tinkerbellQuest.setFairyDNA(FamousFairyData.TINKERBELL_DNA)
        tinkerbellQuest.setFamousFairyId(FamousFairyData.FAMOUS_FAIRY_TINKERBELL)
        tinkerbellQuest.setQuestGiverId(FamousFairyData.TINKERBELL_DO_ID)
        tinkerbellQuest.setRoomID(1)
        tinkerbellQuest.generateWithRequired(ZoneConstants.TINKERS_NOOK)

        TEST_SHOP_DATA = [
            (
                1, # collectionId
                1, # currencyId (COLLECTION_CURRENCYSUPPORT_BOTH)
                [ # items
                (
                    77515, # itemId (Pink Bunny Ears)
                    100, # goldPrice
                    0, # color1
                    0, # color2
                    1, # itemCount
                    0, # specialType
                    100, # price
                    0, # status
                    0, # howAcquired
                    100 # memberGoldPrice
                )
                ],
                [ # outfits
                ]
            )
        ]

        for zone, shopConfig in SHOPS.items():
            shopData = SHOPDATA.get(zone, TEST_SHOP_DATA)
            shop = DistributedFairyShopkeeperNPCAI(self)
            shop.setShopId(shopConfig["shopID"])
            shop.setName(shopConfig["name"])
            shop.setFairyDNA(shopConfig["fairyDNA"])
            shop.setPosition(shopConfig["position"][0], shopConfig["position"][1])
            shop.setFamousFairyId(shopConfig["famousFairyID"])
            shop.setRoomID(1)
            shop.setShopItems(shopData)
            shop.generateWithRequired(zone)

        self.badgeManager = self.generateGlobalObject(OTP_DO_ID_FAIRIES_BADGE_MANAGER, "FairiesBadgeManager")

        # The Magic Word Manager
        self.magicWordManager = FairiesMagicWordManagerAI(self)
        self.magicWordManager.generateOtpObject(
            self.getGameDoId(), COMMUNITY_ALERTS_ALL,
            doId=self.allocateChannel())

        self.setAIReceiver(self.magicWordManager.getDoId(), self.ourChannel)

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
        dbo.readObject(fairyPlayer, [])

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
