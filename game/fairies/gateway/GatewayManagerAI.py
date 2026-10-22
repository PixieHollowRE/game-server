"""
Keeps the district's DistributedGateways in step with the live holiday tags.

Gateways used to be generated once at startup. Now they are regenerated whenever
the tag set moves: a gateway whose fields changed is deleted and re-created
rather than patched in place, because the client derives its sign art from the
name at generate time and a live setName would leave the old art up.

Started once by FairiesAIRepository.createObjects().
"""

from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

from game.fairies.gateway.DistributedGatewayAI import DistributedGatewayAI
from game.fairies.gateway.GatewayConstants import get_gateway_name
from game.fairies.gateway.GatewayResolver import resolve_gateways
from game.fairies.uberdog.HolidayManagerUD import getActiveTags

# Tags only move with the clock (season, holiday windows), so this can be lazy.
POLL_SECONDS = 60.0

_Key = tuple[int, int]


class GatewayManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory("GatewayManagerAI")
    taskName = "gatewayManagerPoll"

    def __init__(self, air) -> None:
        self.air = air
        self.live: dict[_Key, tuple[tuple, DistributedGatewayAI]] = {}

    def start(self) -> None:
        self.refresh()
        taskMgr.doMethodLater(POLL_SECONDS, self._poll, self.taskName)

    def stop(self) -> None:
        taskMgr.remove(self.taskName)

    def _poll(self, task):
        self.refresh()
        return Task.again

    def refresh(self) -> None:
        tags = tuple(sorted(getActiveTags()))
        wanted: dict[_Key, tuple[dict, tuple]] = {}

        for zoneId, entries in resolve_gateways(tags).items():
            for gw in entries:
                wanted[(zoneId, gw["targetZoneID"])] = (gw, self._signature(gw))

        for key in [k for k in self.live if k not in wanted]:
            self._remove(key)

        for key, (gw, signature) in wanted.items():
            current = self.live.get(key)

            if current is not None and current[0] == signature:
                continue

            if current is not None:
                self._remove(key)

            self._spawn(key, gw, signature)

    @staticmethod
    def _signature(gw: dict) -> tuple:
        return (
            get_gateway_name(gw["name"]),
            tuple(gw["position"]),
            gw["targetLocationName"],
            tuple(gw.get("rewardList", ())),
        )

    def _spawn(self, key: _Key, gw: dict, signature: tuple) -> None:
        self.notify.debug("Spawning gateway %s" % (key,))
        gate = DistributedGatewayAI(self.air)
        gate.setName(signature[0])
        gate.setPosition(*gw["position"])
        gate.setTargetLocationName(gw["targetLocationName"])
        gate.setTargetZoneID(gw["targetZoneID"])

        if rewardList := gw.get("rewardList"):
            gate.setRewardList(rewardList)

        gate.generateWithRequired(key[0])
        self.live[key] = (signature, gate)

    def _remove(self, key: _Key) -> None:
        _, gate = self.live.pop(key)
        gate.requestDelete()
