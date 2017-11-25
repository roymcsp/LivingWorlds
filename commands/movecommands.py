from evennia import CmdSet
from commands.command import MuxCommand


class CmdExitError(MuxCommand):
    """Parent class for all exit errors."""
    locks = "cmd:all()"
    arg_regex = r"\s|$"
    auto_help = False

    def func(self):
        """returns the error"""
        self.caller.msg("You cannot move %s." % self.key)


class CmdNationExitError(MuxCommand):
    """Parent class for all exit errors."""
    locks = "cmd:all()"
    arg_regex = r"\s|$"
    auto_help = False

    def func(self):
        """returns the error"""
        self.caller.msg("You must first agree to the rules before travelling on.")


class CmdExitErrorNorth(CmdExitError, MuxCommand):
    key = "north"
    aliases = ["n"]


class CmdExitErrorEast(CmdExitError, MuxCommand):
    key = "east"
    aliases = ["e"]


class CmdExitErrorSouth(CmdExitError, MuxCommand):
    key = "south"
    aliases = ["s"]


class CmdExitErrorWest(CmdExitError, MuxCommand):
    key = "west"
    aliases = ["w"]


class CmdExitErrorNortheast(CmdExitError, MuxCommand):
    key = "northeast"
    aliases = ["ne"]


class CmdExitErrorNorthwest(CmdExitError, MuxCommand):
    key = "northwest"
    aliases = ["nw"]


class CmdExitErrorSoutheast(CmdExitError, MuxCommand):
    key = "southeast"
    aliases = ["se"]


class CmdExitErrorSouthwest(CmdExitError, MuxCommand):
    key = "southwest"
    aliases = ["sw"]


class CmdExitErrorUp(CmdExitError, MuxCommand):
    key = "up"
    aliases = ["u"]


class CmdExitErrorDown(CmdExitError, MuxCommand):
    key = "down"
    aliases = ["d"]


class CmdExitErrorIn(CmdExitError, MuxCommand):
    key = "in"


class CmdExitErrorOut(CmdExitError, MuxCommand):
    key = "out"


class ExitErrorCmdSet(CmdSet,):

    def at_cmdset_creation(self):
        self.add(CmdExitErrorNorth())
        self.add(CmdExitErrorEast())
        self.add(CmdExitErrorSouth())
        self.add(CmdExitErrorWest())
        self.add(CmdExitErrorNortheast())
        self.add(CmdExitErrorNorthwest())
        self.add(CmdExitErrorSoutheast())
        self.add(CmdExitErrorSouthwest())
        self.add(CmdExitErrorUp())
        self.add(CmdExitErrorDown())
        self.add(CmdExitErrorIn())
        self.add(CmdExitErrorOut())
