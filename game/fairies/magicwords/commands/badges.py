"""
Magic words that drive the badge book.

Every write to badgeData belongs to FairiesBadgeManagerUD -- that is what keeps
two districts from double-awarding the same badge -- so none of these touch
Mongo directly. They go out over the AI-side handle and the uberdog decides what
they mean, exactly like a badge earned in play.
"""

from game.fairies.badges import badge_events
from game.fairies.magicwords.registry import command


@command("get-badge", "get-badge <badgeId>")
def getBadge(ctx) -> str:
    badgeId = ctx.intArg(0)

    _awardBadge(ctx, ctx.avatar.doId, badgeId)

    return f"awarded badge {badgeId}"


@command("give-badge", "give-badge <badgeId> <fairy>")
def giveBadge(ctx) -> str:
    badgeId = ctx.intArg(0)
    targetId = ctx.targetId(1)

    _awardBadge(ctx, targetId, badgeId)

    return f"awarded badge {badgeId} to {targetId}"


def _awardBadge(ctx, avatarId: int, badgeId: int) -> None:
    # unlockBadge first: giveBadge only touches a row that is already being
    # tracked, and a GM handing out a badge from a chapter this server doesn't
    # follow yet would otherwise silently do nothing. Both land on the same
    # uberdog over the same connection, so they arrive in this order.
    ctx.air.badgeManager.d_unlockBadge(avatarId, badgeId)
    ctx.air.badgeManager.d_giveBadge(avatarId, badgeId)


@command("get-badge-page", "get-badge-page <pageId>")
def getBadgePage(ctx) -> str:
    pageId = ctx.intArg(0)

    ctx.air.badgeManager.d_unlockPage(ctx.avatar.doId, pageId)

    return f"unlocked badge page {pageId}"


@command("give-badge-page", "give-badge-page <pageId> <fairy>")
def giveBadgePage(ctx) -> str:
    pageId = ctx.intArg(0)
    targetId = ctx.targetId(1)

    ctx.air.badgeManager.d_unlockPage(targetId, pageId)

    return f"unlocked badge page {pageId} for {targetId}"


@command("accumulate-badge", "accumulate-badge <eventId> [amount]")
def accumulateBadge(ctx) -> str:
    eventId = ctx.intArg(0)
    amount = ctx.optIntArg(1, 1)

    if not badge_events.get_badges_for_event(eventId):
        ctx.fail(f"no badge listens for event {eventId} (see badge_events)")

    ctx.air.badgeManager.d_accumulate(ctx.avatar.doId, eventId, amount)

    return f"accumulated {amount} toward event {eventId}"


@command("clear-visited-meadows", "clear-visited-meadows")
def clearVisitedMeadows(ctx) -> str:
    # Meadow Explorer badges count distinct zones rather than occurrences, so
    # "clear" means wiping the set of meadows already stood in -- which is what
    # unlockBadge does when it resets a row. Re-entering a meadow then counts
    # again; setActualZoneId reports every entry and lets the uberdog dedupe.
    for badgeId in badge_events.MEADOW_EXPLORER_ZONES:
        ctx.air.badgeManager.d_unlockBadge(ctx.avatar.doId, badgeId)

    count = len(badge_events.MEADOW_EXPLORER_ZONES)

    return f"reset {count} meadow explorer badge(s) -- re-walk the meadows to re-earn"
