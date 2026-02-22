from game.fairies.ai import ZoneConstants

GATEWAYS = {
    ZoneConstants.ACORN_SUMMIT: [
        {
            # Fairy Fireworks
            "name": "9024",
            "position": (460, 52),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAIRY_FIREWORKS_GAME,
            "rewardList": [8001, 8002, 8003]
        },
        {
            # Vidia's Daily Spin
            "name": "9228",
            "position": (967, 185),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.VIDIAS_DAILY_SPIN,
        },
        {
            # Summit Style
            "name": "9023",
            "position": (964, 402),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SUMMIT_STYLE,
        },
        {
            # Pumpkin Patch
            "name": "9201",
            "position": (70, 870),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PUMPKIN_PATCH,
        },
        {
            # Maple Tree Hill
            "name": "9072",
            "position": (900, 920),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.MAPLE_TREE_HILL,
        },
        {
            # Cottonpuff Field
            "name": "9080",
            "position": (1460, 800),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.COTTONPUFF_SQUARE,
        },
        {
            # Snowcap Glade
            "name": "9108",
            "position": (1650, 300),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SNOWCAP_GLADE,
        },
    ],
    ZoneConstants.HAVENDISH_SQUARE: [
        {
            # Springtime Orchard
            "name": "9028",
            "position": (1995, 760),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
    ]
}
