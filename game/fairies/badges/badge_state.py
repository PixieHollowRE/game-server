"""
The shape of a fairy's stored badgeData, and reading it back.

FairiesBadgeManagerUD owns every write to badgeData -- that is what stops two
districts from double-awarding the same badge -- but a district sometimes needs
to know what a fairy has already earned before it acts. Vidia's Daily Spin is
the case this was written for: it must not offer a prize badge to a fairy who
already has it. Reads are safe from anywhere; writes belong to the uberdog.
"""

STATUS_ACTIVE = "Active"
STATUS_EARNED = "Earned"


def get_earned_badge_ids(air, avatarId: int, badgeIds=None) -> set[int]:
    """
    Return which badges a fairy has earned, narrowed to `badgeIds` when given.

    Passing the handful you care about is worth it: the projection still fetches
    the whole badge list either way, but the caller gets back a set it can test
    directly rather than one holding every badge the fairy owns.
    """
    fairy = air.mongoInterface.mongodb.fairies.find_one(
        {"_id": avatarId}, {"badgeData.badges": 1}
    )

    if not fairy:
        return set()

    rows = (fairy.get("badgeData") or {}).get("badges") or []
    earned = {
        row["badgeId"] for row in rows if row.get("status") == STATUS_EARNED
    }

    if badgeIds is None:
        return earned

    return earned & set(badgeIds)
