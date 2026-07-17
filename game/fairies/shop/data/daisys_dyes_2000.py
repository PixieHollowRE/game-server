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
    zone=ZoneConstants.DAISYS_DYES,
    shopId=2000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.DAISY,
        position=(390, 434),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_DAISY
    ),
    # Dye Bottle Item IDs are 14000 + Color ID in colorAssets.xml
    collections=[
        ShopCollection(
            collectionId=2003, # Seasonal Dyes
            purchaseType=PurchaseType.POUCH,
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=14034, price=10, goldPrice=2), # Primrose Pink
                ShopItem(itemId=14231, price=10, goldPrice=2), # Sunny Orange
                ShopItem(itemId=14255, price=10, goldPrice=2), # Canary Yellow
                ShopItem(itemId=14259, price=10, goldPrice=2), # Kiwi Green
                ShopItem(itemId=14069, price=10, goldPrice=2), # Powder Blue
                ShopItem(itemId=14208, price=10, goldPrice=2), # Cerulean Blue
                ShopItem(itemId=14274, price=10, goldPrice=2), # Bellflower Purple
                ShopItem(itemId=14285, price=10, goldPrice=2), # Jazzberry Red
            ],
        ),
        ShopCollection(
            collectionId=2020, # Red & Purple Dyes
            purchaseType=PurchaseType.POUCH,
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[ # 57
                ShopItem(itemId=14110, price=5, goldPrice=1), # Rosy Pink
                ShopItem(itemId=14121, price=5, goldPrice=1), # Daisy Pink
                ShopItem(itemId=14016, price=5, goldPrice=1), # Camellia Pink
                ShopItem(itemId=14194, price=5, goldPrice=1), # Electric Pink
                ShopItem(itemId=14008, price=5, goldPrice=1), # Watermelon Pink
                ShopItem(itemId=14013, price=5, goldPrice=1), # Coral Pink
                ShopItem(itemId=14026, price=5, goldPrice=1), # Raspberry Pink
                ShopItem(itemId=14286, price=5, goldPrice=1), # Cherry Pink
                ShopItem(itemId=14113, price=5, goldPrice=1), # Pale Rose Red
                ShopItem(itemId=14045, price=5, goldPrice=1), # Strawberry Red
                ShopItem(itemId=14082, price=5, goldPrice=1), # Raspberry Red
                ShopItem(itemId=14230, price=5, goldPrice=1), # Scarlet Red
                ShopItem(itemId=14201, price=5, goldPrice=1), # Velvet Red
                ShopItem(itemId=14044, price=5, goldPrice=1), # Plumblossom Pink
                ShopItem(itemId=14053, price=5, goldPrice=1), # Hyacinth Pink
                ShopItem(itemId=14081, price=5, goldPrice=1), # Crimson Red
                ShopItem(itemId=14130, price=5, goldPrice=1), # Orchid Pink
                ShopItem(itemId=14140, price=5, goldPrice=1), # Bunnynose Pink
                ShopItem(itemId=14144, price=5, goldPrice=1), # Petal Pink
                ShopItem(itemId=14156, price=5, goldPrice=1), # Friendship Pink
                ShopItem(itemId=14181, price=5, goldPrice=1), # Cupcake Pink
                ShopItem(itemId=14174, price=5, goldPrice=1), # Rosetta Red
                ShopItem(itemId=14189, price=5, goldPrice=1), # Ladybug Red
                ShopItem(itemId=14199, price=5, goldPrice=1), # Cherryblossom Pink
                ShopItem(itemId=14200, price=5, goldPrice=1), # Ruby Pink
                ShopItem(itemId=14220, price=5, goldPrice=1), # Dusty Pink
                ShopItem(itemId=14283, price=5, goldPrice=1), # Thistle Pink
                ShopItem(itemId=14287, price=5, goldPrice=1), # Dianthus Red
                ShopItem(itemId=14005, price=5, goldPrice=1), # Wysteria Purple
                ShopItem(itemId=14014, price=5, goldPrice=1), # Plum Purple
                ShopItem(itemId=14073, price=5, goldPrice=1), # Grape Purple
                ShopItem(itemId=14061, price=5, goldPrice=1), # Pale Lilac Purple
                ShopItem(itemId=14072, price=5, goldPrice=1), # Mauve Purple
                ShopItem(itemId=14135, price=5, goldPrice=1), # Boysenberry Purple
                ShopItem(itemId=14183, price=5, goldPrice=1), # Vidia Purple
                ShopItem(itemId=14184, price=5, goldPrice=1), # Hummingbird Purple
                ShopItem(itemId=14210, price=5, goldPrice=1), # Lotus Purple
                ShopItem(itemId=14211, price=5, goldPrice=1), # Gentian Purple
                ShopItem(itemId=14212, price=5, goldPrice=1), # Indigo Purple
                ShopItem(itemId=14225, price=5, goldPrice=1), # Eggplant Purple
                ShopItem(itemId=14229, price=5, goldPrice=1), # Electric Indigo
                ShopItem(itemId=14276, price=5, goldPrice=1), # Dusk Purple
                ShopItem(itemId=14129, price=5, goldPrice=1), # Fig Purple
                ShopItem(itemId=14134, price=5, goldPrice=1), # Heather Purple
                ShopItem(itemId=14278, price=5, goldPrice=1), # Aster Purple
                ShopItem(itemId=14277, price=5, goldPrice=1), # Misty Purple
                ShopItem(itemId=14117, price=5, goldPrice=1), # Amethyst Purple
                ShopItem(itemId=14033, price=5, goldPrice=1), # Iris Purple
                ShopItem(itemId=14197, price=5, goldPrice=1), # Electric Purple
                ShopItem(itemId=14032, price=5, goldPrice=1), # Mulberry Purple
                ShopItem(itemId=14275, price=5, goldPrice=1), # Shadowy Purple
                ShopItem(itemId=14152, price=5, goldPrice=1), # Pale Purple
                ShopItem(itemId=14192, price=5, goldPrice=1), # Royal Purple
                ShopItem(itemId=14279, price=5, goldPrice=1), # Kingfisher Purple
                ShopItem(itemId=14280, price=5, goldPrice=1), # Berry Purple
                ShopItem(itemId=14281, price=5, goldPrice=1), # Deep Violet Purple
                ShopItem(itemId=14284, price=5, goldPrice=1), # Deep Magenta Purple
            ],
        ),
        ShopCollection(
            collectionId=2001, # Orange & Yellow Dyes
            purchaseType=PurchaseType.POUCH,
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[ # 43
                ShopItem(itemId=14025, price=5, goldPrice=1), # Peachy Orange
                ShopItem(itemId=14031, price=5, goldPrice=1), # Sunset Orange
                ShopItem(itemId=14138, price=5, goldPrice=1), # Persimmon Orange
                ShopItem(itemId=14109, price=5, goldPrice=1), # Soft Orange
                ShopItem(itemId=14123, price=5, goldPrice=1), # Squash Orange
                ShopItem(itemId=14010, price=5, goldPrice=1), # Cantaloupe Orange
                ShopItem(itemId=14237, price=5, goldPrice=1), # Melon Orange
                ShopItem(itemId=14187, price=5, goldPrice=1), # Maple Orange
                ShopItem(itemId=14196, price=5, goldPrice=1), # Electric Orange
                ShopItem(itemId=14228, price=5, goldPrice=1), # Duckbill Orange
                ShopItem(itemId=14234, price=5, goldPrice=1), # Flame Orange
                ShopItem(itemId=14232, price=5, goldPrice=1), # Rusty orange
                ShopItem(itemId=14233, price=5, goldPrice=1), # Apricot Orange
                ShopItem(itemId=14030, price=5, goldPrice=1), # Pumpkin Orange
                ShopItem(itemId=14114, price=5, goldPrice=1), # Foxtail Orange
                ShopItem(itemId=14173, price=5, goldPrice=1), # Carrot Orange
                ShopItem(itemId=14238, price=5, goldPrice=1), # Zesty Orange
                ShopItem(itemId=14178, price=5, goldPrice=1), # Fawn Orange
                ShopItem(itemId=14235, price=5, goldPrice=1), # Tawny Orange
                ShopItem(itemId=14111, price=5, goldPrice=1), # Sparkling Yellow
                ShopItem(itemId=14047, price=5, goldPrice=1), # Buttercup Yellow
                ShopItem(itemId=14142, price=5, goldPrice=1), # Bumble Bee Yellow
                ShopItem(itemId=14162, price=5, goldPrice=1), # Sunglow Yellow
                ShopItem(itemId=14252, price=5, goldPrice=1), # Starshine Yellow
                ShopItem(itemId=14090, price=5, goldPrice=1), # Custard Yellow
                ShopItem(itemId=14247, price=5, goldPrice=1), # Jasmine Yellow
                ShopItem(itemId=14027, price=5, goldPrice=1), # Corn Cob Yellow
                ShopItem(itemId=14253, price=5, goldPrice=1), # Dandelion Yellow
                ShopItem(itemId=14186, price=5, goldPrice=1), # Honeycomb Yellow
                ShopItem(itemId=14248, price=5, goldPrice=1), # Saffron Yellow
                ShopItem(itemId=14011, price=5, goldPrice=1), # Marigold Yellow
                ShopItem(itemId=14242, price=5, goldPrice=1), # Amber Yellow
                ShopItem(itemId=14249, price=5, goldPrice=1), # Antique Yellow
                ShopItem(itemId=14244, price=5, goldPrice=1), # Fairygold Yellow
                ShopItem(itemId=14243, price=5, goldPrice=1), # Harvest Yellow
                ShopItem(itemId=14254, price=5, goldPrice=1), # Sunflower Yellow
                ShopItem(itemId=14179, price=5, goldPrice=1), # Iridessa Yellow
                ShopItem(itemId=14168, price=5, goldPrice=1), # Never Gold
                ShopItem(itemId=14226, price=5, goldPrice=1), # Goldenrod Yellow
                ShopItem(itemId=14198, price=5, goldPrice=1), # Electric Yellow
                ShopItem(itemId=14256, price=5, goldPrice=1), # Pear Yellow
            ],
        ),
        ShopCollection(
            collectionId=2008, # Blue & Green Dyes
            purchaseType=PurchaseType.POUCH,
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[ # 85
                ShopItem(itemId=14037, price=5, goldPrice=1), # Cloudy Blue
                ShopItem(itemId=14062, price=5, goldPrice=1), # Bluebird Blue
                ShopItem(itemId=14051, price=5, goldPrice=1), # Periwinkle Blue
                ShopItem(itemId=14004, price=5, goldPrice=1), # Bluebell Blue
                ShopItem(itemId=14022, price=5, goldPrice=1), # Blue Jay Blue
                ShopItem(itemId=14042, price=5, goldPrice=1), # Blueberry Blue
                ShopItem(itemId=14063, price=5, goldPrice=1), # Butterfly Blue
                ShopItem(itemId=14006, price=5, goldPrice=1), # Havendish Blue
                ShopItem(itemId=14024, price=5, goldPrice=1), # Sky Blue
                ShopItem(itemId=14050, price=5, goldPrice=1), # Cornflower Blue
                ShopItem(itemId=14118, price=5, goldPrice=1), # Sapphire Blue
                ShopItem(itemId=14071, price=5, goldPrice=1), # Dewdrop Blue
                ShopItem(itemId=14133, price=5, goldPrice=1), # Marina Blue
                ShopItem(itemId=14124, price=5, goldPrice=1), # Forget-Me-Not Blue
                ShopItem(itemId=14136, price=5, goldPrice=1), # Peacock Blue
                ShopItem(itemId=14070, price=5, goldPrice=1), # Tinker blue
                ShopItem(itemId=14219, price=5, goldPrice=1), # Crystal Blue
                ShopItem(itemId=14267, price=5, goldPrice=1), # Celestial Blue
                ShopItem(itemId=14195, price=5, goldPrice=1), # Electric Blue
                ShopItem(itemId=14018, price=5, goldPrice=1), # Waterfall Blue
                ShopItem(itemId=14158, price=5, goldPrice=1), # Icicle Blue
                ShopItem(itemId=14068, price=5, goldPrice=1), # Huckleberry Blue
                ShopItem(itemId=14049, price=5, goldPrice=1), # Robin Egg Blue
                ShopItem(itemId=14265, price=5, goldPrice=1), # Bright Sky Blue
                ShopItem(itemId=14040, price=5, goldPrice=1), # Candy Blue
                ShopItem(itemId=14041, price=5, goldPrice=1), # Moonshadow Blue
                ShopItem(itemId=14149, price=5, goldPrice=1), # Snowflake Blue
                ShopItem(itemId=14153, price=5, goldPrice=1), # Frostbunny Blue
                ShopItem(itemId=14155, price=5, goldPrice=1), # Frosty Blue
                ShopItem(itemId=14176, price=5, goldPrice=1), # Silvermist Blue
                ShopItem(itemId=14180, price=5, goldPrice=1), # Seashell Blue
                ShopItem(itemId=14207, price=5, goldPrice=1), # Diamond Blue
                ShopItem(itemId=14209, price=5, goldPrice=1), # Deep Sea Blue
                ShopItem(itemId=14213, price=5, goldPrice=1), # Cobalt Blue
                ShopItem(itemId=14223, price=5, goldPrice=1), # Teal Blue
                ShopItem(itemId=14266, price=5, goldPrice=1), # Ocean Blue
                ShopItem(itemId=14271, price=5, goldPrice=1), # True Blue
                ShopItem(itemId=14270, price=5, goldPrice=1), # Horizon Blue
                ShopItem(itemId=14036, price=5, goldPrice=1), # Hydrangea Blue
                ShopItem(itemId=14182, price=5, goldPrice=1), # Twilight Blue
                ShopItem(itemId=14268, price=5, goldPrice=1), # Navy Blue
                ShopItem(itemId=14185, price=5, goldPrice=1), # Midnight Blue
                ShopItem(itemId=14163, price=5, goldPrice=1), # Tundra Blue
                ShopItem(itemId=14001, price=5, goldPrice=1), # Mint Green
                ShopItem(itemId=14002, price=5, goldPrice=1), # Clover Green
                ShopItem(itemId=14003, price=5, goldPrice=1), # Spruce Green
                ShopItem(itemId=14017, price=5, goldPrice=1), # Tendershoot Green
                ShopItem(itemId=14020, price=5, goldPrice=1), # Grassblade Green
                ShopItem(itemId=14021, price=5, goldPrice=1), # Zucchini Green
                ShopItem(itemId=14035, price=5, goldPrice=1), # Celery Green
                ShopItem(itemId=14039, price=5, goldPrice=1), # Springtime Green
                ShopItem(itemId=14048, price=5, goldPrice=1), # Sea Green
                ShopItem(itemId=14064, price=5, goldPrice=1), # Emerald Green
                ShopItem(itemId=14067, price=5, goldPrice=1), # Chartreuse Green
                ShopItem(itemId=14115, price=5, goldPrice=1), # Asparagus Green
                ShopItem(itemId=14120, price=5, goldPrice=1), # Fern Green
                ShopItem(itemId=14122, price=5, goldPrice=1), # Lettuce Leaf Green
                ShopItem(itemId=14127, price=5, goldPrice=1), # Grasshopper Green
                ShopItem(itemId=14139, price=5, goldPrice=1), # Seedling Green
                ShopItem(itemId=14038, price=5, goldPrice=1), # Apple Green
                ShopItem(itemId=14258, price=5, goldPrice=1), # Spearmint Green
                ShopItem(itemId=14143, price=5, goldPrice=1), # June Bug Green
                ShopItem(itemId=14193, price=5, goldPrice=1), # Electric Green
                ShopItem(itemId=14222, price=5, goldPrice=1), # Keylime Green
                ShopItem(itemId=14263, price=5, goldPrice=1), # Aquamarine Green
                ShopItem(itemId=14221, price=5, goldPrice=1), # Jade Green
                ShopItem(itemId=14125, price=5, goldPrice=1), # Pine Green
                ShopItem(itemId=14147, price=5, goldPrice=1), # Broccoli Stem Green
                ShopItem(itemId=14150, price=5, goldPrice=1), # Dry Moss Green
                ShopItem(itemId=14175, price=5, goldPrice=1), # Creek Green
                ShopItem(itemId=14190, price=5, goldPrice=1), # Firefly Green
                ShopItem(itemId=14202, price=5, goldPrice=1), # Honeydew Green
                ShopItem(itemId=14203, price=5, goldPrice=1), # Shadow Green
                ShopItem(itemId=14159, price=5, goldPrice=1), # Tea Green
                ShopItem(itemId=14165, price=5, goldPrice=1), # Spring Breeze Green
                ShopItem(itemId=14170, price=5, goldPrice=1), # Olive Green
                ShopItem(itemId=14172, price=5, goldPrice=1), # Forest Green
                ShopItem(itemId=14204, price=5, goldPrice=1), # Bamboo Green
                ShopItem(itemId=14205, price=5, goldPrice=1), # Myrtle Green
                ShopItem(itemId=14218, price=5, goldPrice=1), # Laurel Green
                ShopItem(itemId=14257, price=5, goldPrice=1), # Lime Green
                ShopItem(itemId=14260, price=5, goldPrice=1), # Peridot Green
                ShopItem(itemId=14261, price=5, goldPrice=1), # Kelly Green
                ShopItem(itemId=14264, price=5, goldPrice=1), # Jungle Green
                ShopItem(itemId=14145, price=5, goldPrice=1), # Tinker Bell Green

            ],
        ),
        ShopCollection(
            collectionId=2009, # Brown & Neutral Dyes
            purchaseType=PurchaseType.POUCH,
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[ # 47
                ShopItem(itemId=14087, price=5, goldPrice=1), # Driftwood Brown
                ShopItem(itemId=14083, price=5, goldPrice=1), # Cherry Brown
                ShopItem(itemId=14079, price=5, goldPrice=1), # Sienna Brown
                ShopItem(itemId=14075, price=5, goldPrice=1), # Umber Brown
                ShopItem(itemId=14236, price=5, goldPrice=1), # Dusty Brown
                ShopItem(itemId=14078, price=5, goldPrice=1), # Fawn Brown
                ShopItem(itemId=14056, price=5, goldPrice=1), # Bole Brown
                ShopItem(itemId=14076, price=5, goldPrice=1), # Chocolate Brown
                ShopItem(itemId=14089, price=5, goldPrice=1), # Seashore Brown
                ShopItem(itemId=14085, price=5, goldPrice=1), # Quail Brown
                ShopItem(itemId=14246, price=5, goldPrice=1), # Bear Brown
                ShopItem(itemId=14240, price=5, goldPrice=1), # Ironwood Brown
                ShopItem(itemId=14161, price=5, goldPrice=1), # Buried Treasure Brown
                ShopItem(itemId=14088, price=5, goldPrice=1), # Fruitwood Brown
                ShopItem(itemId=14084, price=5, goldPrice=1), # Copper Brown
                ShopItem(itemId=14074, price=5, goldPrice=1), # Soil Brown
                ShopItem(itemId=14241, price=5, goldPrice=1), # Desert Brown
                ShopItem(itemId=14154, price=5, goldPrice=1), # Beetle Brown
                ShopItem(itemId=14046, price=5, goldPrice=1), # Bark Brown
                ShopItem(itemId=14077, price=5, goldPrice=1), # Sepia Brown
                ShopItem(itemId=14250, price=5, goldPrice=1), # Caramel Tan
                ShopItem(itemId=14146, price=5, goldPrice=1), # Beech Brown
                ShopItem(itemId=14245, price=5, goldPrice=1), # Earthy Tan
                ShopItem(itemId=14251, price=5, goldPrice=1), # Polished Brown
                ShopItem(itemId=14177, price=5, goldPrice=1), # Mud Brown
                ShopItem(itemId=14166, price=5, goldPrice=1), # Snow White
                ShopItem(itemId=14262, price=5, goldPrice=1), # Minty White
                ShopItem(itemId=14269, price=5, goldPrice=1), # Crisp White
                ShopItem(itemId=14282, price=5, goldPrice=1), # Magnolia White
                ShopItem(itemId=14224, price=5, goldPrice=1), # Ivory White
                ShopItem(itemId=14157, price=5, goldPrice=1), # Starry White
                ShopItem(itemId=14116, price=5, goldPrice=1), # Mushroom White
                ShopItem(itemId=14128, price=5, goldPrice=1), # Carnation White
                ShopItem(itemId=14227, price=5, goldPrice=1), # Moonlight Gray
                ShopItem(itemId=14169, price=5, goldPrice=1), # Squirrel Gray
                ShopItem(itemId=14214, price=5, goldPrice=1), # Smokey Gray
                ShopItem(itemId=14272, price=5, goldPrice=1), # Charcoal Gray
                ShopItem(itemId=14239, price=5, goldPrice=1), # Coffee Black
                ShopItem(itemId=14206, price=5, goldPrice=1), # Raven Black
                ShopItem(itemId=14217, price=5, goldPrice=1), # Soft Gray
                ShopItem(itemId=14215, price=5, goldPrice=1), # Pewter Gray
                ShopItem(itemId=14141, price=5, goldPrice=1), # Thundercloud Gray
                ShopItem(itemId=14273, price=5, goldPrice=1), # Panther Black
                ShopItem(itemId=14167, price=5, goldPrice=1), # Never Silver
                ShopItem(itemId=14216, price=5, goldPrice=1), # Slate Gray
                ShopItem(itemId=14191, price=5, goldPrice=1), # Vidia Black
                ShopItem(itemId=14055, price=5, goldPrice=1), # Pepper Black
            ],
        ),
    ],
)