from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.PurchaseType import PurchaseType
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.EMBERS_ESSENTIALS,
    shopId=1002,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.EMBER,
        position=(433, 432),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_EMBER
    ),
    collections=[
        ShopCollection(
            collectionId=1019, # Shelves, Sacks, and Storage
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=6504, price=17, goldPrice=5, color1=258, color2=152), # Spearmint Green Nutshell Bookcase
                ShopItem(itemId=6534, price=17, goldPrice=5, color1=154, color2=154), # Beetle Brown Waterdrop Wall Shelf
                ShopItem(itemId=6570, price=10, goldPrice=3, color1=152, color2=6), # Pale Purple Glittery Jars
                ShopItem(itemId=6584, price=27, goldPrice=8, color1=258, color2=99), # Spearmint Green Hardwood Hutch
                ShopItem(itemId=6589, price=17, goldPrice=5, color1=99, color2=99), # Papyrus Tan Stack 'Em High Shelves
                ShopItem(itemId=6626, price=17, goldPrice=5, color1=84, color2=215), # Copper Brown Great Gears Shelves with Pewter Gray Trim
                ShopItem(itemId=6630, price=27, goldPrice=8, color1=108, color2=108), # Creamy Tan Farmhouse Hutch
                ShopItem(itemId=6645, price=17, goldPrice=5, color1=207, color2=0), # Diamond Blue Chilly Shelves
                ShopItem(itemId=6677, price=17, goldPrice=5, color1=236, color2=0), # Dusty Brown Trophy Case
                ShopItem(itemId=6703, price=27, goldPrice=8, color1=227, color2=0), # Moonlight Gray Silver Trees Bookshelf
                ShopItem(itemId=6723, price=17, goldPrice=5, color1=45, color2=59), # Strawberry Red Wacky Bookshelf
                ShopItem(itemId=7501, price=10, goldPrice=3, color1=139, color2=0), # Seedling Green Butterfly Bowl
                ShopItem(itemId=7510, price=10, goldPrice=3, color1=215, color2=0), # Pewter Gray Tin Thimble
                ShopItem(itemId=7522, price=10, goldPrice=3, color1=267, color2=0), # Celestial Blue Jewel Box
                ShopItem(itemId=7548, price=10, goldPrice=3, color1=89, color2=0), # Seashore Brown Autumn Harvest Bag
                ShopItem(itemId=7670, price=10, goldPrice=3, color1=152, color2=28), # Pale Purple Deluxe Egg Basket
                ShopItem(itemId=7684, price=10, goldPrice=3, color1=89, color2=142), # Seashore Brown Sweet Bee Pots
                ShopItem(itemId=7700, price=17, goldPrice=5, color1=28, color2=258), # Cinnamon Brown Sunset Chest
                ShopItem(itemId=7714, price=10, goldPrice=3, color1=5, color2=54), # Wysteria Purple Seashell Jewelry Boxes
                ShopItem(itemId=7508, price=10, goldPrice=3, color1=28, color2=0), # Cinnamon Brown Lavender Sachet
                ShopItem(itemId=6519, price=10, goldPrice=3, color1=99, color2=0), # Papyrus Tan Seashell Shelf
                ShopItem(itemId=6520, price=10, goldPrice=3, color1=99, color2=0), # Papyrus Tan Driftwood Mantle
                ShopItem(itemId=6539, price=10, goldPrice=3, color1=99, color2=189), # Papyrus Tan Four-Peg Oak Hanger
                ShopItem(itemId=7512, price=10, goldPrice=3, color1=154, color2=0), # Beetle Brown Woven Basket
                ShopItem(itemId=7569, price=10, goldPrice=3, color1=99, color2=8), # Papyrus Tan Egg Collector Basket
            ],
        ),
    ],
)