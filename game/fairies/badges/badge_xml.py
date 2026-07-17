"""
The bits of the client's badges.xml the server needs to agree with it on.

Two things live here, both read from the client's own copy rather than
duplicated server-side:

  goals       -- <goals><goal10592>5</goal10592>. The same number the badge book
                 renders into "#CURRENT# of #GOAL#", so reading it is what keeps
                 the threshold we award at and the threshold the player is shown
                 from drifting apart.

  velvet rope -- the velvetRope attribute on <copy><name10592 velvetRope="0">,
                 marking a badge Member-only.

Loaded on first use and cached, since badges.xml only changes when the XML data
is redeployed (which restarts the uberdog anyway).
"""

import re
import xml.etree.ElementTree as ET

from paths import XML

BADGES_XML = XML / "badges.xml"

# <goals> and <copy> both bake the badge id into the tag name.
_GOAL_TAG = re.compile(r"^goal(\d+)$")
_NAME_TAG = re.compile(r"^name(\d+)$")

_goals: dict[int, int] | None = None
_velvetRope: dict[int, str] | None = None


def _parse(path) -> tuple[dict[int, int], dict[int, str]]:
    root = ET.parse(path).getroot()

    goalsNode = root.find("goals")
    if goalsNode is None:
        raise ValueError(f"{path} has no <goals> section")

    copyNode = root.find("copy")
    if copyNode is None:
        raise ValueError(f"{path} has no <copy> section")

    goals = {}
    for element in goalsNode:
        match = _GOAL_TAG.match(element.tag)
        text = (element.text or "").strip()

        if match is None or not text.isdigit():
            continue

        goals[int(match.group(1))] = int(text)

    # Keep the attribute exactly as written, including absent (None) and empty,
    # because the client distinguishes those from "0" -- see
    # is_velvet_rope_restricted.
    velvetRope = {}
    for element in copyNode:
        match = _NAME_TAG.match(element.tag)

        if match is None:
            continue

        velvetRope[int(match.group(1))] = element.get("velvetRope")

    return goals, velvetRope


def load() -> None:
    global _goals, _velvetRope

    if _goals is None:
        _goals, _velvetRope = _parse(BADGES_XML)


def get_goal(badge_id: int) -> int | None:
    load()
    return _goals.get(badge_id)


def is_velvet_rope_restricted(badge_id: int) -> bool:
    """
    Whether a badge is Member-only.

    This mirrors BadgeItem.isVelvetRopeRestricted in framework.swf exactly,
    quirks included: the client starts from 1 (restricted) and only climbs down
    if the attribute is present and parses as a number, so a badge with no
    velvetRope attribute at all is Member-only. Most of the higher Ingredient
    tiers are exactly that -- only the base tiers say velvetRope="0" -- so
    getting this backwards would hand out every Member badge for free.
    """
    load()
    raw = _velvetRope.get(badge_id)

    if raw is None or raw == "":
        return True

    try:
        return int(float(raw)) != 0
    except ValueError:
        # Present but not a number: the client's Number() gives NaN and it keeps
        # its restricted default.
        return True
