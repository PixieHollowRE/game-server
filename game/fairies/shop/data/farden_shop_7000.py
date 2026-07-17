from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.GARDEN_SUPPLY,
    shopId=7000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.BROOK,
        position=(418, 453),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_BROOK
    ),
    collections=[
        ShopCollection(
            collectionId=119, # Basic Seeds
            items=[
                ShopItem(itemId=89002, goldPrice=1), # Dulcie's Cookie Seeds
                ShopItem(itemId=89017, goldPrice=1), # Dulcie's Truffle Seeds
                ShopItem(itemId=89001, goldPrice=1), # Colorful Sweet Seeds
                ShopItem(itemId=89023, goldPrice=1), # Rainbow Sweet Seeds
                ShopItem(itemId=89018, goldPrice=1), # Sweet Trails Seeds
                ShopItem(itemId=89031, goldPrice=1), # Summer Sweets Seeds
            ],
        ),
        ShopCollection(
            collectionId=118, # Special Edition Seeds
            items=[
                ShopItem(itemId=89009, goldPrice=1), # Garden Premier Seeds
                ShopItem(itemId=89022, goldPrice=1), # Autumn Breeze Seeds
                ShopItem(itemId=89021, goldPrice=1), # Winter Wardrobe Seeds
                ShopItem(itemId=89030, goldPrice=1), # Spring Style Seeds
                ShopItem(itemId=89038, goldPrice=1), # Summer Chic Seeds
            ],
        ),
        ShopCollection(
            collectionId=132, # Summer 2012 Seeds
            items=[
                ShopItem(itemId=89004, goldPrice=1), # Fancy Flower Seeds
                ShopItem(itemId=89000, goldPrice=1), # Rainbow Dye Seeds
                ShopItem(itemId=89006, goldPrice=1), # Teatime Seeds
                ShopItem(itemId=89008, goldPrice=1), # Little Gardener Seeds
                ShopItem(itemId=89005, goldPrice=1), # To-Fly-For Top Seeds
                ShopItem(itemId=89007, goldPrice=1), # Skirt or Slacks Seeds
                ShopItem(itemId=89003, goldPrice=1), # Stylish Shoe Seeds
            ],
        ),
        ShopCollection(
            collectionId=131, # Fall 2012 Seeds
            items=[
                ShopItem(itemId=89014, goldPrice=1), # Autumn Masquerade Dye Seeds
                ShopItem(itemId=89019, goldPrice=1), # Autumn Harvest Seeds
            ],
        ),
        ShopCollection(
            collectionId=130, # Winter 2012 Seeds
            items=[
                ShopItem(itemId=89012, goldPrice=1), # Chilly Plants Seeds
                ShopItem(itemId=89013, goldPrice=1), # Winter Wonderland Dye Seeds
                ShopItem(itemId=89016, goldPrice=1), # Tink's Decorating Seeds
                ShopItem(itemId=89010, goldPrice=1), # Festive Ornament Seeds
                ShopItem(itemId=89011, goldPrice=1), # Flitterific Tops Seeds
                ShopItem(itemId=89015, goldPrice=1), # Flitterific Skirt or Slacks Seeds
                ShopItem(itemId=89020, goldPrice=1), # Flitterific Shoe Seeds
            ],
        ),
        ShopCollection(
            collectionId=129, # Spring 2013 Seeds
            items=[
                ShopItem(itemId=89029, goldPrice=1), # Springtime Flower Seeds
                ShopItem(itemId=89028, goldPrice=1), # Never Dove Egg Dye Seeds
                ShopItem(itemId=89027, goldPrice=1), # Clover Comfort Seeds
                ShopItem(itemId=89024, goldPrice=1), # Springtime Top Seeds
                ShopItem(itemId=89025, goldPrice=1), # Springtime Skirt or Slacks Seeds
                ShopItem(itemId=89026, goldPrice=1), # Springtime Shoe Seeds
            ],
        ),
        ShopCollection(
            collectionId=120, # Summer 2013 Seeds
            items=[
                ShopItem(itemId=89033, goldPrice=1), # Sprightly Sprouts Seeds
                ShopItem(itemId=89032, goldPrice=1), # Midsummer Dye Seeds
                ShopItem(itemId=89035, goldPrice=1), # Blooming Benches Seeds
                ShopItem(itemId=89036, goldPrice=1), # Tropical Tops Seeds
                ShopItem(itemId=89037, goldPrice=1), # Sunny Skirt or Slacks Seeds
                ShopItem(itemId=89034, goldPrice=1), # Summertime Shoes Seeds
            ],
        ),
    ],
)