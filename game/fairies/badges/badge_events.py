import game.fairies.ai.FairiesConstants as fc
import game.fairies.ai.ZoneConstants as zc
import game.fairies.minigame.MinigameConstants as mc

# ─────────────────────────────────── CLIENT STUFF ─────────────────────────────────── #
# mmo.swf FriendsManager.checkForAcceptance and friendMessages.swf
# FriendMessage both call dispatchAccumulateForMe(25003) when an invite is
# accepted. It is the only event the client raises on its own; every other
# badge below is driven by the server.
EVENT_FRIEND_ADDED = 25003

# What the client may raise on its own. Anything else turning up via
# accumulateForMe is a modified client trying to award itself a badge it never
# earned, since everything below is only ever raised by the server.
CLIENT_RAISED_EVENTS = frozenset({EVENT_FRIEND_ADDED})

# ───────────────────────────────────── MINIGAMES ──────────────────────────────────── #
EVENT_PLAYED_FIREFLY_LIGHT_UP = 30001
EVENT_PLAYED_WATER_WEB = 30002
EVENT_PLAYED_HARVEST_HUSTLE = 30003
EVENT_PLAYED_TINKER_TOSS = 30004
EVENT_PLAYED_SEED_SORTER = 30005
EVENT_PLAYED_SNOWY_LULLABY = 30006
EVENT_PLAYED_PETAL_PICKUP = 30007
EVENT_PLAYED_PINECONE_POP = 30008
EVENT_PLAYED_GEM_JUGGLE = 30009
EVENT_PLAYED_SUNBEAM_BEND = 30010
EVENT_PLAYED_BUBBLE_BOUNCE = 30011
EVENT_PLAYED_BUTTERFLY_PAINTER = 30012
EVENT_PLAYED_FAIRY_FIREWORKS = 30013
EVENT_PLAYED_SNOWFLAKE_SWEEP = 30014
EVENT_PLAYED_FIRST_FLIGHT = 30015
EVENT_PLAYED_DAILY_SPIN = 30016

# ───────────────────────────────────── CRAFTING ───────────────────────────────────── #
# Each craft has two four-tier ladders (goals 5/25/100/500, read from badges.xml).
# The two are driven by the two crafting styles, which count genuinely different
# things:
#
#   practice  - community/"practice" crafts. They make nothing and spend nothing
#               (DistributedCraftingMinigameAI bails before granting an item), but
#               they are exactly what "practicing baking" in the badge text means,
#               so they advance the practice ladder from inside that bail.
#   personal  - personal crafts, which spend ingredients and yield an item. These
#               advance the personal ladder once something has actually been made.
EVENT_PRACTICE_TAILORING = 30020
EVENT_PRACTICE_BAKING = 30021
EVENT_PRACTICE_TINKERING = 30022
EVENT_PERSONAL_TAILORING = 30023
EVENT_PERSONAL_BAKING = 30024
EVENT_PERSONAL_TINKERING = 30025

# ──────────────────────────────────── DAILY SPIN ──────────────────────────────────── #
# EVENT_PLAYED_DAILY_SPIN above counts spins taken; these count what came out of
# them. Everything on Vidia's Games (page 12054) is one or the other.
#
# amount = how many rocks that spin turned up, so a member pulling three at once
# counts three.
EVENT_WON_ROCK = 30030

# The three badges that are themselves prizes in the spin. Each has a goal of 1,
# so the event saying it was won is also what earns it.
EVENT_WON_SOUR_PLUM_BADGE = 30031
EVENT_WON_LUCKY_PURPLE_FEATHERS_BADGE = 30032
EVENT_WON_SNEAKY_MR_TWITCHES_BADGE = 30033

# ──────────────────────────────────── INGREDIENTS ─────────────────────────────────── #
COLLECTION_EVENT_BASE = 30100


# Every ingredient has the same four tiers, in ascending goal order:
#
#   plain (50) -> Super (200) -> Flitterific (1000) -> Royal (9000)
#
# All four hang off the one collection event and count the same lifetime total,
# so Royal means 9000 collected outright, not 9000 more after the other three.
# The plain tier of the five starter ingredients lives on the Starter Badges
# pages; every other tier is in the Ingredients chapter.
#
# Read straight out of badges.xml -- note Truffles, whose plain tier (10748) is
# numbered above its own higher tiers.
INGREDIENT_BADGE_TIERS: dict[int, tuple[int, int, int, int]] = {
    fc.ACORNS:            (10654, 10655, 10656, 10657),
    fc.BITS_OF_METAL:     (10723, 10724, 10725, 10726),
    fc.BLUEBERRIES:       (10634, 10635, 10636, 10637),
    fc.BLUE_GEMS:         (10719, 10720, 10721, 10722),
    fc.BUTTERCUP_PETALS:  (10618, 10619, 10620, 10621),
    fc.DAISY_PETALS:      (10622, 10623, 10624, 10625),
    fc.DANDELION_FLUFF:   (10674, 10675, 10676, 10677),
    fc.FEATHERS:          (10744, 10745, 10746, 10747),
    fc.HONEYCOMBS:        (10690, 10691, 10692, 10693),
    fc.IVY:               (10678, 10679, 10680, 10681),
    fc.LILY_PETALS:       (10626, 10627, 10628, 10629),
    fc.MAPLE_LEAVES:      (10642, 10643, 10644, 10645),
    fc.MEADOW_GRASS:      (10670, 10671, 10672, 10673),
    fc.OAK_LEAVES:        (10646, 10647, 10648, 10649),
    fc.PINE_NEEDLES:      (10650, 10651, 10652, 10653),
    fc.RASPBERRIES:       (10638, 10639, 10640, 10641),
    fc.ROSE_PETALS:       (10630, 10631, 10632, 10633),
    fc.SNOWFLAKES:        (10662, 10663, 10664, 10665),
    fc.SPIDER_SILK:       (10666, 10667, 10668, 10669),
    fc.SUNFLOWER_SEEDS:   (10658, 10659, 10660, 10661),
    fc.TRUFFLES:          (10748, 10712, 10713, 10714),
    fc.TWIGS:             (10686, 10687, 10688, 10689),
    fc.YELLOW_GEMS:       (10715, 10716, 10717, 10718),
}

INGREDIENT_TO_EVENT: dict[int, int] = {
    itemId: COLLECTION_EVENT_BASE + index
    for index, itemId in enumerate(sorted(INGREDIENT_BADGE_TIERS))
}


EVENT_TO_BADGES: dict[int, tuple[int, ...]] = {
    # Friendly Fairy (1) / Circle of Friends (5) / Social Butterfly (25). The
    # client raises this once per accepted invite, on both sides -- the inviter
    # via FriendsManager.checkForAcceptance and the accepter via FriendMessage
    # -- so each new friendship advances both fairies by one.
    EVENT_FRIEND_ADDED:               (10531, 10532, 10533),

    EVENT_PLAYED_FIREFLY_LIGHT_UP:    (10576, 10577, 10578),  # Firefly Helper
    EVENT_PLAYED_WATER_WEB:           (10584, 10585, 10586),  # Web Wonder
    EVENT_PLAYED_HARVEST_HUSTLE:      (10592, 10593, 10594),  # Harvest Helper
    EVENT_PLAYED_TINKER_TOSS:         (10740, 10741, 10742),  # Tinker Sorter
    EVENT_PLAYED_SEED_SORTER:         (10785, 10786, 10787),  # Seed Sorter Helper
    EVENT_PLAYED_SNOWY_LULLABY:       (10761, 10762, 10763),  # Lullaby Helper
    EVENT_PLAYED_PETAL_PICKUP:        (10588, 10589, 10590),  # Petal Collector
    EVENT_PLAYED_PINECONE_POP:        (10970, 10971, 10972),  # Pinecone Popper
    EVENT_PLAYED_GEM_JUGGLE:          (10981, 10982, 10983),  # Gem Juggler
    EVENT_PLAYED_SUNBEAM_BEND:        (11015, 11016, 11017),  # Sunbeam Bender
    EVENT_PLAYED_BUBBLE_BOUNCE:       (10580, 10581, 10582),  # Fish Bouncer
    EVENT_PLAYED_BUTTERFLY_PAINTER:   (10889, 10890, 10891),  # Butterfly Painter
    EVENT_PLAYED_FAIRY_FIREWORKS:     (10600, 10601, 10602),  # Fireworks Helper
    EVENT_PLAYED_SNOWFLAKE_SWEEP:     (10682, 10683, 10684),  # Snowflake Star
    EVENT_PLAYED_FIRST_FLIGHT:        (10817, 10818, 10819),  # First Flight Helper
    EVENT_PLAYED_DAILY_SPIN:          (10899, 10900, 10901),  # Daily Spin Challenger

    # Practice ladders. Tier 1 (the free "Helper") sits on the Starter Badges
    # page; tiers 2-4 are the craft's own chapter (18/19/20).
    EVENT_PRACTICE_BAKING:    (10772, 10773, 10774, 10804),  # Baking Helper / Big Help / Super Star / Royal Star
    EVENT_PRACTICE_TINKERING: (10798, 10799, 10800, 11136),  # Tinkering Helper / Big Help / Super Star / Royal Star
    EVENT_PRACTICE_TAILORING: (10883, 10884, 10885, 10894),  # Tailoring Helper / Big Help / Super Star / Royal Star

    # Personal ladders. All four tiers live on the craft's own chapter.
    EVENT_PERSONAL_BAKING:    (10775, 10776, 10777, 10805),  # Beginning / Bright / Brilliant / Royal Brilliance Baker
    EVENT_PERSONAL_TINKERING: (10801, 10802, 10803, 11129),  # Tinker-tastic / Super / Flitterific / Royal
    EVENT_PERSONAL_TAILORING: (10886, 10887, 10888, 10895),  # Talented Tailor / Super / Flitterific / Royal

    EVENT_WON_ROCK:                   (10974, 10975, 10976),  # Rocks / Rock and Roll / Rock Star

    EVENT_WON_SOUR_PLUM_BADGE:             (10903,),  # Sour Plum
    EVENT_WON_LUCKY_PURPLE_FEATHERS_BADGE: (10902,),  # Lucky Purple Feathers
    EVENT_WON_SNEAKY_MR_TWITCHES_BADGE:    (11130,),  # Sneaky Mr. Twitches
}

EVENT_TO_BADGES.update(
    {
        INGREDIENT_TO_EVENT[itemId]: tiers
        for itemId, tiers in INGREDIENT_BADGE_TIERS.items()
    }
)

# Starter Badges also contains Party Guest (10727, "playing at least 1 party
# game hosted by another Fairy"). There is no party system on the server yet, so
# nothing raises its event; it sits at 0 progress in the badge book until there
# is one.

GAME_TO_EVENT: dict[int, int] = {
    mc.MINIGAME_FIREFLY_LIGHT_UP: EVENT_PLAYED_FIREFLY_LIGHT_UP,
    mc.MINIGAME_WATER_WEB:        EVENT_PLAYED_WATER_WEB,
    mc.MINIGAME_HARVEST_HUSTLE:   EVENT_PLAYED_HARVEST_HUSTLE,
    mc.MINIGAME_TINKER_TOSS:      EVENT_PLAYED_TINKER_TOSS,
    mc.MINIGAME_SEED_SORTING:     EVENT_PLAYED_SEED_SORTER,
    mc.MINIGAME_LULLABY:          EVENT_PLAYED_SNOWY_LULLABY,
    mc.MINIGAME_PETAL_PICKUP:     EVENT_PLAYED_PETAL_PICKUP,
    mc.MINIGAME_PINECONE_POP:     EVENT_PLAYED_PINECONE_POP,
    mc.MINIGAME_GEM_JUGGLE:       EVENT_PLAYED_GEM_JUGGLE,
    mc.MINIGAME_LIGHT_PIPE:       EVENT_PLAYED_SUNBEAM_BEND,
    mc.MINIGAME_BUBBLE_BOUNCE:    EVENT_PLAYED_BUBBLE_BOUNCE,
    mc.MINIGAME_BUTTERFLY:        EVENT_PLAYED_BUTTERFLY_PAINTER,
    mc.MINIGAME_FAIRY_FIREWORKS:  EVENT_PLAYED_FAIRY_FIREWORKS,
    mc.MINIGAME_SNOWFLAKE_SWEEP:  EVENT_PLAYED_SNOWFLAKE_SWEEP,
    mc.MINIGAME_FIRST_FLIGHT:     EVENT_PLAYED_FIRST_FLIGHT,
}

# High Score badges (chapter 7) are not accumulated like the Helper badges: a
# fairy earns one outright the first time their score in a single run reaches
# that game's requiredForHighScoreBadge threshold (mirrored server-side as
# MinigameRewards.GAMES[gameId].badge_threshold). Because that threshold is a
# score -- up to 155000, well past the int16 `amount` in accumulate() -- the
# district compares against it and hands the badge over directly with
# giveBadge(), rather than routing the score through the badge manager.
#
# Read straight out of badges.xml: each game's High Score badge sits one past
# its three Helper tiers in EVENT_TO_BADGES above.
GAME_TO_HIGH_SCORE_BADGE: dict[int, int] = {
    mc.MINIGAME_FIREFLY_LIGHT_UP: 10579,
    mc.MINIGAME_WATER_WEB:        10587,
    mc.MINIGAME_HARVEST_HUSTLE:   10595,
    mc.MINIGAME_TINKER_TOSS:      10743,
    mc.MINIGAME_SEED_SORTING:     10788,
    mc.MINIGAME_LULLABY:          10764,
    mc.MINIGAME_PETAL_PICKUP:     10591,
    mc.MINIGAME_PINECONE_POP:     10973,
    mc.MINIGAME_GEM_JUGGLE:       10984,
    mc.MINIGAME_LIGHT_PIPE:       11018,  # Sunbeam Bend
    mc.MINIGAME_BUBBLE_BOUNCE:    10583,
    mc.MINIGAME_BUTTERFLY:        10892,
    mc.MINIGAME_FAIRY_FIREWORKS:  10603,
    mc.MINIGAME_SNOWFLAKE_SWEEP:  10685,
    mc.MINIGAME_FIRST_FLIGHT:     10820,
}

# Which event a finished craft raises, split by style: practice crafts take the
# first map, personal crafts the second. Keyed by professionId (see
# MinigameConstants.CRAFT_TYPE_*).
PROFESSION_TO_PRACTICE_EVENT: dict[int, int] = {
    mc.CRAFT_TYPE_TAILORING: EVENT_PRACTICE_TAILORING,
    mc.CRAFT_TYPE_BAKING:    EVENT_PRACTICE_BAKING,
    mc.CRAFT_TYPE_TINKERING: EVENT_PRACTICE_TINKERING,
}

PROFESSION_TO_PERSONAL_EVENT: dict[int, int] = {
    mc.CRAFT_TYPE_TAILORING: EVENT_PERSONAL_TAILORING,
    mc.CRAFT_TYPE_BAKING:    EVENT_PERSONAL_BAKING,
    mc.CRAFT_TYPE_TINKERING: EVENT_PERSONAL_TINKERING,
}

# Keyed by badge id, since the Daily Spin draws the badge itself as a prize and
# has to work back to the event that awards it. Mirrors SPIN_BADGE_IDS in
# DailyChanceConstants, which is what puts them in the pool.
SPIN_BADGE_TO_EVENT: dict[int, int] = {
    10903: EVENT_WON_SOUR_PLUM_BADGE,
    10902: EVENT_WON_LUCKY_PURPLE_FEATHERS_BADGE,
    11130: EVENT_WON_SNEAKY_MR_TWITCHES_BADGE,
}


# ─────────────────────────────────── MEADOW EXPLORER ──────────────────────────────── #
# The four seasonal Meadow Explorer badges (Exploration chapter) are earned by
# visiting each meadow of a season, not by a running tally -- so they sit
# outside EVENT_TO_BADGES/accumulate and take the uberdog's distinct-zone path.
#
# A zone's season is its id band (100s spring, 200s autumn, 300s winter, 400s
# summer). The curated sets below leave out each band's troop hideouts and the
# non-meadow buildings and coves (Ice Palace, Frosted Forest, Mermaid Grotto),
# so every set is exactly the goal badges.xml renders for that badge.
#
# Visits ride the accumulate field under this event id (see
# FairiesBadgeManagerAI.d_exploreMeadow): a dclass method of its own would
# renumber every field after it and break the client handshake, so the zone
# travels in the amount slot and the uberdog routes it here.
EVENT_EXPLORE_MEADOW = 30200

MEADOW_EXPLORER_ZONES: dict[int, tuple[int, ...]] = {
    10534: (  # Spring Meadow Explorer (goal 5)
        zc.CHERRYBLOSSOM_HEIGHTS,
        zc.SPRINGTIME_ORCHARD,
        zc.DEWDROP_VALE,
        zc.NEVERBERRY_THICKET,
        zc.TREETOP_BEND,
    ),
    10554: (  # Autumn Meadow Explorer (goal 4)
        zc.ACORN_SUMMIT,
        zc.COTTONPUFF_FIELD,
        zc.MAPLE_TREE_HILL,
        zc.PUMPKIN_PATCH,
    ),
    10604: (  # Winter Meadow Explorer (goal 3)
        zc.EVERGREEN_OVERLOOK,
        zc.SNOWCAP_GLADE,
        zc.CHILLY_FALLS,
    ),
    10694: (  # Summer Meadow Explorer (goal 3)
        zc.PALM_TREE_COVE,
        zc.SUNFLOWER_GULLY,
        zc.NEVERFRUIT_GROVE,
    ),
}

ZONE_TO_MEADOW_BADGE: dict[int, int] = {
    zoneId: badgeId
    for badgeId, zoneIds in MEADOW_EXPLORER_ZONES.items()
    for zoneId in zoneIds
}


def get_badges_for_event(event_id: int) -> tuple[int, ...]:
    """Return the badge ids an event advances, empty if nothing tracks it."""
    return EVENT_TO_BADGES.get(event_id, ())


def get_meadow_badge_for_zone(zone_id: int) -> int | None:
    """Return the Meadow Explorer badge a zone counts toward, or None."""
    return ZONE_TO_MEADOW_BADGE.get(zone_id)
