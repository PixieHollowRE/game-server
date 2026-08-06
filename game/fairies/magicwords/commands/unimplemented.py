"""
Magic words for systems this server does not have yet.

They are registered rather than left out on purpose. An unregistered command
comes back as "unknown magic word", which reads like a typo; these come back
naming the system that is missing, so it is obvious the console spelling was
right and the feature simply isn't there. When one of these systems lands,
delete its entry here and write the real handler alongside its siblings.
"""

from direct.directnotify.DirectNotifyGlobal import directNotify

from game.fairies.magicwords.registry import command

notify = directNotify.newCategory("MagicWords")

# system -> the commands that wait on it, with the arguments LiveMod sends so
# the shape is on record for whoever implements it.
UNIMPLEMENTED = {
    # DistributedFairyQuestNPCAI answers requestQuestChoices with an empty list;
    # there is no quest state on the fairy at all.
    "quests": [
        ("unlock-quest", "unlock-quest <questId>"),
        ("set-quest-accumulate", "set-quest-accumulate <questId> <amount>"),
        ("complete-quest", "complete-quest <questId>"),
        ("complete-step", "complete-step <stepId>"),
    ],

    # The Wilderness / Adventure content (libwilderness.swf). No instance, no
    # challenge, no enemies -- create-wilderness teleports the client into a
    # zone nothing ever builds.
    "the wilderness": [
        ("create-wilderness", "create-wilderness <wildernessId> <zoneId>"),
        ("set-wilderness-id", "set-wilderness-id <wildernessId>"),
        ("set-challenge-level", "set-challenge-level [level]"),
        ("set-challenge-spells", "set-challenge-spells [spells]"),
        ("set-microgames", "set-microgames [microgames]"),
        ("defeat-all-enemies", "defeat-all-enemies"),
        ("complete-all-crafts", "complete-all-crafts"),
    ],

    # Garden plots. setGardenType exists in the .dc and the client has the
    # panels, but nothing on the server owns a plot or grows anything in it.
    "gardens": [
        ("set-garden-type-id", "set-garden-type-id <gardenTypeId>"),
        ("plot-next-stage", "plot-next-stage <plotId>"),
    ],

    # PetMgrUD answers every profile request with an empty pet; nothing stores
    # a pet, its DNA, or its hunger/health/happiness/growth numbers.
    "pets": [
        ("get-pet", "get-pet <itemId> <color1> <color2> <color3> <name>"),
        ("set-pet-hunger", "set-pet-hunger <value>"),
        ("set-pet-health", "set-pet-health <value>"),
        ("set-pet-happiness", "set-pet-happiness <value>"),
        ("set-pet-growth", "set-pet-growth <value>"),
    ],

    # Animal friend gifts -- the presents a pet brings back and leaves lying in
    # the meadow. No pet system means no gift system.
    "animal friend gifts": [
        ("request-gift", "request-gift <mask> <delay>"),
        ("make-gift", "make-gift <itemId> <x> <y>"),
        ("clear-gifts", "clear-gifts"),
    ],

    # Per-holiday one-time flags on the fairy. HolidayManagerUD serves a fixed
    # tag list and keeps no per-fairy state to clear.
    "holiday flags": [
        ("clear-holiday-flags", "clear-holiday-flags"),
    ],

    # Targeted advertising. Nothing on the server decides who is eligible for
    # an ad; the client-only `show-ad` and `targeted-ad` still work for testing
    # the popups themselves.
    "advertising eligibility": [
        ("set-ad-eligible", "set-ad-eligible <adId> <eligible>"),
    ],

    # Turning a meadow game on/off from the console. There is no server-side
    # switch for a game: DistributedMeadowGameAI instances are created at
    # district startup and are always available.
    "meadow game toggles": [
        ("game-on", "game-on <gameId>"),
    ],
}


def _register(name: str, usage: str, system: str) -> None:
    @command(name, usage)
    def handler(ctx, _system=system) -> str:
        notify.info(
            f"{ctx.name} from {ctx.avatar.doId}: {_system} is not implemented"
        )

        return f"{ctx.name}: {_system} is not implemented on this server"


for _system, _commands in UNIMPLEMENTED.items():
    for _name, _usage in _commands:
        _register(_name, _usage, _system)
