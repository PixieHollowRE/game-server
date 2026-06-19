"""Client-side DC stub for PlayerFriendsManager.

Pixie Hollow account friends are implemented in config/FMPlayerFriendsManager.lua.
The Flash client handles UI; this class exists only for DC import resolution.
"""

from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify.DirectNotifyGlobal import directNotify


class PlayerFriendsManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('PlayerFriendsManager')
