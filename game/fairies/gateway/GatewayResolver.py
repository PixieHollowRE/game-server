from collections.abc import Iterable
from copy import deepcopy

from direct.directnotify import DirectNotifyGlobal

from game.fairies.gateway.GatewayConstants import GATEWAYS
from game.fairies.gateway.holidays import HOLIDAY_MODULES

notify = DirectNotifyGlobal.directNotify.newCategory("GatewayResolver")


def resolve_gateways(activeTags: Iterable[str]) -> dict[int, list[dict]]:
    """GATEWAYS with every live holiday's overrides applied, base left untouched."""
    active = set(activeTags)
    resolved = deepcopy(GATEWAYS)

    for module in HOLIDAY_MODULES:
        if module.TAG not in active:
            continue

        for zoneId, entries in module.OVERRIDES.items():
            zone = resolved.setdefault(zoneId, [])

            for entry in entries:
                _apply(module.TAG, zoneId, zone, entry)

    return resolved


def _apply(tag: str, zoneId: int, zone: list[dict], entry: dict) -> None:
    target = entry["targetZoneID"]
    index = next((i for i, gw in enumerate(zone) if gw["targetZoneID"] == target), None)

    if entry.get("remove"):
        if index is None:
            notify.warning(f"{tag}: no gateway in zone {zoneId} to {target} to remove")
        else:
            del zone[index]
        return

    if index is None:
        missing = {"name", "position", "targetLocationName"} - entry.keys()

        if missing:
            notify.warning(f"{tag}: new gateway {zoneId}->{target} lacks {sorted(missing)}")
            return

        zone.append(dict(entry))
        return

    zone[index].update(entry)
