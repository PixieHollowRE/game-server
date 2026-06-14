from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

from game.fairies.badges.BadgeProgressService import (
    build_login_payload,
    ensure_badges_bootstrapped,
    load_fairy_doc,
    persist_fairy_badge_state,
)
from game.fairies.stats.FriendAcceptService import apply_friend_accepted


class FairiesBadgeManagerUD(DistributedObjectGlobalUD):
    def __init__(self, air) -> None:
        super().__init__(air)

    def announceGenerate(self) -> None:
        DistributedObjectGlobalUD.announceGenerate(self)

        self.accept("avatarOnline", self.avatarOnline)

    def accumulate(self, avId: int, eventId: int, amount: int) -> None:
        apply_friend_accepted(self, avId, eventId, amount)

    def avatarOnline(self, avatarId, avatarType) -> None:
        # avatarType is unused, but it is sent over the messenger anyways.
        doc = load_fairy_doc(self.air, avatarId)
        doc, changed = ensure_badges_bootstrapped(doc)

        if changed:
            persist_fairy_badge_state(self.air, avatarId, doc)

        earned_badges, unlocked_page_ids, badge_progress = build_login_payload(doc)

        self.sendUpdateToAvatarId(
            avatarId, "setBadges", [earned_badges, unlocked_page_ids, badge_progress]
        )
