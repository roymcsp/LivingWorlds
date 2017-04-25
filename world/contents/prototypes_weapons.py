"""
Prototype module containing weapons and shields.
"""

from evennia.utils import fill
from world.economy import PP, GP, SP, CP
from random import randint
## Weapons from D&D

# One-handed Melee Weapons
HAND_AXE = {
    "key": "Hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

BATTLE_AXE = {
    "key": "Battle axe",
    "aliases": ["battleaxe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

CLUB ={
    "key": "Club",
    "aliases": ["club"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

DAGGER = {
    "key": "Dagger",
    "aliases": ["axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

FLAIL = {
    "key": "Flail",
    "aliases": ["flail"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

HAMMER_LIGHT ={
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

KAMA = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

KATANA = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

MACE_HEAVY = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

MACE_LIGHT = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

MORNINGSTAR = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

NAGE_YARI = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

NUNCHAKU = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

PICK_HEAVY ={
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

PICK_LIGHT = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

RAPIER = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SAI = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SCIMITAR = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SICKLE = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SPEAR = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SPEAR_SHORT = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SWORD_LONG = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

SWORD_SHORT = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

TANTO = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

TRIDENT = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

WAKAZASHI = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

WAR_FAN = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

WAR_HAMMER = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

WHIP = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}

YARI = {
    "key": "hand axe",
    "aliases": ["hand axe", "axe"],
    "typeclass": "typeclasses.weapons.Weapon",
    "desc": "The blade of this axe appears well-used and slightly "
            "tarnished, but its handle is straight and sturdy.",
    "weight": 2,
    "value": 60*CP,
    "damage_roll": "1d4",
    "range": "melee"
}


#Two-Handed Melee Weapons
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

