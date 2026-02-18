from game.otp.ai.AIMsgTypes import *
FairiesAIMsgName2Id = {
    # PlayerFriendsManager messages:
    'FRIENDMANAGER_ACCOUNT_ONLINE': 10000,
    'FRIENDMANAGER_ACCOUNT_OFFLINE': 10001,
    'FRIENDMANAGER_INVITE_RACE': 10002,
    'FRIENDMANAGER_INVITE_RESP': 10003,
    # ShardManager messages:
    'SHARDMANAGER_ONLINE': 20000}
FairiesAIMsgId2Names = invertDictLossless(FairiesAIMsgName2Id)
for name, value in list(FairiesAIMsgName2Id.items()):
    exec('%s = %s' % (name, value))

del name
del value
