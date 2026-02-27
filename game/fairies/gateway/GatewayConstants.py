from game.fairies.ai import ZoneConstants

GATEWAYS: dict[int, list[dict]] = {
    ZoneConstants.ACORN_SUMMIT: [
        {
            # Fairy Fireworks
            "name": "9024",
            "position": (460, 52),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.FAIRY_FIREWORKS_GAME,
            "rewardList": [8001, 8002, 8013],
        },
        {
            # Vidia's Daily Spin
            "name": "9228",
            "position": (967, 185),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.VIDIAS_DAILY_SPIN,
        },
        {
            # Summit Style
            "name": "9023",
            "position": (964, 402),
            "targetLocationName": "shopEntrance",
            "targetZoneID": ZoneConstants.SUMMIT_STYLE,
        },
        {
            # Pumpkin Patch
            "name": "9201",
            "position": (70, 870),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.PUMPKIN_PATCH,
        },
        {
            # Maple Tree Hill
            "name": "9072",
            "position": (900, 920),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.MAPLE_TREE_HILL,
        },
        {
            # Cottonpuff Field
            "name": "9080",
            "position": (1460, 800),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
        {
            # Snowcap Glade
            "name": "9108",
            "position": (1650, 300),
            "targetLocationName": "fromAcornSummit",
            "targetZoneID": ZoneConstants.SNOWCAP_GLADE,
        },
    ],
    ZoneConstants.HAVENDISH_SQUARE: [
        {
            # Fairy Coliseum
            "name": "9274",
            "position": (65, 90),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAIRY_COLISEUM,
        },
        {
            # Cottonpuff Field
            "name": "9083",
            "position": (2, 314),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.COTTONPUFF_FIELD,
        },
        {
            # Queen's Boutique
            "name": "9282",
            "position": (40, 23),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.QUEENS_BOUTIQUE,
        },
        {
            # Cassie's Costume Shop
            "name": "9214",
            "position": (270, 100),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.CASSIES_COSTUME_SHOP,
        },
        {
            # Pixie Dust Mill
            "name": "9267",
            "position": (290, 1160),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PIXIE_DUST_MILL,
        },
        {
            # Fairy Tale Theater
            "name": "9179",
            "position": (851, 439),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAIRY_TALE_THEATER,
        },
        {
            # Neverfruit Grove
            "name": "9161",
            "position": (990, 1145),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.NEVERFRUIT_GROVE,
        },
        {
            # Ballroom
            "name": "9188",
            "position": (1272, 388),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.THE_BALLROOM,
        },
        {
            # Pixie Postings
            "name": "9206", # 9206 (Spring), 9225 (Summer), 9181 (Autumn), 9183 (Winter)
            "position": (1635, 949),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.PIXIE_POSTINGS,
        },
        {
            # Tearoom
            "name": "9180",
            "position": (2001, 457),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.THE_TEAROOM,
        },
        {
            # Springtime Orchard
            "name": "9028",
            "position": (1995, 760),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SPRINGTIME_ORCHARD,
        },
    ],
    ZoneConstants.QUEENS_BOUTIQUE: [
        {
            # Havendish Square
            "name": "9283",
            "position": (209, 336),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.FAIRY_TALE_THEATER: [
        {
            # Havendish Square
            "name": "9174",
            "position": (0, 310),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Cassie's Costume Shop
            "name": "9169",
            "position": (1173, 176),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.CASSIES_COSTUME_SHOP,
        },
    ],
    ZoneConstants.CASSIES_COSTUME_SHOP: [
        {
            # Fairy Tale Theater
            "name": "9198",
            "position": (252, 248),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAIRY_TALE_THEATER,
        },
    ],
    ZoneConstants.THE_BALLROOM: [
        {
            # Havendish Square
            "name": "9186",
            "position": (750, 305),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.THE_TEAROOM: [
        {
            # Havendish Square
            "name": "9185",
            "position": (61, 57),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.LIZZYS_HOUSE: [
        {
            # Havendish Square
            "name": "9237",
            "position": (46, 140),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
    ZoneConstants.FAIRY_COLISEUM: [
        {
            # Havendish Square
            "name": "9174",
            "position": (35, 253),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
        {
            # Marina's Place
            "name": "9273",
            "position": (360, 482),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.MARINAS_PLACE,
        },
        {
            # Zephyr's Zoom Room
            "name": "9276",
            "position": (762, 219),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.ZEPHYRS_ZOOM_ROOM,
        },
    ],
    ZoneConstants.ZEPHYRS_ZOOM_ROOM: [
        {
            # Fairy Coliseum
            "name": "9277",
            "position": (175, 303),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.FAIRY_COLISEUM,
        },
    ],
    ZoneConstants.EVERGREEN_OVERLOOK: [
        {
            # Chilly Falls
            "name": "9120",
            "position": (840, 398),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.CHILLY_FALLS,
        },
        {
            # Kits
            "name": "9280",
            "position": (908, 1082),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.KITS_PLACE,
        },
        {
            # Snowflake Sweep
            "name": "9125",
            "position": (645, 1500),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SNOWFLAKE_SWEEP_GAME,
            "rewardList": [8003, 8015, 8016],
        },
        {
            # Snowcap Glade
            "name": "9114",
            "position": (35, 1618),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.SNOWCAP_GLADE,
        },
        {
            # Havendish Square
            "name": "9177",
            "position": (875, 1600),
            "targetLocationName": "",
            "targetZoneID": ZoneConstants.HAVENDISH_SQUARE,
        },
    ],
}
