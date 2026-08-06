"""
The magic word dispatch table, and the context a handler is given.

A handler is a plain function registered with @command. It receives a Context
and returns a string, which is sent back to the GM's client as
setMagicWordResponse -- the Flash client only writes that to its debug log
(FairiesMagicWordManager.setMagicWordResponse), so it is a log line, not a
player-facing message, and can say whatever is most useful when a command
misbehaves.

Anything a handler cannot do raises MagicWordError; the manager turns that into
the same response channel rather than letting it reach the district's reader
loop. Nothing else is caught, so a genuine bug still surfaces as a traceback.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass


class MagicWordError(Exception):
    """
    A command that cannot be carried out as asked.

    The message goes straight to the GM, so write it for a person: "no fairy
    named Rosetta Sparkle Dust", not a repr.
    """


@dataclass(frozen=True)
class Command:
    name: str
    usage: str
    handler: Callable[["Context"], str | None]


_COMMANDS: dict[str, Command] = {}


def command(name: str, usage: str = ""):
    """
    Register a magic word handler.

    `usage` is shown when the arguments don't add up, so spell out the argument
    names: "give-badge <badgeId> <fairy>".
    """
    def register(handler: Callable[["Context"], str | None]) -> Callable:
        if name in _COMMANDS:
            raise ValueError(f"magic word {name!r} is already registered")

        _COMMANDS[name] = Command(name, usage or name, handler)
        return handler

    return register


def get(name: str) -> Command | None:
    return _COMMANDS.get(name)


def names() -> list[str]:
    return sorted(_COMMANDS)


class Context:
    """
    Everything a handler is allowed to know about the command it is running.

    `avatar` is the GM who typed it -- already looked up and known to be on this
    district, so handlers never have to re-check it. `args` is the command split
    on whitespace with the command name dropped.
    """

    def __init__(self, air, avatar, name: str, args: list[str], zoneId: int) -> None:
        self.air = air
        self.avatar = avatar
        self.name = name
        self.args = args
        self.zoneId = zoneId

    @property
    def usage(self) -> str:
        cmd = get(self.name)
        return cmd.usage if cmd else self.name

    def fail(self, message: str) -> None:
        raise MagicWordError(message)

    # ── arguments ─────────────────────────────────────────────────────────── #

    def arg(self, index: int) -> str:
        if index >= len(self.args):
            self.fail(f"not enough arguments -- usage: {self.usage}")

        return self.args[index]

    def intArg(self, index: int) -> int:
        value = self.arg(index)

        try:
            return int(value)
        except ValueError:
            self.fail(f"{value!r} is not a number -- usage: {self.usage}")

    def optIntArg(self, index: int, default: int) -> int:
        if index >= len(self.args):
            return default

        return self.intArg(index)

    def tail(self, index: int) -> str:
        """
        Everything from `index` on, rejoined.

        Fairy names have spaces in them ("Rosetta Sparkle Dust"), so every
        command that names one takes it last and reads it through here.
        """
        if index >= len(self.args):
            self.fail(f"not enough arguments -- usage: {self.usage}")

        return " ".join(self.args[index:])

    # ── other fairies ─────────────────────────────────────────────────────── #

    def targetId(self, index: int) -> int:
        """
        Resolve the fairy named from `index` onwards to a doId.

        Accepts a doId as well as a name, since a GM chasing a bug usually has
        the doId in front of them and a name can be ambiguous.
        """
        token = self.tail(index)

        if token.isdigit():
            doId = int(token)

            if not self.air.mongoInterface.mongodb.fairies.find_one({"_id": doId}, {"_id": 1}):
                self.fail(f"no fairy with doId {doId}")

            return doId

        # Names are stored as typed; match without case so a GM doesn't have to
        # guess it. Anchored so "Rose" can't pick up "Rosetta".
        fairy = self.air.mongoInterface.mongodb.fairies.find_one(
            {"name": {"$regex": f"^{re.escape(token)}$", "$options": "i"}},
            {"_id": 1, "name": 1},
        )

        if not fairy:
            self.fail(f"no fairy named {token!r}")

        return fairy["_id"]

    def onlineTarget(self, index: int) -> object:
        """
        The same, but the fairy has to be generated on *this* district.

        For anything that only makes sense against a live object -- muting,
        forcing a spin. A fairy on another district is reported as offline
        rather than silently ignored, because from here they are the same thing.
        """
        doId = self.targetId(index)
        avatar = self.air.doId2do.get(doId)

        if avatar is None:
            self.fail(f"fairy {doId} is not on this district")

        return avatar


def dispatch(air, avatar, magicWord: str, zoneId: int) -> str:
    """
    Run `magicWord` on behalf of `avatar` and return the reply for the GM.

    Raises MagicWordError for anything the caller should report rather than log
    as a fault -- an unknown command, bad arguments, a fairy who isn't there.
    """
    parts = magicWord.split()

    if not parts:
        raise MagicWordError("empty magic word")

    name = parts[0].lower()
    cmd = get(name)

    if cmd is None:
        raise MagicWordError(f"unknown magic word {name!r}")

    response = cmd.handler(Context(air, avatar, name, parts[1:], zoneId))

    return response if response is not None else f"{name}: ok"
