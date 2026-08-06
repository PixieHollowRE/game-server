"""
Magic words that hand out meadow giveaways.

Both forms are GM overrides: they pay out whether or not the fairy has already
collected that giveaway, because a GM asking for one wants the item, not a
lecture about eligibility. The collected list is still written, so a fairy given
one this way finds it greyed out in the meadow afterwards.

There is no command to take one back. The client's magic word list is fixed
(see LiveMod), so a name it doesn't already know never reaches the server --
clearing a fairy's collected list means editing `giveawaysCollected` on their
fairy document directly.
"""

from game.fairies.meadow import GiveawayReward
from game.fairies.meadow.GiveawaySpawnData import get_giveaway
from game.fairies.magicwords.registry import command


@command("get-giveaway", "get-giveaway <giveawayId>")
def getGiveaway(ctx) -> str:
    giveawayId = ctx.intArg(0)

    return _award(ctx, ctx.avatar.doId, giveawayId)


@command("give-giveaway", "give-giveaway <giveawayId> <fairy>")
def giveGiveaway(ctx) -> str:
    giveawayId = ctx.intArg(0)
    targetId = ctx.targetId(1)

    return _award(ctx, targetId, giveawayId)


def _award(ctx, avatarId: int, giveawayId: int) -> str:
    definition = get_giveaway(giveawayId)

    if definition is None:
        ctx.fail(f"no giveaway {giveawayId} in GiveawaySpawnData")

    # Record it either way, but only say "already had it" when this is the call
    # that failed to claim -- that is the difference between handing out a
    # first copy and overriding the once-only rule.
    claimed = GiveawayReward.claim(ctx.air, avatarId, giveawayId)

    if not GiveawayReward.award(
        ctx.air, avatarId, giveawayId, definition.reward_item_id
    ):
        if claimed:
            GiveawayReward.release(ctx.air, avatarId, giveawayId)

        ctx.fail(
            f"could not award giveaway {giveawayId} "
            f"(reward {definition.reward_item_id}) to {avatarId}"
        )

    again = "" if claimed else " (had already collected it)"

    return (
        f"gave giveaway {giveawayId} '{definition.display_name}' "
        f"-- reward {definition.reward_item_id} -- to {avatarId}{again}"
    )
