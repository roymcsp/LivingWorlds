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
    toughness = 0
    slots = ['']

    def at_object_creation(self):
        super(Armor, self).at_object_creation()
        self.db.toughness = self.toughness

    def at_equip(self, character):
        character.traits.PDEF.mod += self.db.toughness

    def at_remove(self, character):
        character.traits.PDEF.mod -= self.db.toughness


class Torso(Armor):
    slots = ['armor']


class Shield(Armor):
    """Typeclass for shield prototypes."""

    slots = ['wield1', 'wield2']
    multi_slot = False


class Helm(Armor):
    slots = ['helm']


class Boots(Armor):
    slots = ['boots']


class Gloves(Armor):
    slots = ['gloves']


class Necklace(Armor):
    slots = ['necklace']


class Bracers(Armor):
    slots = ['bracers']


class Belt(Armor):
    slots = ['belt']


class Ring(Armor):
    slots = ['ring1', 'ring2']
    multi_slot = False