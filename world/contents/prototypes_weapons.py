"""
Prototype module containing weapons and shields.
"""

from evennia.utils import fill
from world.economy import PP, GP, SP, CP

# Weapons from D&D

# One-handed Melee Weapons
HAND_AXE = {
    "key": "Hand Axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "this small axe has a short wood handle and sharp single blade "
            "on one side of the head with a thick heavy sledge on the other. ",
    "weight": 2,
    "value": 600*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

BATTLE_AXE = {
    "key": "Battle axe",
    "aliases": ["battleaxe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "Sturdy and with significant heft, this axe has a menacingly "
            "large blade, and a hard swing of it can send enemies flying. ",
    "weight": 6,
    "value": 1000*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

CLUB = {
    "key": "Club",
    "aliases": ["club"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "Roughly whittled from some dense wood, this club features "
            "a large round head that tapers to a narrow handle. ",
    "weight": 3,
    "value": 200*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

DAGGER = {
    "key": "Dagger",
    "aliases": ["dagger"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "This dagger consists of a double edged and razor sharp blade "
            "expertly mounted onto a simple leather-wrapped hilt.",
    "weight": 1,
    "value": 200*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

FLAIL = {
    "key": "Flail",
    "aliases": ["flail"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "the flail has a single spiked ball connected to a slender wooden "
            "leather wrapped handle with a foot of chain.",
    "weight": 5.0,
    "value": 800*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

HAMMER_LIGHT = {
    "key": "Light hammer",
    "aliases": ["light hammer", "hammer"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 100*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

KAMA = {
    "key": "Kama",
    "aliases": ["kama"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 200*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

KATANA = {
    "key": "Katana",
    "aliases": ["katana"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 10,
    "value": 4000*CP,
    "damage_roll": "1d10",
    "range": "melee"
}

MACE_HEAVY = {
    "key": "Heavy mace",
    "aliases": ["heavy mace", "mace"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 8,
    "value": 1200*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

MACE_LIGHT = {
    "key": "Light mace",
    "aliases": ["light mace", "mace"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 4,
    "value": 500*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

MORNINGSTAR = {
    "key": "Morningstar",
    "aliases": ["morningstar"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 6,
    "value": 200*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

NAGE_YARI = {
    "key": "Yari",
    "aliases": ["yari"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 3,
    "value": 300*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

NUNCHAKU = {
    "key": "Nunchaku",
    "aliases": ["Nunchaku"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 200*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

PICK_HEAVY = {
    "key": "Heavy pick",
    "aliases": ["heavy pick", "pick"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 6,
    "value": 800*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

PICK_LIGHT = {
    "key": "Light pick",
    "aliases": ["light pick", "pick"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 3,
    "value": 400*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

RAPIER = {
    "key": "Rapier",
    "aliases": ["rapier"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 2000*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

SAI = {
    "key": "Sai",
    "aliases": ["sai"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 1,
    "value": 100*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SCIMITAR = {
    "key": "Scimitar",
    "aliases": ["scimitar"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 4,
    "value": 1500*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

SICKLE = {
    "key": "Sickle",
    "aliases": ["sickle"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 600*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

SPEAR = {
    "key": "Spear",
    "aliases": ["Spear"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 6,
    "value": 200*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

SPEAR_SHORT = {
    "key": "Short spear",
    "aliases": ["short spear", "spear"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 3,
    "value": 100*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

SWORD_LONG = {
    "key": "Longsword",
    "aliases": ["longsword", "sword"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 4,
    "value": 1500*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

SWORD_SHORT = {
    "key": "Short sword",
    "aliases": ["short sword", "sword"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 1000*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

TANTO = {
    "key": "Tanto",
    "aliases": ["tanto"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 1,
    "value": 300*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

TRIDENT = {
    "key": "Trident",
    "aliases": ["trident"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 4,
    "value": 1500*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

WAKAZASHI = {
    "key": "Wakazashi",
    "aliases": ["wakazashi"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 3,
    "value": 3000*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

WAR_FAN = {
    "key": "War fan",
    "aliases": ["War fan", "fan"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 3,
    "value": 3000*CP,
    "damage_roll": "1d6",
    "range": "melee"
}

WAR_HAMMER = {
    "key": "Warhammer",
    "aliases": ["warhammer", "hammer"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 3,
    "value": 1200*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

WHIP = {
    "key": "Whip",
    "aliases": ["whip"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 100*CP,
    "damage_roll": "1d3",
    "range": "melee"
}

YARI = {
    "key": "Yari",
    "aliases": ["yari"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 5,
    "value": 500*CP,
    "damage_roll": "1d8",
    "range": "melee"
}


# Two-Handed Melee Weapons
SWORD_BASTARD = {
    "key": "Bastard Sword",
    "aliases": ["sword"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 6,
    "value": 3500*CP,
    "damage_roll": "1d10 ",
    "range": "melee"}

DIE_TSUCHI = {
    "key": "Die-Tsuchi",
    "aliases": ["die-tsuchi"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 12,
    "value": 1200*CP,
    "damage_roll": "1d8",
    "range": "melee"
}

FALCHION = {
    "key": "Falchion",
    "aliases": ["falchion"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 8,
    "value": 7500*CP,
    "damage_roll": "2d4 ",
    "range": "melee"
}

FLAIL_HEAVY = {
    "key": "Heavy Flail",
    "aliases": ["flail"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 1500*CP,
    "damage_roll": "1d10 ",
    "range": "melee"
}

GLAIVE = {
    "key": "Glaive",
    "aliases": ["glaive"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 800*CP,
    "damage_roll": "1d10",
    "range": "melee"
}

GREAT_AXE = {
    "key": "Great Axe",
    "aliases": ["axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 12,
    "value": 2000*CP,
    "damage_roll": "1d12",
    "range": "melee"
}

GREAT_CLUB = {
    "key": "Great Club",
    "aliases": ["club"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 8,
    "value": 500*CP,
    "damage_roll": "1d10 ",
    "range": "melee"
}

GREAT_SWORD = {
    "key": "Great Sword",
    "aliases": ["sword"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 8,
    "value": 5000*CP,
    "damage_roll": "2d6 ",
    "range": "melee"
}

GUISARME = {
    "key": "Guisarme",
    "aliases": ["guisarme"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 12,
    "value": 900*CP,
    "damage_roll": "2d4 ",
    "range": "melee"
}

HALBERD = {
    "key": "Halberd",
    "aliases": ["halberd"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 12,
    "value": 1000*CP,
    "damage_roll": "1d10",
    "range": "melee"
}

KAWANAGA = {
    "key": "Kawanaga",
    "aliases": ["kawanaga"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 1,
    "value": 1000*CP,
    "damage_roll": "2d4 ",
    "range": "melee"
}

KUSARI_GAMA = {
    "key": "Kusari Gama",
    "aliases": ["kusari gama"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 3,
    "value": 1000*CP,
    "damage_roll": "2d4 ",
    "range": "melee"
}

LANCE = {
    "key": "Lance",
    "aliases": ["lance"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 1000*CP,
    "damage_roll": "1d8",
    "range": "melee"
}
SPEAR_LONG = {
"key": "Long Spear",
    "aliases": ["long spear"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 9,
    "value": 500*CP,
    "damage_roll": "1d8",
    "range": "melee"
}
LUCERNE_HAMMER = {
"key": "Lucerne Hammer",
    "aliases": ["hammer"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 1200*CP,
    "damage_roll": "2d4",
    "range": "melee"
}
MANRIKI_GUSARI = {
"key": "Manriki Gusari",
    "aliases": ["mariki gusari"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 5,
    "value": 500*CP,
    "damage_roll": "2d6",
    "range": "melee"
}
MAUL = {
"key": "Maul",
    "aliases": ["maul"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 20,
    "value": 1500*CP,
    "damage_roll": "1d10",
    "range": "melee"
}
NAGIMAKI = {
"key": "Nagimaki",
    "aliases": ["nagimaki"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 8000*CP,
    "damage_roll": "2d4",
    "range": "melee"
}
NAGINATA = {
"key": "Naginata",
    "aliases": ["naginata"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 15,
    "value": 1000*CP,
    "damage_roll": "1d10",
    "range": "melee"
}
NO_DACHI = {
"key": "No-Dachi",
    "aliases": ["no dachi"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 12,
    "value": 5000*CP,
    "damage_roll": "2d6",
    "range": "melee"
}
ONO = {
"key": "Ono",
    "aliases": ["ono"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 2000*CP,
    "damage_roll": "1d10",
    "range": "melee"
}
QUARTERSTAFF = {
"key": "Quarterstaff",
    "aliases": ["staff"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 4,
    "value": 100*CP,
    "damage_roll": "1d6",
    "range": "melee"
}
RANSUER = {
"key": "Ransuer",
    "aliases": ["ransuer"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 12,
    "value": 1000*CP,
    "damage_roll": "2d4",
    "range": "melee"
}

SCYTHE = {
"key": "Scythe",
    "aliases": ["scythe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 10,
    "value": 1800*CP,
    "damage_roll": "2d4",
    "range": "melee"
}

TETSUBO = {
"key": "Tetsubo",
    "aliases": ["tetsubo"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": " "
            " ",
    "weight": 15,
    "value": 2500*CP,
    "damage_roll": "1d8",
    "range": "melee"
}



# Ranged Weapons

LONG_BOW = {
    "key": "a long bow",
    "aliases": ["long bow", "bow"],
    "typeclass": "typeclasses.weapons.TwoHandedRanged",
    "desc": "This bow has a rich patina from years of use, but its draw is "
            "firm and it will still accurately deliver an arrow to the heart "
            "of your enemies.",
    "weight": 1,
    "value": 40*CP,
    "damage": 1,
    "ammunition": "arrow",
    "range": "ranged"
}


# Ammunition

ARROW = {
    "key": "an obsidian-tipped arrow",
    "aliases": ["arrow"],
    "typeclass": "typeclasses.items.Bundlable",
    "desc": "Arrows crafted from reed wood and obsidian stone.",
    "weight": 1,
    "value": 2*CP,
    "bundle_size": 10,
    "prototype_name": "ARROW"
}


ARROW_BUNDLE = {
    "key": "a bundle of arrows",
    "aliases": ["bundle of arrows", "bundle arrow", "arrows"],
    "typeclass": "typeclasses.items.Bundle",
    "desc": "A bundle of arrows held together with a thin leather strap.",
    "weight": 10,
    "value": 25*CP,
    "quantity": 10,
    "prototype_name": "ARROW",
}


# Thrown Ranged

THROWING_AXE = {
    "key": "a throwing axe",
    "aliases": ["throwing axe", "th axe", "thr axe", "axe"],
    "typeclass": "typeclasses.weapons.RangedWeapon",
    "desc": "This axe is light and sharp. It is balanced to spin fast "
            "and true when thrown.",
    "weight": 2,
    "value": 80*CP,
    "damage": 0,
    "range": "reach",
    "ammunition": "throwing axe"
}
