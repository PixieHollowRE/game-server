import xml.etree.ElementTree as ET
from dataclasses import dataclass

from direct.directnotify import DirectNotifyGlobal

from game.fairies.uberdog.HolidayManagerUD import getActiveTags
from paths import MEADOWS, XML

notify = DirectNotifyGlobal.directNotify.newCategory("meadow_xml")

# Per-id hotspot assets, keyed by `id` not tagId; only resting frames are read
HOTSPOT_ASSETS_XML = XML / "hotspotAssets.xml"

# MMOConstants.HOTSPOT_PLAY_AT_OFFSET — frames at or above it jump and stop
PLAY_AT_OFFSET = 8000

# Talent spots; the client never re-arms these itself, so the server resets them
CLIENT_SKILL_ANIMATION = 6

# Hotspot.CLIENT_CHAT_PHRASE — hidden until the server lights it via a giveaway
CLIENT_CHAT_PHRASE = 7

# Anything that isn't literally "full" is keyframe on the client too
PLAY_TYPE_FULL = 0
PLAY_TYPE_KEYFRAME = 1

# playHotspotServer just tests `frame == -1`; MMOConstants has no name for it
PLAY_FROM_START = -1

# ChatTrigger.as defaults for a missing attribute
CHAT_TRIGGER_UNSET = -1

# ChatTrigger.TYPE_*, from typeToTrigger
CHAT_TRIGGER_HOTSPOT = 1
CHAT_TRIGGER_WARDROBE = 2
CHAT_TRIGGER_STORAGE = 3
CHAT_TRIGGER_POUCH = 4


@dataclass(frozen=True)
class HotspotDef:
    tagId: int
    hotspotId: int
    shared: bool
    clientTrigger: int
    playType: int
    refreshMs: int
    # Meadow coordinates, the same space as a fairy's setPosition
    x: int
    y: int
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


@dataclass(frozen=True)
class ChatTriggerDef:
    """One <chatTrigger> row; fields the attribute omits stay CHAT_TRIGGER_UNSET."""
    # Lowercased, since the client lowercases both sides before matching
    messages: tuple[str, ...]
    typeToTrigger: int
    # The hotspot's `id` attribute, not its tagId
    itemId: int
    tagId: int
    eligibleGiveAwayId: int
    delay: int
    color1: int
    color2: int
    amount: int
    velvetRope: bool


_rawByZone: dict[int, tuple[_RawHotspot, ...]] = {}
_chatTriggersByZone: dict[int, tuple[ChatTriggerDef, ...]] = {}
_resolvedByZoneAndTags: dict[tuple[int, tuple[str, ...]], dict[int, HotspotDef]] = {}


def _splitTags(value: str | None) -> frozenset[str]:
    if not value:
        return frozenset()

    return frozenset(tag for tag in (part.strip() for part in value.split(",")) if tag)


def _refreshMs(value: str | None) -> int:
    # Hotspot.as: seconds in the file, milliseconds in the client; -1 if absent
    if value is None:
        return -1

    try:
        return int(float(value) * 1000)
    except ValueError:
        return -1


def _coordinate(value: str | None) -> int:
    # Some rows carry fractions ("238.95"); AS3 int() truncates, so this does too
    try:
        return int(float(value or 0))
    except ValueError:
        return 0


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
                # Util.toboolean accepts either spelling
                shared=element.get("shared") in ("true", "1"),
                clientTrigger=int(element.get("clientTrigger") or 0),
                playType=(PLAY_TYPE_FULL if element.get("playType") == "full"
                          else PLAY_TYPE_KEYFRAME),
                refreshMs=_refreshMs(element.get("refresh")),
                x=_coordinate(element.get("x")),
                y=_coordinate(element.get("y")),
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
        # Not every zone has scene data; a missing file costs hotspots, not the district
        notify.warning(f"no meadow config for zone {zoneId} at {path}")
        raws = ()
    except ET.ParseError as e:
        notify.warning(f"could not parse meadow config for zone {zoneId}: {e}")
        raws = ()

    _rawByZone[zoneId] = raws
    return raws


def _resolve(raws: tuple[_RawHotspot, ...], activeTags: frozenset[str]) -> dict[int, HotspotDef]:
    # MeadowContent.as:317-366, in document order: a live-tagged row overrides
    # earlier claims; an untagged row fills only unclaimed tagIds, unless excluded
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


def _intAttr(element, name: str) -> int:
    value = element.get(name)

    if value is None:
        return CHAT_TRIGGER_UNSET

    try:
        return int(value)
    except ValueError:
        notify.warning(f"unusable {name}={value!r} on <chatTrigger>")
        return CHAT_TRIGGER_UNSET


def _parseChatTriggers(path) -> tuple[ChatTriggerDef, ...]:
    root = ET.parse(path).getroot()
    triggers = []

    for element in root.iterfind("chatTriggers/chatTrigger"):
        amount = _intAttr(element, "amount")

        triggers.append(ChatTriggerDef(
            messages=tuple(
                message.lower() for message in (element.get("message") or "").split("|")
            ),
            typeToTrigger=_intAttr(element, "typeToTrigger"),
            itemId=_intAttr(element, "itemid"),
            tagId=_intAttr(element, "tagId"),
            eligibleGiveAwayId=_intAttr(element, "eligibleGiveAwayId"),
            delay=_intAttr(element, "delay"),
            color1=_intAttr(element, "setColor1"),
            color2=_intAttr(element, "setColor2"),
            # ChatTrigger.as defaults amount to 1, not unset
            amount=1 if amount == CHAT_TRIGGER_UNSET else amount,
            velvetRope=element.get("setVelvetRope", "1") in ("true", "1"),
        ))

    return tuple(triggers)


def getChatTriggers(zoneId: int) -> tuple[ChatTriggerDef, ...]:
    """
    The phrase triggers a meadow declares, in document order.

    Unlike hotspots these carry no seasonal tags; the client builds one for every
    row (MeadowContent.as:367), and what makes a trigger seasonal is that its
    hotspot is tagged, so look the hotspot up through getHotspot to find out.
    """
    if zoneId in _chatTriggersByZone:
        return _chatTriggersByZone[zoneId]

    path = MEADOWS / f"zone{zoneId}" / "config.xml"

    try:
        triggers = _parseChatTriggers(path)
    except FileNotFoundError:
        notify.warning(f"no meadow config for zone {zoneId} at {path}")
        triggers = ()
    except ET.ParseError as e:
        notify.warning(f"could not parse meadow config for zone {zoneId}: {e}")
        triggers = ()

    _chatTriggersByZone[zoneId] = triggers
    return triggers


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
