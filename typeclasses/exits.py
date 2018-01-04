"""
Exits

Exits are connectors between Rooms. An exit always has a destination property
set and has a single command defined on itself with the same name as its key,
for allowing Characters to traverse the exit to its destination.

"""
from evennia.server.sessionhandler import SESSIONS
from evennia import DefaultExit
from evennia.utils.utils import pad

class Exit(DefaultExit):
    """
    Exits are connectors between rooms. Exits are normal Objects except
    they defines the `destination` property. It also does work in the
    following methods:

     basetype_setup() - sets default exit locks (to change, use `at_object_creation` instead).
     at_cmdset_get(**kwargs) - this is called when the cmdset is accessed and should
                              rebuild the Exit cmdset along with a command matching the name
                              of the Exit object. Conventionally, a kwarg `force_init`
                              should force a rebuild of the cmdset, this is triggered
                              by the `@alias` command when aliases are changed.
     at_failed_traverse() - gives a default error message ("You cannot
                            go there") if exit traversal fails and an
                            attribute `err_traverse` is not defined.

    Relevant hooks to overload (compared to other types of Objects):
        at_traverse(traveller, target_loc) - called to do the actual traversal and calling of the other hooks.
                                            If overloading this, consider using super() to use the default
                                            movement implementation (and hook-calling).
        at_after_traverse(traveller, source_loc) - called by at_traverse just after traversing.
        at_failed_traverse(traveller) - called by at_traverse if traversal failed for some reason. Will
                                        not be called if the attribute `err_traverse` is
                                        defined, in which case that will simply be echoed.
    """
    def at_traverse(self, traversing_object, target_location):
        """
        Implements the actual traversal, using utils.delay to delay the move_to.
        """
        move_delay = self.destination.mv_delay
        move_cost = self.destination.mv_cost

        # make sure the character isn't already moving

        if traversing_object.nattributes.has('currently_moving'):
            traversing_object.msg("You are aleady moving. Use the 'stop' "
                                  "command and try again to change "
                                  "destinations.")
            return

        # check the movement cost

        if (hasattr(traversing_object, 'traits') and
                'EP' in traversing_object.traits.all):
            if traversing_object.traits.EP.actual < move_cost:
                traversing_object.msg('Moving so far so fast has worn you out. '
                                      'You pause for a moment to gather your '
                                      'composure.')
                return

        # then handle the move with the appropriate delay

        def move_callback():
            "This callback will be called by utils.delay after move_delay seconds."
            source_location = traversing_object.location
            if traversing_object.move_to(target_location):
                # deduct MV cost for the move
                if (hasattr(traversing_object, 'traits') and
                        'EP' in traversing_object.traits.all):
                    traversing_object.traits.EP.current -= move_cost

                self.at_after_traverse(traversing_object, source_location)
            else:
                if self.db.err_traverse:
                    # if exit has a better error message, let's use it.
                    self.caller.msg(self.db.err_traverse)
                else:
                    # No shorthand error message. Call hook.
                    self.at_failed_traverse(traversing_object)
            # clean up the 'currently_moving' ndb attribute
            if traversing_object.nattributes.has('currently_moving'):
                del traversing_object.ndb.currently_moving

        if move_delay > 0:
            start_msg = self.destination.db.msg_start_move or "You start moving {exit}."
            traversing_object.msg(start_msg.format(exit=self.key))
            # create a delayed movement
            deferred = utils.delay(move_delay, callback=move_callback)
            # we store the deferred on the character, this will allow us
            # to abort the movement. We must use an ndb here since
            # deferreds cannot be pickled.
            traversing_object.ndb.currently_moving = deferred
        else:
            # delay is 0, so we just run the callback now
            move_callback()


class NationExit(DefaultExit):
    
    """ an exit that applies something to the traverser after traversing """
    def at_after_traverse(self,traverser,source_location):
        traverser.db.nation = str(self.db.nation)

        if traverser.db.nation == "Kingdom":
            message = "|/             |555************[|315WORLD CRIER|555]**************|n|/|/" \
                      "                      %s joins the game|/" \
                      "               |035Starting in the Kingdom of Iusticia|/|/ " \
                      "             |555***************************************|/" % (traverser)
            SESSIONS.announce_all(message)

        if traverser.db.nation == "Caliphate":
            message = "|/             |555************[|315WORLD CRIER|555]**************|n|/|/" \
                      "                      %s joins the game|/" \
                      "               |500Starting in the Caliphate of Ashran|/|/" \
                      "             |555***************************************|/" % (traverser)
            SESSIONS.announce_all(message)

        if traverser.db.nation == "Empire":
            message = "             |555************[|315WORLD CRIER|555]**************|n|/|/" \
                      "                    %s joins the game|/" \
                      "                |030Starting in the Empire of Kosun|/|/" \
                      "              |555***************************************|/" % (traverser)
            SESSIONS.announce_all(message)
