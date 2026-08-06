"""
Magic words for the weekly and seasonal high score boards.

The districts hold no board state, so both of these are messages to
LeaderBoardMgrUD, which decides whether a score places and owns the rows.
"""

from game.fairies.leaderboard.leaderboard_period import TYPE_SEASONAL, TYPE_WEEKLY
from game.fairies.magicwords.registry import command


@command("game-score", "game-score <gameId> <score>")
def gameScore(ctx) -> str:
    gameId = ctx.intArg(0)
    score = ctx.intArg(1)

    # Submitted unconditionally: the uberdog holds the per-game threshold and
    # keeps the score only if it beats both that and the fairy's own best this
    # period, which is exactly what a real finished run does.
    ctx.air.leaderBoardManager.d_putToLeaderBoard(ctx.avatar.doId, gameId, score)

    return f"submitted {score} on game {gameId}"


@command("lb-rollover", "lb-rollover <weekly|seasonal>")
def lbRollover(ctx) -> str:
    boardType = _readBoardType(ctx)

    ctx.air.leaderBoardManager.d_forceRollover(boardType)

    return f"rolled over the {ctx.arg(0)} board"


def _readBoardType(ctx) -> int:
    token = ctx.arg(0).lower()

    byName = {
        "weekly": TYPE_WEEKLY,
        "week": TYPE_WEEKLY,
        "seasonal": TYPE_SEASONAL,
        "season": TYPE_SEASONAL,
    }

    if token in byName:
        return byName[token]

    # The client sends whatever was typed straight through, so a GM who knows
    # the numbers can use them too.
    if token.isdigit() and int(token) in (TYPE_WEEKLY, TYPE_SEASONAL):
        return int(token)

    ctx.fail(f"unknown board type {token!r} -- usage: {ctx.usage}")
