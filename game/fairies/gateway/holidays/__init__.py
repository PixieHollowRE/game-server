"""
Holiday overrides for GATEWAYS, one file per holiday.

A holiday file defines two names:

    TAG        the HolidayManagerUD tag that switches it on
    OVERRIDES  {zoneId: [entry, ...]}, patched over GatewayConstants.GATEWAYS

Entries are matched to the base gateway in the same zone by targetZoneID (the
"sign in zone X that leads to Y"; unique per zone in GATEWAYS). Then:

    {"targetZoneID": Y, "position": (x, y)}    patch: only the keys given change
    {"targetZoneID": Y, "remove": True}        the gateway is gone for the holiday
    {...every field...}                        no base match: a new gateway

To add a holiday, drop a file here and list its module in HOLIDAY_MODULES.
"""

# Applied in this order, so a later holiday wins where two touch the same gateway.
HOLIDAY_MODULES = (

)
