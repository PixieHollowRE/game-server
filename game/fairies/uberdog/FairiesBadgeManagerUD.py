from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class FairiesBadgeManagerUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

        self.accept("avatarOnline", self.avatarOnline)

    def avatarOnline(self, avatarId, avatarType):
        # avatarType is unused, but it is sent over the messenger anyways.
        dateEarned = ""

        FOUNDING_FAIRY = 10573
        HONORS_PAGE = 12000

        earnedBadges = []
        earnedBadges.append([FOUNDING_FAIRY, dateEarned])

        unlockedPageIds = []
        unlockedPageIds.append(HONORS_PAGE)

        badgeProgress = []
        badgeProgress.append([FOUNDING_FAIRY, 1])

        self.sendUpdateToAvatarId(avatarId, "pageUnlocked", [HONORS_PAGE, badgeProgress])
        self.sendUpdateToAvatarId(avatarId, "badgeUnlocked", [badgeProgress[0]])
        self.sendUpdateToAvatarId(avatarId, "setBadges", [earnedBadges, unlockedPageIds, badgeProgress])
        self.sendUpdateToAvatarId(avatarId, "progressUpdate", [FOUNDING_FAIRY, 1])
