from game.otp.ai.AIMsgTypes import *
FairiesAIMsgName2Id = {
    # PlayerFriendsManager messages:
    'FRIENDMANAGER_ACCOUNT_ONLINE': 10000,
    'FRIENDMANAGER_ACCOUNT_OFFLINE': 10001,
    'FRIENDMANAGER_INVITE_RACE': 10002,
    'FRIENDMANAGER_INVITE_RESP': 10003,
    # AI -> UberDOG messages:
    'DISTRICT_REGISTER': 20000,
    # Object messages (For AI and UD):
    'GENERATE_OBJECT': 30000,
    'GENERATE_OBJECT_RESP': 30001}
FairiesAIMsgId2Names = invertDictLossless(FairiesAIMsgName2Id)
for name, value in list(FairiesAIMsgName2Id.items()):
    exec('%s = %s' % (name, value))

del name
del value
