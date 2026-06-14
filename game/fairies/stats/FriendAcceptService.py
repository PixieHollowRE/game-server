from __future__ import annotations

from game.fairies.badges.BadgeProgressService import apply_friend_accepted_progress
from game.fairies.badges.FriendBadgeRegistry import FRIEND_ACCEPT_EVENT_ID


def apply_friend_accepted(badge_manager, av_id: int, event_id: int, amount: int = 1) -> None:
    if event_id != FRIEND_ACCEPT_EVENT_ID or amount <= 0:
        return

    for _ in range(amount):
        apply_friend_accepted_progress(badge_manager, av_id)
