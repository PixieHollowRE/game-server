from game.otp.ai.AIMsgTypes import *
FairiesAIMsgName2Id = {
    # ShardManager messages:
    'SHARDMANAGER_ONLINE': 20000}
FairiesAIMsgId2Names = invertDictLossless(FairiesAIMsgName2Id)
for name, value in list(FairiesAIMsgName2Id.items()):
    exec('%s = %s' % (name, value))

del name
del value
