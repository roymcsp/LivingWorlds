
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
            'finger1': None,
            'finger2': None,        
        }
        
        self.limbs = (
            ('r_hand', ('wield1',)),
            ('l_hand', ('wield2',)),
            ('head', ('head',)),
            ('neck', ('neck',)),
            ('torso', ('torso',)),
            ('waist', ('waist',)),
            ('wrists', ('wrists',)),
            ('hands', ('hands',)),
            ('finger1', ('finger1',)),
            ('finger2', ('finger2',)),
        )
        
        self.bonuses = {}
        self.language = {}
        
class Human(Race):
    """Class representing human attributes."""
    def __init__(self):
        super(Human, self).__init__()
        self.name = "Human"
        self.plural = "Humans"
        self.size = "medium"
        self.language = "common"
        
class Elf(Race):
    """Class reresenting elven attributes."""
    def __init__(self):
        super(Human, self).__init__()
        self.name = "Elf"
        self.plural = "Elves"
        self.size = "medium"
        self.bonuses = {'Dexterity': 2,
                        'Constitution': -2}
        self.language = "Elven"
        