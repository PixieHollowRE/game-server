"""
Whether a fairy name is one the client could actually have picked.

The rename panel (fairyNameSelector.swf) builds a name out of three word lists
in caf/nameGenerator.xml -- a First name, and a last name that is exactly one
Prefix glued to one Suffix -- and toggles the two halves on and off, never both
off. So the only shapes it can produce are "First PrefixSuffix", "First", and
" PrefixSuffix". requestSendUpdateFairyName then sends the finished string, and
an edited client can put anything it likes in it.

This mirrors web-api's validateFairyName (services/WebService.js), which guards
the create-a-fairy path, so both ways a name can be stored agree on what a legal
one is.

Loaded on first use and cached.
"""

import xml.etree.ElementTree as ET

from paths import XML

# The in-game picker reads this copy, not localization/, via the config.xml
# "fairyNameGenerator" table.
NAME_GENERATOR_XML = XML / "caf" / "nameGenerator.xml"

_words: dict[str, frozenset[str]] | None = None


def _parse(path) -> dict[str, frozenset[str]]:
    root = ET.parse(path).getroot()

    words = {}
    for selector in root.findall("NameSelector"):
        listType = selector.get("type")

        if listType is None:
            continue

        words[listType] = frozenset(
            text
            for element in selector.findall("name")
            if (text := (element.text or "").strip())
        )

    for listType in ("First", "Prefix", "Suffix"):
        if not words.get(listType):
            raise ValueError(f"{path} has no <NameSelector type=\"{listType}\"> names")

    return words


def load() -> None:
    global _words

    if _words is None:
        _words = _parse(NAME_GENERATOR_XML)


def normalize(name: str) -> str:
    """
    Trim both ends and collapse inner whitespace runs.

    The picker omits whichever half the player toggled off but leaves the
    separator in, so a last-name-only pick arrives as " Bellbreeze".
    """
    return " ".join(name.split())


def _is_last_name(word: str) -> bool:
    load()

    # Prefix and Suffix share starts ("bee"/"beetle"), so try every split point.
    return any(
        word[:i] in _words["Prefix"] and word[i:] in _words["Suffix"]
        for i in range(1, len(word))
    )


def is_valid(name: str) -> bool:
    """Whether `name` is composable from the picker's word lists."""
    load()

    parts = normalize(name).split(" ")

    if len(parts) > 2:
        return False

    # A single part is either a first name on its own or a last name on its own.
    if len(parts) == 1:
        return parts[0] in _words["First"] or _is_last_name(parts[0])

    firstName, lastName = parts
    return firstName in _words["First"] and _is_last_name(lastName)
