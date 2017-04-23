from evennia import Command
# from evennia.utils.evmenu import get_input
from evennia import Command as BaseCommand
from evennia.commands import cmdhandler
from evennia.utils import logger
from evennia import Command, CmdSet

_CMD_NOMATCH = cmdhandler.CMD_NOMATCH
_CMD_NOINPUT = cmdhandler.CMD_NOINPUT

class CmdRules(Command):
    """
    Display and agree to rules.
 
    Usage:
      rules
    """
 
    key = "rules"
    locks = "cmd:all()"
    
    def func(self):
        
        get_input(self.caller, "  Have you read the rules and agree to abide by them (Yes/No)?", self.yesno)

        
    def yesno(self, caller, prompt, result):
        if result.lower() in ("y","yes"):
            caller.msg('You agree to the rules and may now continue To the Kingdom, Caliphate or Empire')
            caller.db.rules = True
        if result.lower() in ("n","no"):
            caller.msg('You must read the rules and agree to them before proceeding')
            caller.db.rules = False

class CmdGender(Command):
    """
    Sets gender on yourself

    Usage:
      gender male||female

    """
    key = "gender"
    locks = "cmd:all()"

    def func(self):
        """
        Implements the command.
        """
        caller = self.caller
        arg = self.args.strip().lower()
        if not arg in ("male", "female"):
            caller.msg("Usage: gender male||female")
            return
        caller.db.gender = arg
        caller.msg("Your gender was set to %s." % arg)
        
"""
Commands
 
Commands describe the input the player can do to the game.
 
"""
 
 
_CMD_NOMATCH = cmdhandler.CMD_NOMATCH
_CMD_NOINPUT = cmdhandler.CMD_NOINPUT
 
  
class CmdGetInput(Command):
    """
    Enter your data and press return.
    """
    key = _CMD_NOMATCH
    aliases = _CMD_NOINPUT
 
    def func(self):
        """This is called when user enters anything."""
        caller = self.caller
        try:
            getinput = caller.ndb._getinput
            if not getinput and hasattr(caller, "player"):
                getinput = caller.player.ndb._getinput
                caller = caller.player
            callback = getinput._callback
 
            caller.ndb._getinput._session = self.session
            prompt = caller.ndb._getinput._prompt
            args = caller.ndb._getinput._args
            kwargs = caller.ndb._getinput._kwargs
            result = self.raw_string.strip()  # we strip the ending line break caused by sending
 
            ok = not callback(caller, prompt, result, *args, **kwargs)
            if ok:
                # only clear the state if the callback does not return
                # anything
                del caller.ndb._getinput
                caller.cmdset.remove(InputCmdSet)
        except Exception:
            # make sure to clean up cmdset if something goes wrong
            caller.msg("|rError in get_input. Choice not confirmed (report to admin)|n")
            logger.log_trace("Error in get_input")
            caller.cmdset.remove(InputCmdSet)
 
 
class InputCmdSet(CmdSet):
    """
    This stores the input command
    """
    key = "input_cmdset"
    priority = 1
    mergetype = "Replace"
    no_objs = True
    no_exits = True
    no_channels = False
 
    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdGetInput())
 
 
class _Prompt(object):
    """Dummy holder"""
    pass
 
 
def get_input(caller, prompt, callback, session=None, *args, **kwargs):
    """
    This is a helper function for easily request input from
    the caller.
 
    Args:
        caller (Player or Object): The entity being asked
            the question. This should usually be an object
            controlled by a user.
        prompt (str): This text will be shown to the user,
            in order to let them know their input is needed.
        callback (callable): A function that will be called
            when the user enters a reply. It must take three
            arguments: the `caller`, the `prompt` text and the
            `result` of the input given by the user. If the
            callback doesn't return anything or return False,
            the input prompt will be cleaned up and exited. If
            returning True, the prompt will remain and continue to
            accept input.
        session (Session, optional): This allows to specify the
            session to send the prompt to. It's usually only
            needed if `caller` is a Player in multisession modes
            greater than 2. The session is then updated by the
            command and is available (for example in callbacks)
            through `caller.ndb.getinput._session`.
 
    Raises:
        RuntimeError: If the given callback is not callable.
 
    Notes:
        The result value sent to the callback is raw and not
        processed in any way. This means that you will get
        the ending line return character from most types of
        client inputs. So make sure to strip that before
        doing a comparison.
 
        When the prompt is running, a temporary object
        `caller.ndb._getinput` is stored; this will be removed
        when the prompt finishes.
        If you need the specific Session of the caller (which
        may not be easy to get if caller is a player in higher
        multisession modes), then it is available in the
        callback through `caller.ndb._getinput._session`.
 
    """
    if not callable(callback):
        raise RuntimeError("get_input: input callback is not callable.")
    caller.ndb._getinput = _Prompt()
    caller.ndb._getinput._callback = callback
    caller.ndb._getinput._prompt = prompt
    caller.ndb._getinput._session = session
    caller.ndb._getinput._args = args
    caller.ndb._getinput._kwargs = kwargs
    caller.cmdset.add(InputCmdSet)
    caller.msg(prompt, session=session)