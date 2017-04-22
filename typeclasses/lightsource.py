# -------------------------------------------------------------
#
# LightSource
#
# This object emits light. Once it has been turned on it
# cannot be turned off. When it burns out it will delete
# itself.
#
# This could be implemented using a single-repeat Script or by
# registering with the TickerHandler. We do it simpler by
# using the delay() utility function. This is very simple
# to use but does not survive a server @reload. Because of
# where the light matters (in the Dark Room where you can
# find new light sources easily), this is okay here.
#
# -------------------------------------------------------------

class CmdLight(Command):
    """
    Creates light where there was none. Something to burn.
    """
    key = "on"
    aliases = ["light", "burn"]
    # only allow this command if command.obj is carried by caller.
    locks = "cmd:holds()"
    help_category = "TutorialWorld"

    def func(self):
        """
        Implements the light command. Since this command is designed
        to sit on a "lightable" object, we operate only on self.obj.
        """

        if self.obj.light():
            self.caller.msg("You light %s." % self.obj.key)
            self.caller.location.msg_contents("%s lights %s!" % (self.caller, self.obj.key), exclude=[self.caller])
        else:
            self.caller.msg("%s is already burning." % self.obj.key)


class CmdSetLight(CmdSet):
    """CmdSet for the lightsource commands"""
    key = "lightsource_cmdset"
    # this is higher than the dark cmdset - important!
    priority = 3

    def at_cmdset_creation(self):
        """called at cmdset creation"""
        self.add(CmdLight())


class LightSource(TutorialObject):
    """
    This implements a light source object.

    When burned out, the object will be deleted.
    """
    def at_init(self):
        """
        If this is called with the Attribute is_giving_light already
        set, we know that the timer got killed by a server
        reload/reboot before it had time to finish. So we kill it here
        instead. This is the price we pay for the simplicity of the
        non-persistent delay() method.
        """
        if self.db.is_giving_light:
            self.delete()

    def at_object_creation(self):
        """Called when object is first created."""
        super(LightSource, self).at_object_creation()
        self.db.tutorial_info = "This object can be lit to create light. It has a timeout for how long it burns."
        self.db.is_giving_light = False
        self.db.burntime = 60 * 3  # 3 minutes
        # this is the default desc, it can of course be customized
        # when created.
        self.db.desc = "A splinter of wood with remnants of resin on it, enough for burning."
        # add the Light command
        self.cmdset.add_default(CmdSetLight, permanent=True)

    def _burnout(self):
        """
        This is called when this light source burns out. We make no
        use of the return value.
        """
        # delete ourselves from the database
        self.db.is_giving_light = False
        try:
            self.location.location.msg_contents("%s's %s flickers and dies." %
                                                (self.location, self.key), exclude=self.location)
            self.location.msg("Your %s flickers and dies." % self.key)
            self.location.location.check_light_state()
        except AttributeError:
            try:
                self.location.msg_contents("A %s on the floor flickers and dies." % self.key)
                self.location.location.check_light_state()
            except AttributeError:
                # Mainly happens if we happen to be in a None location
                pass
        self.delete()

    def light(self):
        """
        Light this object - this is called by Light command.
        """
        if self.db.is_giving_light:
            return False
        # burn for 3 minutes before calling _burnout
        self.db.is_giving_light = True
        # if we are in a dark room, trigger its light check
        try:
            self.location.location.check_light_state()
        except AttributeError:
            try:
                # maybe we are directly in the room
                self.location.check_light_state()
            except AttributeError:
                # we are in a None location
                pass
        finally:
            # start the burn timer. When it runs out, self._burnout
            # will be called. We store the deferred so it can be
            # killed in unittesting.
            self.deferred = utils.delay(60 * 3, self._burnout)
        return True