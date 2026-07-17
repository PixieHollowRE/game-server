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
    zone=ZoneConstants.HARMONYS_SWEET_SHOP,
    shopId=8000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.HARMONY,
        position=(417, 455),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_HARMONY,
    ),
    collections=[
        ShopCollection(
            collectionId=146, # Scrumptious Cookies
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22502, goldPrice=1), # Sunflower Cookie
                ShopItem(itemId=22503, goldPrice=1), # Honey Cookie
                ShopItem(itemId=22504, goldPrice=1), # Raspberry Cookie
                ShopItem(itemId=22505, goldPrice=1), # Blueberry Cookie
                ShopItem(itemId=22506, goldPrice=1), # Honey Maple Cookie
                ShopItem(itemId=22507, goldPrice=1), # Truffle Cookie
                ShopItem(itemId=22508, goldPrice=1), # Honey Truffle Cookie
                ShopItem(itemId=22509, goldPrice=1), # Raspberry Truffle Cookie
                ShopItem(itemId=22510, goldPrice=1), # Blueberry Truffle Cookie
                ShopItem(itemId=22532, goldPrice=1), # Sunflower Double Truffle Cookie
                ShopItem(itemId=22533, goldPrice=1), # Honey Double Truffle Cookie
                ShopItem(itemId=22534, goldPrice=1), # Raspberry Double Truffle Cookie
                ShopItem(itemId=22535, goldPrice=1), # Blueberry Double Truffle Cookie
                ShopItem(itemId=22542, goldPrice=1), # Honey Maple Double Truffle Cookie
            ],
        ),
        ShopCollection(
            collectionId=61, # Delectable Cupcakes
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22551, goldPrice=1), # Sunflower Cupcake
                ShopItem(itemId=22552, goldPrice=1), # Honey Cupcake
                ShopItem(itemId=22553, goldPrice=1), # Raspberry Cupcake
            ],
        ),
        ShopCollection(
            collectionId=147, # Color Changing Silly Sweets
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22520, goldPrice=1), # Red
                ShopItem(itemId=22521, goldPrice=1), # Orange
                ShopItem(itemId=22522, goldPrice=1), # Yellow
                ShopItem(itemId=22518, goldPrice=1), # Green
                ShopItem(itemId=22516, goldPrice=1), # Blue
                ShopItem(itemId=22519, goldPrice=1), # Purple
                ShopItem(itemId=22514, goldPrice=1), # Pink
                ShopItem(itemId=22515, goldPrice=1), # White
                ShopItem(itemId=22517, goldPrice=1), # Gray
                ShopItem(itemId=22523, goldPrice=1), # Cool Rainbow
                ShopItem(itemId=22524, goldPrice=1), # Bright Rainbow
                ShopItem(itemId=22525, goldPrice=1), # Invisible
            ],
        ),
        ShopCollection(
            collectionId=38, # Aura Silly Sweets
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22527, goldPrice=1), # Rainbow Glow
                ShopItem(itemId=22526, goldPrice=1), # Bubble
                ShopItem(itemId=22543, goldPrice=1), # Bubble Trail
                ShopItem(itemId=22530, goldPrice=1), # Tornado
                ShopItem(itemId=22528, goldPrice=1), # Dizzy
                ShopItem(itemId=22529, goldPrice=1), # Bright Idea
                ShopItem(itemId=22539, goldPrice=1), # Puffy Cloud
                ShopItem(itemId=22536, goldPrice=1), # Fairy Cupcake
                ShopItem(itemId=22537, goldPrice=1), # Fireworks
                ShopItem(itemId=22538, goldPrice=1), # Snowglobe
                ShopItem(itemId=22540, goldPrice=1), # Ice Cube
                ShopItem(itemId=22541, goldPrice=1), # Snowman
                ShopItem(itemId=22544, goldPrice=1), # Flower Trail
                ShopItem(itemId=22545, goldPrice=1), # Snowflake Trail
                ShopItem(itemId=22546, goldPrice=1), # Raining Cloud
                ShopItem(itemId=22547, goldPrice=1), # Snowing Cloud
                ShopItem(itemId=22548, goldPrice=1), # Shrinking
                ShopItem(itemId=22549, goldPrice=1), # Growing
                ShopItem(itemId=22550, goldPrice=1), # Flip-Flop
            ],
        ),
        ShopCollection(
            collectionId=21, # Wing Changing Silly Sweets
            purchaseType=PurchaseType.POUCH,
            items=[
                ShopItem(itemId=22571, goldPrice=1), # Sparkly Wings
                ShopItem(itemId=22572, goldPrice=1), # Pepper Black Wings
                ShopItem(itemId=22573, goldPrice=1), # Bluejay Blue Wings
                ShopItem(itemId=22574, goldPrice=1), # Electric Blue Wings
                ShopItem(itemId=22575, goldPrice=1), # Friendship Pink Wings
                ShopItem(itemId=22576, goldPrice=1), # Electric Pink Wings
                ShopItem(itemId=22577, goldPrice=1), # Electric Orange Wings
                ShopItem(itemId=22578, goldPrice=1), # Electric Purple Wings
                ShopItem(itemId=22579, goldPrice=1), # Lemon Yellow Wings
                ShopItem(itemId=22580, goldPrice=1), # Rosetta Red Wings
                ShopItem(itemId=22581, goldPrice=1), # Electric Green Wings
            ],
        ),
    ],
)