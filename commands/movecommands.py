from evennia import default_cmds

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

class CmdExitErrorKingdom(CmdNationExitError):
    key = "kingdom"
    aliases = ["k"]
    
class CmdExitErrorCaliphate(CmdNationExitError):
    key = "caliphate"
    aliases = ["c"]
    
class CmdExitErrorEmpire(CmdNationExitError):
    key = "empire"
    aliases = ["e"]