PRIMARY_TRAITS = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
ABILITY_MODIFIER_TRAITS = ('STRMOD', 'DEXMOD', 'CONMOD', 'INTMOD', 'WISMOD', 'CHAMOD')
SECONDARY_TRAITS = ('HP', 'SP')
SAVE_ROLLS = ('FORT', 'REFL', 'WILL')
COMBAT_TRAITS = ('ATKM', 'ATKR', 'ATKU', 'PDEF', 'MDEF')
OTHER_TRAITS = ('LVL', 'XP', 'ENC', 'EP')

ability_modifiers = {
# primary ability modifier
    'STRMOD': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Strength Modifier'},
    'DEXMOD': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Dexterity Modifier'},
    'CONMOD': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Constitution Modifier'},
    'INTMOD': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Intelligence Modifier'},
    'WISMOD': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Wisdom Modifier'},
    'CHAMOD': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Charisma Modifier'},
}

abilitymodifiers = {
    '1': '-5',
    '2': '-4',
    '3': '-4',
    '4': '-3',
    '5': '-3',
    '6': '-2',
    '7': '-2',
    '8': '-1',
    '9': '-1',
    '10': '0',
    '11': '0',
    '12': '+1',
    '13': '+1',
    '14': '+2',
    '15': '+2',
    '16': '+3',
    '17': '+3',
    '18': '+4',
    '19': '+4',
    '20': '+5',
    '21': '+5',
    '22': '+6',
    '23': '+6',
    '24': '+7',
    '25': '+7',
    '26': '+8',
    '27': '+9',
    '28': '+10',
    '29': '+10',
    '30': '+11',
}

def calculate_ability_modifiers(traits):
    """
    take each PRIMARY_TRAITS actual value as a key for abilitymodifiers to get the matching
    modifier for each ability_modifiers base value, then add that to the character.
    """

def calculate_secondary_traits(traits):
    """
    Calculations for secondary traits
    """
    # secondary traits
    traits.HP.base = 100 + ((traits.STRMOD.actual + traits.DEXMOD.actual + traits.CONMOD.actual) / 3)
    traits.SP.base = 100 + ((traits.INTMOD.actual + traits.WISMOD.actual) / 2)
    # save rolls
    traits.FORT.base = traits.CONMOD.actual
    traits.REFL.base = traits.DEXMOD.actual
    traits.WILL.base = traits.INTMOD.actual
    # combat
    traits.ATKM.base = traits.STRMOD.actual
    traits.ATKR.base = traits.DEXMOD.actual
    traits.ATKU.base = traits.DEXMOD.actual
    traits.PDEF.base = 10 + traits.DEXMOD.actual
    traits.MDEF.base = 10 + traits.INTMOD.actual
    # misc
    traits.STR.carry_factor = 10
    traits.STR.lift_factor = 20
    traits.STR.push_factor = 40
    traits.ENC.max = traits.STR.lift_factor * traits.STR.actual