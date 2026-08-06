"""
Every magic word handler, grouped by the system it drives.

Importing this package is what fills the registry in, so FairiesMagicWordManagerAI
imports it for the side effect. A new module of handlers has to be listed here
or its commands will never be found.
"""

from . import (  # noqa: F401 -- imported for the @command registrations
    avatar,
    badges,
    giveaways,
    items,
    leaderboard,
    minigames,
    moderation,
    unimplemented,
)
