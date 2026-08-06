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
    zone=ZoneConstants.NEVILLES_NEW_HOMES,
    shopId=6000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.NEVILLE,
        position=(785, 458),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_NEVILLE,
        gender=2
    ),
    collections=[
        ShopCollection(
            collectionId=6000, # Small Homes
            purchaseType=PurchaseType.HOME_TYPE,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=29001, price=40, goldPrice=20), # Knothole Nest (HOME ID 1)
                ShopItem(itemId=29002, price=40, goldPrice=20), # Blossom Bungalow (HOME ID 2)
                ShopItem(itemId=29003, price=40, goldPrice=20), # Sunflower Studio (HOME ID 3)
                ShopItem(itemId=29004, price=40, goldPrice=20), # Lotus Loft (HOME ID 4)
                ShopItem(itemId=29005, price=40, goldPrice=20), # Mosswall Cottage (HOME ID 5)
            ],
        ),
        ShopCollection(
            collectionId=6001, # Large Homes
            purchaseType=PurchaseType.HOME_TYPE,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=29026, price=160, goldPrice=80), # Snowflake Estate (HOME ID 26)
                ShopItem(itemId=29021, price=110, goldPrice=55), # Hollow Tree Heights (HOME ID 21)
                ShopItem(itemId=29022, price=110, goldPrice=55), # Petalstem Palace (HOME ID 22)
                ShopItem(itemId=29023, price=100, goldPrice=50), # Sunglow Spire (HOME ID 23)
                ShopItem(itemId=29024, price=130, goldPrice=65), # Streamside Suite (HOME ID 24)
                ShopItem(itemId=29025, price=100, goldPrice=50), # Greenleaf Tower (HOME ID 25)
            ],
        ),
        ShopCollection(
            collectionId=6003, # Home Basics
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=6607, price=16, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Flooring
                ShopItem(itemId=6614, price=16, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Stacked Floor
                ShopItem(itemId=6643, price=16, goldPrice=8, color1=77, color2=77), # Sepia Brown Fallen Wood Stacked Loft
                ShopItem(itemId=6620, price=16, goldPrice=8, color1=77, color2=77), # Sepia Brown Longer Ladder
                ShopItem(itemId=6618, price=10, goldPrice=5, color1=39, color2=77), # Springtime Green Leaf Screen Wall
                ShopItem(itemId=6619, price=10, goldPrice=5, color1=39, color2=77), # Springtime Green Leaf Screen Back
            ],
        ),
        ShopCollection(
            collectionId=1075, # Platforms
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=6615, price=20, goldPrice=10, color1=112, color2=41), # Splashy Blue Oyster Shell Flooring
                ShopItem(itemId=6616, price=20, goldPrice=10, color1=116, color2=177), # Mushroom White Mushroom Flooring with Brown Trim
                ShopItem(itemId=6617, price=18, goldPrice=9, color1=20, color2=21), # Grassblade Green Tall Grass Flooring
                ShopItem(itemId=6658, price=18, goldPrice=9, color1=20, color2=77), # Grassblade Green Leafy Platform
                ShopItem(itemId=6669, price=18, goldPrice=9, color1=143, color2=116), # June Bug Green Petal Perfect Platform
                ShopItem(itemId=6662, price=24, goldPrice=12, color1=111, color2=249), # Sparkling Yellow Giant Gem Platform
                ShopItem(itemId=6667, price=20, goldPrice=10, color1=166, color2=138), # Snow White Lost Teacup Saucer
                ShopItem(itemId=7715, price=16, goldPrice=8, color1=215, color2=219), # Pewter Gray Stay-Cool Pool
                ShopItem(itemId=6681, price=16, goldPrice=8, color1=230, color2=226), # Scarlet Red Book Flooring
                ShopItem(itemId=6704, price=16, goldPrice=8, color1=166, color2=207), # Snow White Ice Rink Platform with Diamond Blue Trim
                ShopItem(itemId=6689, price=18, goldPrice=9, color1=100, color2=33), # Golden Tan Paintbrush Platform
                ShopItem(itemId=6711, price=16, goldPrice=8, color1=239, color2=28), # Coffee Black Chocolatey Chip Platform
                ShopItem(itemId=6710, price=16, goldPrice=8, color1=152, color2=91), # Pale Purple Overgrown Platform
                ShopItem(itemId=6747, price=20, goldPrice=10, color1=109, color2=207), # Soft Orange Sandy Platform
                ShopItem(itemId=6599, price=30, goldPrice=15, color1=269, color2=269), # Crisp White Baroque Balcony
                ShopItem(itemId=6603, price=24, goldPrice=12, color1=20, color2=166), # Grassblade Green Winter Crossing Platform
                ShopItem(itemId=6774, price=24, goldPrice=12, color1=166, color2=166), # Snow White Cloud Platform
                ShopItem(itemId=6770, price=30, goldPrice=15, color1=162, color2=11), # Sunglow Yellow Scallop Shell Platform
                ShopItem(itemId=6768, price=40, goldPrice=20, color1=84, color2=168), # Copper Brown Summer Sun Mosaic Platform
                ShopItem(itemId=6779, price=34, goldPrice=17, color1=261, color2=161), # Kelly Green Campground Clearing
                ShopItem(itemId=7849, price=16, goldPrice=8, color1=166, color2=166), # Snow White Snowy Platform
                ShopItem(itemId=7816, price=16, goldPrice=8, color1=109, color2=189), # Soft Orange Sandcastle Platform with Red Trim
                ShopItem(itemId=7806, price=16, goldPrice=8, color1=227, color2=227), # Moonlight Gray Lily Pad Pond
                ShopItem(itemId=6666, price=16, goldPrice=8, color1=224, color2=286), # Ivory White Lost Teacup Pool
                ShopItem(itemId=6752, price=36, goldPrice=18, color1=57, color2=77), # Adobe Brown Ship's Deck Platform
                ShopItem(itemId=6602, price=16, goldPrice=8, color1=207, color2=166), # Diamond Blue Frosty Gazebo
            ],
        ),
        ShopCollection(
            collectionId=1076, # Staircases and Ladders
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=6611, price=30, goldPrice=15, color1=167, color2=55), # Never Silver Grand Metal Staircase
                ShopItem(itemId=6649, price=16, goldPrice=8, color1=152, color2=117), # Pale Purple Spiral Shell Stairs
                ShopItem(itemId=6613, price=16, goldPrice=8, color1=150, color2=172), # Dry Moss Green Moss Staircase with Forest Green Trim
                ShopItem(itemId=6621, price=16, goldPrice=8, color1=118, color2=4), # Sapphire Blue Comb Climber
                ShopItem(itemId=6622, price=16, goldPrice=8, color1=239, color2=46), # Coffee Black Bobby Ladder
                ShopItem(itemId=6657, price=16, goldPrice=8, color1=20, color2=106), # Grassblade Green Leafy Ladder with Tan Trim
                ShopItem(itemId=6665, price=30, goldPrice=15, color1=111, color2=249), # Sparkling Yellow Dazzling Steps
                ShopItem(itemId=6678, price=16, goldPrice=8, color1=154, color2=157), # Beetle Brown Beach Pier Stairs
                ShopItem(itemId=6709, price=18, goldPrice=9, color1=77, color2=28), # Sepia Brown Oak Staircase
                ShopItem(itemId=6705, price=16, goldPrice=8, color1=207, color2=223), # Diamond Blue Grand Icicle Staircase
                ShopItem(itemId=6730, price=16, goldPrice=8, color1=76, color2=90), # Chocolate Brown Eclair Stairs with Custard Yellow Trim
                ShopItem(itemId=6727, price=18, goldPrice=9, color1=64, color2=218), # Emerald Green Ivy Stairs
                ShopItem(itemId=6732, price=32, goldPrice=16, color1=196, color2=195), # Electric Orange Winding Stairs
                ShopItem(itemId=6740, price=16, goldPrice=8, color1=159, color2=247), # Tea Green Sunflower Steps with Jasmine Yellow Trim
                ShopItem(itemId=6757, price=26, goldPrice=13, color1=70, color2=118), # Tinker Blue Gear Staircase
                ShopItem(itemId=6601, price=30, goldPrice=15, color1=99, color2=78), # Papyrus Tan Haunted Staircase
                ShopItem(itemId=6668, price=20, goldPrice=10, color1=99, color2=90), # Papyrus Tan Tea Biscuit Steps
                ShopItem(itemId=6772, price=32, goldPrice=16, color1=166, color2=166), # Snow White Nimbus Staircase
                ShopItem(itemId=6769, price=36, goldPrice=18, color1=217, color2=215), # Soft Gray Mermaid Grotto Stairs
                ShopItem(itemId=6766, price=16, goldPrice=8, color1=274, color2=1), # Bellflower Purple Buttercup Steps
                ShopItem(itemId=6771, price=16, goldPrice=8, color1=17, color2=161), # Tendershoot Green Grassy Trail
                ShopItem(itemId=6612, price=16, goldPrice=8, color1=153, color2=215), # Frostbunny Blue Fun Fungi Staircase
                ShopItem(itemId=6680, price=16, goldPrice=8, color1=152, color2=5), # Pale Purple Bookshelf Steps
                ShopItem(itemId=6778, price=16, goldPrice=8, color1=113, color2=230), # Pale Rose Red Storytime Staircase
            ],
        ),
        ShopCollection(
            collectionId=1077, # Dividers
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=6623, price=16, goldPrice=8, color1=142, color2=142), # Bumble Bee Yellow Sweet Bee Wall
                ShopItem(itemId=6624, price=16, goldPrice=8, color1=142, color2=142), # Bumble Bee Yellow Sweet Bee Cubby
                ShopItem(itemId=6659, price=16, goldPrice=8, color1=154, color2=128), # Beetle Brown Trellis Room Divider
                ShopItem(itemId=6660, price=16, goldPrice=8, color1=154, color2=128), # Beetle Brown Trellis Side Divider
                ShopItem(itemId=6663, price=16, goldPrice=8, color1=165, color2=182), # Spring Breeze Green Light Bright Canopy
                ShopItem(itemId=6664, price=16, goldPrice=8, color1=13, color2=224), # Coral Pink Seaside Canopy
                ShopItem(itemId=7702, price=16, goldPrice=8, color1=152, color2=134), # Pale Purple Shell Net Room Divider
                ShopItem(itemId=6692, price=16, goldPrice=8, color1=89, color2=268), # Seashore Brown Sweet Wheat Divider
                ShopItem(itemId=6695, price=16, goldPrice=8, color1=89, color2=268), # Seashore Brown Sweet Wheat Front Divider
                ShopItem(itemId=6717, price=16, goldPrice=8, color1=45, color2=221), # Strawberry Red Candy Cane Side Divider
                ShopItem(itemId=6718, price=16, goldPrice=8, color1=45, color2=221), # Strawberry Red Candy Cane Room Divider
                ShopItem(itemId=6751, price=16, goldPrice=8, color1=226, color2=17), # Goldenrod Yellow Blooming Flower Canopy
                ShopItem(itemId=7895, price=16, goldPrice=8, color1=44, color2=37), # Plumblossom Pink Colorful Carousel Canopy
                ShopItem(itemId=6748, price=16, goldPrice=8, color1=203, color2=125), # Shadow Green Palm Leaf Panel
                ShopItem(itemId=6767, price=16, goldPrice=8, color1=83, color2=126), # Cherry Brown Raindrop Room Divider
                ShopItem(itemId=7896, price=16, goldPrice=8, color1=108, color2=207), # Creamy Tan Bubble Cascade Curtains
                ShopItem(itemId=7888, price=16, goldPrice=8, color1=121, color2=199), # Daisy Pink Teapot Flower Pots
                ShopItem(itemId=6753, price=16, goldPrice=8, color1=57, color2=128), # Adobe Brown Woodblock Divider
                ShopItem(itemId=6715, price=16, goldPrice=8, color1=45, color2=273), # Strawberry Red Shinto Side Divider
                ShopItem(itemId=6716, price=16, goldPrice=8, color1=45, color2=273), # Strawberry Red Shinto Room Divider
            ]
        ),
        ShopCollection(
            collectionId=6002, # Plants and Garden Decor
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["LILY_PETALS"].id,
            items=[
                ShopItem(itemId=6553, price=16, goldPrice=8, color1=99, color2=119), # Papyrus Tan Neverwood Trellis
                ShopItem(itemId=6737, price=16, goldPrice=8, color1=215, color2=167), # Pewter Gray Garden Hearts Trellis
                ShopItem(itemId=6514, price=16, goldPrice=8, color1=121, color2=121), # Daisy Pink Daisy Bloom Swing
                ShopItem(itemId=6765, price=16, goldPrice=8, color1=172, color2=35), # Forest Green Water Bog Tree Swing
                ShopItem(itemId=6562, price=16, goldPrice=8, color1=264, color2=264), # Jungle Green Clover Swing
                ShopItem(itemId=6713, price=16, goldPrice=8, color1=99, color2=230), # Papyrus Tan Friendship Swing
                ShopItem(itemId=6540, price=16, goldPrice=8, color1=123, color2=175), # Squash Orange Twig Porch Swing
                ShopItem(itemId=7587, price=16, goldPrice=8, color1=267, color2=57), # Celestial Blue Dangling Blossoms Basket
                ShopItem(itemId=7588, price=16, goldPrice=8, color1=159, color2=57), # Tea Green Fancy Topiary
                ShopItem(itemId=7609, price=16, goldPrice=8, color1=76, color2=76), # Chocolate Brown Small Decorating Tree
                ShopItem(itemId=7610, price=16, goldPrice=8, color1=76, color2=76), # Chocolate Brown Tall Decorating Tree
                ShopItem(itemId=7611, price=16, goldPrice=8, color1=100, color2=121), # Golden Tan Prickly Pear Plant
                ShopItem(itemId=7617, price=16, goldPrice=8, color1=264, color2=74), # Jungle Green Potted Palm Tree
                ShopItem(itemId=7618, price=16, goldPrice=8, color1=152, color2=167), # Pale Purple Blooming Bonsai
                ShopItem(itemId=7619, price=16, goldPrice=8, color1=230, color2=55), # Scarlet Red Pepper 'N Rose
                ShopItem(itemId=7620, price=16, goldPrice=8, color1=140, color2=99), # Bunnynose Pink Box of Buds
                ShopItem(itemId=7621, price=16, goldPrice=8, color1=267, color2=166), # Celestial Blue Salt 'N Daisies
                ShopItem(itemId=7691, price=16, goldPrice=8, color1=127, color2=46), # Grasshopper Green Large Lion Topiary
                ShopItem(itemId=7692, price=16, goldPrice=8, color1=17, color2=46), # Tendershoot Green Zebra Topiary
                ShopItem(itemId=7693, price=16, goldPrice=8, color1=150, color2=46), # Dry Moss Green Great Giraffe Topiary
                ShopItem(itemId=7729, price=16, goldPrice=8, color1=105, color2=147), # Siltstone Tan Bubbly Bog Fountain
                ShopItem(itemId=7768, price=16, goldPrice=8, color1=99, color2=2), # Papyrus Tan Clover Topiary
                ShopItem(itemId=7769, price=16, goldPrice=8, color1=45, color2=120), # Strawberry Red Peppermint Trees
                ShopItem(itemId=7766, price=16, goldPrice=8, color1=45, color2=168), # Strawberry Red Peppermint Planter
                ShopItem(itemId=7803, price=16, goldPrice=8, color1=236, color2=150), # Dusty Brown Bunny Flowerpot
                ShopItem(itemId=7804, price=16, goldPrice=8, color1=200, color2=226), # Ruby Pink Butterfly Statue
                ShopItem(itemId=7807, price=16, goldPrice=8, color1=203, color2=150), # Shadow Green Turtle Sprinkler
                ShopItem(itemId=7808, price=16, goldPrice=8, color1=100, color2=230), # Golden Tan Wheelbarrow Gnome
                ShopItem(itemId=7809, price=16, goldPrice=8, color1=209, color2=265), # Deep Sea Blue Lamplight Gnome
                ShopItem(itemId=7810, price=16, goldPrice=8, color1=170, color2=256), # Olive Green Lady Gnome
                ShopItem(itemId=7811, price=16, goldPrice=8, color1=60, color2=129), # Tyrian Purple Rake Gnome
                ShopItem(itemId=7812, price=16, goldPrice=8, color1=99, color2=121), # Papyrus Tan Flower Basket
                ShopItem(itemId=7813, price=16, goldPrice=8, color1=216, color2=166), # Slate Gray Planter Box
                ShopItem(itemId=7835, price=16, goldPrice=8, color1=172, color2=116), # Forest Green Spooky Tree
                ShopItem(itemId=7863, price=16, goldPrice=8, color1=153, color2=60), # Frostbunny Blue Aurora Fountain
                ShopItem(itemId=7877, price=16, goldPrice=8, color1=100, color2=230), # Golden Tan Potted Rainbow
                ShopItem(itemId=7885, price=16, goldPrice=8, color1=154, color2=172), # Beetle Brown Potted Fern
                ShopItem(itemId=6764, price=16, goldPrice=8, color1=154, color2=172), # Beetle Brown Water Bog Tree Stump
                ShopItem(itemId=7716, price=16, goldPrice=8, color1=27, color2=267), # Corn Cob Yellow Carved Flower Column
                ShopItem(itemId=7717, price=16, goldPrice=8, color1=152, color2=5), # Pale Purple Carved Hibiscus Column
                ShopItem(itemId=7833, price=16, goldPrice=8, color1=227, color2=227), # Moonlight Gray Gargoyle Kitty
                ShopItem(itemId=7771, price=16, goldPrice=8, color1=247, color2=57), # Jasmine Yellow Sassy Sunflower Umbrella
                ShopItem(itemId=7775, price=16, goldPrice=8, color1=121, color2=98), # Daisy Pink Cute Carnation Umbrella
                ShopItem(itemId=7776, price=16, goldPrice=8, color1=224, color2=99), # Ivory White Darling Daisy Umbrella
                ShopItem(itemId=7777, price=16, goldPrice=8, color1=51, color2=98), # Periwinkle Blue Fancy Flower Umbrella
                ShopItem(itemId=7850, price=16, goldPrice=8, color1=206, color2=121), # Raven Black Fairy Snowman
                ShopItem(itemId=7562, price=16, goldPrice=8, color1=99, color2=119), # Papyrus Tan Wind Chime
                ShopItem(itemId=7524, price=16, goldPrice=8, color1=99, color2=99), # Papyrus Tan Grass Houseplant
                ShopItem(itemId=7546, price=16, goldPrice=8, color1=99, color2=99), # Papyrus Tan Purple Posy Plant
                ShopItem(itemId=7817, price=16, goldPrice=8, color1=161, color2=128), # Buried Treasure Brown Straw Umbrella
                ShopItem(itemId=7805, price=16, goldPrice=8, color1=227, color2=227), # Moonlight Gray Rainbow Flower Arch
            ]
        )
    ]
)