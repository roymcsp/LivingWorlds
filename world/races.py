
class Race(object):
    """Base class for race attributes"""
    def __init__(self):
        self.name = ""
        self.plural = ""
        self.size = ""
        self.slots = {
            'wield1': None,
            'wield2': None,
            'head': None,
            'neck': None,
            'torso': None,
            'waist':None,
            'wrists': None,
            'hands': None,
            'ringer1': None,
            'finger2': None,        
        }
        
        self.limbs = (
            ('r_hand', ('wield1',)),
            ('l_hand', ('wield2',)),
            ('', ('',)),
            ('', ('',)),
            ('', ('',)),
            ('', ('',)),
            ('', ('',)),
            ('', ('',)),
            ('', ('',)),
            ('', ('',)),
        )
        
        self.bonuses = {}
        self.language = {}
        