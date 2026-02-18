from typing import Dict, List

import requests
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from game.fairies.ai.FairiesAIMsgTypes import *
from game.fairies.ai.DatabaseObject import DatabaseObject
from game.fairies.carplayer.DistributedCarPlayerAI import DistributedCarPlayerAI
from game.fairies.carplayer.DistributedRaceCarAI import DistributedRaceCarAI
from game.fairies.carplayer.games.DocsClinicAI import DocsClinicAI
from game.fairies.carplayer.games.LuigisCasaDellaTiresAI import \
    LuigisCasaDellaTiresAI
from game.fairies.carplayer.games.MatersSlingShootAI import MatersSlingShootAI
from game.fairies.carplayer.npcs.MaterAI import MaterAI
from game.fairies.carplayer.npcs.RamoneAI import RamoneAI
from game.fairies.carplayer.npcs.TractorAI import TractorAI
from game.fairies.carplayer.npcs.LightningMcQueenAI import LightningMcQueenAI
from game.fairies.carplayer.shops.FillmoreFizzyFuelHutAI import \
    FillmoreFizzyFuelHutAI
from game.fairies.carplayer.shops.MackShopAI import MackShopAI
from game.fairies.carplayer.shops.SpyShopAI import SpyShopAI
from game.fairies.carplayer.zones.GenericInteractiveObjectAI import GenericInteractiveObjectAI
from game.fairies.carplayer.zones.HayBaleBombAI import HayBaleBombAI
from game.fairies.carplayer.zones.MessyMixAI import MessyMixAI
from game.fairies.carplayer.zones.RedhoodValleyAI import RedhoodValleyAI
from game.fairies.carplayer.zones.SponsorBoothAI import SponsorBoothAI
from game.fairies.carplayer.zones.WaterTowerAI import WaterTowerAI
from game.fairies.distributed.FairiesRealmAI import FairiesRealmAI
from game.fairies.distributed.FairiesGlobals import *
from game.fairies.distributed.MongoInterface import MongoInterface
from game.fairies.dungeon.DistributedTutorialDungeonAI import DistributedTutorialDungeonAI
from game.fairies.dungeon.DistributedYardAI import DistributedYardAI
from game.fairies.racing.DistributedSinglePlayerRacingLobbyAI import \
    DistributedSinglePlayerRacingLobbyAI
from game.fairies.racing.DistributedFriendsLobbyAI import \
    DistributedFriendsLobbyAI
from game.fairies.racing.DistributedCrossShardLobbyAI import \
    DistributedCrossShardLobbyAI
from game.fairies.zone import ZoneConstants
from game.otp.ai.AIDistrict import AIDistrict
from game.otp.server.ServerBase import ServerBase
from game.otp.server.ServerGlobals import WORLD_OF_CARS_ONLINE


class FairiesAIRepository(AIDistrict, ServerBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("FairiesAIRepository")

    def __init__(self, *args, **kw):
        AIDistrict.__init__(self, *args, **kw)
        ServerBase.__init__(self)

        self.mongoInterface = MongoInterface(self)

        self.staffMembers: List[int] = []
        self.accountMap: Dict[int, str] = {}

        self.shops = requests.get("http://127.0.0.1:8013/getShopItemData").json()
        self.notify.info(f"Loaded {len(self.shops)} shops item data.")

    def getShopItem(self, shopId: str, itemId: int) -> None | dict:
        for item in self.shops[shopId]:
            if item.get("itemId", 0) == itemId:
                return item

        return None

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

        # mark district as enabled
        # NOTE: Only setEnabled is used in the client
        # instead of setAvailable.
        self.district.b_setEnabled(1)

        if self.isProdServer():
            # Register us with the API server
            self.sendPopulation()

        self.notify.info("Ready!")

    def updateShard(self):
        if self.isProdServer():
            # This is the production server.
            # Send our population update.
            self.sendPopulation()

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

    def fillInCarsPlayer(self, carPlayer) -> None:
        dbo = DatabaseObject(self, carPlayer.doId)
        # Add more fields if needed. (Good spot to look if the field you want
        # is an ownrequired field, but no required or ram.)
        dbo.readObject(carPlayer, ["setCarCoins", "setYardStocks"])

    def readRaceCar(self, racecarId, fields = None, doneEvent = '') -> DistributedRaceCarAI:
        dbo = DatabaseObject(self, racecarId, doneEvent)
        return dbo.readRaceCar(fields)

    def sendPopulation(self):
        data = {
            'token': config.GetString('api-token'),
            'population': self.getPopulation(),
            'serverType': WORLD_OF_CARS_ONLINE,
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
