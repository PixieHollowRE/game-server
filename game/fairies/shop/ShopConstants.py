from game.fairies.ai import ZoneConstants
from game.fairies.fairy import FamousFairyData

SHOPS: dict[int, dict] = {
    ZoneConstants.GALES_OUTFITTERS: {
        "shopID": 3,
        "name": FamousFairyData.GALE,
        "fairyDNA": FamousFairyData.GALE_DNA,
        "position": (434, 429),
        "famousFairyID": FamousFairyData.FAMOUS_FAIRY_GALE,
    },
    ZoneConstants.CASSIES_COSTUME_SHOP: {
        "shopID": 4,
        "name": FamousFairyData.CASSIE,
        "fairyDNA": FamousFairyData.CASSIE_DNA,
        "position": (500, 350),
        "famousFairyID": FamousFairyData.FAMOUS_FAIRY_CASSIE,
    },
    ZoneConstants.PRISMS_PIXIE_SPA: {
        "shopID": 9000,
        "name": FamousFairyData.PRISM,
        "fairyDNA": FamousFairyData.PRISM_DNA,
        "position": (290, 460),
        "famousFairyID": FamousFairyData.FAMOUS_FAIRY_PRISM,
    }
}
