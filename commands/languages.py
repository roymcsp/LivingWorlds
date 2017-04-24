class CmdSay(COMMAND_DEFAULT_CLASS):
    """
    speak as your racial language

    Usage:
      say <message>

    Talk to those in your current location.
    """

    key = "say"
    aliases = ['"', "'"]
    locks = "cmd:all()"

    def func(self):
        """Run the say command"""

        caller = self.caller

        if not self.args:
            caller.msg("Say what?")
            return

        speech = self.args

        # calling the speech hook on the location
        speech = caller.location.at_say(caller, speech)

        # Feedback for the object doing the talking.
        caller.msg('You say, "%s|n"' % speech)

        # Build the string to emit to neighbors.
        emit_string = '%s says, "%s|n"' % (caller.name, speech)
        caller.location.msg_contents(text=(emit_string, {"type": "say"}),
                                     exclude=caller, from_obj=caller)

class CmdWhisper(COMMAND_DEFAULT_CLASS):
    """
    Speak privately as your character to another

    Usage:
      whisper <player> = <message>

    Talk privately to those in your current location, without
    others being informed.
    """

    key = "whisper"
    locks = "cmd:all()"

    def func(self):
        """Run the whisper command"""

        caller = self.caller

        if not self.lhs or not self.rhs:
            caller.msg("Usage: whisper <player> = <message>")
            return

        receiver = caller.search(self.lhs)

        if not receiver:
            return

        if caller == receiver:
            caller.msg("You can't whisper to yourself.")
            return

        speech = self.rhs

        # Feedback for the object doing the talking.
        caller.msg('You whisper to %s, "%s|n"' % (receiver.key, speech))

        # Build the string to emit to receiver.
        emit_string = '%s whispers, "%s|n"' % (caller.name, speech)
        receiver.msg(text=(emit_string, {"type": "whisper"}), from_obj=caller)

class CmdCommon(Command):
    """
     speak in the common tongue only people who know the language can understand it

     Usages:
       common <message> 
       common <target> <message>

     Talk to those in your current location.
     """
    key = "common"
    locks = "cmd:all()"

    def func(self):
        """run the common command"""

        caller = self.caller

        if not self.args:
            caller.msg("Say what in common?")
            return

        speech = self.

        # calling the speech hook on the location
        speech = caller.location.at_say(caller, speech)

        # Feedback for the object doing the talking.
        caller.msg('You say, "%s|n"' % speech)

        # Build the string to emit to neighbors.
        emit_string = '%s says, "%s|n"' % (caller.name, speech)
        caller.location.msg_contents(text=(emit_string, {"type": "say"}),
                                     exclude=caller, from_obj=caller)

        receiver = caller.search(self.lhs)
