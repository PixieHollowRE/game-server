"""
Trick-or-treating: say the phrase beside a lit pumpkin while wearing the basket.

The client forwards every line the fairy says as setChatMessage and decides
nothing itself, so every rule lives here. Each pumpkin is a chat-phrase hotspot
paired with a DistributedGiveaway whose reward item is the trigger's
eligibleGiveAwayId; collecting that giveaway is what spends the pumpkin.
"""

from direct.directnotify import DirectNotifyGlobal

from game.fairies.badges import badge_events
from game.fairies.meadow import meadow_xml

notify = DirectNotifyGlobal.directNotify.newCategory("TrickOrTreat")

# No original figure survives; "close, not on top of it" is a guess to tune
TRICK_OR_TREAT_RANGE = 50

BASKET_ITEM_ID = 1583

# 1-based position of "wrist" in DistributedFairyPlayerAI.OUTFIT_SLOT_ORDER
BASKET_WRIST_SLOT = 6

PUMPKIN_BODIES: dict[int, tuple[int, int, int, int]] = {
    27660: (56, 163, 193, 438),   # Palm Tree Cove
    27672: (89, 210, 220, 471),   # Acorn Summit
    27673: (109, 215, 241, 479),  # Treetop Bend
    27674: (89, 208, 221, 460),   # Cherryblossom Heights
    27675: (55, 207, 217, 478),   # Chilly Falls
    27676: (85, 204, 232, 487),   # Dewdrop Vale
    27677: (53, 47, 242, 465),    # Evergreen Overlook
    27678: (97, 189, 243, 468),   # Neverberry Thicket
    27679: (111, 216, 241, 480),  # Pumpkin Patch
    27680: (17, 189, 298, 483),   # Snowcap Glade
    27681: (117, 203, 249, 472),  # Springtime Orchard
    27689: (11, 149, 161, 273),   # Neverfruit Grove
}

def isWearingBasket(air, avId: int) -> bool:
    return air.mongoInterface.mongodb.fairies.find_one(
        {
            "_id": avId,
            "avatar.items": {
                "$elemMatch": {
                    "location": "Equipped",
                    "slot": BASKET_WRIST_SLOT,
                    "item_id": BASKET_ITEM_ID,
                }
            },
        },
        {"_id": 1},
    ) is not None

def distanceToPumpkin(position: tuple[int, int], hotspot: meadow_xml.HotspotDef) -> float:
    left, top, right, bottom = PUMPKIN_BODIES.get(hotspot.hotspotId, (0, 0, 0, 0))
    x, y = position

    # Zero inside the body; otherwise the gap to its nearest edge or corner
    dx = max(hotspot.x + left - x, 0, x - (hotspot.x + right))
    dy = max(hotspot.y + top - y, 0, y - (hotspot.y + bottom))

    return (dx * dx + dy * dy) ** 0.5

def findGiveaway(air, zoneId: int, rewardItemId: int):
    for giveaway in air.giveawaySpawnMgr.giveaways:
        if giveaway.zoneId == zoneId and giveaway.getItemID() == rewardItemId:
            return giveaway

    return None

def handleChat(air, avatar, message: str) -> None:
    # The client already trims and lowercases, but a modified one needn't
    phrase = message.strip().lower()
    zoneId = avatar.zoneId

    for trigger in meadow_xml.getChatTriggers(zoneId):
        if (trigger.typeToTrigger == meadow_xml.CHAT_TRIGGER_HOTSPOT
                and phrase in trigger.messages):
            _tryTrigger(air, avatar, zoneId, trigger)

def _tryTrigger(air, avatar, zoneId: int, trigger: meadow_xml.ChatTriggerDef) -> None:
    hotspot = meadow_xml.getHotspot(zoneId, trigger.tagId)

    # None means the holiday's tag isn't live, so there is no pumpkin to speak to
    if hotspot is None or hotspot.clientTrigger != meadow_xml.CLIENT_CHAT_PHRASE:
        notify.info(
            "%d said the phrase in zone %d but tagId %d has no live pumpkin hotspot"
            % (avatar.doId, zoneId, trigger.tagId)
        )
        return

    position = avatar.getPosition()
    distance = distanceToPumpkin(position, hotspot)

    if distance > TRICK_OR_TREAT_RANGE:
        notify.info(
            "%d is %.0f px from pumpkin %d in zone %d (at %s, limit %d)"
            % (avatar.doId, distance, hotspot.hotspotId, zoneId, position,
               TRICK_OR_TREAT_RANGE)
        )
        return

    giveaway = findGiveaway(air, zoneId, trigger.eligibleGiveAwayId)

    if giveaway is None:
        notify.warning(
            "no giveaway with reward %d in zone %d for hotspot %d"
            % (trigger.eligibleGiveAwayId, zoneId, hotspot.hotspotId)
        )
        return

    if not isWearingBasket(air, avatar.doId):
        notify.info("%d is not wearing the trick or treat basket" % avatar.doId)
        return

    if giveaway.collectByPhrase(avatar.doId):
        air.badgeManager.d_accumulate(avatar.doId, badge_events.EVENT_TRICK_OR_TREATED)
    else:
        notify.info(
            "%d already collected the pumpkin in zone %d" % (avatar.doId, zoneId)
        )
