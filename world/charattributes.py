PRIMARY_TRAITS = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
SECONDARY_TRAITS = ('HP', 'SP')
SAVE_ROLLS = ('FORT', 'REFL', 'WILL')
COMBAT_TRAITS = ('ATKM', 'ATKR', 'ATKU', 'PDEF', 'MDEF')
OTHER_TRAITS = ('LEVEL', 'XP', 'ENC', 'EP')

ALL_TRAITS = (PRIMARY_TRAITS + SECONDARY_TRAITS +
              SAVE_ROLLS + COMBAT_TRAITS + OTHER_TRAITS)


"""
Calculations for secondary traits
"""
# secondary traits
traits.HP.base = 100 + ((traits.STR.actual + traits.DEX.actual + traits.CON.actual) / 3)
traits.SP.base = 100 + ((traits.INT.actual + traits.WIS.actual) / 2)
# save rolls
traits.FORT.base = traits.CON.actual
traits.REFL.base = traits.DEX.actual
traits.WILL.base = traits.INT.actual
# combat
traits.ATKM.base = traits.STR.actual
traits.ATKR.base = traits.DEX.actual
traits.ATKU.base = traits.DEX.actual
traits.PDEF.base = traits.DEX.actual
traits.MDEF.base = traits.INT.actual
# misc
traits.STR.carry_factor = 10
traits.STR.lift_factor = 20
traits.STR.push_factor = 40
traits.ENC.max = traits.STR.lift_factor * traits.STR.actual


self.health_roll = None
