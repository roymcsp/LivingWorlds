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

    - `apply_race(char, race)`:
        have a character "become" a member of the specified race with
        the specified focus
        
    """

from evennia import Command
from evennia.utils.evmenu import get_input   


class CmdRace(Command):

    """
    command for setting the race on the character
    takes one arg in the form of the race name
    
    args:
    
    
    Usage:
       select <race>
    """
    key = "select"
    locks = "cmd:all()"
    
    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        race = caller.db.race
        if race in ALL_RACES:
        
            get_input(caller, "You have already selected your race, do you wish to change it? (Yes/No)?", self.choice)
           
        else:
            apply_race(caller, args)

    def choice(self, caller, prompt, result):
        if result.lower() in ("y", "yes"):
            caller.msg('Your race has been changed to %s.' % self.args)
            apply_race(caller, self.args)

        if result.lower() in ("n", "no"):
            caller.msg('No changes made')


class RaceException(Exception):
    """Base exception class for races module."""
    def __init__(self, msg):
        self.msg = msg

ALL_RACES = ('Human', 'Elf', 'Dwarf', 'Gnome', 'Centaur', 'Ogryn', 'Drow', 'Duergar', 'Svirfneblin', 'Wemic', 'Drakkar',
             'Ursine', 'Feline', 'Lupine', 'Vulpine', 'Naga')
KINGDOM_RACES = ('Human', 'Elf', 'Dwarf', 'Gnome', 'Centaur', 'Ogryn')
CALIPHATE_RACES = ('Human', 'Drow', 'Duergar', 'Svirfneblin', 'Wemic', 'Drakkar')
EMPIRE_RACES = ('Human', 'Ursine', 'Feline', 'Lupine', 'Vulpine', 'Naga')


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
        character: the character object becoming a member of race
        race (str, Race): the name of the race to apply
        """
    # if objects are passed in, reload Race objects
    # by name to ensure we have un-modified versions of them
    if isinstance(race, Race):
        race = race.name

    race = load_race(race)

    # make sure the race is allowed for the nation
    if character.db.nation == 'kingdom' and race not in KINGDOM_RACES:
        character.msg('Race {} is not available to the kingdom.'.format(race.name))
        return

    elif character.db.nation == 'caliphate' and race not in CALIPHATE_RACES:
        character.msg('Race {} is not available to the caliphate.'.format(race.name))
        return

    elif character.db.nation == 'empire' and race not in EMPIRE_RACES:
        character.msg('Race {} is not available to the empire.'.format(race.name))
        return

    # set race and related attributes on the character
    character.db.race = race.name
    character.db.slots = race.slots
    character.db.limbs = race.limbs
    character.msg('You become {}.' .format(race.name))
    
    # apply race-based bonuses
    # for trait, bonus in race.bonuses.iteritems():
    #    char.traits[trait].mod += bonus


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
            'belt': None,
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
            ('feet', ('boots',)),
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
        
# Kingdom Races


class Elf(Race):
    """Class representing elven attributes."""
    def __init__(self):
        super(Elf, self).__init__()
        self.name = "Elf"
        self.plural = "Elves"
        self.size = "medium"
        self.bonuses = {'Dexterity': 2,
                        'Constitution': -2
                        }
        self.language = "Elven"


class Dwarf(Race): 
    """Class representing dwarven attributes."""
    def __init__(self):
        super(Dwarf, self).__init__()
        self.name = "Dwarf"
        self.plural = "Dwarfs"
        self.size = "medium"
        self.bonuses = {'Constitution': 2,
                        'Charisma': -2
                        }
        self.language = "Dwarven"


class Gnome(Race): 
    """Class representing gnomish attributes."""
    def __init__(self):
        super(Gnome, self).__init__()
        self.name = "Gnome"
        self.plural = "Gnomes"
        self.size = "small"
        self.bonuses = {'Constitution': 2,
                        'Strength': -2
                        }
        self.language = "Gnomish"


class Centaur(Race): 
    """Class representing centaur attributes."""
    def __init__(self):
        super(Centaur, self).__init__()
        self.name = "Centaur"
        self.plural = "Centaur"
        self.size = "large"
        self.bonuses = {'Wisdom': 2,
                        'Intelligence': -2
                        }
        self.language = "Centaur" 


class Ogryn(Race): 
    """Class representing Ogryn attributes."""
    def __init__(self):
        super(Ogryn, self).__init__()
        self.name = "Ogryn"
        self.plural = "Ogryn"
        self.size = "medium"
        self.bonuses = {'Strength': 2,
                        'Intelligence': -2
                        }
        self.language = "Ogryn"
          

# Caliphate Races

class Drow(Race): 
    """Class representing Drow attributes."""
    def __init__(self):
        super(Drow, self).__init__()
        self.name = "Drow"
        self.plural = "Drow"
        self.size = "medium"
        self.bonuses = {'Dexterity': 2,
                        'Intelligence': 2,
                        'Charisma': 2,
                        'Constitution': -2
                        }
        self.language = "Drow"


class Duergar(Race): 
    """Class reresenting elven attributes."""
    def __init__(self):
        super(Duergar, self).__init__()
        self.name = "Duergar"
        self.plural = "Duergar"
        self.size = "medium"
        self.bonuses = {'Constitution': 2,
                        'Wisdom': 2,
                        'Charisma': -2
                        }
        self.language = "Duergar"        


class Svirfneblin(Race): 
    """Class reresenting Svirfneblin attributes."""
    def __init__(self):
        super(Svirfneblin, self).__init__()
        self.name = "Svirfneblin"
        self.plural = "Svirfneblin"
        self.size = "small"
        self.bonuses = {'Dexterity': 2,
                        'Wisdom': 2,
                        'Strength': -2,
                        'Charisma': -2
                        }
        self.language = "Svirfneblin"


class Wemic(Race): 
    """Class reresenting Wemic attributes."""
    def __init__(self):
        super(Wemic, self).__init__()
        self.name = "Wemic"
        self.plural = "Wemic"
        self.size = "large"
        self.bonuses = {'Strength': 2,
                        'Constitution': 2,
                        'Wisdom': -2,
                        'Charisma': -2
                        }
        self.language = "Wemic"


class Drakkar(Race): 
    """Class reresenting Drakkari attributes."""
    def __init__(self):
        super(Drakkar, self).__init__()
        self.name = "Drakkar"
        self.plural = "Drakkari"
        self.size = "medium"
        self.bonuses = {'Intelligence': 2,
                        'Constitution': 2,
                        'Charisma': 2,
                        'Dexterity': -2
                        }
        self.language = "Drakkonic"


# Empire Races
 
class Ursine(Race): 
    """Class reresenting elven attributes."""
    def __init__(self):
        super(Ursine, self).__init__()
        self.name = "Ursine"
        self.plural = "Ursine"
        self.size = "large"
        self.bonuses = {'Strength': 2,
                        'Dexterity': -2
                        }
        self.language = "Ursine"


class Lupine(Race): 
    """Class reresenting lupine attributes."""
    def __init__(self):
        super(Lupine, self).__init__()
        self.name = "Lupine"
        self.plural = "Lupine"
        self.size = "medium"
        self.bonuses = {'Constitution': 2,
                        'Intelligence': -2
                        }
        self.language = "Lupine"


class Feline(Race): 
    """Class reresenting feline attributes."""
    def __init__(self):
        super(Feline, self).__init__()
        self.name = "Feline"
        self.plural = "Feline"
        self.size = "medium"
        self.bonuses = {'Dexterity': 2,
                        'Strength': -2
                        }
        self.language = "Feline"


class Vulpine(Race): 
    """Class reresenting vulpine attributes."""
    def __init__(self):
        super(Vulpine, self).__init__()
        self.name = "Vulpine"
        self.plural = "Vulpine"
        self.size = "small"
        self.bonuses = {'Intelligence': 2,
                        'Wisdom': -2
                        }
        self.language = "Vulpine"


class Naga(Race): 
    """Class reresenting nagan attributes."""
    def __init__(self):
        super(Naga, self).__init__()
        self.name = "Naga"
        self.plural = "Naga"
        self.size = "medium"
        self.bonuses = {'Constitution': 2,
                        'Wisdom': 2,
                        'Charisma': -2
                        }
        self.language = "Nagan"
