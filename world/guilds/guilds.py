"""
Primary module for guilds within Mercadia
"""

from world.rulebook import roll_max
from evennia.utils import fill
from evennia import Command

# Melee Type Bases
F_BAB = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
         16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

F_FSAVE = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
           10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17]

F_RSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

F_WSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

# Devine Caster Type Bases
C_BAB = [0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18]

C_FSAVE = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
           10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17]

C_RSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

C_WSAVE = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
           10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17]

# Agile Type Bases
R_BAB = [0, 0, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 18, 19, 20, 21, 21, 22]

R_FSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

R_RSAVE = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
           10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17]

R_WSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

# Trades Type Bases
T_BAB = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]

T_FSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

T_RSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

T_WSAVE = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
           10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17]

# Arcane Caster Type Bases
M_BAB = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15]

M_FSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

M_RSAVE = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4,
           5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10]

M_WSAVE = [0, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9,
           10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17]

# General Type Bases
G_BAB = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

G_FSAVE = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]

G_RSAVE = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]

G_WSAVE = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]


class CmdGuildJoin(Command):
    """This is the command string that will assign a background onto a character,
     and the cooresponding command set."""

    key = "join"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower

        apply_guild(caller, args)


class GuildException(Exception):
    """Base exception class for races module."""

    def __init__(self, msg):
        self.msg = msg


def load_guild(guild):
    """Returns an instance of the named race class.
    Args:
        guild(str): case-insensitive name of background to load
    Returns:
        (guild): instance of the appropriate subclass of `Guild`
    """

    guild = guild.strip().capitalize()

    if guild in all_guilds:
        return globals()[guild]()
    else:
        raise GuildException("Invalid guild specified.")


def apply_guild(character, guild):
    """Causes a Character to "have" a named guild.
    Args: 
        character: the character object having a background
        guild (str, guild): the name of the background to apply
    """
    if isinstance(guild, Guild):
        guild = guild.name

    guild = load_guild(guild)

    character.db.guild = guild.name
    character.message('You join the {} guild.' .format(guild.name))


class Guild(object):
    """Base guild class containing default values for all traits."""
    def __init__(self):
        self.name = None
        self.skills = {}
        self.health_roll = None


class Peon(Guild):
    def __init__(self):
        super(Peon, self).__init__()
        self.name = 'Peon'
        self.skills = {}
        self.health_roll = '1d4'


class Peasant(Guild):
    def __init__(self):
        super(Peasant, self).__init__()
        self.name = 'Peasant'
        self.skills = {}
        self.health_roll = '1d4'


class Slave(Guild):
    def __init__(self):
        super(Slave, self).__init__()
        self.name = 'Slave'
        self.skills = {}
        self.health_roll = '1d4'


class Servant(Guild):
    def __init__(self):
        super(Servant, self).__init__()
        self.name = 'Servant'
        self.skills = {}
        self.health_roll = '1d4'


class Conscript(Guild):
    def __init__(self):
        super(Conscript, self).__init__()
        self.name = 'Conscript'
        self.skills = {}
        self.health_roll = '1d4'


class Commoner(Guild):
    def __init__(self):
        super(Commoner, self).__init__()
        self.name = 'Commoner'
        self.skills = {}
        self.health_roll = '1d4'


# Universal Guilds
class Cleric(Guild):
    def __init__(self):
        super(Cleric, self).__init__()
        self.name = 'Cleric'
        self.skills = {}
        self.health_roll = '1d10'


class Paladin(Guild):
    def __init__(self):
        super(Paladin, self).__init__()
        self.name = 'Paladin'
        self.skills = {}
        self.health_roll = '1d10'


# Kingdom Guilds
class Fighter(Guild):
    def __init__(self):
        super(Fighter, self).__init__()
        self.name = 'Fighter'
        self.skills = {}
        self.health_roll = '1d12'


class Mage(Guild):
    def __init__(self):
        super(Mage, self).__init__()
        self.name = 'Mage'
        self.skills = {}
        self.health_roll = '1d6'


class Merchant(Guild):
    def __init__(self):
        super(Merchant, self).__init__()
        self.name = 'Merchant'
        self.skills = {}
        self.health_roll = '1d6'


class Rogue(Guild):
    def __init__(self):
        super(Rogue, self).__init__()
        self.name = 'Rogue'
        self.skills = {}
        self.health_roll = '1d8'


# Caliphate Guilds
class Warrior(Guild):
    def __init__(self):
        super(Warrior, self).__init__()
        self.name = 'Warrior'
        self.skills = {}
        self.health_roll = '1d12'


class Sorcerer(Guild):
    def __init__(self):
        super(Sorcerer, self).__init__()
        self.name = 'Sorcerer'
        self.skills = {}
        self.health_roll = '1d6'


class Trader(Guild):
    def __init__(self):
        super(Trader, self).__init__()
        self.name = 'Trader'
        self.skills = {}
        self.health_roll = '1d6'


class Scout(Guild):
    def __init__(self):
        super(Scout, self).__init__()
        self.name = 'Scout'
        self.skills = {}
        self.health_roll = '1d8'


# Empire Guilds
class Samurai(Guild):
    def __init__(self):
        super(Samurai, self).__init__()
        self.name = 'Samurai'
        self.skills = {}
        self.health_roll = '1d12'


class Shaman(Guild):
    def __init__(self):
        super(Shaman, self).__init__()
        self.name = 'Shaman'
        self.skills = {}
        self.health_roll = '1d6'


class Artisan(Guild):
    def __init__(self):
        super(Artisan, self).__init__()
        self.name = 'Artisan'
        self.skills = {}
        self.health_roll = '1d6'


class Monk(Guild):
    def __init__(self):
        super(Monk, self).__init__()
        self.name = 'Monk'
        self.skills = {}
        self.health_roll = '1d8'
