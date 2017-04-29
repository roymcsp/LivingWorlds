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

    # misc
    traits.STR.carry_factor = 10
    traits.STR.lift_factor = 20
    traits.STR.push_factor = 40
    traits.ENC.max = traits.STR.lift_factor * traits.STR.actual


"""    
    # saves
    # saves are calculated as base save determined by guild? + (ability modifier + magic modifier + 
                                                                misc modifer + temporary modifier)
    
    traits.FORT.mod = abilitymodifiers[self.traits.CON.actual - 1]
    
    traits.REFL.mod = abilitymodifiers[self.traits.DEX.actual - 1]
    
    traits.WILL.mod = abilitymodifiers[self.traits.WIS.actual - 1]
    
    # combat
    to hit roll is calculated as base + ability modifier + magic modifier
    mab = melee attack bonus, rab = ranged attack bonus,  uab = unarmed attack bonus
     
    traits.MAB.base = 0 + attack
    skill
    traits.MAB.mod = abilitymodifier[self.traits.STR.actual - 1]
    traits.RAB.base = 0 + attack

    traits.RAB.mod = abilitymodifier[self.traits.DEX.actual - 1]
    traits.UAB.base = 0 + attack
    
    traits.UAB.mod = abilitymodifier[self.traits.DEX.actual - 1]
    
    physical defense is calculated by base + sum of all armors modifier + dex modifier + magic modifiers
     
    traits.PDEF.base = 10
    traits.PDEF.mod = abilitymodifier[self.traits.DEX.actual - 1]
    
    magical defense is base + sum of all accessory armor modifiers + int modifier + magic modifiers
    
    traits.MDEF.base = 10 + traits.lvl.actual
    traits.MDEF.mod = abilitymodifier[self.traits.INT.actual - 1]

"""