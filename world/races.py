"""
Races module.
This module contains data and functions relating to Races. Its
public module functions are to be used primarily during the character
creation process.

Classes:

    `Race`: base class for all races
    `Human`: human race class
    `Elf`: elf race class
    `Dwarf`: dwarf race class
    `Gnome`: gnome race class
    `Centaur`: centaur race class
    `Drow`: drow race class
    `Duergar`: duergar race class
    `Svirfneblin`: svirfneblein race class
    `Wemic`: wemic race class
    `Drakkar`: drakkar race class
    `Ursine`: ursine race class
    `Feline`: feline race class
    `Lupine`: lupine race class
    `Vulpine`: vulpine race class
    `Naga`: naga race class

Module Functions

    - `load_race(str)`:
       loads an instance of the named Race class

    - `apply_race(char, race, focus)`:
        have a character "become" a member of the specified race with
        the specified focus
        
    """

class RaceException(Exception):
    """Base exception class for races module."""
    def __init__(self, msg):
        self.msg = msg

# ALL_RACES = ('Human', 'Elf', 'Dwarf','Gnome', 'Centaur', 'Ogryn', 'Drow', 'Duergar', 'Svirfneblin', 'Wemic', 'Drakkar', 'Ursine','Feline', 'Lupine', 'Vulpine', 'Naga')
KINGDOM_RACES = ('Human', 'Elf', 'Dwarf','Gnome', 'Centaur', 'Ogryn')
CALIPHATE_RACES = ('Human', 'Drow', 'Duergar', 'Svirfneblin', 'Wemic', 'Drakkar')
EMPIRE_RACES = ('Human', 'Ursine','Feline', 'Lupine', 'Vulpine', 'Naga')

def load_race(race):
    """Returns an instance of the named race class.
    Args:
        race (str): case-insensitive name of race to load
    Returns:
        (Race): instance of the appropriate subclass of `Race`
    """
    race = race.capitalize()
    if race in ALL_RACES:
        return globals()[race]()
    else:
        raise RaceException("Invalid race specified.")

def apply_race(character, race):
    """Causes a Character to "become" the named race.
    Args:
        char (Character): the character object becoming a member of race
        race (str, Race): the name of the race to apply, or the
        """
    # if objects are passed in, reload Race and Focus objects
    # by name to ensure we have un-modified versions of them
    if isinstance(race, Race):
        race = race.name

    race = load_race(race)

    # make sure the race is allowed for the nation
    if character.db.nation == 'Kingdom' and race.name not in (r.name for r in KINGDOM_RACES):
        raise RaceException(
            'Invalid race specified. '
            'Race {} is not available to nation {}.'.format(race.name, nation.name)
        )
    elif if character.db.nation == 'Calipahte' and race.name not in (r.name for r in CALIPHATE_RACES):
        raise RaceException(
            'Invalid race specified. '
            'Race {} is not available to nation {}.'.format(race.name, nation.name)
        )    
    elif if character.db.nation == 'Empire' and race.name not in (r.name for r in EMPIRE_RACES):
        raise RaceException(
            'Invalid race specified. '
            'Race {} is not available to nation {}.'.format(race.name, nation.name)
        )    
        
    # set race and related attributes on the character
    character.db.race = race.name
    character.db.slots = race.slots
    character.db.limbs = race.limbs

    # apply race-based bonuses
    for trait, bonus in race.bonuses.iteritems():
        char.traits[trait].mod += bonus

class Race(object):
    """Base class for race attributes"""
    def __init__(self):
        self.name = ""
        self.plural = ""
        self.size = ""
        self.slots = {
            'wield1': None,
            'wield2': None,
            'helm': None,
            'necklace': None,
            'armor': None,
            'belt':None,
            'bracers': None,
            'gloves': None,
            'ring1': None,
            'ring2': None,
            'boots': None,            
        }
        
        self.limbs = (
            ('r_hand', ('wield1',)),
            ('l_hand', ('wield2',)),
            ('head', ('helm',)),
            ('neck', ('necklace',)),
            ('torso', ('armor',)),
            ('waist', ('belt',)),
            ('wrists', ('bracers',)),
            ('hands', ('gloves',)),
            ('finger1', ('ring1',)),
            ('finger2', ('ring2',)),
            ('feet' , ('boots',)),
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
#Kingdom Races         
class Elf(Race):
    """Class reresenting elven attributes."""
    def __init__(self):
        super(Elf, self).__init__()
        self.name = "Elf"
        self.plural = "Elves"
        self.size = "medium"
        self.bonuses = {'Dexterity': 2,
                        'Constitution': -2}
        self.language = "Elven"
        
class Dwarf(Race): 
    """Class reresenting dwarven attributes."""
    def __init__(self):
        super(Dwarf, self).__init__()
        self.name = "Dwarf"
        self.plural = "Dwarfs"
        self.size = "medium"
        self.bonuses = {'Constitution': 2,
                        'Charisma': -2}
        self.language = "Dwarven"
        
class Gnome(Race): 
    """Class reresenting gnomish attributes."""
    def __init__(self):
        super(Gnome, self).__init__()
        self.name = "Gnome"
        self.plural = "Gnomes"
        self.size = "small"
        self.bonuses = {'Constitution': 2,
                        'Strength': -2}
        self.language = "Gnomish"

class Centaur(Race): 
    """Class reresenting centaur attributes."""
    def __init__(self):
        super(Centaur, self).__init__()
        self.name = "Centaur"
        self.plural = "Centaur"
        self.size = "large"
        self.bonuses = {'Wisdom': 2,
                        'Intelligence': -2}
        self.language = "Centaur" 

class Ogryn(Race): 
    """Class reresenting Ogryn attributes."""
    def __init__(self):
        super(Dwarf, self).__init__()
        self.name = "Ogryn"
        self.plural = "Ogryn"
        self.size = "medium"
        self.bonuses = {'Strength': 2,
                        'Intelligence': -2}
        self.language = "Ogryn"
          

#Calipahte Races

class Drow(Race): 
    """Class reresenting Drow attributes."""
    def __init__(self):
        super(Drow, self).__init__()
        self.name = "Drow"
        self.plural = "Drow"
        self.size = "medium"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Drow"

class Duergar(Race): 
    """Class reresenting elven attributes."""
    def __init__(self):
        super(Duergar, self).__init__()
        self.name = "Duergar"
        self.plural = "Duergar"
        self.size = "medium"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Duergar"        

class Svirfneblin(Race): 
    """Class reresenting Svirfneblin attributes."""
    def __init__(self):
        super(Svirfneblin, self).__init__()
        self.name = "Svirfneblin"
        self.plural = "Svirfneblin"
        self.size = "small"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Svirfneblin"
 
class Wemic(Race): 
    """Class reresenting Wemic attributes."""
    def __init__(self):
        super(Wemic, self).__init__()
        self.name = "Wemic"
        self.plural = "Wemic"
        self.size = "large"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Wemic"

class Drakkar(Race): 
    """Class reresenting Drakkari attributes."""
    def __init__(self):
        super(Drakkar, self).__init__()
        self.name = "Drakkar"
        self.plural = "Drakkari"
        self.size = "medium"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Drakkonic"


#Empire Races 
class Ursine(Race): 
    """Class reresenting elven attributes."""
    def __init__(self):
        super(Dwarf, self).__init__()
        self.name = "Ursine"
        self.plural = "Ursine"
        self.size = "large"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Ursine"
 
class Lupine(Race): 
    """Class reresenting lupine attributes."""
    def __init__(self):
        super(Lupine, self).__init__()
        self.name = "Lupine"
        self.plural = "Lupine"
        self.size = "medium"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Lupine"

class Feline(Race): 
    """Class reresenting feline attributes."""
    def __init__(self):
        super(Feline, self).__init__()
        self.name = "Feline"
        self.plural = "Feline"
        self.size = "medium"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Feline"
 
class Vulpine(Race): 
    """Class reresenting vulpine attributes."""
    def __init__(self):
        super(Vulpine, self).__init__()
        self.name = "Vulpine"
        self.plural = "Vulpine"
        self.size = "small"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Vulpine"

class Naga(Race): 
    """Class reresenting nagan attributes."""
    def __init__(self):
        super(Naga, self).__init__()
        self.name = "Naga"
        self.plural = "Naga"
        self.size = "medium"
        self.bonuses = {'': 2,
                        '': -2}
        self.language = "Nagan"