"""
Cluster-wide realm (district) population tracking.

Each district runs in its own AI process and only ever counts the avatars
generated on itself, so no process can see another district's headcount. Every
capacity decision needs exactly that:

  * a fairy flying to a friend is answered by the *requester's* district AI,
    which has to know whether the *target's* district is full, and
  * the RealmGuardian (uberdog) has to know which districts still have room
    before it parks a new home realm on one.

So every district AI broadcasts its headcount to BROADCAST_MESSAGE_TO_ALL_AI --
which reaches every district AI *and* the uberdog -- whenever it changes. This
mixin holds the resulting table plus the queries built on top of it, and is
mixed into both FairiesAIRepository and FairiesUberDog.
"""

import json

from direct.distributed.PyDatagram import PyDatagram

from game.fairies.ai.FairiesAIMsgTypes import (
    BROADCAST_MESSAGE_TO_ALL_AI, REALM_POPULATION_UPDATE)
from game.fairies.distributed import RealmGlobals


class RealmPopulationRegistry:

    def __init__(self):
        # district doId -> that district's last reported headcount. A district
        # only appears here once it has broadcast at least once, and an id we
        # have never heard of counts as empty rather than full -- a process
        # that has not reported in yet must never lock anybody out.
        self.districtPopulations = {}

        self._realmPopulationLevels = None

    def getRealmPopulationLevels(self):
        # Parsed lazily: the config is not loaded yet when the repository is
        # constructed in some startup paths.
        if self._realmPopulationLevels is None:
            levels = None
            raw = config.GetString("realm-population-levels", "")
            if raw:
                try:
                    levels = json.loads(raw)
                except ValueError:
                    levels = None

            if not levels or len(levels) < 4:
                self.notify.warning(
                    "realm-population-levels is missing or malformed (%r); "
                    "falling back to %s" % (raw, RealmGlobals.DEFAULT_POPULATION_LEVELS))
                levels = list(RealmGlobals.DEFAULT_POPULATION_LEVELS)

            self._realmPopulationLevels = levels

        return self._realmPopulationLevels

    def getRealmCapacity(self):
        # The headcount at which a realm is considered FULL.
        return self.getRealmPopulationLevels()[3]

    def broadcastRealmPopulation(self):
        # District AIs only: the uberdog hosts no district of its own.
        population = self.getPopulation()
        self.districtPopulations[self.districtId] = population

        dg = PyDatagram()
        dg.addServerHeader(
            BROADCAST_MESSAGE_TO_ALL_AI, self.ourChannel, REALM_POPULATION_UPDATE)
        dg.addUint32(self.districtId)
        dg.addUint32(population)
        self.send(dg)

    def handleRealmPopulationUpdate(self, di):
        districtId = di.getUint32()
        population = di.getUint32()
        self.districtPopulations[districtId] = population

    def getRealmPopulation(self, districtId):
        return self.districtPopulations.get(districtId, 0)

    def getRealmPopulationLevel(self, districtId):
        return RealmGlobals.getPopulationLevel(
            self.getRealmPopulation(districtId), self.getRealmPopulationLevels())

    def isRealmFull(self, districtId):
        # Only ids we have actually heard a population for can be full. That
        # deliberately excludes home realms, which are district-siblings with
        # their own doIds: home capacity is the RealmGuardian's business (see
        # RealmGuardianUD.realmOccupants), not a district headcount.
        if districtId not in self.districtPopulations:
            return False

        return self.getRealmPopulationLevel(districtId) >= RealmGlobals.FULL_LEVEL
