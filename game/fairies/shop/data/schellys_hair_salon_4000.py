from game.fairies.ai import ZoneConstants
from game.fairies.ai.FairiesConstants import DYE_ITEM_ID_OFFSET, INGREDIENTS
from game.fairies.fairy import FamousFairyData
from game.fairies.fairy.structs.PurchaseType import PurchaseType
from game.fairies.fairy.structs.ShopCollection import ShopCollection
from game.fairies.fairy.structs.ShopItem import ShopItem
from game.fairies.fairy.structs.ShopOutfit import ShopOutfit
from game.fairies.fairy.structs.OutfitItem import OutfitItem
from game.fairies.shop.ShopHelpers import NPCShop, Shopkeeper

SHOP = NPCShop(
    zone=ZoneConstants.SCHELLYS_HAIR_SALON,
    shopId=4000,
    shopkeeper=Shopkeeper(
        name=FamousFairyData.SCHELLY,
        position=(290, 470),
        famousFairyId=FamousFairyData.FAMOUS_FAIRY_SCHELLY
    ),
    collections=[
        ShopCollection(
            collectionId=4001, # Classic Hair Fronts (Fairies)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_front", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5001, price=10, goldPrice=2), # Simple Style
                ShopItem(itemId=5002, price=10, goldPrice=2), # Parted Bangs
                ShopItem(itemId=5003, price=10, goldPrice=2), # Center Swoops
                ShopItem(itemId=5004, price=10, goldPrice=2), # Sweepy Side Part
                ShopItem(itemId=5005, price=10, goldPrice=2), # Wind-Swept Bangs
                ShopItem(itemId=5006, price=10, goldPrice=2), # Sleek and Styled
                ShopItem(itemId=5007, price=10, goldPrice=2), # Parted Pomp
                ShopItem(itemId=5008, price=10, goldPrice=2), # Blunt Cut
                ShopItem(itemId=5009, price=10, goldPrice=2), # Swoopy Side Part
                ShopItem(itemId=5010, price=10, goldPrice=2), # Angled Bangs
                ShopItem(itemId=5011, price=10, goldPrice=2), # Pulled Back -- Wavy
                ShopItem(itemId=5012, price=10, goldPrice=2), # Pulled Back -- Glamorous
                ShopItem(itemId=5013, price=10, goldPrice=2), # Pulled Back
                ShopItem(itemId=5014, price=10, goldPrice=2), # Pulled Back -- Wispy
                ShopItem(itemId=5015, price=10, goldPrice=2), # Sweeping Bangs
                ShopItem(itemId=5016, price=10, goldPrice=2), # Shy Style
                ShopItem(itemId=5017, price=10, goldPrice=2), # Tousled Layers
                ShopItem(itemId=5018, price=10, goldPrice=2), # Tousled Top
                ShopItem(itemId=5019, price=10, goldPrice=2), # Long Strand Front
            ],
        ),
        ShopCollection(
            collectionId=4003, # Classic Hair Backs (Fairies)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_back", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5521, price=10, goldPrice=2), # No Back
                ShopItem(itemId=5501, price=10, goldPrice=2), # Classic Back
                ShopItem(itemId=5502, price=10, goldPrice=2), # Pixie Braids
                ShopItem(itemId=5503, price=10, goldPrice=2), # Short Tresses
                ShopItem(itemId=5504, price=10, goldPrice=2), # Fluffy Short
                ShopItem(itemId=5505, price=10, goldPrice=2), # Styled Short
                ShopItem(itemId=5506, price=10, goldPrice=2), # Super Long Braid
                ShopItem(itemId=5507, price=10, goldPrice=2), # Berry Bouffant
                ShopItem(itemId=5508, price=10, goldPrice=2), # Pixie Pom Pom
                ShopItem(itemId=5509, price=10, goldPrice=2), # Big Hair
                ShopItem(itemId=5510, price=10, goldPrice=2), # Long Tresses
                ShopItem(itemId=5511, price=10, goldPrice=2), # Styled Long Strands
                ShopItem(itemId=5512, price=10, goldPrice=2), # Fairy Braids
                ShopItem(itemId=5513, price=10, goldPrice=2), # Long Tapered Tresses
                ShopItem(itemId=5514, price=10, goldPrice=2), # Long Braids
                ShopItem(itemId=5515, price=10, goldPrice=2), # Long and Straight
                ShopItem(itemId=5516, price=10, goldPrice=2), # Short and Teased
                ShopItem(itemId=5517, price=10, goldPrice=2), # Long Flowing Locks
                ShopItem(itemId=5518, price=10, goldPrice=2), # Pixie Pin Curls
                ShopItem(itemId=5519, price=10, goldPrice=2), # Wind-Swept Bun
                ShopItem(itemId=5520, price=10, goldPrice=2), # Thick Ponytails
                ShopItem(itemId=5522, price=10, goldPrice=2), # Puff Ball Back
            ],
        ),
        ShopCollection(
            collectionId=4004, # Stylish Hair Fronts (Fairies)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_front", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5106, price=10, goldPrice=2),
                ShopItem(itemId=5118, price=10, goldPrice=2), # Plaited Side Part Front
                ShopItem(itemId=5119, price=10, goldPrice=2), # Sideswept Barrette Front
                ShopItem(itemId=5121, price=10, goldPrice=2), # Curly Pompadour Front
                ShopItem(itemId=5122, price=10, goldPrice=2), # Short Waves Front
                ShopItem(itemId=5123, price=10, goldPrice=2), # Fashion Bob Front
                ShopItem(itemId=5120, price=10, goldPrice=2), # Beautiful Bangs
                ShopItem(itemId=5124, price=10, goldPrice=2), # Periwinkle's Hair Front
                ShopItem(itemId=5125, price=10, goldPrice=2), # Spike's Hair Front
                ShopItem(itemId=5126, price=10, goldPrice=2), # Long and Curly Front
                ShopItem(itemId=5027, price=10, goldPrice=2), # Pixie Bangs
                ShopItem(itemId=5113, price=10, goldPrice=2), # Original Pixie Bangs
                ShopItem(itemId=5028, price=10, goldPrice=2), # Pixie Pigtails
                ShopItem(itemId=5115, price=10, goldPrice=2), # Original Pixie Pigtails
                ShopItem(itemId=5029, price=10, goldPrice=2), # Star Strands Front
                ShopItem(itemId=5114, price=10, goldPrice=2), # Original Star Strands Front
                ShopItem(itemId=5030, price=10, goldPrice=2), # Side Swept Bangs
                ShopItem(itemId=5116, price=10, goldPrice=2), # Original Side Swept Bangs
                ShopItem(itemId=5032, price=10, goldPrice=2), # Fairy Mary Hair
                ShopItem(itemId=5075, price=10, goldPrice=2), # Cool Waves
                ShopItem(itemId=5077, price=10, goldPrice=2), # Classic Pulled Back
                ShopItem(itemId=5094, price=10, goldPrice=2), # Flowy Pigtails
                ShopItem(itemId=5081, price=10, goldPrice=2), # Sweet and Stylish Bun
                ShopItem(itemId=5080, price=10, goldPrice=2), # Puffy Bangs
                ShopItem(itemId=5093, price=10, goldPrice=2), # Long and Flowing Tieback
                ShopItem(itemId=5084, price=10, goldPrice=2), # Sleek Part
                ShopItem(itemId=5107, price=10, goldPrice=2), # Royal Heart Braids
                ShopItem(itemId=5102, price=10, goldPrice=2), # Lovely Layers
                ShopItem(itemId=5076, price=10, goldPrice=2), # Fairy Fishtails
                ShopItem(itemId=5108, price=10, goldPrice=2), # Will 'O Whisp Bangs
                ShopItem(itemId=5101, price=10, goldPrice=2), # Long Swept Bangs
                ShopItem(itemId=5089, price=10, goldPrice=2), # Braided Tieback
                ShopItem(itemId=5109, price=10, goldPrice=2), # Short Twists
                ShopItem(itemId=5092, price=10, goldPrice=2), # Long and Flitterific Locks
                ShopItem(itemId=5082, price=10, goldPrice=2), # Stylish Ringlets
                ShopItem(itemId=5033, price=10, goldPrice=2), # Side-Part Swirly Bob
                ShopItem(itemId=5034, price=10, goldPrice=2), # Front Swept Bangs
                ShopItem(itemId=5035, price=10, goldPrice=2), # Totally Tousled Bangs
                ShopItem(itemId=5036, price=10, goldPrice=2), # Soft Tousled Bangs
                ShopItem(itemId=5037, price=10, goldPrice=2), # Tight Wave Crop
                ShopItem(itemId=5062, price=10, goldPrice=2), # Perfect Bob
                ShopItem(itemId=5064, price=10, goldPrice=2), # Swift and Swooshy Locks
                ShopItem(itemId=5063, price=10, goldPrice=2), # Long Angled Bangs
                ShopItem(itemId=5066, price=10, goldPrice=2), # Braid Over Bangs
                ShopItem(itemId=5078, price=10, goldPrice=2), # Mouse-Ear Buns
                ShopItem(itemId=5099, price=10, goldPrice=2), # Pulled Back Twists
                ShopItem(itemId=5090, price=10, goldPrice=2), # Inverted Bob
                ShopItem(itemId=5087, price=10, goldPrice=2), # Rock and Roll Bangs
                ShopItem(itemId=5086, price=10, goldPrice=2), # Double Roll Bangs
                ShopItem(itemId=5100, price=10, goldPrice=2), # Triple Braid Bob
                ShopItem(itemId=5079, price=10, goldPrice=2), # Topsy-Turvy Short
                ShopItem(itemId=5105, price=10, goldPrice=2), # Twisty Locks
                ShopItem(itemId=5088, price=10, goldPrice=2), # Bowtie Bob
                ShopItem(itemId=5097, price=10, goldPrice=2), # Long and Curly Twisties

                ShopItem(itemId=5096, price=10, goldPrice=2), # Short and Curly Twisties
                ShopItem(itemId=5104, price=10, goldPrice=2), # Long Braided Front
                ShopItem(itemId=5129, price=10, goldPrice=2), # Fishtail Braid Front
                ShopItem(itemId=5130, price=10, goldPrice=2), # Poufy Pigtails
                ShopItem(itemId=5131, price=10, goldPrice=2), # Swooped Bangs Front
                ShopItem(itemId=5132, price=10, goldPrice=2), # Curly Ringlets Front
                ShopItem(itemId=5133, price=10, goldPrice=2), # Flowery Waves Hair Front
                
            ],
        ),
                ShopCollection(
            collectionId=4010, # Classic Hair Fronts (Sparrowmen)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_front", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5044, price=10, goldPrice=2), # Side Swept Layers
                ShopItem(itemId=5045, price=10, goldPrice=2), # Tousled Locks
                ShopItem(itemId=5046, price=10, goldPrice=2), # Sparrow Man Spike
                ShopItem(itemId=5047, price=10, goldPrice=2), # Casual Layers
                ShopItem(itemId=5048, price=10, goldPrice=2), # Long Bang Sweep
                ShopItem(itemId=5049, price=10, goldPrice=2), # Curl Cut
                ShopItem(itemId=5050, price=10, goldPrice=2), # Square Tapered Sides
                ShopItem(itemId=5051, price=10, goldPrice=2), # Layered Side Swipe
                ShopItem(itemId=5052, price=10, goldPrice=2), # Stylish Center Part
                ShopItem(itemId=5053, price=10, goldPrice=2), # Long Tapered Sides	
                ShopItem(itemId=5054, price=10, goldPrice=2), # Short Knots
                
            ],
        ),
                
            ShopCollection(
            collectionId=4011, # Classic Hair Backs (Sparrowmen)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_back", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5560, price=10, goldPrice=2), # No Back
                ShopItem(itemId=5547, price=10, goldPrice=2), # Clean-Cut Back
                ShopItem(itemId=5548, price=10, goldPrice=2), # Square Trim Crop
                ShopItem(itemId=5549, price=10, goldPrice=2), # Mid-Length Layers
                ShopItem(itemId=5550, price=10, goldPrice=2), # Close Cropped Cap
                ShopItem(itemId=5551, price=10, goldPrice=2), # Long-Stranded Back
                ShopItem(itemId=5552, price=10, goldPrice=2), # Short Wave Trim
                ShopItem(itemId=5553, price=10, goldPrice=2), # Wide Bob Back
                ShopItem(itemId=5554, price=10, goldPrice=2), # Triple-V Back
                ShopItem(itemId=5555, price=10, goldPrice=2), # Short Angled Back
                ShopItem(itemId=5556, price=10, goldPrice=2), # Narrow Bob Back
                ShopItem(itemId=5557, price=10, goldPrice=2), # Finger Fringe Trim

            ],
        ),


        ShopCollection(
            collectionId=4012, # Stylish Hair Fronts (Sparrowmen)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_front", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5061, price=10, goldPrice=2), # Fly Backwards
                ShopItem(itemId=5060, price=10, goldPrice=2), # Hurricane Crop
                ShopItem(itemId=5083, price=10, goldPrice=2), # Buzzed Do
                ShopItem(itemId=5085, price=10, goldPrice=2), # Light Spikes
                ShopItem(itemId=5095, price=10, goldPrice=2), # Shaggy Locks
                ShopItem(itemId=5103, price=10, goldPrice=2), # Carefree Layers
                ShopItem(itemId=5110, price=10, goldPrice=2), # Adventurer Pony
                ShopItem(itemId=5098, price=10, goldPrice=2), # Short Twists
            ],
        ),
        ShopCollection(
            collectionId=4013, # Stylish Hair Backs (Sparrowmen)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_back", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5562, price=10, goldPrice=2), # Fly Backwards Back
                ShopItem(itemId=5577, price=10, goldPrice=2), # Light Spikes Back 
                ShopItem(itemId=5585, price=10, goldPrice=2), # Shaggy Locks Back
                ShopItem(itemId=5592, price=10, goldPrice=2), # Carefree Layers Back
                ShopItem(itemId=5595, price=10, goldPrice=2), # Adventurer Straight Back
                ShopItem(itemId=5588, price=10, goldPrice=2), # Short Twists Back

            ],
        ),


        ShopCollection(
            collectionId=4005, # Stylish Hair Backs (Fairies)
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_back", 0),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=5521, price=10, goldPrice=2), # No Back
                ShopItem(itemId=5602, price=10, goldPrice=2), # Sideswept Barrette Back
                ShopItem(itemId=5603, price=10, goldPrice=2), # Plaited Side Part Back
                ShopItem(itemId=5605, price=10, goldPrice=2), # Curly Pompadour Back
                ShopItem(itemId=5606, price=10, goldPrice=2), # Pom Pom Pigtails
                ShopItem(itemId=5604, price=10, goldPrice=2), # Beautiful Bangs Back
                ShopItem(itemId=5607, price=10, goldPrice=2), # Periwinkle's Hair Back
                ShopItem(itemId=5601, price=10, goldPrice=2), # Spike's Hair Back
                ShopItem(itemId=5608, price=10, goldPrice=2), # Long and Curly Back
                ShopItem(itemId=5532, price=10, goldPrice=2), # Sweet Bun
                ShopItem(itemId=5533, price=10, goldPrice=2), # Girly Curlies
                ShopItem(itemId=5534, price=10, goldPrice=2), # Pixie Ponytails Back
                ShopItem(itemId=5535, price=10, goldPrice=2), # Star Strands Back
                ShopItem(itemId=5599, price=10, goldPrice=2), # Original Star Strands Back
                ShopItem(itemId=5536, price=10, goldPrice=2), # Pixie Bob Back
                ShopItem(itemId=5537, price=10, goldPrice=2), # Long Pony
                ShopItem(itemId=5598, price=10, goldPrice=2), # Original Long Pony
                ShopItem(itemId=5569, price=10, goldPrice=2), # Cool Waves Back
                ShopItem(itemId=5570, price=10, goldPrice=2), # Braided-Bun
                ShopItem(itemId=5574, price=10, goldPrice=2), # Swept Up Hair Back
                ShopItem(itemId=5573, price=10, goldPrice=2), # Puffy Pigtails
                ShopItem(itemId=5576, price=10, goldPrice=2), # Twin Buns (Highlights)
                ShopItem(itemId=5596, price=10, goldPrice=2), # Twin Buns (No Highlights)
                ShopItem(itemId=5591, price=10, goldPrice=2), # Lovely Layers Back
                ShopItem(itemId=5593, price=10, goldPrice=2), # Whale of a Fishtail
                ShopItem(itemId=5582, price=10, goldPrice=2), # High Flowing Ponytail
                ShopItem(itemId=5584, price=10, goldPrice=2), # Long and Flowing Hair
                ShopItem(itemId=5590, price=10, goldPrice=2), # Swept Up
                ShopItem(itemId=5581, price=10, goldPrice=2), # Bunny Tail Bun
                ShopItem(itemId=5572, price=10, goldPrice=2), # Long Braided Back
                ShopItem(itemId=5594, price=10, goldPrice=2), # Short Twists Back
                ShopItem(itemId=5583, price=10, goldPrice=2), # Long and Flitterific Locks Back
                ShopItem(itemId=5575, price=10, goldPrice=2), # Stylish Ringlets Back
                ShopItem(itemId=5538, price=10, goldPrice=2), # Swirly Glamour Mane
                ShopItem(itemId=5539, price=10, goldPrice=2), # Swept-Up Bun
                ShopItem(itemId=5540, price=10, goldPrice=2), # Totally Rounded Bob
                ShopItem(itemId=5541, price=10, goldPrice=2), # Soft Layered Locks
                ShopItem(itemId=5563, price=10, goldPrice=2), # Perfect Bob Back
                ShopItem(itemId=5565, price=10, goldPrice=2), # Swift and Swooshy Back
                ShopItem(itemId=5564, price=10, goldPrice=2), # Angled Bang Back
                ShopItem(itemId=5566, price=10, goldPrice=2), # Braid and Bun
                ShopItem(itemId=5571, price=10, goldPrice=2), # Draping Locks
                ShopItem(itemId=5580, price=10, goldPrice=2), # Super Long Ponytail
                ShopItem(itemId=5589, price=10, goldPrice=2), # Pulled Back Twists Back
                ShopItem(itemId=5579, price=10, goldPrice=2), # Wavy Silky Tresses
                ShopItem(itemId=5578, price=10, goldPrice=2), # Rolled and Wavy Back
                ShopItem(itemId=5587, price=10, goldPrice=2), # Long and Curly Twisties Back

                ShopItem(itemId=5586, price=10, goldPrice=2), # Short and Curly Twisties Back
                
                ShopItem(itemId=5611, price=10, goldPrice=2), # Simple Ponytail
                ShopItem(itemId=5612, price=10, goldPrice=2), # Curly Ringlets Back
                ShopItem(itemId=5613, price=10, goldPrice=2), # Flowery Braid
            ],
        ),
        ShopCollection(
            collectionId=4014, # Hair Colors
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_color", -DYE_ITEM_ID_OFFSET),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=14055, price=10, goldPrice=1), # Pepper Black
                ShopItem(itemId=14073, price=10, goldPrice=1), # Grape Purple
                ShopItem(itemId=14141, price=10, goldPrice=1), # Thundercloud Gray
                ShopItem(itemId=14075, price=10, goldPrice=1), # Umber Brown
                ShopItem(itemId=14074, price=10, goldPrice=1), # Soil Brown
                ShopItem(itemId=14191, price=10, goldPrice=1), # Vidia Black
                ShopItem(itemId=14177, price=10, goldPrice=1), # Mud Brown
                ShopItem(itemId=14076, price=10, goldPrice=1), # Chocolate Brown
                ShopItem(itemId=14077, price=10, goldPrice=1), # Sepia Brown
                ShopItem(itemId=14078, price=10, goldPrice=1), # Fawn Brown
                ShopItem(itemId=14079, price=10, goldPrice=1), # Sienna Brown
                ShopItem(itemId=14092, price=10, goldPrice=1), # Hawk Brown
                ShopItem(itemId=14057, price=10, goldPrice=1), # Adobe Brown
                ShopItem(itemId=14117, price=10, goldPrice=1), # Amethyst Purple
                ShopItem(itemId=14043, price=10, goldPrice=1), # Violet Purple
                ShopItem(itemId=14183, price=10, goldPrice=1), # Vidia Purple
                ShopItem(itemId=14197, price=10, goldPrice=1), # Electric Purple
                ShopItem(itemId=14080, price=10, goldPrice=1), # Pomegranate Purple
                ShopItem(itemId=14081, price=10, goldPrice=1), # Crimson Red
                ShopItem(itemId=14189, price=10, goldPrice=1), # Ladybug Red
                ShopItem(itemId=14174, price=10, goldPrice=1), # Rosetta Red
                ShopItem(itemId=14045, price=10, goldPrice=1), # Strawberry Red
                ShopItem(itemId=14082, price=10, goldPrice=1), # Raspberry Red
                ShopItem(itemId=14113, price=10, goldPrice=1), # Pale Rose Red
                ShopItem(itemId=14083, price=10, goldPrice=1), # Cherry Brown
                ShopItem(itemId=14114, price=10, goldPrice=1), # Foxtail Orange
                ShopItem(itemId=14013, price=10, goldPrice=1), # Coral Pink
                ShopItem(itemId=14181, price=10, goldPrice=1), # Cupcake Pink
                ShopItem(itemId=14008, price=10, goldPrice=1), # Watermelon Pink
                ShopItem(itemId=14121, price=10, goldPrice=1), # Daisy Pink
                ShopItem(itemId=14084, price=10, goldPrice=1), # Copper Brown
                ShopItem(itemId=14046, price=10, goldPrice=1), # Bark Brown
                ShopItem(itemId=14095, price=10, goldPrice=1), # Sparrow Brown
                ShopItem(itemId=14028, price=10, goldPrice=1), # Cinnamon Brown
                ShopItem(itemId=14086, price=10, goldPrice=1), # Nutmeg Brown
                ShopItem(itemId=14085, price=10, goldPrice=1), # Quail Brown
                ShopItem(itemId=14087, price=10, goldPrice=1), # Driftwood Brown
                ShopItem(itemId=14187, price=10, goldPrice=1), # Maple Orange
                ShopItem(itemId=14171, price=10, goldPrice=1), # Sunrise Yellow
                ShopItem(itemId=14067, price=10, goldPrice=1), # Chartreuse Green
                ShopItem(itemId=14048, price=10, goldPrice=1), # Sea Green
                ShopItem(itemId=14193, price=10, goldPrice=1), # Electric Green
                ShopItem(itemId=14145, price=10, goldPrice=1), # Tinker Bell Green
                ShopItem(itemId=14125, price=10, goldPrice=1), # Pine Green
                ShopItem(itemId=14182, price=10, goldPrice=1), # Twilight Blue
                ShopItem(itemId=14136, price=10, goldPrice=1), # Peacock Blue
                ShopItem(itemId=14176, price=10, goldPrice=1), # Silvermist Blue
                ShopItem(itemId=14180, price=10, goldPrice=1), # Seashell Blue
                ShopItem(itemId=14195, price=10, goldPrice=1), # Electric Blue
                ShopItem(itemId=14006, price=10, goldPrice=1), # Havendish Blue
                ShopItem(itemId=14163, price=10, goldPrice=1), # Tundra Blue
                ShopItem(itemId=14089, price=10, goldPrice=1), # Seashore Brown
                ShopItem(itemId=14161, price=10, goldPrice=1), # Buried Treasure Brown
                ShopItem(itemId=14088, price=10, goldPrice=1), # Fruitwood Brown
                ShopItem(itemId=14196, price=10, goldPrice=1), # Electric Orange
                ShopItem(itemId=14178, price=10, goldPrice=1), # Fawn Orange
                ShopItem(itemId=14179, price=10, goldPrice=1), # Iridessa Yellow
                ShopItem(itemId=14186, price=10, goldPrice=1), # Honeycomb Yellow
                ShopItem(itemId=14027, price=10, goldPrice=1), # Corn Cob Yellow
                ShopItem(itemId=14162, price=10, goldPrice=1), # Sunglow Yellow
                ShopItem(itemId=14090, price=10, goldPrice=1), # Custard Yellow
                ShopItem(itemId=14116, price=10, goldPrice=1), # Mushroom White
                ShopItem(itemId=14109, price=10, goldPrice=1), # Soft Orange
                ShopItem(itemId=14111, price=10, goldPrice=1), # Sparkling Yellow
                ShopItem(itemId=14166, price=10, goldPrice=1), # Snow White
            ]
        ),
        ShopCollection(
            collectionId=4015, # Highlights 
            purchaseType=PurchaseType.DNA,
            dnaFields=(("hair_color2", -DYE_ITEM_ID_OFFSET),),
            currencyId=INGREDIENTS["DAISY_PETALS"].id,
            items=[
                ShopItem(itemId=14055, price=10, goldPrice=1, specialType=2), # Pepper Black
                ShopItem(itemId=14073, price=10, goldPrice=1, specialType=2), # Grape Purple
                ShopItem(itemId=14141, price=10, goldPrice=1, specialType=2), # Thundercloud Gray
                ShopItem(itemId=14075, price=10, goldPrice=1, specialType=2), # Umber Brown
                ShopItem(itemId=14074, price=10, goldPrice=1, specialType=2), # Soil Brown
                ShopItem(itemId=14191, price=10, goldPrice=1, specialType=2), # Vidia Black
                ShopItem(itemId=14177, price=10, goldPrice=1, specialType=2), # Mud Brown
                ShopItem(itemId=14076, price=10, goldPrice=1, specialType=2), # Chocolate Brown
                ShopItem(itemId=14077, price=10, goldPrice=1, specialType=2), # Sepia Brown
                ShopItem(itemId=14078, price=10, goldPrice=1, specialType=2), # Fawn Brown
                ShopItem(itemId=14079, price=10, goldPrice=1, specialType=2), # Sienna Brown
                ShopItem(itemId=14092, price=10, goldPrice=1, specialType=2), # Hawk Brown
                ShopItem(itemId=14057, price=10, goldPrice=1, specialType=2), # Adobe Brown
                ShopItem(itemId=14117, price=10, goldPrice=1, specialType=2), # Amethyst Purple
                ShopItem(itemId=14043, price=10, goldPrice=1, specialType=2), # Violet Purple
                ShopItem(itemId=14183, price=10, goldPrice=1, specialType=2), # Vidia Purple
                ShopItem(itemId=14197, price=10, goldPrice=1, specialType=2), # Electric Purple
                ShopItem(itemId=14080, price=10, goldPrice=1, specialType=2), # Pomegranate Purple
                ShopItem(itemId=14081, price=10, goldPrice=1, specialType=2), # Crimson Red
                ShopItem(itemId=14189, price=10, goldPrice=1, specialType=2), # Ladybug Red
                ShopItem(itemId=14174, price=10, goldPrice=1, specialType=2), # Rosetta Red
                ShopItem(itemId=14045, price=10, goldPrice=1, specialType=2), # Strawberry Red
                ShopItem(itemId=14082, price=10, goldPrice=1, specialType=2), # Raspberry Red
                ShopItem(itemId=14113, price=10, goldPrice=1, specialType=2), # Pale Rose Red
                ShopItem(itemId=14083, price=10, goldPrice=1, specialType=2), # Cherry Brown
                ShopItem(itemId=14114, price=10, goldPrice=1, specialType=2), # Foxtail Orange
                ShopItem(itemId=14013, price=10, goldPrice=1, specialType=2), # Coral Pink
                ShopItem(itemId=14181, price=10, goldPrice=1, specialType=2), # Cupcake Pink
                ShopItem(itemId=14008, price=10, goldPrice=1, specialType=2), # Watermelon Pink
                ShopItem(itemId=14121, price=10, goldPrice=1, specialType=2), # Daisy Pink
                ShopItem(itemId=14084, price=10, goldPrice=1, specialType=2), # Copper Brown
                ShopItem(itemId=14046, price=10, goldPrice=1, specialType=2), # Bark Brown
                ShopItem(itemId=14095, price=10, goldPrice=1, specialType=2), # Sparrow Brown
                ShopItem(itemId=14028, price=10, goldPrice=1, specialType=2), # Cinnamon Brown
                ShopItem(itemId=14086, price=10, goldPrice=1, specialType=2), # Nutmeg Brown
                ShopItem(itemId=14085, price=10, goldPrice=1, specialType=2), # Quail Brown
                ShopItem(itemId=14087, price=10, goldPrice=1, specialType=2), # Driftwood Brown
                ShopItem(itemId=14187, price=10, goldPrice=1, specialType=2), # Maple Orange
                ShopItem(itemId=14171, price=10, goldPrice=1, specialType=2), # Sunrise Yellow
                ShopItem(itemId=14067, price=10, goldPrice=1, specialType=2), # Chartreuse Green
                ShopItem(itemId=14048, price=10, goldPrice=1, specialType=2), # Sea Green
                ShopItem(itemId=14193, price=10, goldPrice=1, specialType=2), # Electric Green
                ShopItem(itemId=14145, price=10, goldPrice=1, specialType=2), # Tinker Bell Green
                ShopItem(itemId=14125, price=10, goldPrice=1, specialType=2), # Pine Green
                ShopItem(itemId=14182, price=10, goldPrice=1, specialType=2), # Twilight Blue
                ShopItem(itemId=14136, price=10, goldPrice=1, specialType=2), # Peacock Blue
                ShopItem(itemId=14176, price=10, goldPrice=1, specialType=2), # Silvermist Blue
                ShopItem(itemId=14180, price=10, goldPrice=1, specialType=2), # Seashell Blue
                ShopItem(itemId=14195, price=10, goldPrice=1, specialType=2), # Electric Blue
                ShopItem(itemId=14006, price=10, goldPrice=1, specialType=2), # Havendish Blue
                ShopItem(itemId=14163, price=10, goldPrice=1, specialType=2), # Tundra Blue
                ShopItem(itemId=14089, price=10, goldPrice=1, specialType=2), # Seashore Brown
                ShopItem(itemId=14161, price=10, goldPrice=1, specialType=2), # Buried Treasure Brown
                ShopItem(itemId=14088, price=10, goldPrice=1, specialType=2), # Fruitwood Brown
                ShopItem(itemId=14196, price=10, goldPrice=1, specialType=2), # Electric Orange
                ShopItem(itemId=14178, price=10, goldPrice=1, specialType=2), # Fawn Orange
                ShopItem(itemId=14179, price=10, goldPrice=1, specialType=2), # Iridessa Yellow
                ShopItem(itemId=14186, price=10, goldPrice=1, specialType=2), # Honeycomb Yellow
                ShopItem(itemId=14027, price=10, goldPrice=1, specialType=2), # Corn Cob Yellow
                ShopItem(itemId=14162, price=10, goldPrice=1, specialType=2), # Sunglow Yellow
                ShopItem(itemId=14090, price=10, goldPrice=1, specialType=2), # Custard Yellow
                ShopItem(itemId=14116, price=10, goldPrice=1, specialType=2), # Mushroom White
                ShopItem(itemId=14109, price=10, goldPrice=1, specialType=2), # Soft Orange
                ShopItem(itemId=14111, price=10, goldPrice=1, specialType=2), # Sparkling Yellow
                ShopItem(itemId=14166, price=10, goldPrice=1, specialType=2), # Snow White
            ]
        )
    ],
)