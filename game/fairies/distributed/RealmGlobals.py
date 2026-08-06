QUIET_LEVEL = 1
IDEAL_LEVEL = 2
CROWDED_LEVEL = 3
FULL_LEVEL = 4

# Object types the RealmGuardian can ask a district AI to spawn remotely.
# (see RealmGuardianUD.remoteGenerateObject / FairiesAIRepository.createRemoteObject)
OBJECT_TYPE_REALM = 0  # a FairiesHomeRealm (player-housing realm)

# Headcount at which a realm enters each level, as (QUIET, IDEAL, CROWDED,
# FULL). Overridden by the realm-population-levels config; this is only the
# fallback for a missing or malformed setting.
DEFAULT_POPULATION_LEVELS = [0, 30, 60, 90]


def getPopulationLevel(population, levels):
    """
    Map a realm headcount onto a *_LEVEL constant using the four thresholds in
    `levels`. FULL_LEVEL is the capacity line: the client greys out full realms
    in the shard chooser, and the server refuses to fly anyone into one.
    """
    if population >= levels[3]:
        return FULL_LEVEL
    elif population >= levels[2]:
        return CROWDED_LEVEL
    elif population >= levels[1]:
        return IDEAL_LEVEL
    else:
        return QUIET_LEVEL
