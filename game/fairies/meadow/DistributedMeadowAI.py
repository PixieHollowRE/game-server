from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.fairy.structs.HotspotState import HotspotState
from game.fairies.meadow import meadow_xml
from game.fairies.meadow.meadow_xml import PLAY_AT_OFFSET

# How long a talent spot stays spent before it re-arms itself.
TALENT_SPOT_RESET_SECS = 300.0 # 5 minutes
TALENT_SPOT_RESET_FRAME = PLAY_AT_OFFSET + 1

class DistributedMeadowAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMeadowAI")

    def __init__(self, air) -> None:
        super().__init__(air)

        self.assetURL: str = ""
        self.crowdBarriers: int = 0

        # The last frame broadcast for each hotspot, keyed by tagId.
        self.hotspotFrames: dict[int, int] = {}

        # tagIds with a re-arm queued, so delete() can drop the tasks.
        self.pendingResets: set[int] = set()

    def delete(self) -> None:
        for tagId in tuple(self.pendingResets):
            self.cancelReset(tagId)

        super().delete()

    def setAssetURL(self, assetURL: str) -> None:
        self.assetURL = assetURL

    def getAssetURL(self) -> str:
        return self.assetURL

    def setCrowdBarriers(self, crowdBarriers: int) -> None:
        self.crowdBarriers = crowdBarriers

    def getCrowdBarriers(self) -> int:
        return self.crowdBarriers

    def d_setHotspotFrame(self, tagId: int, frame: int) -> None:
        hotspot = meadow_xml.getHotspot(self.zoneId, tagId)
        previous = self.hotspotFrames.get(tagId)

        if hotspot is not None and hotspot.rewindsItself:
            # This one walks itself back to frame 1 a few seconds from now, which
            # is where an arriving fairy's clip already is. Remembering the frame
            # would only mean replaying the animation at latecomers who missed it.
            self.hotspotFrames.pop(tagId, None)
        else:
            self.hotspotFrames[tagId] = frame

        if self.notify.getDebug():
            self.notify.debug(
                f"zone {self.zoneId} hotspot {tagId}: sending {frame} "
                f"({self._describeFrame(tagId, frame)}), was {previous}"
            )

        self.sendUpdate("setHotspotFrame", [tagId, frame])

        # A talent spot goes dead the moment it's cast on -- the client disables
        # the target and never re-enables it by itself -- so anything that moves
        # one starts the clock on putting it back. The reset send lands here too,
        # and must not wind the clock up again.
        if hotspot is not None and hotspot.isTalentSpot and frame != TALENT_SPOT_RESET_FRAME:
            self.scheduleReset(tagId)

    def resetTaskName(self, tagId: int) -> str:
        return f"HotspotReset-{self.doId}-{tagId}"

    def scheduleReset(self, tagId: int, delay: float = TALENT_SPOT_RESET_SECS) -> None:
        # Re-casting before the timer runs out restarts it rather than stacking a
        # second reset, so the spot always stays spent for the full delay after
        # the *last* cast.
        taskMgr.remove(self.resetTaskName(tagId))
        self.pendingResets.add(tagId)
        taskMgr.doMethodLater(delay, self._resetTask, self.resetTaskName(tagId), extraArgs=[tagId])

    def cancelReset(self, tagId: int) -> None:
        taskMgr.remove(self.resetTaskName(tagId))
        self.pendingResets.discard(tagId)

    def _resetTask(self, tagId: int) -> int:
        self.pendingResets.discard(tagId)

        self.notify.debug(f"zone {self.zoneId} hotspot {tagId}: re-arming talent spot")

        self.d_setHotspotFrame(tagId, TALENT_SPOT_RESET_FRAME)

        return Task.done

    def _describeFrame(self, tagId: int, frame: int) -> str:
        # What the client will do with this, so the log reads the way the meadow
        # looks: MeadowView.triggerHotspot splits on PLAY_AT_OFFSET, and only the
        # low road animates -- the high road is a hard gotoAndStop.
        if frame >= PLAY_AT_OFFSET:
            return f"snap to frame {frame - PLAY_AT_OFFSET} and hold"

        if frame == -1:
            return "play from the start"

        hotspot = meadow_xml.getHotspot(self.zoneId, tagId)
        stopFrames = meadow_xml.getStopFrames(hotspot.hotspotId) if hotspot else ()

        # A frame that isn't one the clip rests on means whoever reported it was
        # mid-animation when it was read, and everyone is about to be sent into
        # the middle of a segment. Only checkable for the ids that declare
        # stopFrames; the rest keep their stops inside the .swf.
        if stopFrames and frame not in stopFrames:
            return (
                f"play on from frame {frame} -- NOT a resting frame, "
                f"expected one of {','.join(str(f) for f in stopFrames)}"
            )

        return f"play on from frame {frame}"

    def requestHotspotStates(self) -> None:
        # DistributedMeadow.afterGenerate asks for this the moment the zone comes
        # up, before the hotspot movieclips have finished loading -- MeadowView
        # parks frames for hotspots it doesn't have yet in _missedHotspotTiggers
        # and replays them on arrival, so answering immediately is fine.
        avId = self.air.getAvatarIdFromSender()

        if not avId:
            self.notify.warning("requestHotspotStates from an unknown sender")
            return

        states = []
        for tagId, frame in self.hotspotFrames.items():
            state = HotspotState()
            state.hotspotId = tagId
            state.frameId = frame
            states.append(state.asTuple())

        self.notify.debug(
            f"zone {self.zoneId}: sending {len(states)} hotspot states to "
            f"{avId} -- {dict(self.hotspotFrames)}"
        )

        self.sendUpdateToAvatarId(avId, "setHotspotStates", [avId, states])
