import xml.etree.ElementTree as ET
from dataclasses import dataclass

from direct.directnotify import DirectNotifyGlobal

from game.fairies.uberdog.HolidayManagerUD import getActiveTags
from paths import MEADOWS, XML

notify = DirectNotifyGlobal.directNotify.newCategory("meadow_xml")

# The client's per-id hotspot asset table, keyed by the `id` attribute rather
# than tagId. Only the resting frames are read out of it -- see getStopFrames.
HOTSPOT_ASSETS_XML = XML / "hotspotAssets.xml"

# MMOConstants.HOTSPOT_PLAY_AT_OFFSET. A frame at or above this tells the client
# to jump to (frame - offset) and *stop* instead of playing on from it.
PLAY_AT_OFFSET = 8000

# Hotspot.CLIENT_SKILL_ANIMATION -- the talent spots, where a fairy spends pixie
# dust to cast a talent skill rather than just clicking. They're the one kind the
# client will not re-arm on its own (MeadowHotspot.refreshUpdate has a bare
# `break` for them), so the server owes them a reset.
CLIENT_SKILL_ANIMATION = 6

# Hotspot.PLAY_TYPE_FULL / PLAY_TYPE_KEYFRAME. The client reads anything that
# isn't the literal "full" as keyframe, so this parses the same way.
PLAY_TYPE_FULL = 0
PLAY_TYPE_KEYFRAME = 1

# The frame a full-play hotspot is told to play from: MMOConstants has no name
# for it, playHotspotServer just tests `frame == -1`.
PLAY_FROM_START = -1


@dataclass(frozen=True)
class HotspotDef:
    tagId: int
    hotspotId: int
    shared: bool
    clientTrigger: int
    playType: int
    refreshMs: int
    # (tagId, frame) pairs from <resets>, in document order.
    resets: tuple[tuple[int, int], ...]

    @property
    def isTalentSpot(self) -> bool:
        return self.clientTrigger == CLIENT_SKILL_ANIMATION

    @property
    def playsFull(self) -> bool:
        return self.playType == PLAY_TYPE_FULL

    @property
    def rewindsItself(self) -> bool:
        """
        Whether the client walks this one back to frame 1 without being told.

        refreshUpdate does `_content.playBackwards()` for a full-play hotspot
        once its refresh timer runs out, so its resting state is frame 1 -- the
        same place a newcomer's clip starts. Worth knowing before recording a
        frame to replay at arrivals.
        """
        return self.playsFull and self.refreshMs > 0


@dataclass(frozen=True)
class _RawHotspot:
    """One <hotspot> row before seasonal tags are applied."""
    definition: HotspotDef
    tags: frozenset[str]
    excludingTags: frozenset[str]


_rawByZone: dict[int, tuple[_RawHotspot, ...]] = {}
_resolvedByZoneAndTags: dict[tuple[int, tuple[str, ...]], dict[int, HotspotDef]] = {}


def _splitTags(value: str | None) -> frozenset[str]:
    if not value:
        return frozenset()

    return frozenset(tag for tag in (part.strip() for part in value.split(",")) if tag)


def _refreshMs(value: str | None) -> int:
    # Hotspot.as: `int(Number(@refresh) * 1000)`, or -1 when the attribute is
    # absent. Seconds in the file, milliseconds everywhere in the client.
    if value is None:
        return -1

    try:
        return int(float(value) * 1000)
    except ValueError:
        return -1


def _parseResets(element) -> tuple[tuple[int, int], ...]:
    resets = []

    for reset in element.iterfind("resets/reset"):
        hsId, keyframe = reset.get("hsId"), reset.get("keyframe")

        if hsId is None or not hsId.isdigit() or keyframe is None or not keyframe.isdigit():
            notify.warning(f"unusable <reset> under hotspot {element.get('tagId')}: "
                           f"hsId={hsId} keyframe={keyframe}")
            continue

        resets.append((int(hsId), int(keyframe)))

    return tuple(resets)


def _parse(path) -> tuple[_RawHotspot, ...]:
    root = ET.parse(path).getroot()

    hotspotsNode = root.find("hotspots")
    if hotspotsNode is None:
        return ()

    raws = []
    for element in hotspotsNode.iter("hotspot"):
        tagId = element.get("tagId")
        if tagId is None or not tagId.lstrip("-").isdigit():
            continue

        raws.append(_RawHotspot(
            definition=HotspotDef(
                tagId=int(tagId),
                hotspotId=int(element.get("id") or 0),
                # Util.toboolean, which the client runs this attribute through,
                # accepts either spelling.
                shared=element.get("shared") in ("true", "1"),
                clientTrigger=int(element.get("clientTrigger") or 0),
                playType=(PLAY_TYPE_FULL if element.get("playType") == "full"
                          else PLAY_TYPE_KEYFRAME),
                refreshMs=_refreshMs(element.get("refresh")),
                resets=_parseResets(element),
            ),
            tags=_splitTags(element.get("tags")),
            excludingTags=_splitTags(element.get("excludingTags")),
        ))

    return tuple(raws)


def _getRaw(zoneId: int) -> tuple[_RawHotspot, ...]:
    if zoneId in _rawByZone:
        return _rawByZone[zoneId]

    path = MEADOWS / f"zone{zoneId}" / "config.xml"

    try:
        raws = _parse(path)
    except FileNotFoundError:
        # Not every zone the AI hosts is a meadow with scene data on disk, and a
        # missing file should cost the zone its hotspots, not the district.
        notify.warning(f"no meadow config for zone {zoneId} at {path}")
        raws = ()
    except ET.ParseError as e:
        notify.warning(f"could not parse meadow config for zone {zoneId}: {e}")
        raws = ()

    _rawByZone[zoneId] = raws
    return raws


def _resolve(raws: tuple[_RawHotspot, ...], activeTags: frozenset[str]) -> dict[int, HotspotDef]:
    # MeadowContent.as:317-366, in document order: a tagged row wins its tagId
    # whenever one of its tags is live, overriding anything claimed earlier; an
    # untagged row only fills a tagId nothing has claimed yet, and steps aside
    # entirely if one of its excludingTags is live.
    resolved: dict[int, HotspotDef] = {}

    for raw in raws:
        if raw.tags:
            if raw.tags & activeTags:
                resolved[raw.definition.tagId] = raw.definition
        elif raw.definition.tagId not in resolved and not (raw.excludingTags & activeTags):
            resolved[raw.definition.tagId] = raw.definition

    return resolved


def getHotspots(zoneId: int) -> dict[int, HotspotDef]:
    """The hotspots live in this zone right now, keyed by tagId."""
    activeTags = tuple(sorted(getActiveTags()))
    key = (zoneId, activeTags)

    if key not in _resolvedByZoneAndTags:
        _resolvedByZoneAndTags[key] = _resolve(_getRaw(zoneId), frozenset(activeTags))

    return _resolvedByZoneAndTags[key]


def getHotspot(zoneId: int, tagId: int) -> HotspotDef | None:
    return getHotspots(zoneId).get(tagId)


_stopFrames: dict[int, tuple[int, ...]] | None = None


def getStopFrames(hotspotId: int) -> tuple[int, ...]:
    """
    The frames a hotspot's movieclip comes to rest on, from hotspotAssets.xml.

    Diagnostic only -- nothing here drives a decision. It's the client's own
    statement of where an animation lands, which is what you need in front of you
    when a hotspot is stopping somewhere it shouldn't: the frames the server
    hands out should be values from this list, and one that isn't means a client
    reported its clip mid-animation and the whole zone got sent there.

    Empty for most hotspots -- 31 ids declare the attribute, and the rest rely on
    stop() actions baked into the .swf timeline, which isn't readable from here.
    """
    global _stopFrames

    if _stopFrames is None:
        _stopFrames = {}

        try:
            root = ET.parse(HOTSPOT_ASSETS_XML).getroot()
        except (FileNotFoundError, ET.ParseError) as e:
            notify.warning(f"could not read {HOTSPOT_ASSETS_XML}: {e}")
            root = None

        if root is not None:
            for element in root.iter("hotspot"):
                frames = element.get("stopFrames")
                assetId = element.get("id")

                if not frames or not assetId or not assetId.isdigit():
                    continue

                _stopFrames[int(assetId)] = tuple(
                    int(part) for part in frames.split(",") if part.strip().isdigit()
                )

    return _stopFrames.get(hotspotId, ())
