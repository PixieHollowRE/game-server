# Internal
dc-file config/dclass/fairy.dc
dc-file config/dclass/otp.dc

mongodb-host mongodb://127.0.0.1:27017
mongodb-name PixieHollow

default-directnotify-level info

# Population Levels (for FairiesRealm):
# (QUIET, IDEAL, CROWDED, FULL)
# The FULL threshold is the realm's hard capacity: the shard chooser greys the
# realm out at that headcount, and the server stops flying fairies into it.
realm-population-levels [0, 30, 60, 90]

# How many fairies may be inside one home realm (house + garden together)
# before the RealmGuardian reports it population-locked. The owner and GMs are
# always let in. Fairies still on their way in are counted. Set to 0 to disable
# the cap.
home-realm-max-occupants 30

# Seconds an empty home realm is kept alive before the RealmGuardian deletes it.
# The realm is the parent an arriving client sets interest on, so deleting one
# mid-teleport hangs that client on the loading screen for good. Don't set this
# to 0.
home-realm-teardown-grace 30

# Seconds the RealmGuardian holds a place in a home realm for a fairy it has
# answered but who has not arrived yet. Must comfortably outlast a slow client's
# loading screen; when it lapses the slot is returned and an unused realm is
# reclaimed.
home-realm-reservation-timeout 60
