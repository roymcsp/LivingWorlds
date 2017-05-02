from evennia import default_cmds, CmdSet

class CmdExitError(default_cmds.MuxCommand):
    """Parent class for all exit errors."""
    locks = "cmd:all()"
    arg_regex = r"\s|$"
    auto_help = False
    def func(self):
        """returns the error"""
        self.caller.msg("You cannot move %s." % self.key)

class CmdNationExitError(default_cmds.MuxCommand):
    """Parent class for all exit errors."""
    locks = "cmd:all()"
    arg_regex = r"\s|$"
    auto_help = False
    def func(self):
        """returns the error"""
        self.caller.msg("You must first agree to the rules before travelling on.")
     
class CmdExitErrorNorth(CmdExitError):
    key = "north"
    aliases = ["n"]
    
class CmdExitErrorEast(CmdExitError):
    key = "east"
    aliases = ["e"]
    
class CmdExitErrorSouth(CmdExitError):
    key = "south"
    aliases = ["s"]
    
class CmdExitErrorWest(CmdExitError):
    key = "west"
    aliases = ["w"]

class CmdExitErrorNortheast(CmdExitError):
    key = "northeast"
    aliases = ["ne"]
    
class CmdExitErrorNorthwest(CmdExitError):
    key = "northwest"
    aliases = ["nw"]
    
class CmdExitErrorSoutheast(CmdExitError):
    key = "southeast"
    aliases = ["se"]
    
class CmdExitErrorSouthwest(CmdExitError):
    key = "southwest"
    aliases = ["sw"]
    
class CmdExitErrorUp(CmdExitError):
    key = "up"
    aliases = ["u"]
    
class CmdExitErrorDown(CmdExitError):
    key = "down"
    aliases = ["d"]

class CmdExitErrorIn(CmdExitError):
    key = "in"


class CmdExitErrorOut(CmdExitError):
    key = "out"


class ExitErrorCmdSet(CmdSet):

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
