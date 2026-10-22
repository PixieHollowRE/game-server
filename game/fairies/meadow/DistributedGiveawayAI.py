"""
A meadow giveaway -- the free item standing in a meadow that each fairy may
collect exactly once.

Shares DistributedSpawnStack's wire protocol with the ingredient stacks, but
behaves nothing like one. An ingredient stack is a single object that the first
fairy to click takes away; a giveaway is permanent scenery that stays generated
forever and is eligible or not *per fairy*, so none of the base class's spawn
manager, respawn or `collected` latch applies. Both eligibility and collection
are overridden here to answer from the fairy's own collected list instead.

The client drives three exchanges, all of them per fairy:

  afterGenerate -> acquisitionRequest    "is this one I have to be a Member for?"
                <- acquisitionResponse

  afterGenerate -> setEligible(bogus)    "have I already had this one?"
                <- setEligible(0 or 1)   0 greys the art out and kills the click

                -> setCollectRequest     the click itself
                                         (no reply -- the client hides the
                                         giveaway locally the moment it sends)

Because the client removes the art on its own and never asks again, a refusal
here is invisible to the fairy who clicked: they see it vanish and get nothing.
That is only reachable by racing or by a broken reward id, and it is why the
claim is conditional and gets released when the payout fails.
"""

from direct.directnotify import DirectNotifyGlobal

from game.fairies.meadow import GiveawayReward
from game.fairies.meadow.DistributedSpawnStackAI import DistributedSpawnStackAI


class DistributedGiveawayAI(DistributedSpawnStackAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGiveawayAI")

    def __init__(self, air) -> None:
        super().__init__(air)

        self.giveawayID: int = 0
        self.eventID: int = 0
        self.holidayBit: int = 0
        self.itemEventId: int = 0

        # Server-side only; reaches the client as acquisitionResponse.
        self.membersOnly: bool = False

        # Server-side only, and unrelated to setColorIDs (the meadow art)
        self.rewardColor1: int = 0
        self.rewardColor2: int = 0
        self.rewardAmount: int = 1

        # What the fairy's collected list records; 0 falls back to giveawayID
        self.claimId: int = 0
        self.phraseOnly: bool = False

    # ── required fields ──────────────────────────────────────────────────── #

    def setGiveawayID(self, giveawayID: int) -> None:
        self.giveawayID = giveawayID

    def getGiveawayID(self) -> int:
        return self.giveawayID

    def setEventID(self, eventID: int) -> None:
        self.eventID = eventID

    def getEventID(self) -> int:
        return self.eventID

    def setHolidayBit(self, holidayBit: int) -> None:
        self.holidayBit = holidayBit

    def getHolidayBit(self) -> int:
        return self.holidayBit

    def setItemEventId(self, itemEventId: int) -> None:
        self.itemEventId = itemEventId

    def getItemEventId(self) -> int:
        return self.itemEventId

    def setMembersOnly(self, membersOnly: bool) -> None:
        self.membersOnly = membersOnly

    def setRewardColors(self, color1: int, color2: int) -> None:
        self.rewardColor1 = color1
        self.rewardColor2 = color2

    def setRewardAmount(self, amount: int) -> None:
        self.rewardAmount = amount

    def setClaimId(self, claimId: int) -> None:
        self.claimId = claimId

    def setPhraseOnly(self, phraseOnly: bool) -> None:
        self.phraseOnly = phraseOnly

    def _claimKey(self) -> int:
        return self.claimId or self.giveawayID

    # ── client exchanges ─────────────────────────────────────────────────── #

    def acquisitionRequest(self) -> None:
        avId = self.air.getAvatarIdFromSender()

        self.sendUpdateToAvatarId(
            avId, "acquisitionResponse", [1 if self.membersOnly else 0]
        )

    def setEligible(self, bogus: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        collected = GiveawayReward.has_collected(self.air, avId, self._claimKey())

        self.sendUpdateToAvatarId(avId, "setEligible", [0 if collected else 1])

    def setCollectRequest(self, bogus: int) -> None:
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)

        if not avatar:
            self.notify.warning(
                f"No avatar present on AI for setCollectRequest: {avId}"
            )
            return
        
        if self.phraseOnly:
            # A click would skip the basket and range rules
            self.notify.debug(
                "giveaway %d is phrase-only, ignoring click from %d"
                % (self._claimKey(), avId)
            )
            return

        self.collect(avId)

    def collect(self, avId: int) -> bool:
        """
        Claim this giveaway for the fairy and pay it out; True only if both held.
        """
        key = self._claimKey()

        # The claim write is what decides, so it comes before the payout
        if not GiveawayReward.claim(self.air, avId, key):
            self.notify.debug(
                "giveaway %d refused for %d: already collected" % (key, avId)
            )
            return False

        if not GiveawayReward.award(
            self.air,
            avId,
            key,
            self.getItemID(),
            self.rewardColor1,
            self.rewardColor2,
            self.rewardAmount,
        ):
            # Nothing was handed over, so stay eligible to retry once it's fixed
            GiveawayReward.release(self.air, avId, key)
            return False

        self.notify.debug(
            "giveaway %d (reward %d) collected by %d"
            % (key, self.getItemID(), avId)
        )
        return True

    def collectByPhrase(self, avId: int) -> bool:
        """
        Collect for a fairy who didn't click it, then tell their client it's spent.

        A click hides the art client-side; a spoken phrase has nothing to hide, so
        without this the pumpkin it lights would stay lit.
        """
        if not self.collect(avId):
            return False

        self.sendUpdateToAvatarId(avId, "setEligible", [0])
        return True
