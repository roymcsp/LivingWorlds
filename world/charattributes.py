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


        # base traits data
        self.traits = {
            # primary
            'STR': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Strength'},
            'DEX': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Dexterity'},
            'CON': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Constitution'},
            'INT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Intelligence'},
            'WIS': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Wisdom'},
            'CHA': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Charisma'},
            # secondary
            'HP': {'type': 'gauge', 'base': 0, 'mod': 0, 'name': 'Health'},
            'SP': {'type': 'gauge', 'base': 0, 'mod': 0, 'name': 'Spell Power'},
            # saves
            'FORT': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Fortitude Save'},
            'REFL': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Reflex Save'},
            'WILL': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Will Save'},
            # combat
            'ATKM': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Melee Attack'},
            'ATKR': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Ranged Attack'},
            'ATKU': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Unarmed Attack'},
            'PDEF': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Physical Defense'},
            'MDEF': {'type': 'counter', 'base': 0, 'mod': 0, 'min': 0, 'name': 'Magical Defense'},

            # misc
            'ENC': {'type': 'counter', 'base': 0, 'mod': 0, 'min': 0, 'name': 'Carry Weight'},
            'EP': {'type': 'gauge', 'base': 6, 'mod': 0, 'min': 0, 'name': 'Endurance Points'},
            'LV': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Level'},
            'XP': {'type': 'static', 'base': 0, 'mod': 0, 'name': 'Experience',
                   'extra': {'level_boundaries': (500, 2000, 4500, 'unlimited')}},
        }
        self.health_roll = None
