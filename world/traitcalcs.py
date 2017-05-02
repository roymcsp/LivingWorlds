PRIMARY_TRAITS = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
ABILITY_MODIFIER_TRAITS = ('STRMOD', 'DEXMOD', 'CONMOD', 'INTMOD', 'WISMOD', 'CHAMOD')
SECONDARY_TRAITS = ('HP', 'SP')
SAVE_ROLLS = ('FORT', 'REFL', 'WILL')
COMBAT_TRAITS = ('ATKM', 'ATKR', 'ATKU', 'PDEF', 'MDEF')
OTHER_TRAITS = ('LVL', 'XP', 'ENC', 'EP')


abilitymodifiers = [-5, -4, -4, -3, -3, -2, -2, -1, -1, -0, -0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
                    10, 10, 11]


def calculate_secondary_traits(traits):
    """
    Calculations for secondary traits
    """
    # secondary traits
    traits.HP.mod = abilitymodifiers[traits.CON.actual - 1]
    traits.SP.mod = abilitymodifiers[traits.INT.actual - 1] + abilitymodifiers[traits.WIS.actual - 1]
    # saves
    traits.FORT.mod = abilitymodifiers[traits.CON.actual - 1]
    traits.REFL.mod = abilitymodifiers[traits.DEX.actual - 1]
    traits.WILL.mod = abilitymodifiers[traits.WIS.actual - 1]
    # combat
    traits.MAB.mod = abilitymodifiers[traits.STR.actual - 1]
    traits.RAB.mod = abilitymodifiers[traits.DEX.actual - 1]
    traits.UAB.mod = abilitymodifiers[traits.DEX.actual - 1]
    # misc
    traits.STR.carry_factor = 10
    traits.STR.lift_factor = 20
    traits.STR.push_factor = 40
    traits.ENC.max = traits.STR.lift_factor * traits.STR.actual
    traits.PDEF.mod = abilitymodifiers[traits.DEX.actual - 1]
    traits.MDEF.mod = abilitymodifiers[traits.INT.actual - 1]
