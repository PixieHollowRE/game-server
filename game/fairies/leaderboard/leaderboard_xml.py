"""
The bits of the client's leaderboards.xml the server needs to agree with it on.

The panel at web-xml/xml/panels/leaderboards.xml is what the client reads to
build the game drop-down and to show "Minimum #TYPE# needed: N" under each
board. The server reads the same file so that the threshold it gates entries on
and the threshold the player is shown never drift apart, and so that the set of
games with a board is defined in exactly one place.

  thresholds -- <game><id>2</id><threshold>10000</threshold></game>. A run below
                this never earns a place on that game's board (see
                LeaderBoardMgrUD). For the three "wins" games (see WINS_GAME_IDS)
                the threshold is a minimum win count instead of a score, and is
                enforced on read rather than write, since wins accumulate one at
                a time and could never reach it otherwise.

Loaded on first use and cached, since leaderboards.xml only changes when the XML
data is redeployed (which restarts the uberdog anyway).
"""

import xml.etree.ElementTree as ET

from paths import XML

LEADERBOARDS_XML = XML / "panels" / "leaderboards.xml"

# The three Meadow games keep a running win count rather than a high score, so
# their boards are fed by addToLeaderBoard ($inc) instead of putToLeaderBoard
# ($max) -- see MMOConstants.MEADOW_GAME_* and Leaderboards.updateThresholdCopy,
# which is what labels these three "wins" and every other board "score".
WINS_GAME_IDS = frozenset({
    13070,  # Crazy Cakes  (MEADOW_GAME_CRAZY_EIGHTS)
    13072,  # Two for Tea  (MEADOW_GAME_TWO_FOR_TEA)
    13073,  # Animal Derby (MEADOW_GAME_CART_RACING)
})

_thresholds: dict[int, int] | None = None


def _parse(path) -> dict[int, int]:
    root = ET.parse(path).getroot()

    gamesNode = root.find("config/games")
    if gamesNode is None:
        raise ValueError(f"{path} has no <config><games> section")

    thresholds = {}
    for game in gamesNode.findall("game"):
        idText = (game.findtext("id") or "").strip()
        thresholdText = (game.findtext("threshold") or "").strip()

        if not idText.isdigit() or not thresholdText.isdigit():
            continue

        thresholds[int(idText)] = int(thresholdText)

    return thresholds


def load() -> None:
    global _thresholds

    if _thresholds is None:
        _thresholds = _parse(LEADERBOARDS_XML)


def is_leaderboard_game(game_id: int) -> bool:
    """Whether this game has a board at all (i.e. appears in leaderboards.xml)."""
    load()
    return game_id in _thresholds


def get_threshold(game_id: int) -> int | None:
    """The minimum score (or win count) needed to place on this game's board."""
    load()
    return _thresholds.get(game_id)
