"""UD DC stub for PlayerFriendsManager.

Server logic lives in config/FMPlayerFriendsManager.lua (FriendManager role).
"""

from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD


class PlayerFriendsManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('PlayerFriendsManagerUD')
