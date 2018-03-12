# -------------------------------------------------------------
#
# Readable - an object that can be "read"
#
# -------------------------------------------------------------

#
# Read command
#
from objects import Object
from commands.command import MuxCommand


class CmdRead(MuxCommand):
    """
    Usage:
      read [obj]

    Read some text of a readable object.
    """

    key = "read"
    locks = "cmd:all()"
    help_category = "Senses"

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
        read_text = obj.db.readable_text
        if read_text:
            string = "You read the |C%s|n:\n  %s" % (obj.key, read_text)
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
        Attribute.
        """
        super(Readable, self).at_object_creation()
        self.db.readable_text = "There is no text written on the %s." % self.key
        # define a command on the object.
