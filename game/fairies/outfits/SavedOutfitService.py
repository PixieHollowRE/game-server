"""Mongo persistence and DC wire packing for saved outfit presets."""

from __future__ import annotations

from typing import Any

# Client tabs = (maxOutfitSlots + 1) // 2  (SavedOutfits.as redisplayTabs)
# Valid stored values are odd: 1, 3, 5, …, 27  (= MAX_OUTFIT_TABS * 2 - 1)
SAVED_OUTFIT_SLOT_MAX = 27
SAVED_OUTFIT_SLOT_PURCHASE_STEP = 2
SAVED_OUTFIT_SLOT_DEFAULT = 1
SAVED_OUTFIT_SLOT_ITEM_ID = 90001
SAVED_OUTFIT_SLOT_PRICE = 10
MTX_ITEM_ID = 8499

SLOT_KEYS = ("head", "necklace", "shirt", "belt", "skirt", "wrist", "ankle", "shoes")
_PLAYER_SLOT_ATTRS = (
    ("head", "headItem"),
    ("necklace", "necklace"),
    ("shirt", "chestItem"),
    ("belt", "belt"),
    ("skirt", "skirt"),
    ("wrist", "wrist"),
    ("ankle", "ankle"),
    ("shoes", "shoes"),
)
_VALID_LOCATIONS = frozenset({"Wardrobe", "Equipped"})

_SAVED_OUTFIT_DOC_FIELDS = {
    "_id": 1,
    "maxOutfitSlots": 1,
    "savedOutfits": 1,
    "avatar.items": 1,
}


def empty_slot() -> dict[str, int]:
    return {
        "inv_id": 0,
        "item_id": 0,
        "color1": 0,
        "color2": 0,
        "how_acquired": 0,
    }


def normalize_max_outfit_slots(max_slots: int) -> int:
    """Clamp and snap to valid client wire values (odd: 1, 3, 5, …)."""
    value = int(max_slots)
    if value < SAVED_OUTFIT_SLOT_DEFAULT:
        value = SAVED_OUTFIT_SLOT_DEFAULT
    if value > SAVED_OUTFIT_SLOT_MAX:
        value = SAVED_OUTFIT_SLOT_MAX
    if value > 1 and value % 2 == 0:
        value = min(value + 1, SAVED_OUTFIT_SLOT_MAX)
    return value


def ensure_defaults(doc: dict[str, Any]) -> dict[str, Any]:
    raw_max = doc.get("maxOutfitSlots")
    max_slots = normalize_max_outfit_slots(
        int(raw_max if raw_max is not None else SAVED_OUTFIT_SLOT_DEFAULT)
    )

    outfits = doc.get("savedOutfits")
    if outfits is None:
        outfits = []
    elif not isinstance(outfits, list):
        outfits = []

    return {
        "maxOutfitSlots": max_slots,
        "savedOutfits": outfits,
    }


def load_saved_outfit_doc(air, av_id: int) -> dict[str, Any]:
    doc = air.mongoInterface.mongodb.fairies.find_one(
        {"_id": av_id},
        _SAVED_OUTFIT_DOC_FIELDS,
    )
    if not doc:
        return ensure_defaults({})
    full = dict(doc)
    full.update(ensure_defaults(full))
    return full


def persist_saved_outfit_state(
    air,
    av_id: int,
    *,
    max_outfit_slots: int | None = None,
    saved_outfits: list | None = None,
) -> None:
    fields: dict[str, Any] = {}
    if max_outfit_slots is not None:
        fields["maxOutfitSlots"] = int(max_outfit_slots)
    if saved_outfits is not None:
        fields["savedOutfits"] = saved_outfits
    if not fields:
        return

    air.mongoInterface.mongodb.fairies.update_one(
        {"_id": av_id},
        {"$set": fields},
        upsert=True,
    )


def _avatar_items(doc: dict[str, Any]) -> list[dict[str, Any]]:
    avatar = doc.get("avatar") or {}
    items = avatar.get("items")
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def _live_equipped_inv_ids(player) -> set[int]:
    inv_ids: set[int] = set()
    for _slot_key, attr in _PLAYER_SLOT_ATTRS:
        lite = getattr(player, attr, None)
        if lite is None:
            continue
        inv_id = int(getattr(lite, "invId", 0) or 0)
        if inv_id:
            inv_ids.add(inv_id)
    return inv_ids


def _merge_avatar_items_with_player(
    avatar_items: list[dict[str, Any]],
    player,
) -> list[dict[str, Any]]:
    by_inv: dict[int, dict[str, Any]] = {}
    for item in avatar_items:
        inv_id = int(item.get("inv_id") or 0)
        if inv_id:
            by_inv[inv_id] = dict(item)

    for _slot_key, attr in _PLAYER_SLOT_ATTRS:
        lite = getattr(player, attr, None)
        if lite is None:
            continue
        inv_id = int(getattr(lite, "invId", 0) or 0)
        if not inv_id:
            continue

        merged = dict(by_inv.get(inv_id) or {})
        merged.update(
            {
                "inv_id": inv_id,
                "item_id": int(getattr(lite, "itemId", 0) or 0),
                "color1": int(getattr(lite, "color1", 0) or 0),
                "color2": int(getattr(lite, "color2", 0) or 0),
                "location": "Equipped",
            }
        )
        if "how_acquired" not in merged:
            merged["how_acquired"] = int(merged.get("howAcquired") or 0)
        by_inv[inv_id] = merged

    return list(by_inv.values())


def _resolved_avatar_items(doc: dict[str, Any], player=None) -> list[dict[str, Any]]:
    items = _avatar_items(doc)
    if player is None:
        return items
    return _merge_avatar_items_with_player(items, player)


def _find_avatar_item(avatar_items: list[dict[str, Any]], inv_id: int) -> dict[str, Any] | None:
    if not inv_id:
        return None
    for item in avatar_items:
        if int(item.get("inv_id") or 0) == int(inv_id):
            return item
    return None


def build_lite_inv_item(
    avatar_items: list[dict[str, Any]],
    inv_id: int,
    *,
    player=None,
) -> tuple[int, int, int, int, int]:
    if not inv_id:
        return (0, 0, 0, 0, 0)

    item = _find_avatar_item(avatar_items, inv_id)
    if item is None and player is not None and inv_id in _live_equipped_inv_ids(player):
        for _slot_key, attr in _PLAYER_SLOT_ATTRS:
            lite = getattr(player, attr, None)
            if lite is None or int(getattr(lite, "invId", 0) or 0) != int(inv_id):
                continue
            return (
                inv_id,
                int(getattr(lite, "itemId", 0) or 0),
                int(getattr(lite, "color1", 0) or 0),
                int(getattr(lite, "color2", 0) or 0),
                0,
            )

    if item is None:
        return (0, 0, 0, 0, 0)

    location = item.get("location") or ""
    if location not in _VALID_LOCATIONS and not (
        player is not None and inv_id in _live_equipped_inv_ids(player)
    ):
        return (0, 0, 0, 0, 0)

    return (
        int(item.get("inv_id") or 0),
        int(item.get("item_id") or 0),
        int(item.get("color1") or 0),
        int(item.get("color2") or 0),
        int(item.get("how_acquired") or item.get("howAcquired") or 0),
    )


def _slot_doc_from_lite(lite: tuple[int, int, int, int, int]) -> dict[str, int]:
    return {
        "inv_id": lite[0],
        "item_id": lite[1],
        "color1": lite[2],
        "color2": lite[3],
        "how_acquired": lite[4],
    }


def validate_inv_ids(
    avatar_items: list[dict[str, Any]],
    inv_ids: list[int],
    *,
    player=None,
) -> bool:
    live_ids = _live_equipped_inv_ids(player) if player is not None else set()
    for inv_id in inv_ids:
        if not inv_id:
            continue
        if inv_id in live_ids:
            continue
        item = _find_avatar_item(avatar_items, inv_id)
        if item is None:
            return False
        if (item.get("location") or "") not in _VALID_LOCATIONS:
            return False
    return True


def snapshot_outfit_from_inv_ids(
    avatar_items: list[dict[str, Any]],
    outfit_id: int,
    inv_ids: list[int],
    *,
    player=None,
) -> dict[str, Any]:
    outfit: dict[str, Any] = {"outfit_id": int(outfit_id)}
    for key, inv_id in zip(SLOT_KEYS, inv_ids):
        lite = build_lite_inv_item(avatar_items, inv_id, player=player)
        outfit[key] = _slot_doc_from_lite(lite)
    return outfit


def pack_lite_inv_for_client(slot: dict[str, Any] | None) -> tuple[int, int, int, int, int]:
    if not isinstance(slot, dict):
        return (0, 0, 0, 0, 0)
    return (
        int(slot.get("inv_id") or 0),
        int(slot.get("item_id") or 0),
        int(slot.get("color1") or 0),
        int(slot.get("color2") or 0),
        int(slot.get("how_acquired") or slot.get("howAcquired") or 0),
    )


def pack_saved_outfit_for_client(outfit: dict[str, Any]) -> tuple[Any, ...]:
    return (
        int(outfit.get("outfit_id") or 0),
        pack_lite_inv_for_client(outfit.get("head")),
        pack_lite_inv_for_client(outfit.get("necklace")),
        pack_lite_inv_for_client(outfit.get("shirt")),
        pack_lite_inv_for_client(outfit.get("belt")),
        pack_lite_inv_for_client(outfit.get("skirt")),
        pack_lite_inv_for_client(outfit.get("wrist")),
        pack_lite_inv_for_client(outfit.get("ankle")),
        pack_lite_inv_for_client(outfit.get("shoes")),
    )


def pack_saved_outfits_for_client(doc: dict[str, Any]) -> list[tuple[Any, ...]]:
    state = ensure_defaults(doc)
    outfits = state.get("savedOutfits") or []
    if not isinstance(outfits, list):
        return []
    return [pack_saved_outfit_for_client(outfit) for outfit in outfits if isinstance(outfit, dict)]


def get_max_outfit_slots(doc: dict[str, Any]) -> int:
    return ensure_defaults(doc)["maxOutfitSlots"]


def client_outfit_tabs(max_outfit_slots: int) -> int:
    """Unlocked Saved Outfits tabs — matches SavedOutfits.as floor((max+1)/2)."""
    return (int(max_outfit_slots) + 1) // 2


def resolve_monotonic_max_outfit_slots(
    mongo_max: int,
    client_high_water: int | None,
    *,
    force: bool = False,
) -> tuple[int, bool]:
    """Return (value_to_send, suppressed_stale_lower_value)."""
    if force or client_high_water is None:
        return mongo_max, False
    if mongo_max < client_high_water:
        return client_high_water, True
    return mongo_max, False


def lookup_item_for_equip(air, av_id: int, inv_id: int) -> dict[str, Any] | None:
    if not inv_id:
        return None

    doc = load_saved_outfit_doc(air, av_id)
    item = _find_avatar_item(_avatar_items(doc), inv_id)
    if item is not None:
        return dict(item)

    for outfit in ensure_defaults(doc).get("savedOutfits") or []:
        if not isinstance(outfit, dict):
            continue
        for slot_key in SLOT_KEYS:
            slot = outfit.get(slot_key)
            if not isinstance(slot, dict):
                continue
            if int(slot.get("inv_id") or 0) != int(inv_id):
                continue
            return {
                "inv_id": int(slot.get("inv_id") or 0),
                "item_id": int(slot.get("item_id") or 0),
                "color1": int(slot.get("color1") or 0),
                "color2": int(slot.get("color2") or 0),
                "howAcquired": int(slot.get("how_acquired") or 0),
                "location": "Wardrobe",
                "slot": 0,
            }
    return None


def add_saved_outfit(
    air,
    av_id: int,
    inv_ids: list[int],
    player=None,
) -> tuple[dict[str, Any] | None, str | None]:
    doc = load_saved_outfit_doc(air, av_id)
    state = ensure_defaults(doc)
    avatar_items = _resolved_avatar_items(doc, player)

    if len(state["savedOutfits"]) >= state["maxOutfitSlots"]:
        return None, "slots_full"

    if not validate_inv_ids(avatar_items, inv_ids, player=player):
        return None, "invalid_inv_ids"

    outfit_id = air.mongoInterface.getNextDoId()
    outfit = snapshot_outfit_from_inv_ids(avatar_items, outfit_id, inv_ids, player=player)
    saved_outfits = list(state["savedOutfits"])
    saved_outfits.append(outfit)

    persist_saved_outfit_state(air, av_id, saved_outfits=saved_outfits)
    return {
        "maxOutfitSlots": state["maxOutfitSlots"],
        "savedOutfits": saved_outfits,
    }, None


def update_saved_outfit(
    air,
    av_id: int,
    outfit_id: int,
    inv_ids: list[int],
    player=None,
) -> tuple[dict[str, Any] | None, str | None]:
    doc = load_saved_outfit_doc(air, av_id)
    state = ensure_defaults(doc)
    avatar_items = _resolved_avatar_items(doc, player)

    if not validate_inv_ids(avatar_items, inv_ids, player=player):
        return None, "invalid_inv_ids"

    saved_outfits = list(state["savedOutfits"])
    index = next(
        (i for i, outfit in enumerate(saved_outfits) if int(outfit.get("outfit_id") or 0) == int(outfit_id)),
        None,
    )
    if index is None:
        return None, "unknown_outfit_id"
    if index >= state["maxOutfitSlots"]:
        return None, "beyond_max_slots"

    saved_outfits[index] = snapshot_outfit_from_inv_ids(
        avatar_items,
        outfit_id,
        inv_ids,
        player=player,
    )
    persist_saved_outfit_state(air, av_id, saved_outfits=saved_outfits)
    return {
        "maxOutfitSlots": state["maxOutfitSlots"],
        "savedOutfits": saved_outfits,
    }, None


def remove_saved_outfits(air, av_id: int, outfit_ids: list[int]) -> dict[str, Any]:
    doc = load_saved_outfit_doc(air, av_id)
    state = ensure_defaults(doc)
    remove_set = {int(outfit_id) for outfit_id in outfit_ids if outfit_id}
    saved_outfits = [
        outfit
        for outfit in state["savedOutfits"]
        if int(outfit.get("outfit_id") or 0) not in remove_set
    ]
    persist_saved_outfit_state(air, av_id, saved_outfits=saved_outfits)
    return {
        "maxOutfitSlots": state["maxOutfitSlots"],
        "savedOutfits": saved_outfits,
    }


def extract_outfit_ids(long_types: list) -> list[int]:
    outfit_ids: list[int] = []
    for entry in long_types or []:
        if isinstance(entry, dict):
            value = entry.get("longVal", entry.get("longval"))
            if value is None and len(entry) == 1:
                value = next(iter(entry.values()))
            outfit_ids.append(int(value or 0))
        elif isinstance(entry, (list, tuple)) and entry:
            outfit_ids.append(int(entry[0]))
        elif hasattr(entry, "longVal"):
            outfit_ids.append(int(getattr(entry, "longVal", 0) or 0))
        else:
            outfit_ids.append(int(entry or 0))
    return [outfit_id for outfit_id in outfit_ids if outfit_id]


def get_outfit_slot_price(current_max: int) -> int:
    """Flat 10 diamonds — matches SavedOutfits.SLOT_COST in panel SWF."""
    if current_max >= SAVED_OUTFIT_SLOT_MAX:
        return SAVED_OUTFIT_SLOT_PRICE
    return SAVED_OUTFIT_SLOT_PRICE


def purchase_outfit_slot(air, av_id: int, player) -> int | None:
    doc = load_saved_outfit_doc(air, av_id)
    state = ensure_defaults(doc)
    current_max = state["maxOutfitSlots"]
    price = get_outfit_slot_price(current_max)

    if current_max >= SAVED_OUTFIT_SLOT_MAX:
        return None

    if not player.takeGold(price):
        return None

    new_max = min(current_max + SAVED_OUTFIT_SLOT_PURCHASE_STEP, SAVED_OUTFIT_SLOT_MAX)
    persist_saved_outfit_state(air, av_id, max_outfit_slots=new_max)
    return new_max
