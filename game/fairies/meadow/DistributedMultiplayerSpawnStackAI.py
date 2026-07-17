"""
Multiplayer bunch — a spawn stack that rewards everyone who joins in.

Unlike a plain stack (collected instantly by whoever clicks first), a bunch runs
a shared countdown. The first click starts the timer and adds that fairy to the
recipient list; every fairy who clicks before it expires joins too. When the
timer hits zero, every recipient is paid out, scaled by how many joined:

    multiplier = min(len(recipients), MAX_MULTIPLIER)

so five fairies working the same bunch each walk away with five times the items.
The client mirrors this formula in DistributedMultiplayerSpawnStack.multiplier
to render the "item x N" bubble over each recipient, so the two must agree.

Only ingredients with a bunch asset in spawnableAssets.xml <spawnableIdRemaps>
can be spawned this way — the client remaps our itemID to the bunch art itself.
We always broadcast the base ingredient ID; the remap is the client's job.
"""
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from direct.task.TaskManagerGlobal import taskMgr

from game.fairies.meadow.DistributedSpawnStackAI import DistributedSpawnStackAI

# Matches DistributedMultiplayerSpawnStack.MAX_MULTIPLIER on the client.
MAX_MULTIPLIER = 5

# Seconds the countdown runs, as in the original game. The client plays its
# countdown sting once half of this has elapsed.
COUNTDOWN_SEC = 10

# Client treats -1 as "no timer yet" and 0 as "expired, remove me".
COUNTDOWN_IDLE = -1
COUNTDOWN_EXPIRED = 0


class DistributedMultiplayerSpawnStackAI(DistributedSpawnStackAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMultiplayerSpawnStackAI")

    def __init__(self, air) -> None:
        super().__init__(air)

        self.countdown: int = COUNTDOWN_IDLE
        self.recipients: list[int] = []
        self.countdownTaskName: str | None = None

    def setCountdown(self, countdown: int) -> None:
        self.countdown = countdown

    def getCountdown(self) -> int:
        return self.countdown

    def d_setCountdown(self, countdown: int) -> None:
        self.sendUpdate("setCountdown", [countdown])

    def b_setCountdown(self, countdown: int) -> None:
        self.setCountdown(countdown)
        self.d_setCountdown(countdown)

    def setRecipients(self, recipients: list[int]) -> None:
        self.recipients = list(recipients)

    def getRecipients(self) -> list[int]:
        return self.recipients

    def d_setRecipients(self, recipients: list[int]) -> None:
        self.sendUpdate("setRecipients", [recipients])

    def b_setRecipients(self, recipients: list[int]) -> None:
        self.setRecipients(recipients)
        self.d_setRecipients(self.recipients)

    def getMultiplier(self) -> int:
        return min(len(self.recipients), MAX_MULTIPLIER)

    def setCollectRequest(self, bogus: int) -> None:
        if self.collected or self.countdown == COUNTDOWN_EXPIRED:
            return

        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(f"No avatar present on AI for setCollectRequest: {avId}")
            return

        if avId in self.recipients:
            return

        self.b_setRecipients(self.recipients + [avId])

        if self.countdown == COUNTDOWN_IDLE:
            self.startCountdown()

    def startCountdown(self) -> None:
        self.b_setCountdown(COUNTDOWN_SEC)

        self.countdownTaskName = "mp-bunch-countdown-%d" % self.doId
        taskMgr.doMethodLater(1.0, self.countdownTask, self.countdownTaskName)

    def stopCountdown(self) -> None:
        if self.countdownTaskName is not None:
            taskMgr.remove(self.countdownTaskName)
            self.countdownTaskName = None

    def countdownTask(self, task: Task) -> int:
        self.b_setCountdown(self.countdown - 1)

        if self.countdown > COUNTDOWN_EXPIRED:
            return Task.again

        self.countdownTaskName = None
        self.awardRecipients()
        return Task.done

    def awardRecipients(self) -> None:
        if self.collected:
            return

        # Latch before paying out: awarding re-enters the AI, and a bunch must
        # never pay a recipient twice.
        self.collected = True

        itemID, multiplier = self.getItemID(), self.getMultiplier()
        itemCount = self.getItemCount() * multiplier

        for avId in self.recipients:
            if avId not in self.air.doId2do:
                # Wandered off to another district before the timer expired.
                continue

            self.air.inventoryManager.addIngredientsToPouchWithPickupFeedback(
                avId, itemID, itemCount, -1
            )

        self.notify.debug(
            "%s awarded %d each to %d recipient(s) (multiplier %d)"
            % (self.name, itemCount, len(self.recipients), multiplier)
        )

        if self.spawnMgr is not None:
            self.spawnMgr.onCollected(self)

    def delete(self) -> None:
        self.stopCountdown()
        super().delete()
