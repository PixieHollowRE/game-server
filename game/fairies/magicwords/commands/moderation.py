"""
Magic words that silence a fairy or a whole meadow.

Important limitation: there is no server-side chat gate on this server. Both
setMute (on the fairy) and setMute (on the meadow) are messages the client acts
on -- ChatManager.changeMuteStatus and DistributedMeadow.setMute respectively --
and nothing here drops an incoming setTalk. A modified client can talk straight
through a mute, and a mute does not survive a relog, because setMute carries no
`db` keyword and so is never written to the fairy document.

These are wired up because the client half genuinely works and is worth being
able to exercise. Do not treat them as moderation.
"""

from game.fairies.magicwords.registry import command

MUTED = 1
UNMUTED = 0


@command("mute-fairy", "mute-fairy <fairy>")
def muteFairy(ctx) -> str:
    return _setFairyMute(ctx, MUTED)


@command("unmute-fairy", "unmute-fairy <fairy>")
def unmuteFairy(ctx) -> str:
    return _setFairyMute(ctx, UNMUTED)


# The client offers a "special" unmute as a separate command. On this server
# there is only one kind of mute to lift, so it does the same thing; it stays
# registered so the console command doesn't come back "unknown magic word".
@command("special-unmute-fairy", "special-unmute-fairy <fairy>")
def specialUnmuteFairy(ctx) -> str:
    return _setFairyMute(ctx, UNMUTED)


def _setFairyMute(ctx, mute: int) -> str:
    target = ctx.onlineTarget(0)

    # setMute is owner-directed: only the muted fairy's own client needs to know,
    # since it is their chat input that gets disabled.
    target.d_setMute(mute)

    what = "muted" if mute else "unmuted"

    return f"{what} fairy {target.doId} (client-side only -- clears on relog)"


@command("mute-meadow", "mute-meadow")
def muteMeadow(ctx) -> str:
    return _setMeadowMute(ctx, MUTED)


@command("unmute-meadow", "unmute-meadow")
def unmuteMeadow(ctx) -> str:
    return _setMeadowMute(ctx, UNMUTED)


def _setMeadowMute(ctx, mute: int) -> str:
    meadow = ctx.air.zoneToMeadow.get(ctx.avatar.zoneId)

    if meadow is None:
        ctx.fail(f"zone {ctx.avatar.zoneId} is not a meadow")

    # setMute on DistributedMeadow is `broadcast`, so this reaches everyone
    # standing in the zone, not just the GM who asked.
    meadow.sendUpdate("setMute", [mute])

    what = "muted" if mute else "unmuted"

    return f"{what} meadow {ctx.avatar.zoneId} for everyone in it"
