"""
backgrounds module.
This module contains data and functions relating to backgrounds. Its
public module functions are to be used primarily during the character
creation process.

Classes:

    `Background`: base class for all backgrounds
    `Farmer`: farmer background
    `Gypsy`: gypsy background
    `Noble`: noble background
    `Nomad`: nomad background
    `Tradesman`: tradesman background
    `Urchin`: urchin background
    

Module Functions

    - `load_background(str)`:
       loads an instance of the named Background class

    - `apply_background(character, background)`:
        have a character "become" a member of the specified background with
        the specified background command
    """

from evennia import Command
from commands.powers import bgpowers

URCHIN_SKILLS = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
                 'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
                 'FOC': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Focus'},}

NOBLE_SKILLS = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
                'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
                'LEA': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Leadership'},}

NOMAD_SKILLS = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
                'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
                'MAR': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Martial'},}

GYPSY_SKILLS = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'DOD': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Dodge'},}

FARMER_SKILLS = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'ORG': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Organize'},}

TRADESMAN_SKILLS = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'FOR': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Forge'},}


class CmdBackground(Command):
    """
    command for setting the background on the character
    takes one arg in the form of the background name
    
    args:
    
    
    Usage:
       choose <background>
    """

    key = "choose"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower()
        background = caller.db.background
        if background in ALL_BACKGROUNDS:
            bgmsg = "You have aready chosen your background"
            caller.msg(bgmsg)
            return
        else:
            apply_background(caller, args)


class BackgroundException(Exception):
    """Base exception class for background module."""

    def __init__(self, msg):
        self.msg = msg


ALL_BACKGROUNDS = ("Farmer", "Gypsy", "Noble", "Nomad", "Tradesman", "Urchin")


def load_background(background, character):
    """Returns an instance of the named background class.
    Args:
        background (str): case-insensitive name of background to load
    Returns:
        (Background): instance of the appropriate subclass of `Background`
    """

    background = background.strip().capitalize()

    if background in ALL_BACKGROUNDS:
        return globals()[background](character)
    else:
        raise BackgroundException("Invalid background specified.")


def apply_background(character, background):
    """Causes a Character to "have" a named background.
    Args: 
        character: the character object having a background
        background (str, Background): the name of the background to apply
    """
    if isinstance(background, Background):
        background = background.name

    background = load_background(background)

    character.db.background = background.name
    character.message('Your background has been set to {}.' .format(background.name))


class Background(object):
    def __init__(self, character):
        self.name = ""


class Urchin(Background):
    def __init__(self, character):
        super(Urchin, self).__init__(character)
        self.name = "Urchin"
        character.cmdset.add(bgpowers.UrchinCmdSet, permanent=True)
        for key, kwargs in URCHIN_SKILLS.iteritems():
            character.skills.add(key, **kwargs)


class Noble(Background):
    def __init__(self, character):
        super(Noble, self).__init__(character)
        self.name = 'Noble'
        character.cmdset.add(bgpowers.NobleCmdSet, permanent=True)
        for key, kwargs in NOBLE_SKILLS.iteritems():
            character.skills.add(key, **kwargs)


class Nomad(Background):
    def __init__(self, character):
        super(Nomad, self).__init__(character)
        self.name = "Nomad"
        character.cmdset.add(bgpowers.NomadCmdSet, permanent=True)
        for key, kwargs in NOMAD_SKILLS.iteritems():
            character.skills.add(key, **kwargs)


class Gypsy(Background):
    def __init__(self, character):
        super(Gypsy, self). __init__(character)
        self.name = 'Gypsy'
        character.cmdset.add(bgpowers.GpysyCmdSet, permanent=True)
        for key, kwargs in GYPSY_SKILLS.iteritems():
            character.skills.add(key, **kwargs)


class Farmer(Background):
    def __init__(self, character):
        super(Farmer, self). __init__(character)
        self.name = 'Farmer'
        character.cmdset.add(bgpowers.FarmerCmdSet, permanent=True)
        for key, kwargs in FARMER_SKILLS.iteritems():
            character.skills.add(key, **kwargs)


class Tradesman(Background):
    def __init__(self, character):
        super(Tradesman, self). __init__(character)
        self.name = 'Tradesman'
        character.cmdset.add(bgpowers.TradesmanCmdSet, permanent=True)
        for key, kwargs in TRADESMAN_SKILLS.iteritems():
            character.skills.add(key, **kwargs)