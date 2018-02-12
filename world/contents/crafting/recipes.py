from world.economy import PP, GP, SP, CP

RECIPES = {
    "dagger": {"aliases": ["dagger"],
            "typeclass": "typeclasses.weapons.Weapon",
            "desc": "This dagger consists of a double edged and razor sharp blade "
                    "expertly mounted onto a simple leather-wrapped hilt.",
            "weight": 1,
            "value": 200*CP,
            "damage_roll": "1d4",
            "range": "melee",
            "hardness": 1,
            "durability": 1,},

    "longsword":{"aliases": ["longsword", "sword"],
            "typeclass": "typeclasses.weapons.Weapon",
            "desc": "This sword consists of a double edged and razor sharp blade "
                    "expertly mounted onto a simple leather-wrapped hilt.",
            "weight": 4,
            "value": 1500*CP,
            "damage_roll": "1d8",
            "range": "melee",
            "hardness": 1,
            "durability": 1,},
     }
