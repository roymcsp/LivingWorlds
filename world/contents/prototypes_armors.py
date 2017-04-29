"""
Prototype module containing armor.
"""

from evennia.utils import fill
from world.economy import SP, CP

# Armor

SIMPLE_ROBE = {
    "key": "|YSimple robe",
    "aliases": ["simple robe", "robe"],
    "typeclass": "typeclasses.armors.Torso",
    "desc": "Made of soft cloth, this robe provides minimal protection.",
    "weight": 2,
    "value": 0*CP,
    "physical_bonus": 1,
}