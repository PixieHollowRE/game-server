from game.fairies.ai.FairiesConstants import COLOR_IDS as c_id

AURA_MAPPING = {
    22526: 1,  # Bubble
    22528: 2,  # Dizzy
    22529: 3,  # Bright Idea
    22527: 4,  # Rainbow Glow
    22530: 5,  # Tornado
    22539: 6,  # Puffy Cloud
    22536: 7,  # Fairy Cupcake
    22537: 8,  # Fireworks
    22540: 9,  # Ice Cube
    22541: 10, # Snowman
    22546: 11, # Raining Cloud
    22547: 12, # Snowing Cloud
    22543: 13, # Bubble Trail
    22544: 14, # Flower Trail
    22545: 15, # Snowflake Trail
    22538: 16, # Snowglobe
    # 17 is Cupcake Use Aura #
    22549: 18, # Growing
    22548: 19, # Shrinking
    22550: 20, # Flip-Flop
    22555: 21, # Blackberry
    22556: 22, # Deluxe Cupcake
    22557: 23, # Ice Cream
    22563: 24, # Fish Bubble
    22562: 25, # Rainbow Trail
    22561: 26, # Heart Trail
    22558: 27, # Candy Heart "Pixie Pals"
    22559: 28, # Candy Heart "Fly With U"
    22560: 29, # Candy Heart "Sweet Heart"
    # 30 is Unused Disco Ball Aura # 
    22564: 31, # Camp Fireworks
    22567: 32, # Troop Otter
    22566: 33, # Troop Butterfly
    22569: 34, # Troop Glowworm
    22565: 35, # Troop Rabbit
    22568: 36, # Troop Turtle
    22570: 37, # Candy Corn
    22571: 38, # Sparkle Wings
    22582: 39, # Baby Bunny
    22583: 40, # Baby Chipmunk
    22584: 41, # Baby Owl
    22585: 42, # Baby Kitten
    22585: 43, # Bunny Bubble
}

SKIN_COLOR_MAPPING = {
    # Skin
    22514: c_id["Cupcake Pink"],
    22515: c_id["Snow White"],
    22516: c_id["Silvermist Blue"],
    22517: c_id["Squirrel Gray"],
    22518: c_id["Tinker Bell Green"],
    22519: c_id["Mulberry Purple"],
    22520: c_id["Strawberry Red"],
    22521: c_id["Pumpkin Orange"],
    22522: c_id["Marigold Yellow"],
    22523: [c_id["Snow White"], c_id["Silvermist Blue"], c_id["Squirrel Gray"], c_id["Mulberry Purple"]],
    22524: [c_id["Cupcake Pink"], c_id["Tinker Bell Green"], c_id["Strawberry Red"], c_id["Marigold Yellow"]],
    22581: c_id["Electric Green"],
}

WING_COLOR_MAPPING = {
    # Wings
    22572: c_id["Pepper Black"],
    22573: c_id["Blue Jay Blue"],
    22574: c_id["Electric Blue"],
    22575: c_id["Friendship Pink"],
    22576: c_id["Electric Pink"],
    22577: c_id["Electric Orange"],
    22578: c_id["Electric Purple"],
    22579: c_id["Lemon Yellow"],
    22580: c_id["Rosetta Red"],
}