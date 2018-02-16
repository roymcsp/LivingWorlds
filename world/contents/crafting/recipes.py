from world.economy import PP, GP, SP, CP

RECIPES = {
    "battleaxe": {
        "key": "battle axe",
        "aliases": ["battleaxe", "axe"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "Sturdy and with significant heft, this axe has a menacingly "
                "large blade, and a hard swing of it can send enemies flying. ",
        "weight": 6.0,
        "value": 1000*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "club": {
        "key": "club",
        "aliases": ["club"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "Roughly whittled from some dense wood, this club features "
                "a large round head that tapers to a narrow handle. ",
        "weight": 3.0,
        "value": 200*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "dagger": {
        "key": "dagger",
        "aliases": ["dagger"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "This dagger consists of a double edged and razor sharp blade "
                "expertly mounted onto a simple leather-wrapped hilt.",
        "weight": 1.0,
        "value": 200 * CP,
        "damage_roll": "1d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "flail": {
        "key": "flail",
        "aliases": ["flail"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "the flail has a single spiked ball connected to a slender wooden "
                "leather wrapped handle with a foot of chain.",
        "weight": 5.0,
        "value": 800*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "handaxe": {
        "key": "hand axe",
        "aliases": ["hand axe", "axe"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "this small axe has a short wood handle and sharp single blade "
                "on one side of the head with a thick heavy sledge on the other. ",
        "weight": 2.0,
        "value": 600 * CP,
        "damage_roll": "1d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "heavymace": {
        "key": "heavy mace",
        "aliases": ["heavy mace", "mace"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 8.0,
        "value": 1200*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "heavypick": {
        "key": "heavy pick",
        "aliases": ["heavy pick", "pick"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 6.0,
        "value": 800*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "kama": {
        "key": "kama",
        "aliases": ["kama"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 200 * CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "katana": {
        "key": "katana",
        "aliases": ["katana"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 10.0,
        "value": 4000*CP,
        "damage_roll": "1d10",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "longsword": {
        "key": "long sword",
        "aliases": ["longsword", "sword"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "This sword consists of a double edged and razor sharp blade "
                "expertly mounted onto a simple leather-wrapped hilt.",
        "weight": 4.0,
        "value": 1500 * CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "lighthammer": {
        "key": "light hammer",
        "aliases": ["light hammer", "hammer"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 100*CP,
        "damage_roll": "1d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "lightmace": {
        "key": "light mace",
        "aliases": ["light mace", "mace"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 4.0,
        "value": 500*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "lightpick": {
        "key": "Light pick",
        "aliases": ["light pick", "pick"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 3.0,
        "value": 400*CP,
        "damage_roll": "1d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "morningstar": {
        "key": "morningstar",
        "aliases": ["morningstar"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 6.0,
        "value": 200*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "nageyari": {
        "key": "nage yari",
        "aliases": ["yari"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 3.0,
        "value": 300*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "nunchaku": {
        "key": "nunchaku",
        "aliases": ["Nunchaku"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 200*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "rapier": {
        "key": "rapier",
        "aliases": ["rapier"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 2000*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "sai": {
        "key": "sai",
        "aliases": ["sai"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 1.0,
        "value": 100*CP,
        "damage_roll": "1d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "scimitar": {
        "key": "scimitar",
        "aliases": ["scimitar"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 4.0,
        "value": 1500*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "sickle": {
        "key": "sickle",
        "aliases": ["sickle"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 600*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "spear": {
        "key": "spear",
        "aliases": ["Spear"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 6.0,
        "value": 200*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "shortspear": {
        "key": "short spear",
        "aliases": ["short spear", "spear"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 3.0,
        "value": 100*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "shortsword": {
        "key": "short sword",
        "aliases": ["short sword", "sword"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 1000*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "tanto": {
        "key": "tanto",
        "aliases": ["tanto"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 1.0,
        "value": 300*CP,
        "damage_roll": "1d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "trident": {
        "key": "trident",
        "aliases": ["trident"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 4.0,
        "value": 1500*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "wakazashi": {
        "key": "wakazashi",
        "aliases": ["wakazashi"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 3.0,
        "value": 3000*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "warfan": {
        "key": "war fan",
        "aliases": ["War fan", "fan"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 3.0,
        "value": 3000*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "warhammer": {
        "key": "warhammer",
        "aliases": ["warhammer", "hammer"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 3.0,
        "value": 1200*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "whip": {
        "key": "whip",
        "aliases": ["whip"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 2.0,
        "value": 100*CP,
        "damage_roll": "1d3",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "yari": {
        "key": "yari",
        "aliases": ["yari"],
        "typeclass": "typeclasses.weapons.Weapon",
        "desc": "The blade of this axe appears well-used and slightly "
                "tarnished, but its handle is straight and sturdy.",
        "weight": 5.0,
        "value": 500*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    # Two-Handed Melee Weapons

    "bastardsword": {
        "key": "bastard Sword",
        "aliases": ["sword"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 6.0,
        "value": 3500*CP,
        "damage_roll": "1d10 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "dietsuchi": {
        "key": "die-tsuchi",
        "aliases": ["die-tsuchi"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 12.0,
        "value": 1200*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "falchion": {
        "key": "falchion",
        "aliases": ["falchion"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 8.0,
        "value": 7500*CP,
        "damage_roll": "2d4 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "heavyflail": {
        "key": "heavy flail",
        "aliases": ["flail"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 1500*CP,
        "damage_roll": "1d10 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "glaive": {
        "key": "glaive",
        "aliases": ["glaive"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 800*CP,
        "damage_roll": "1d10",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "greataxe": {
        "key": "great axe",
        "aliases": ["axe"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 12.0,
        "value": 2000*CP,
        "damage_roll": "1d12",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "greatclub": {
        "key": "great club",
        "aliases": ["club"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 8.0,
        "value": 500*CP,
        "damage_roll": "1d10 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "greatsword": {
        "key": "great sword",
        "aliases": ["sword"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 8.0,
        "value": 5000*CP,
        "damage_roll": "2d6 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "guisarme": {
        "key": "guisarme",
        "aliases": ["guisarme"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 12.0,
        "value": 900*CP,
        "damage_roll": "2d4 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "halberd": {
        "key": "halberd",
        "aliases": ["halberd"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 12.0,
        "value": 1000*CP,
        "damage_roll": "1d10",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "kawanaga": {
        "key": "kawanaga",
        "aliases": ["kawanaga"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 1.0,
        "value": 1000*CP,
        "damage_roll": "2d4 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "kusarigama": {
        "key": "kusari Gama",
        "aliases": ["kusari gama"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 3.0,
        "value": 1000*CP,
        "damage_roll": "2d4 ",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "lance": {
        "key": "lance",
        "aliases": ["lance"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 1000*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "longspear": {
        "key": "long spear",
        "aliases": ["long spear"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 9.0,
        "value": 500*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "lucernehammer": {
        "key": "lucerne hammer",
        "aliases": ["hammer"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 1200*CP,
        "damage_roll": "2d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "manrikigusari": {
        "key": "manriki gusari",
        "aliases": ["mariki gusari"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 5.0,
        "value": 500*CP,
        "damage_roll": "2d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "maul": {
        "key": "maul",
        "aliases": ["maul"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 20.0,
        "value": 1500*CP,
        "damage_roll": "1d10",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "nagimaki": {
        "key": "nagimaki",
        "aliases": ["nagimaki"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 8000*CP,
        "damage_roll": "2d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "naginata": {
        "key": "naginata",
        "aliases": ["naginata"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 15.0,
        "value": 1000*CP,
        "damage_roll": "1d10",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "nodachi": {
        "key": "no-dachi",
        "aliases": ["no dachi"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 12.0,
        "value": 5000*CP,
        "damage_roll": "2d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "ono": {
        "key": "ono",
        "aliases": ["ono"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 2000*CP,
        "damage_roll": "1d10",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "quarterstaff": {
        "key": "quarterstaff",
        "aliases": ["staff"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 4.0,
        "value": 100*CP,
        "damage_roll": "1d6",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "ransuer": {
        "key": "ransuer",
        "aliases": ["ransuer"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 12.0,
        "value": 1000*CP,
        "damage_roll": "2d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "scythe": {
        "key": "scythe",
        "aliases": ["scythe"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 10.0,
        "value": 1800*CP,
        "damage_roll": "2d4",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    "tetsubo": {
        "key": "tetsubo",
        "aliases": ["tetsubo"],
        "typeclass": "typeclasses.weapons.TwoHandedWeapon",
        "desc": " "
                " ",
        "weight": 15.0,
        "value": 2500*CP,
        "damage_roll": "1d8",
        "range": "melee",
        "hardness": 1,
        "durability": 1, },

    # Torso Armor
    "robe": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 2.0,
        "value": 0 * CP,
        "physical_bonus": 1,
        "magical_bonus": 1,
        "hardness": 1,
        "durability": 1},

    "paddedarmor": {
        "key": "padded armor",
        "aliases": ["padded armor"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 10.0,
        "value": 500*CP,
        "physical_bonus": 1,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "leatherarmor": {
        "key": "leather armor",
        "aliases": ["leather armor"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 15.0,
        "value": 1000 * CP,
        "physical_bonus": 2,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "studdedleather": {
        "key": "robe",
        "aliases": ["studded leather"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 20.0,
        "value": 2500 * CP,
        "physical_bonus": 3,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "chainshirt": {
        "key": "chain shirt",
        "aliases": ["chain shirt"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 25.0,
        "value": 10000 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "hidearmor": {
        "key": "hide armor",
        "aliases": ["hide armor"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 25.0,
        "value": 1500 * CP,
        "physical_bonus": 3,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "scalemail": {
        "key": "scale mail",
        "aliases": ["scalemail", "scale mail"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 30.0,
        "value": 5000 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "chainmail": {
        "key": "chainmail",
        "aliases": ["chainmail", "chain mail"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 40.0,
        "value": 15000 * CP,
        "physical_bonus": 5,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "breastplate": {
        "key": "breastplate",
        "aliases": ["breastplate"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 30.0,
        "value": 20000 * CP,
        "physical_bonus": 5,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},


    "splintmail": {
        "key": "splint mail",
        "aliases": ["splint mail", "splintmail"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 45.0,
        "value": 20000 * CP,
        "physical_bonus": 6,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "bandedmail": {
        "key": "banded mail",
        "aliases": ["banded mail", "bandedmail"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 25000 * CP,
        "physical_bonus": 6,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "halfplate": {
        "key": "half plate",
        "aliases": ["half plate"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 50.0,
        "value": 60000 * CP,
        "physical_bonus": 7,
        "magical_bonus": 1,
        "hardness": 1,
        "durability": 1},

    "fullplate": {
        "key": "platemail",
        "aliases": ["platemail", "plate mail"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 50.0,
        "value": 150000 * CP,
        "physical_bonus": 8,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "leatherscale": {
        "key": "leather scale",
        "aliases": ["leatherscale", "leather scale"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 20.0,
        "value": 3500 * CP,
        "physical_bonus": 3,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "brigandine": {
        "key": "brigandine",
        "aliases": ["brigandine"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 40.0,
        "value": 3000 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "lamellar": {
        "key": "lamellar",
        "aliases": ["lamellar"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 15000 * CP,
        "physical_bonus": 5,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "oyoroi": {
        "key": "o-yoroi",
        "aliases": ["oyoroi"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 45.0,
        "value": 100000*CP,
        "physical_bonus": 7,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    "ringmail": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Torso",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1},

    # helms
    "helm": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Helm",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1, },


    # Shields

    "shield": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Shield",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1, },


    # gloves

    "gloves": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Gloves",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1, },


    # boots

    "boots": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Boots",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1, },


    # bracers

    "bracers": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Bracers",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1, },


    # belts

    "belt": {
        "key": "robe",
        "aliases": ["robe"],
        "typeclass": "typeclasses.armors.Belts",
        "desc": "Made of soft cloth, this robe provides minimal protection.",
        "weight": 35.0,
        "value": 75 * CP,
        "physical_bonus": 4,
        "magical_bonus": 0,
        "hardness": 1,
        "durability": 1, },

}
