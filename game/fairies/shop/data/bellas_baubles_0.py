from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.BELLAS_BAUBLES,
    shopId=0,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.BELLA_ROSE,
        position=(420, 420),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_BELLA_ROSE
    ),
    collections=[
        ShopCollection(
            collectionId=6, # Hats and Hairpieces
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=2005, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Vine Headband
                ShopItem(itemId=2009, price=30, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Rose Bloom Barrettes
                ShopItem(itemId=2012, price=30, goldPrice=3, color1=186, color2=186, itemType="HeadItem"), # Honeycomb Yellow Hickory Leaf Headdress
                ShopItem(itemId=2013, price=30, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Feather Cap
                ShopItem(itemId=2032, price=30, goldPrice=3, color1=258, color2=258, itemType="HeadItem"), # Spearmint Green Little Lily Pad Barrette
                ShopItem(itemId=2097, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Coin Headband
                ShopItem(itemId=2098, price=30, goldPrice=3, color1=227, color2=227, itemType="HeadItem"), # Moonlight Gray Timely Barrette
                ShopItem(itemId=2237, price=30, goldPrice=3, color1=206, color2=206, itemType="HeadItem"), # Raven Black Spider Web Veil Hat
                ShopItem(itemId=2400, price=30, goldPrice=3, color1=161, color2=78,  itemType="HeadItem"), # Buried Treasure Brown Straw Fascinator with Fawn Brown Trim
                ShopItem(itemId=2401, price=30, goldPrice=3, color1=141, color2=141, itemType="HeadItem"), # Thundercloud Gray Peacock Plume Fascinator
                ShopItem(itemId=2402, price=30, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Butterfly Fascinator
                ShopItem(itemId=2404, price=30, goldPrice=3, color1=168, color2=168, itemType="HeadItem"), # Never Gold Gemstone Accessory Set
                ShopItem(itemId=2417, price=30, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Cherry Pie Hat
                ShopItem(itemId=2419, price=30, goldPrice=3, color1=277, color2=277, itemType="HeadItem"), # Misty Purple Cute Cupcake Headband
                ShopItem(itemId=2420, price=30, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Cake Slice Headband
                ShopItem(itemId=2168, price=30, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Friendship Headband
                ShopItem(itemId=2291, price=30, goldPrice=3, color1=224, color2=267, itemType="HeadItem"), # Ivory White Cherry-On-Top Hat with Celestial Blue Trim
                ShopItem(itemId=2437, price=30, goldPrice=3, color1=10,  color2=10,  itemType="HeadItem"), # Cantaloupe Orange Siren Style Headband
                ShopItem(itemId=2095, price=30, goldPrice=3, color1=126, color2=126, itemType="HeadItem"), # Raindrop Blue Clam Ribbon Headband
                ShopItem(itemId=2094, price=30, goldPrice=3, color1=109, color2=139, itemType="HeadItem"), # Soft Orange Sand Dollar Headband with Seedling Green Trim
                ShopItem(itemId=2270, price=30, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Feather Headpiece
                ShopItem(itemId=2305, price=30, goldPrice=3, color1=140, color2=140, itemType="HeadItem"), # Bunnynose Pink Beautiful Bow Headband
                ShopItem(itemId=2196, price=30, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Dewdrop Headpiece
                ShopItem(itemId=2207, price=30, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Sun 'n' Sand Beach Hat
                ShopItem(itemId=2468, price=30, goldPrice=3, color1=224, color2=18,  itemType="HeadItem"), # Ivory White Enchantress Crown with Waterfall Blue Trim
                ShopItem(itemId=2469, price=30, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Sorceress Barrette
                ShopItem(itemId=2199, price=30, goldPrice=3, color1=121, color2=121, itemType="HeadItem"), # Daisy Pink Little Bow Cap
                ShopItem(itemId=2202, price=30, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Cute Little Cap
                ShopItem(itemId=2198, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Fly Backwards Cap
                ShopItem(itemId=2210, price=30, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Tassled Knit Hat
                ShopItem(itemId=2211, price=30, goldPrice=3, color1=267, color2=267, itemType="HeadItem"), # Celestial Blue Chunky Knit Hat
                ShopItem(itemId=2212, price=30, goldPrice=3, color1=221, color2=221, itemType="HeadItem"), # Jade Green Pixie Puff Beanie
                ShopItem(itemId=2197, price=30, goldPrice=3, color1=126, color2=126, itemType="HeadItem"), # Raindrop Blue Teardrop Headpiece
                ShopItem(itemId=2369, price=30, goldPrice=3, color1=207, color2=207, itemType="HeadItem"), # Diamond Blue Frozen Flower Tiara
                ShopItem(itemId=2236, price=30, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Harvest Moon Tiara
                ShopItem(itemId=2388, price=30, goldPrice=3, color1=188, color2=188, itemType="HeadItem"), # Dahlia Pink Butterfly Tiara
                ShopItem(itemId=2389, price=30, goldPrice=3, color1=167, color2=167, itemType="HeadItem"), # Never Silver Crystal Tiara
                ShopItem(itemId=2390, price=30, goldPrice=3, color1=207, color2=162, itemType="HeadItem"), # Diamond Blue Frosty Tiara with Sunglow Yellow Trim
                ShopItem(itemId=2146, price=30, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Wintry Comb
                ShopItem(itemId=2145, price=30, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Wintry Chain
                ShopItem(itemId=2147, price=30, goldPrice=3, color1=153, color2=153, itemType="HeadItem"), # Frostbunny Blue Wintry Tiara
                ShopItem(itemId=2044, price=30, goldPrice=3, color1=283, color2=283, itemType="HeadItem"), # Thistle Pink Flower Sunglasses
                ShopItem(itemId=2324, price=30, goldPrice=3, color1=206, color2=162, itemType="HeadItem"), # Raven Black Casual Shades with Yellow Trim
                ShopItem(itemId=2141, price=30, goldPrice=3, color1=215, color2=215, itemType="HeadItem"), # Pewter Gray Sharp Sun-Shades
                ShopItem(itemId=2159, price=30, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Heart Glasses
            ],
        ),
        
        ShopCollection(
            collectionId=7, # Bracelets
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=1663, price=10, goldPrice=1, color1=168, color2=168, itemType="WristItem"), # Never Gold Gemstone Bangle
                ShopItem(itemId=1519, price=10, goldPrice=1, color1=121, color2=230, itemType="WristItem"), # Daisy Pink Friendship Bracelet with Scarlet Red Trim
                ShopItem(itemId=1560, price=10, goldPrice=1, color1=211, color2=211, itemType="WristItem"), # Gentian Purple Friendship Wrap
                ShopItem(itemId=1628, price=10, goldPrice=1, color1=45,  color2=45,  itemType="WristItem"), # Strawberry Red Licorice Twist Bracelet
                ShopItem(itemId=1549, price=10, goldPrice=1, color1=42,  color2=42,  itemType="WristItem"), # Blueberry Blue Rainbow Wrist Bands
                ShopItem(itemId=1548, price=10, goldPrice=1, color1=126, color2=227, itemType="WristItem"), # Raindrop Blue Raindrop Bracelet with Moonlight Gray Trim
                ShopItem(itemId=1681, price=10, goldPrice=1, color1=121, color2=224, itemType="WristItem"), # Daisy Pink Delicate Daisy Corsage with Ivory White Trim
                ShopItem(itemId=1680, price=10, goldPrice=1, color1=63,  color2=63,  itemType="WristItem"), # Butterfly Blue Opulent Orchid Corsage
                ShopItem(itemId=1679, price=10, goldPrice=1, color1=166, color2=166, itemType="WristItem"), # Snow White Ravishing Rose Corsage
                ShopItem(itemId=1526, price=10, goldPrice=1, color1=180, color2=180, itemType="WristItem"), # Seashell Blue Clam Ribbon Bracelet
                ShopItem(itemId=1527, price=10, goldPrice=1, color1=152, color2=152, itemType="WristItem"), # Pale Purple Shell Bracelet
                ShopItem(itemId=1604, price=10, goldPrice=1, color1=221, color2=221, itemType="WristItem"), # Jade Green Feathered Bracelet
                ShopItem(itemId=1631, price=10, goldPrice=1, color1=200, color2=200, itemType="WristItem"), # Ruby Pink Ribbon Wrap
                ShopItem(itemId=1561, price=10, goldPrice=1, color1=30,  color2=30,  itemType="WristItem"), # Pumpkin Orange Freesia Wrist Flounce
                ShopItem(itemId=1523, price=10, goldPrice=1, color1=200, color2=200, itemType="WristItem"), # Ruby Pink Dear Droplets Bracelet
                ShopItem(itemId=1546, price=10, goldPrice=1, color1=18,  color2=18,  itemType="WristItem"), # Waterfall Blue Triple Tie Bracelet
                ShopItem(itemId=1629, price=10, goldPrice=1, color1=162, color2=162, itemType="WristItem"), # Sunglow Yellow Twirly Jeweled Bracelet
                ShopItem(itemId=1566, price=10, goldPrice=1, color1=138, color2=138, itemType="WristItem"), # Persimmon Orange Bottle Cap Bracelet
                ShopItem(itemId=1649, price=10, goldPrice=1, color1=129, color2=129, itemType="WristItem"), # Fig Purple Jeweled Bracelet Ring
                ShopItem(itemId=1650, price=10, goldPrice=1, color1=221, color2=221, itemType="WristItem"), # Jade Green Pearl Pendant Ring
                ShopItem(itemId=1652, price=10, goldPrice=1, color1=162, color2=162, itemType="WristItem"), # Sunglow Yellow Chain Ring Bracelet
                ShopItem(itemId=1598, price=10, goldPrice=1, color1=221, color2=221, itemType="WristItem"), # Jade Green Clover Bracelet
                ShopItem(itemId=1522, price=10, goldPrice=1, color1=126, color2=126, itemType="WristItem"), # Raindrop Blue Teardrop Bracelet
                ShopItem(itemId=1516, price=10, goldPrice=1, color1=69,  color2=69,  itemType="WristItem"), # Powder Blue Double Bubble Bracelet
                ShopItem(itemId=1509, price=10, goldPrice=1, color1=64,  color2=64,  itemType="WristItem"), # Emerald Green Grass Multi-Wrap Bracelet
                ShopItem(itemId=1653, price=10, goldPrice=1, color1=45,  color2=45,  itemType="WristItem"), # Strawberry Red Spider Web Bracelet
                ShopItem(itemId=1521, price=10, goldPrice=3, color1=265, color2=10,  itemType="WristItem"), # Bright Sky Blue Tiger Lily Bracelet with Cantaloupe Orange Trim
                ShopItem(itemId=1593, price=10, goldPrice=3, color1=162, color2=162, itemType="WristItem"), # Sunglow Yellow Harvest Moon Bracelet
                ShopItem(itemId=1543, price=10, goldPrice=3, color1=216, color2=216, itemType="WristItem"), # Slate Gray Pinned Cuff
                ShopItem(itemId=1544, price=10, goldPrice=3, color1=277, color2=277, itemType="WristItem"), # Misty Purple Knotted Cuff	
                ShopItem(itemId=1545, price=10, goldPrice=3, color1=258, color2=258, itemType="WristItem"), # Spearmint Green Two Ribbon Bracelet
                ShopItem(itemId=1636, price=10, goldPrice=3, color1=121, color2=121, itemType="WristItem"), # Daisy Pink Festive Ball Bracelet
                ShopItem(itemId=1607, price=10, goldPrice=3, color1=135, color2=135, itemType="WristItem"), # Boysenberry Purple Pixie Pals Bracelet
                ShopItem(itemId=1606, price=10, goldPrice=3, color1=230, color2=230, itemType="WristItem"), # Scarlet Red Fairy Friends Forever Bracelet
                ShopItem(itemId=1584, price=10, goldPrice=3, color1=17,  color2=17,  itemType="WristItem"), # Tendershoot Green Trinity Leaf Bracelet
                ShopItem(itemId=1575, price=10, goldPrice=3, color1=247, color2=247, itemType="WristItem"), # Jasmine Yellow Flower Pom-Pom
                ShopItem(itemId=1542, price=10, goldPrice=3, color1=167, color2=167, itemType="WristItem"), # Never Silver Vine Wrap Cuff
                ShopItem(itemId=1541, price=10, goldPrice=3, color1=208, color2=208, itemType="WristItem"), # Cerulean Blue Bandana Cuff
                ShopItem(itemId=1528, price=10, goldPrice=3, color1=227, color2=227, itemType="WristItem"), # Moonlight Gray Tinkered Cuff
                ShopItem(itemId=1510, price=10, goldPrice=3, color1=121, color2=121, itemType="WristItem"), # Daisy Pink Buttercup Bracelet
                ShopItem(itemId=1507, price=10, goldPrice=3, color1=69,  color2=69,  itemType="WristItem"), # Powder Blue Cherry Blossom Bracelet
                ShopItem(itemId=1505, price=10, goldPrice=3, color1=139, color2=139, itemType="WristItem"), # Seedling Green Silk Leaf Sprouter
                ShopItem(itemId=1504, price=10, goldPrice=3, color1=27,  color2=27,  itemType="WristItem"), # Corn Cob Yellow Hibiscus Wrap Bracelet
                ShopItem(itemId=1503, price=10, goldPrice=3, color1=152, color2=152, itemType="WristItem"), # Pale Purple Double Blossom Bracelet
                ShopItem(itemId=1502, price=10, goldPrice=3, color1=201, color2=201, itemType="WristItem"), # Velvet Red Rose Bud Bracelet
            ],
        ),

        ShopCollection(
            collectionId=8, # Purses and Props
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=1574, price=10, goldPrice=1, color1=154, color2=154, itemType="WristItem"), # Beetle Brown Frilly Flower Tote
                ShopItem(itemId=1579, price=10, goldPrice=1, color1=136, color2=162, itemType="WristItem"), # Peacock Blue Peacock Clutch with Sunglow Yellow Trim
                ShopItem(itemId=1580, price=10, goldPrice=1, color1=189, color2=189, itemType="WristItem"), # Ladybug Red Polka-Dot Clutch
                ShopItem(itemId=1581, price=10, goldPrice=1, color1=265, color2=265, itemType="WristItem"), # Bright Sky Blue Flower Clutch
                ShopItem(itemId=1678, price=10, goldPrice=1, color1=30,  color2=30,  itemType="WristItem"), # Pumpkin Orange Sweet Spring Citrus Purse
                ShopItem(itemId=1668, price=10, goldPrice=1, color1=211, color2=211, itemType="WristItem"), # Gentian Purple Elegant Egg Purse
                ShopItem(itemId=1576, price=10, goldPrice=1, color1=199, color2=199, itemType="WristItem"), # Cherryblossom Pink Posey Purse
                ShopItem(itemId=2645, price=10, goldPrice=1, color1=105, color2=105, itemType="Necklace"), # Siltstone Tan Ruffled Rose Purse
                ShopItem(itemId=2619, price=10, goldPrice=1, color1=267, color2=267, itemType="Necklace"), # Celestial Blue Feather Fringe Purse
                ShopItem(itemId=2620, price=10, goldPrice=1, color1=10,  color2=10,  itemType="Necklace"), # Cantaloupe Orange Vine Chain Purse
                ShopItem(itemId=2623, price=10, goldPrice=1, color1=221, color2=221, itemType="Necklace"), # Jade Green Peacock Plume Purse
                ShopItem(itemId=1672, price=10, goldPrice=1, color1=168, color2=168, itemType="WristItem"), # Never Gold Radiant Rainbow Clutch
                ShopItem(itemId=1677, price=10, goldPrice=1, color1=18,  color2=18,  itemType="WristItem"), # Waterfall Blue Siren's Scepter
                ShopItem(itemId=1676, price=10, goldPrice=1, color1=18,  color2=18,  itemType="WristItem"), # Waterfall Blue Siren's Harp
                ShopItem(itemId=1588, price=10, goldPrice=1, color1=121, color2=121, itemType="WristItem"), # Daisy Pink Spring Bouquet
                ShopItem(itemId=1589, price=10, goldPrice=1, color1=69,  color2=69,  itemType="WristItem"), # Powder Blue Summer Bouquet
                ShopItem(itemId=1587, price=10, goldPrice=1, color1=45,  color2=45,  itemType="WristItem"), # Strawberry Red Autumn Bouquet
                ShopItem(itemId=1590, price=10, goldPrice=1, color1=207, color2=207, itemType="WristItem"), # Diamond Blue Winter Bouquet
                ShopItem(itemId=1632, price=10, goldPrice=1, color1=224, color2=111, itemType="WristItem"), # Ivory White Shopping Bags with Sparkling Yellow Trim
                ShopItem(itemId=2640, price=10, goldPrice=1, color1=154, color2=154, itemType="Necklace"), # Beetle Brown Box Camera
                ShopItem(itemId=1675, price=10, goldPrice=1, color1=109, color2=109, itemType="WristItem"), # Soft Orange Camping Backpack
                ShopItem(itemId=1671, price=10, goldPrice=1, color1=63,  color2=63,  itemType="WristItem"), # Butterfly Blue Butterfly Umbrella
                ShopItem(itemId=1657, price=10, goldPrice=1, color1=162, color2=106, itemType="WristItem"), # Sunglow Yellow Star Wand with Butternut Tan Trim
                ShopItem(itemId=1656, price=10, goldPrice=1, color1=111, color2=111, itemType="WristItem"), # Sparkling Yellow Wooden Wand
                ShopItem(itemId=1644, price=10, goldPrice=1, color1=199, color2=199, itemType="WristItem"), # Cherryblossom Pink Hand Fan

            ],
        ),

        ShopCollection(
            collectionId=13, # Necklaces
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=2630, price=10, goldPrice=1, color1=168, color2=168, itemType="Necklace"), # Never Gold Gemstone Necklace
                ShopItem(itemId=2580, price=10, goldPrice=1, color1=152, color2=152, itemType="Necklace"), # Pale Purple Twisty Winter Warmer
                ShopItem(itemId=2594, price=10, goldPrice=1, color1=10,  color2=18,  itemType="Necklace"), # Cantaloupe Orange Gummy Necklace with Waterfall Blue Trim
                ShopItem(itemId=2633, price=10, goldPrice=1, color1=166, color2=166, itemType="Necklace"), # Snow White Rainbow Scarf
                ShopItem(itemId=2550, price=10, goldPrice=1, color1=126, color2=227, itemType="Necklace"), # Raindrop Blue Raindrop Necklace with Moonlight Gray Trim
                ShopItem(itemId=2638, price=10, goldPrice=1, color1=199, color2=199, itemType="Necklace"), # Cherryblossom Pink Siren Style Necklace
                ShopItem(itemId=2597, price=10, goldPrice=1, color1=200, color2=200, itemType="Necklace"), # Ruby Pink Ravishing Ribbon Necklace
                ShopItem(itemId=2521, price=10, goldPrice=1, color1=13,  color2=13,  itemType="Necklace"), # Coral Pink Leafy Necklace
                ShopItem(itemId=2535, price=10, goldPrice=1, color1=200, color2=200, itemType="Necklace"), # Ruby Pink Dear Droplets Necklace
                ShopItem(itemId=2530, price=10, goldPrice=1, color1=5,   color2=69,  itemType="Necklace"), # Wysteria Purple Flowery Lei with Powder Blue Trim
                ShopItem(itemId=2595, price=10, goldPrice=1, color1=162, color2=162, itemType="Necklace"), # Sunglow Yellow Twirly Jeweled Necklace
                ShopItem(itemId=2563, price=10, goldPrice=1, color1=30,  color2=30,  itemType="Necklace"), # Pumpkin Orange Bottle Cap Pendant
                ShopItem(itemId=2553, price=10, goldPrice=1, color1=2,   color2=2,   itemType="Necklace"), # Clover Green Rainbow Necklace
                ShopItem(itemId=2532, price=10, goldPrice=1, color1=126, color2=126, itemType="Necklace"), # Raindrop Blue Teardrop Necklace
                ShopItem(itemId=2523, price=10, goldPrice=1, color1=208, color2=208, itemType="Necklace"), # Cerulean Blue Triple Bubble Necklace
                ShopItem(itemId=2511, price=10, goldPrice=1, color1=35,  color2=35,  itemType="Necklace"), # Celery Green Multi-Sweetwrap Necklace
                ShopItem(itemId=2622, price=10, goldPrice=1, color1=45,  color2=45,  itemType="Necklace"), # Strawberry Red Spider Web Necklace
                ShopItem(itemId=2628, price=10, goldPrice=1, color1=207, color2=207, itemType="Necklace"), # Diamond Blue Frozen Flower Necklace
                ShopItem(itemId=2579, price=10, goldPrice=1, color1=162, color2=162, itemType="Necklace"), # Sunglow Yellow Harvest Moon Necklace
                ShopItem(itemId=2551, price=10, goldPrice=1, color1=129, color2=129, itemType="Necklace"), # Fig Purple Fringed Scarf
                ShopItem(itemId=2552, price=10, goldPrice=1, color1=175, color2=175, itemType="Necklace"), # Creek Green Striped Scarf
                ShopItem(itemId=2626, price=10, goldPrice=1, color1=840, color2=84,  itemType="Necklace"), # Copper Brown Golden Acorn Necklace
                ShopItem(itemId=2611, price=10, goldPrice=1, color1=267, color2=267, itemType="Necklace"), # Celestial Blue Silky Scarf
                ShopItem(itemId=2601, price=10, goldPrice=1, color1=121, color2=121, itemType="Necklace"), # Daisy Pink Casual Scarf
                ShopItem(itemId=2600, price=10, goldPrice=1, color1=265, color2=265, itemType="Necklace"), # Bright Sky Blue Puffball Necklace
                ShopItem(itemId=2598, price=10, goldPrice=1, color1=10,  color2=10,  itemType="Necklace"), # Cantaloupe Orange Skinny Tie
                ShopItem(itemId=2585, price=10, goldPrice=1, color1=230, color2=230, itemType="Necklace"), # Scarlet Red Fairy Friends Necklace
                ShopItem(itemId=2576, price=10, goldPrice=1, color1=35,  color2=35,  itemType="Necklace"), # Celery Green Trinity Leaf Necklace
                ShopItem(itemId=2546, price=10, goldPrice=1, color1=86,  color2=86,  itemType="Necklace"), # Nutmeg Brown Camp Pixie Dust Kerchief
                ShopItem(itemId=2537, price=10, goldPrice=1, color1=129, color2=129, itemType="Necklace"), # Fig Purple Coiled Gear Necklace
                ShopItem(itemId=2536, price=10, goldPrice=1, color1=69,  color2=69,  itemType="Necklace"), # Powder Blue Mermaid Shell Necklace
                ShopItem(itemId=2529, price=10, goldPrice=1, color1=224, color2=224, itemType="Necklace"), # Ivory White Never Pearl Necklace
                ShopItem(itemId=2522, price=10, goldPrice=1, color1=64,  color2=64,  itemType="Necklace"), # Emerald Green Cottonpuff Pendant
                ShopItem(itemId=2514, price=10, goldPrice=1, color1=11,  color2=11,  itemType="Necklace"), # Marigold Yellow Stargazer Pendant
                ShopItem(itemId=2510, price=10, goldPrice=1, color1=130, color2=130, itemType="Necklace"), # Orchid Pink Buttercup Pendant
                ShopItem(itemId=2507, price=10, goldPrice=1, color1=277, color2=277, itemType="Necklace"), # Misty Purple Chain of Hearts
                ShopItem(itemId=2506, price=10, goldPrice=1, color1=270, color2=270, itemType="Necklace"), # Horizon Blue Berry Bead Necklace
                ShopItem(itemId=2504, price=10, goldPrice=1, color1=201, color2=201, itemType="Necklace"), # Velvet Red Rose Bud Pendant
                ShopItem(itemId=2502, price=10, goldPrice=1, color1=11,  color2=11,  itemType="Necklace"), # Marigold Yellow Blossom Chain
                ShopItem(itemId=2624, price=10, goldPrice=1, color1=18,  color2=18,  itemType="Necklace"), # Waterfall Blue Sparkly Wings Necklace

            ],
        ),

        ShopCollection(
            collectionId=29, # Belts
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=639, price=10, goldPrice=1, color1=200, color2=200, itemType="Belt"), # Ruby Pink Short Sarong
                ShopItem(itemId=586, price=10, goldPrice=1, color1=35,  color2=35,  itemType="Belt"), # Celery Green Clover Belt
                ShopItem(itemId=630, price=10, goldPrice=1, color1=152, color2=152, itemType="Belt"), # Pale Purple Gardening Utility Belt
                ShopItem(itemId=642, price=10, goldPrice=1, color1=45,  color2=45,  itemType="Belt"), # Strawberry Red Spider Web Belt
                ShopItem(itemId=648, price=10, goldPrice=1, color1=154, color2=154, itemType="Belt"), # Beetle Brown Autumn Leaves Belt
                ShopItem(itemId=646, price=10, goldPrice=1, color1=154, color2=154, itemType="Belt"), # Beetle Brown Super Striped Belt
                ShopItem(itemId=647, price=10, goldPrice=1, color1=126, color2=126, itemType="Belt"), # Raindrop Blue Lovely Links Belt
                ShopItem(itemId=645, price=10, goldPrice=1, color1=28,  color2=28,  itemType="Belt"), # Cinnamon Brown Wonderful Woven Belt
                ShopItem(itemId=591, price=10, goldPrice=1, color1=227, color2=227, itemType="Belt"), # Moonlight Gray Whisk Belt
                ShopItem(itemId=589, price=10, goldPrice=1, color1=184, color2=184, itemType="Belt"), # Hummingbird Purple Raven Feather Belt
                ShopItem(itemId=587, price=10, goldPrice=1, color1=91,  color2=91,  itemType="Belt"), # Coconut Brown Basic Belt
                ShopItem(itemId=576, price=10, goldPrice=1, color1=183, color2=183, itemType="Belt"), # Vidia Purple Fast-Flying Feather
                ShopItem(itemId=565, price=10, goldPrice=1, color1=139, color2=139, itemType="Belt"), # Seedling Green Artsy Floral Belt
                ShopItem(itemId=545, price=10, goldPrice=1, color1=208, color2=208, itemType="Belt"), # Cerulean Blue Pinecone Belt
                ShopItem(itemId=544, price=10, goldPrice=1, color1=161, color2=161, itemType="Belt"), # Buried Treasure Brown Artists Clothing Belt
                ShopItem(itemId=531, price=10, goldPrice=1, color1=121, color2=121, itemType="Belt"), # Daisy Pink Ruffled Myrtle Leaf Belt
                ShopItem(itemId=521, price=10, goldPrice=1, color1=27,  color2=27,  itemType="Belt"), # Corn Cob Yellow Pleated Petal Sash
                ShopItem(itemId=520, price=10, goldPrice=1, color1=69,  color2=69,  itemType="Belt"), # Powder Blue Spider Silk Tie Belt
                ShopItem(itemId=519, price=10, goldPrice=1, color1=152, color2=152, itemType="Belt"), # Pale Purple Raindrop Sash
                ShopItem(itemId=514, price=10, goldPrice=1, color1=258, color2=258, itemType="Belt"), # Spearmint Green Sunburst Petal Belt
                ShopItem(itemId=513, price=10, goldPrice=1, color1=125, color2=125, itemType="Belt"), # Pine Green Stringbean Sash	
                ShopItem(itemId=510, price=10, goldPrice=1, color1=10,  color2=10,  itemType="Belt"), # Cantaloupe Orange Starfire Sash
                ShopItem(itemId=507, price=10, goldPrice=1, color1=139, color2=139, itemType="Belt"), # Seedling Green Wax Leaf Sash

            ],
        ),

        ShopCollection(
            collectionId=32, # Earrings and Anklets
            currencyId=INGREDIENTS["SPIDER_SILK"].id,
            items=[
                ShopItem(itemId=2233, price=10, goldPrice=3, color1=136, color2=136, itemType="HeadItem"), # Peacock Blue Feather Earrings
                ShopItem(itemId=2247, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Harvest Moon Earrings
                ShopItem(itemId=2255, price=10, goldPrice=3, color1=274, color2=274, itemType="HeadItem"), # Bellflower Purple Beaded Row Earrings
                ShopItem(itemId=2261, price=10, goldPrice=3, color1=30,  color2=30,  itemType="HeadItem"), # Pumpkin Orange Button Earrings
                ShopItem(itemId=2264, price=10, goldPrice=3, color1=258, color2=258, itemType="HeadItem"), # Spearmint Green Bottlecap Earrings
                ShopItem(itemId=2233, price=10, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Feather Earrings
                ShopItem(itemId=2268, price=10, goldPrice=3, color1=35,  color2=35,  itemType="HeadItem"), # Celery Green Trinity Leaf Earrings
                ShopItem(itemId=2368, price=10, goldPrice=3, color1=207, color2=207, itemType="HeadItem"), # Diamond Blue Frozen Flower Earrings
                ShopItem(itemId=2366, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Darling Dandelion Earrings
                ShopItem(itemId=2365, price=10, goldPrice=3, color1=27,  color2=64,  itemType="HeadItem"), # Corn Cob Yellow Sweet Wheat Earrings with Emerald Green Trim
                ShopItem(itemId=2364, price=10, goldPrice=3, color1=199, color2=199, itemType="HeadItem"), # Cherryblossom Pink Maple Leaf Earrings
                ShopItem(itemId=2363, price=10, goldPrice=3, color1=84,  color2=84,  itemType="HeadItem"), # Copper Brown Acorn Earrings
                ShopItem(itemId=2251, price=10, goldPrice=3, color1=208, color2=208, itemType="HeadItem"), # Cerulean Blue Bubble Earrings
                ShopItem(itemId=2322, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Blooming Earrings
                ShopItem(itemId=2321, price=10, goldPrice=3, color1=175, color2=175, itemType="HeadItem"), # Creek Green Pearly Flower Earrings
                ShopItem(itemId=2258, price=10, goldPrice=3, color1=2,   color2=2,   itemType="HeadItem"), # Clover Green Lucky Rainbow Earrings
                ShopItem(itemId=2320, price=10, goldPrice=3, color1=35,  color2=35,  itemType="HeadItem"), # Celery Green Beautiful Bud Earrings
                ShopItem(itemId=2300, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Twirly Jeweled Earrings
                ShopItem(itemId=2254, price=10, goldPrice=3, color1=200, color2=200, itemType="HeadItem"), # Ruby Pink Dewdrop Earrings
                ShopItem(itemId=2446, price=10, goldPrice=3, color1=227, color2=227, itemType="HeadItem"), # Moonlight Gray Lost Spoon Danglies
                ShopItem(itemId=2447, price=10, goldPrice=3, color1=230, color2=230, itemType="HeadItem"), # Scarlet Red Rose Pearl Danglies
                ShopItem(itemId=2445, price=10, goldPrice=3, color1=152, color2=152, itemType="HeadItem"), # Pale Purple Beaded Heart Danglies
                ShopItem(itemId=2253, price=10, goldPrice=3, color1=126, color2=227, itemType="HeadItem"), # Raindrop Blue Raindrop Earrings with Moonlight Gray Trim
                ShopItem(itemId=2426, price=10, goldPrice=3, color1=168, color2=168, itemType="HeadItem"), # Never Gold Simple Hoops
                ShopItem(itemId=2424, price=10, goldPrice=3, color1=113, color2=113, itemType="HeadItem"), # Pale Rose Red Heart-Shaped Hoops
                ShopItem(itemId=2425, price=10, goldPrice=3, color1=162, color2=162, itemType="HeadItem"), # Sunglow Yellow Shimmery Hoops
                ShopItem(itemId=3033, price=10, goldPrice=1, color1=121, color2=121, itemType="AnkleItem"), # Daisy Pink Friendship Anklet
                ShopItem(itemId=3051, price=10, goldPrice=1, color1=45,  color2=45,  itemType="AnkleItem"), # Strawberry Red Licorice Twist Anklet
                ShopItem(itemId=3032, price=10, goldPrice=1, color1=42,  color2=42,  itemType="AnkleItem"), # Blueberry Blue Rainbow Ankle Bands
                ShopItem(itemId=3031, price=10, goldPrice=1, color1=126, color2=227, itemType="AnkleItem"), # Raindrop Blue Raindrop Anklet with Moonlight Gray Trim
                ShopItem(itemId=3023, price=10, goldPrice=1, color1=180, color2=180, itemType="AnkleItem"), # Seashell Blue Clam Ribbon Anklet
                ShopItem(itemId=3022, price=10, goldPrice=1, color1=152, color2=152, itemType="AnkleItem"), # Pale Purple Shell Anklet
                ShopItem(itemId=3049, price=10, goldPrice=1, color1=221, color2=221, itemType="AnkleItem"), # Jade Green Fine Feathered Anklet
                ShopItem(itemId=3034, price=10, goldPrice=1, color1=13,  color2=13,  itemType="AnkleItem"), # Coral Pink Freesia Ankle Flounce
                ShopItem(itemId=3021, price=10, goldPrice=1, color1=200, color2=200, itemType="AnkleItem"), # Ruby Pink Dear Droplets Anklet
                ShopItem(itemId=3052, price=10, goldPrice=1, color1=162, color2=162, itemType="AnkleItem"), # Sunglow Yellow Twirly Jeweled Anklet
                ShopItem(itemId=3036, price=10, goldPrice=1, color1=30,  color2=30,  itemType="AnkleItem"), # Pumpkin Orange Bottle Cap Anklet
                ShopItem(itemId=3020, price=10, goldPrice=1, color1=126, color2=126, itemType="AnkleItem"), # Raindrop Blue Teardrop Anklet
                ShopItem(itemId=3015, price=10, goldPrice=1, color1=69,  color2=69,  itemType="AnkleItem"), # Powder Blue Bubble Anklet
                ShopItem(itemId=3008, price=10, goldPrice=1, color1=35,  color2=35,  itemType="AnkleItem"), # Celery Green Grass Wrap Anklet
                ShopItem(itemId=3045, price=10, goldPrice=1, color1=162, color2=162, itemType="AnkleItem"), # Sunglow Yellow Harvest Moon Anklet
                ShopItem(itemId=3043, price=10, goldPrice=1, color1=35,  color2=35,  itemType="AnkleItem"), # Celery Green Trinity Leaf Anklet
                ShopItem(itemId=3024, price=10, goldPrice=1, color1=227, color2=227, itemType="AnkleItem"), # Moonlight Gray Tinkered Anklet
                ShopItem(itemId=3006, price=10, goldPrice=1, color1=267, color2=267, itemType="AnkleItem"), # Celestial Blue Tropic Flower Anklet
                ShopItem(itemId=3003, price=10, goldPrice=1, color1=152, color2=152, itemType="AnkleItem"), # Pale Purple Triple Blossom Anklet

            ]
        ),
    ]
)