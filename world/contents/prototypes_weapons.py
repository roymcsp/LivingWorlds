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
    "weight": 5,
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
SWORD_BASTARD = {}
DIE_TSUCHI = {}
FALCHION = {}
FLAIL_HEAVY = {}
GLAIVE = {}
GREAT_AXE = {}
GREAT_CLUB = {}
GREAT_SWORD = {}
GUISARME = {}
HALBERD = {}
KAWANAGA = {}
KUSARI_GAMA = {}
LANCE = {}
SPEAR_LONG = {}
LUCERNE_HAMMER = {}
MANRIKI_GUSARI = {}
MAUL = {}
NAGIMAKI = {}
NAGINATA = {}
NO_DACHI = {}
ONO = {}
QUARTERSTAFF = {}
RANSUER = {}
TETSUBO = {}

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
