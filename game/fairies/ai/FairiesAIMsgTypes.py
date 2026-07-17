from game.otp.ai.AIMsgTypes import *
FairiesAIMsgName2Id = {
    # PlayerFriendsManager messages:
    'FRIENDMANAGER_ACCOUNT_ONLINE': 10000,
    'FRIENDMANAGER_ACCOUNT_OFFLINE': 10001,
    'FRIENDMANAGER_INVITE_RACE': 10002,
    'FRIENDMANAGER_INVITE_RESP': 10003,
    # ShardManager messages:
    'SHARDMANAGER_ONLINE': 20000,
    # RealmGuardian <-> district AI messages:
    'REALM_GENERATE_REQUEST': 20010,
    'REALM_GENERATE_RESPONSE': 20011,
    # Broadcast from the RealmGuardian asking every district AI to (re)announce
    # itself. Covers the case where a district came up before the uberdog was
    # listening and its startup SHARDMANAGER_ONLINE was dropped.
    'REALM_REGISTER_REQUEST': 20012,
    # A district AI tells the RealmGuardian that an avatar entered/left a home
    # realm (for occupancy-based teardown).
    'REALM_OCCUPANCY_UPDATE': 20013,
    # The RealmGuardian asks a district AI to delete an empty home realm.
    'REALM_DELETE_REQUEST': 20014}
FairiesAIMsgId2Names = invertDictLossless(FairiesAIMsgName2Id)
for name, value in list(FairiesAIMsgName2Id.items()):
    exec('%s = %s' % (name, value))

del name
del value
