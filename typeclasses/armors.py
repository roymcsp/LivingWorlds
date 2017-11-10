"""
Armor typeclasses
"""

from typeclasses.items import Equippable


class Armor(Equippable):
    """
    Typeclass for armor objects.
    Attributes:
        toughness (int): primary defensive stat
    """
    physical_bonus = 0
    magical_bonus = 0
    slots = None

    def at_object_creation(self):
        super(Armor, self).at_object_creation()
        self.db.physical_bonus = self.physical_bonus
        self.db.magical_bonus = self.magical_bonus

    def at_equip(self, character):
        character.traits.PDEF.mod += self.db.physical_bonus
        character.traits.MDEF.mod += self.db.magical_bonus

    def at_remove(self, character):
        character.traits.PDEF.mod -= self.db.physical_bonus
        character.traits.MDEF.mod -= self.db.magical_bonus


class Torso(Armor):
    slots = ['torso']
    multi_slot = False


class Shield(Armor):
    """Typeclass for shield prototypes."""

    slots = ['wield1', 'wield2']
    multi_slot = False


class Helm(Armor):
    slots = ['helm']
    multi_slot = False


class Boots(Armor):
    slots = ['boots']
    multi_slot = False


class Gloves(Armor):
    slots = ['gloves']
    multi_slot = False


class Necklace(Armor):
    slots = ['necklace']
    multi_slot = False


class Bracers(Armor):
    slots = ['bracers']
    multi_slot = False


class Belt(Armor):
    slots = ['belt']
    multi_slot = False


class Ring(Armor):
    slots = ['ring1', 'ring2']
    multi_slot = False
