from evennia import CmdSet
from commands.command import MuxCommand


class CmdRead(MuxCommand):
    """
    Usage:
      read [obj]

    Read some text of a readable object.
    """

    key = "read"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """
        Implements the read command. This simply looks for an
        Attribute "readable_text" on the object and displays that.
        """

        if self.args:
            obj = self.caller.search(self.args.strip())
        else:
            obj = self.obj
        if not obj:
            return
        # we want an attribute read_text to be defined.
        readtext = obj.db.readable_text
        if readtext:
            string = "You read |C%s|n:\n  %s" % (obj.key, readtext)
        else:
            string = "There is nothing to read on %s." % obj.key
        self.caller.msg(string)
        
"""
 class CmdListen(Command):
"""


class CmdTaste(MuxCommand):
    key = "taste"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """
        Implements the read command. This simply looks for an
        Attribute "readable_text" on the object and displays that.
        """

        if self.args:
            obj = self.caller.search(self.args.strip())
        else:
            obj = self.obj
        if not obj:
            return
        # we want an attribute read_text to be defined.
        tastetext = obj.db.tasteable_text
        if tastetext:
            string = "You taste |C%s|n:\n  %s" % (obj.key, tastetext)
        else:
            string = "There is nothing to taste on %s." % obj.key
        self.caller.msg(string)
        
"""
class CmdSearch(Command):
"""


class CmdFeel(MuxCommand):
    key = "feel"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """
        Implements the read command. This simply looks for an
        Attribute "readable_text" on the object and displays that.
        """

        if self.args:
            obj = self.caller.search(self.args.strip())
        else:
            obj = self.obj
        if not obj:
            return
        # we want an attribute read_text to be defined.
        feeltext = obj.db.feelable_text
        if feeltext:
            string = "You feel |C%s|n:\n  %s" % (obj.key, feeltext)
        else:
            string = "There is nothing to feel on %s." % obj.key
        self.caller.msg(string)


class CmdSmell(MuxCommand):
    key = "smell"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """
        Implements the read command. This simply looks for an
        Attribute "readable_text" on the object and displays that.
        """

        if self.args:
            obj = self.caller.search(self.args.strip())
        else:
            obj = self.obj
        if not obj:
            return
        # we want an attribute read_text to be defined.
        smelltext = obj.db.smellable_text
        if smelltext:
            string = "You smell |C%s|n:\n  %s" % (obj.key, smelltext)
        else:
            string = "There is nothing to smell on %s." % obj.key
        self.caller.msg(string)
        

class SensesCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "General"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdRead())
        self.add(CmdTaste())
        self.add(CmdFeel())
        self.add(CmdSmell())