# -------------------------------------------------------------
#
# Readable - an object that can be "read"
#
# -------------------------------------------------------------

#
# Read command
#
from objects import Object
from evennia import Command, CmdSet

class CmdRead(Command):
    """
    Usage:
      read [obj]

    Read some text of a readable object.
    """

    key = "read"
    locks = "cmd:all()"
    help_category = "TutorialWorld"

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

class Readable(Object):
    """
    This simple object defines some attributes and
    """
    def at_object_creation(self):
        """
        Called when object is created. We make sure to set the needed
        Attribute and add the readable cmdset.
        """
        super(Readable, self).at_object_creation()
        self.db.readable_text = "There is no text written on %s." % self.key
        # define a command on the object.
        