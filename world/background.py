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

class CmdBackground(Command):
    """
    command for setting the background on the character
    takes one arg in the form of the background name
    
    args:
    
    
    Usage:
       select <background>
    """

    key = "choose"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower
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


def load_background(background):
    """Returns an instance of the named background class.
    Args:
        background (str): case-insensitive name of background to load
    Returns:
        (Background): instance of the appropriate subclass of `Background`
    """

    background = background.capitalize()

    if background in ALL_BACKGROUNDS:
        return globals()[background]()
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
    def __init__(self):
        self.name = ""
        for key, kwargs in skills.iteritems():
            self.skills.add(key, **kwargs)


class Urchin(Background):
    skills = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'FOC': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Focus'},}

    def __init__(self):
        super(Urchin, self).__init__()
        self.name = "Urchin"
        self.cmdset.add(bgpowers.CmdSetUrchin, permanent=True)


class Noble(Background):
    skills = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'LEA': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Leadership'},}

    def __init__(self):
        super(Noble, self).__init__()
        self.name = 'Noble'
        self.cmdset.add(bgpowers.CmdSetNoble, permanent=True)


class Nomad(Background):
    skills = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'MAR': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Martial'},}

    def __init__(self):
        super(Nomad, self).__init__()
        self.name = "Nomad"
        self.cmdset.add(bgpowers.CmdSetNomad, permanent=True)


class Gypsy(Background):
    skills = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'DOD': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Dodge'},}

    def __init__(self):
        super(Gypsy, self). __init__()
        self.name = 'Gypsy'
        self.cmdset.add(bgpowers.CmdSetGpysy, permanent=True)


class Farmer(Background):
    skills = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'ORG': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Organize'},}

    def __init__(self):
        super(Farmer, self). __init__()
        self.name = 'Farmer'
        self.cmdset.add(bgpowers.CmdSetFarmer, permanent=True)


class Tradesman(Background):
    skills = {'ATT': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Attack'},
              'DEF': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Defense'},
              'FOR': {'type': 'static', 'base': 1, 'mod': 0, 'name': 'Forge'},}

    def __init__(self):
        super(Tradesman, self). __init__()
        self.name = 'Tradesman'
        self.cmdset.add(bgpowers.CmdSetTradesman, permanent=True)