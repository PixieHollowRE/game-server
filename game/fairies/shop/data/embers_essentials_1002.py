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
        ShopCollection(
            collectionId=1020, # Kitchen and Dining
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=6550, price=17, goldPrice=5, color1=139, color2=92), # Seedling Green Tea Time Serving Cart
                ShopItem(itemId=6644, price=17, goldPrice=5, color1=227, color2=215), # Moonlight Gray Hot Hot Stove
                ShopItem(itemId=7509, price=10, goldPrice=3, color1=224, color2=224), # Ivory White River Stone Pitcher
                ShopItem(itemId=7511, price=10, goldPrice=3, color1=83, color2=83), # Cherry Brown Clay Pot
                ShopItem(itemId=7526, price=10, goldPrice=3, color1=56, color2=56), # Bole Brown Acorn Kettle
                ShopItem(itemId=7557, price=10, goldPrice=3, color1=100, color2=129), # Golden Tan Harvest Cornucopia
                ShopItem(itemId=7558, price=10, goldPrice=3, color1=100, color2=129), # Golden Tan Fancy Cornucopia
                ShopItem(itemId=7563, price=10, goldPrice=3, color1=207, color2=224), # Diamond Blue Hot Cocoa Mug
                ShopItem(itemId=7564, price=10, goldPrice=3, color1=224, color2=207), # Ivory White Hot Cocoa Kettle
                ShopItem(itemId=7565, price=10, goldPrice=3, color1=241, color2=172), # Desert Brown Leafy Cake Stand
                ShopItem(itemId=7567, price=10, goldPrice=3, color1=265, color2=265), # Bright Sky Blue Cookie Jar
                ShopItem(itemId=7573, price=10, goldPrice=3, color1=30, color2=10), # Pumpkin Orange Popcorn Bowl
                ShopItem(itemId=7574, price=10, goldPrice=3, color1=215, color2=111), # Pewter Gray Walnut Casserole Dish
                ShopItem(itemId=7575, price=10, goldPrice=3, color1=282, color2=121), # Magnolia White Butterfly Teacup
                ShopItem(itemId=7576, price=10, goldPrice=3, color1=282, color2=121), # Magnolia White Butterfly Teapot
                ShopItem(itemId=7582, price=10, goldPrice=3, color1=91, color2=86), # Coconut Brown Juice Pitcher
                ShopItem(itemId=7583, price=10, goldPrice=3, color1=91, color2=86), # Coconut Brown Juice Glass
                ShopItem(itemId=7584, price=10, goldPrice=3, color1=139, color2=139), # Seedling Green Sauce Serving Dish
                ShopItem(itemId=7625, price=10, goldPrice=3, color1=70, color2=70), # Tinker Blue Camp Cup
                ShopItem(itemId=7626, price=10, goldPrice=3, color1=199, color2=207), # Cherryblossom Pink Super Sundae
                ShopItem(itemId=7633, price=10, goldPrice=3, color1=45, color2=166), # Strawberry Red Lizzy's Peppermint
                ShopItem(itemId=7642, price=10, goldPrice=3, color1=56, color2=215), # Bole Brown Tray of Cookies
                ShopItem(itemId=7643, price=10, goldPrice=3, color1=150, color2=150), # Dry Moss Green Big Mixing Bowl
                ShopItem(itemId=7653, price=10, goldPrice=3, color1=227, color2=70), # Moonlight Gray Metal Soup Pot and Ladle
                ShopItem(itemId=7669, price=10, goldPrice=3, color1=200, color2=267), # Ruby Pink Cupcake Tower
                ShopItem(itemId=7688, price=10, goldPrice=3, color1=99, color2=99), # Papyrus Tan Woven Basket of Treats
                ShopItem(itemId=7736, price=10, goldPrice=3, color1=214, color2=46), # Smokey Gray Berry Bobber
                ShopItem(itemId=7737, price=10, goldPrice=3, color1=162, color2=94), # Sunglow Yellow Plentiful Pie Rack
                ShopItem(itemId=7740, price=10, goldPrice=3, color1=161, color2=158), # Buried Treasure Brown Festive Jelly Tower
                ShopItem(itemId=7788, price=10, goldPrice=3, color1=162, color2=224), # Sunglow Yellow Teatime Snack Tower with Ivory White Trim
                ShopItem(itemId=7837, price=10, goldPrice=3, color1=208, color2=224), # Cerulean Blue Feast Plate
                ShopItem(itemId=7866, price=10, goldPrice=3, color1=207, color2=89), # Diamond Blue Tray of Tarts
                ShopItem(itemId=7867, price=10, goldPrice=3, color1=224, color2=208), # Ivory White Plate of Pancakes
                ShopItem(itemId=7869, price=10, goldPrice=3, color1=224, color2=208), # Ivory White Plate of Cookies
                ShopItem(itemId=7870, price=10, goldPrice=3, color1=208, color2=224), # Cerulean Blue Cheesecake Plate
                ShopItem(itemId=7871, price=10, goldPrice=3, color1=44, color2=23), # Plumblossom Pink Butterfly Cake
                ShopItem(itemId=7889, price=10, goldPrice=3, color1=35, color2=162), # Celery Green Acorn Chips
            ]
        ),
        ShopCollection(
            collectionId=1010, # Outdoor Activities
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=6554, price=17, goldPrice=5, color1=35, color2=161), # Celery Green Leaf Boat
                ShopItem(itemId=6598, price=17, goldPrice=5, color1=154, color2=215), # Beetle Brown Rockin' Firepit with Pewter Gray Trim
                ShopItem(itemId=6604, price=17, goldPrice=5, color1=71, color2=161), # Dewdrop Blue Camp Tent
                ShopItem(itemId=6605, price=17, goldPrice=5, color1=154, color2=215), # Beetle Brown Mallow Roaster with Pewter Gray Trim
                ShopItem(itemId=6606, price=17, goldPrice=5, color1=154, color2=215), # Beetle Brown Kernel Roaster with Pewter Gray Trim
                ShopItem(itemId=6670, price=17, goldPrice=5, color1=154, color2=215), # Beetle Brown Campfire Cooker with Pewter Gray Trim
                ShopItem(itemId=7507, price=10, goldPrice=3, color1=56, color2=56), # Bole Brown Watering Tin
                ShopItem(itemId=7513, price=10, goldPrice=3, color1=224, color2=224), # Ivory White Gardening Journal
                ShopItem(itemId=7515, price=10, goldPrice=3, color1=154, color2=154), # Beetle Brown Seed Ladle
                ShopItem(itemId=7523, price=10, goldPrice=3, color1=224, color2=224), # Ivory White Firefly Fetcher
                ShopItem(itemId=7570, price=10, goldPrice=3, color1=46, color2=32), # Bark Brown Poppy Puff Picnic Basket with Dark Purple Trim
                ShopItem(itemId=7713, price=10, goldPrice=3, color1=236, color2=267), # Dusty Brown Picnic Basket
                ShopItem(itemId=7848, price=10, goldPrice=3, color1=166, color2=166), # Dusty Brown Picnic Basket
            ]
        ),
        ShopCollection(
            collectionId=1023, # Toys and Trinkets
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=6555, price=17, goldPrice=5, color1=99, color2=99), # Papyrus Tan Vintage Harp
                ShopItem(itemId=6556, price=17, goldPrice=5, color1=250, color2=267), # Caramel Tan Double Drums
                ShopItem(itemId=6557, price=17, goldPrice=5, color1=121, color2=267), # Daisy Pink Petal Wrap Microphone
                ShopItem(itemId=6558, price=17, goldPrice=5, color1=139, color2=57), # Seedling Green Conductor Stand
                ShopItem(itemId=6561, price=17, goldPrice=5, color1=35, color2=57), # Celery Green Music Stand
                ShopItem(itemId=6560, price=17, goldPrice=5, color1=227, color2=267), # Moonlight Gray Itty Bitty Bells
                ShopItem(itemId=6600, price=17, goldPrice=5, color1=227, color2=215), # Moonlight Gray Spooky Piano with Pewter Gray Trim
                ShopItem(itemId=7519, price=10, goldPrice=3, color1=154, color2=154), # Beetle Brown Pebble Finger Harp
                ShopItem(itemId=7520, price=10, goldPrice=3, color1=236, color2=236), # Dusty Brown Reed Flute
                ShopItem(itemId=7547, price=10, goldPrice=3, color1=90, color2=90), # Custard Yellow Mainland-Style Finger Harp
                ShopItem(itemId=7577, price=10, goldPrice=3, color1=111, color2=208), # Sparkling Yellow Shimmering Bell with Blue Trim
                ShopItem(itemId=7527, price=10, goldPrice=3, color1=83, color2=83), # Cherry Brown Squirrel Doll
                ShopItem(itemId=7550, price=10, goldPrice=3, color1=30, color2=88), # Pumpkin Orange Fluffy Fish Pillow
                ShopItem(itemId=7553, price=10, goldPrice=3, color1=44, color2=190), # Plumblossom Pink Firefly Doll
                ShopItem(itemId=7572, price=10, goldPrice=3, color1=98, color2=74), # Sandstone Tan Chipmunk Doll
                ShopItem(itemId=7586, price=10, goldPrice=3, color1=150, color2=206), # Dry Moss Green Tink's Balloon Toy
                ShopItem(itemId=7594, price=10, goldPrice=3, color1=154, color2=154), # Beetle Brown Carved Bunny
                ShopItem(itemId=7595, price=10, goldPrice=3, color1=169, color2=161), # Squirrel Gray Tall Mouse Tale Sculpture
                ShopItem(itemId=7623, price=10, goldPrice=3, color1=267, color2=209), # Celestial Blue Studded Seahorse Comb
                ShopItem(itemId=7624, price=10, goldPrice=3, color1=44, color2=44), # Plumblossom Pink Blaze Plush
                ShopItem(itemId=7627, price=10, goldPrice=3, color1=150, color2=172), # Dry Moss Green Turtle Plush
                ShopItem(itemId=7628, price=10, goldPrice=3, color1=99, color2=74), # Papyrus Tan Rabbit Plush
                ShopItem(itemId=7629, price=10, goldPrice=3, color1=91, color2=166), # Coconut Brown Otter Plush
                ShopItem(itemId=7630, price=10, goldPrice=3, color1=226, color2=251), # Goldenrod Yellow Glowworm Plush
                ShopItem(itemId=7631, price=10, goldPrice=3, color1=230, color2=121), # Scarlet Red Butterfly Plush
                ShopItem(itemId=7650, price=10, goldPrice=3, color1=99, color2=207), # Papyrus Tan Snowman Snowglobe
                ShopItem(itemId=7659, price=10, goldPrice=3, color1=141, color2=189), # Thundercloud Gray Ladybug Sculpture
                ShopItem(itemId=7660, price=10, goldPrice=3, color1=152, color2=184), # Pale Purple Hummingbird Sculpture
                ShopItem(itemId=7661, price=10, goldPrice=3, color1=44, color2=190), # Plumblossom Pink Firefly Sculpture
                ShopItem(itemId=7662, price=10, goldPrice=3, color1=133, color2=1), # Marina Blue Dragonfly Sculpture with Green Trim
                ShopItem(itemId=7663, price=10, goldPrice=3, color1=142, color2=224), # Bumble Bee Yellow Bee Sculpture with Ivory White Trim
                ShopItem(itemId=7683, price=10, goldPrice=3, color1=139, color2=17), # Seedling Green Froggy Toy
                ShopItem(itemId=7685, price=10, goldPrice=3, color1=267, color2=184), # Celestial Blue Hummingbird Toy
                ShopItem(itemId=7687, price=10, goldPrice=3, color1=199, color2=169), # Cherryblossom Pink Mousey Toy
                ShopItem(itemId=7698, price=10, goldPrice=3, color1=154, color2=74), # Beetle Brown Playful Blocks
                ShopItem(itemId=7701, price=10, goldPrice=3, color1=265, color2=125), # Bright Sky Blue Choo Choo Sleeper
                ShopItem(itemId=7882, price=10, goldPrice=3, color1=30, color2=206), # Pumpkin Orange Stuffed Tiger
                ShopItem(itemId=7514, price=10, goldPrice=3, color1=130, color2=130), # Orchid Pink Butterfly Sculpture
                ShopItem(itemId=6671, price=17, goldPrice=5, color1=161, color2=161), # Buried Treasure Brown Pixie Weight Set
                ShopItem(itemId=6673, price=17, goldPrice=5, color1=204, color2=38), # Bamboo Green Pixie Medicine Ball
                ShopItem(itemId=6675, price=17, goldPrice=5, color1=35, color2=98), # Celery Green Pixie Bench Press
                ShopItem(itemId=6579, price=17, goldPrice=5, color1=206, color2=68), # Raven Black Play Pirate Ship
                ShopItem(itemId=7590, price=10, goldPrice=3, color1=152, color2=267), # Pale Purple Painter's Vase
                ShopItem(itemId=7593, price=10, goldPrice=3, color1=99, color2=178), # Papyrus Tan Painterly Buckets
                ShopItem(itemId=7682, price=10, goldPrice=3, color1=178, color2=58), # Fawn Orange Critter Print Pot
                ShopItem(itemId=6640, price=17, goldPrice=5, color1=99, color2=203), # Papyrus Tan Classroom Chalkboard with Shadow Green Trim
                ShopItem(itemId=6699, price=17, goldPrice=5, color1=168, color2=111), # Never Gold Elegant Easel
                ShopItem(itemId=7711, price=10, goldPrice=3, color1=44, color2=5), # Plumblossom Pink Designer Leaf Fish
                ShopItem(itemId=7674, price=10, goldPrice=3, color1=18, color2=208), # Waterfall Blue Animal Friend Mobile
                ShopItem(itemId=7638, price=10, goldPrice=3, color1=35, color2=57), # Celery Green Pad and Pencil
                ShopItem(itemId=7890, price=10, goldPrice=3, color1=258, color2=265), # Spearmint Green Ball of Yarn
                ShopItem(itemId=7891, price=10, goldPrice=3, color1=224, color2=126), # Ivory White Book of Lullabies
                ShopItem(itemId=7892, price=10, goldPrice=3, color1=127, color2=207), # Grasshopper Green Soap Bubble Basket
                ShopItem(itemId=7834, price=10, goldPrice=3, color1=207, color2=150), # Diamond Blue Crystal Ball
                ShopItem(itemId=7566, price=10, goldPrice=3, color1=152, color2=129), # Pale Purple Fairy Tales Collection
                ShopItem(itemId=6575, price=17, goldPrice=5, color1=224, color2=287), # Ivory White Lost Wind-Up Box Base
                ShopItem(itemId=6578, price=17, goldPrice=5, color1=168, color2=168), # Never Gold Precious Treasure
                ShopItem(itemId=6580, price=17, goldPrice=5, color1=84, color2=168), # Copper Brown Precious Compass with Never Gold Trim
                ShopItem(itemId=7649, price=10, goldPrice=3, color1=181, color2=143), # Cupcake Pink Tulip Balloons
                ShopItem(itemId=7832, price=10, goldPrice=3, color1=215, color2=206), # Pewter Gray Bat Pumpkin
                ShopItem(itemId=7552, price=10, goldPrice=3, color1=99, color2=74), # Papyrus Tan Firefly Light-Up Basket
                ShopItem(itemId=7676, price=10, goldPrice=3, color1=27, color2=27), # Corn Cob Yellow Beautiful Bird
                ShopItem(itemId=7779, price=10, goldPrice=3, color1=95, color2=74), # Sparrow Brown Baby Chipmunk Plush
                ShopItem(itemId=7780, price=10, goldPrice=3, color1=141, color2=141), # Thundercloud Gray Kitten Plush
                ShopItem(itemId=7781, price=10, goldPrice=3, color1=166, color2=207), # Snow White Baby Owl Plush
                ShopItem(itemId=7782, price=10, goldPrice=3, color1=59, color2=46), # Bunny Brown Baby Bunny Plush 
            ]
        ),
        ShopCollection(
            collectionId=1011, # Odds and Ends
            purchaseType=PurchaseType.HOME_ITEM,
            currencyId=INGREDIENTS["PINE_NEEDLES"].id,
            items=[
                ShopItem(itemId=7503, price=10, goldPrice=3, color1=16, color2=16), # Camellia Pink Camillia Pillows
                ShopItem(itemId=7525, price=10, goldPrice=3, color1=20, color2=20), # Grassblade Green Leaf Blanket
                ShopItem(itemId=7551, price=10, goldPrice=3, color1=195, color2=19), # Electric Blue Bubble Stand
                ShopItem(itemId=7561, price=10, goldPrice=3, color1=139, color2=139), # Seedling Green Snow Blanket
                ShopItem(itemId=7686, price=10, goldPrice=3, color1=189, color2=55), # Ladybug Red Ladybug Pillow
                ShopItem(itemId=7881, price=10, goldPrice=3, color1=207, color2=207), # Diamond Blue Rainbow Pillow
                ShopItem(itemId=7632, price=10, goldPrice=3, color1=128, color2=128), # Carnation White Lizzy's Stamp
                ShopItem(itemId=7635, price=10, goldPrice=3, color1=168, color2=166), # Never Gold Lizzy's Pocketwatch
                ShopItem(itemId=7636, price=10, goldPrice=3, color1=152, color2=152), # Pale Purple Lizzy's Button
                ShopItem(itemId=7712, price=10, goldPrice=3, color1=99, color2=111), # Papyrus Tan Happy Fish Habitat
                ShopItem(itemId=7648, price=10, goldPrice=3, color1=35, color2=205), # Celery Green Ribbon and Twig Present
                ShopItem(itemId=7651, price=10, goldPrice=3, color1=152, color2=60), # Pale Purple Ribbon-Wrapped Present
                ShopItem(itemId=7652, price=10, goldPrice=3, color1=208, color2=36), # Cerulean Blue Leaf-Wrapped Present
                ShopItem(itemId=7787, price=10, goldPrice=3, color1=224, color2=215), # Ivory White Teapot Clock with Pewter Gray Trim
                ShopItem(itemId=7554, price=10, goldPrice=3, color1=127, color2=127), # Grasshopper Green Tinker's Hammer
                ShopItem(itemId=7556, price=10, goldPrice=3, color1=159, color2=128), # Tea Green Blueprint Scrolls
                ShopItem(itemId=6610, price=17, goldPrice=5, color1=168, color2=206), # Never Gold Found Flashlight
                ShopItem(itemId=7879, price=10, goldPrice=3, color1=207, color2=51), # Diamond Blue Frozen Periwinkle Flower
                ShopItem(itemId=7761, price=10, goldPrice=3, color1=2, color2=74), # Clover Green Bell Jar Bouquet with Brown Trim
                ShopItem(itemId=7517, price=10, goldPrice=3, color1=35, color2=35), # Celery Green Never Land Map 
            ]
        )
    ],
)