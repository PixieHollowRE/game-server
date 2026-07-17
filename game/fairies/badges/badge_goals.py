"""
How much progress each badge needs before it is earned.

The goals are not kept server-side: they live in the client's own badges.xml,
under <goals>, as one element per badge (<goal10592>5</goal10592>). That is the
same number the badge book renders into "#CURRENT# of #GOAL#", so reading it
here is what keeps the threshold we award at and the threshold the player is
shown from drifting apart.

Loaded on first use and cached, since badges.xml only changes when the XML data
is redeployed (which restarts the uberdog anyway).
"""

import re
import xml.etree.ElementTree as ET

from paths import XML

BADGES_XML = XML / "badges.xml"

# <goals> holds one element per badge, with the badge id baked into the tag name.
_GOAL_TAG = re.compile(r"^goal(\d+)$")

_goals: dict[int, int] | None = None


def _parse(path) -> dict[int, int]:
    goalsNode = ET.parse(path).getroot().find("goals")
    if goalsNode is None:
        raise ValueError(f"{path} has no <goals> section")

    goals = {}
    for element in goalsNode:
        match = _GOAL_TAG.match(element.tag)
        text = (element.text or "").strip()

        if match is None or not text.isdigit():
            continue

        goals[int(match.group(1))] = int(text)

    return goals


def load() -> dict[int, int]:
    global _goals

    if _goals is None:
        _goals = _parse(BADGES_XML)

    return _goals


def get_goal(badge_id: int) -> int | None:
    return load().get(badge_id)
