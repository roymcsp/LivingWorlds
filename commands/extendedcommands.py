from evennia import default_cmds, utils
from evennia import gametime

class CmdExtendedLook(default_cmds.CmdLook):
    """
    look

    Usage:
      look
      look <obj>
      look <room detail>
      look *<account>

    Observes your location, details at your location or objects in your vicinity.
    """
    def func(self):
        """
        Handle the looking - add fallback to details.
        """
        caller = self.caller
        args = self.args
        if args:
            looking_at_obj = caller.search(args,
                                           candidates=caller.location.contents + caller.contents,
                                           use_nicks=True,
                                           quiet=True)
            if not looking_at_obj:
                # no object found. Check if there is a matching
                # detail at location.
                location = caller.location
                if location and hasattr(location, "return_detail") and callable(location.return_detail):
                    detail = location.return_detail(args)
                    if detail:
                        # we found a detail instead. Show that.
                        caller.msg(detail)
                        return
                # no detail found. Trigger delayed error messages
                _AT_SEARCH_RESULT(looking_at_obj, caller, args, quiet=False)
                return
            else:
                # we need to extract the match manually.
                looking_at_obj = utils.make_iter(looking_at_obj)[0]
        else:
            looking_at_obj = caller.location
            if not looking_at_obj:
                caller.msg("You have no location to look at!")
                return

        if not hasattr(looking_at_obj, 'return_appearance'):
            # this is likely due to us having an account instead
            looking_at_obj = looking_at_obj.character
        if not looking_at_obj.access(caller, "view"):
            caller.msg("Could not find '%s'." % args)
            return
        # get object's appearance
        caller.msg(looking_at_obj.return_appearance(caller))
        # the object's at_desc() method.
        looking_at_obj.at_desc(looker=caller)


# Custom build commands for setting seasonal descriptions
# and detailing extended rooms.

class CmdExtendedDesc(default_cmds.CmdDesc):
    """
    `@desc` - describe an object or room.

    Usage:
      @desc[/switch] [<obj> =] <description>
      @detail[/del] [<key> = <description>]


    Switches for `@desc`:
      spring  - set description for <season> in current room.
      summer
      autumn
      winter

    Switch for `@detail`:
      del   - delete a named detail.

    Sets the "desc" attribute on an object. If an object is not given,
    describe the current room.

    The alias `@detail` allows to assign a "detail" (a non-object
    target for the `look` command) to the current room (only).

    You can also embed special time markers in your room description, like this:

        ```
        <night>In the darkness, the forest looks foreboding.</night>.
        ```

    Text marked this way will only display when the server is truly at the given
    timeslot. The available times are night, morning, afternoon and evening.

    Note that `@detail`, seasons and time-of-day slots only work on rooms in this
    version of the `@desc` command.

    """
    aliases = ["@describe", "@detail"]

    def reset_times(self, obj):
        """By deleteting the caches we force a re-load."""
        obj.ndb.last_season = None
        obj.ndb.last_timeslot = None

    def func(self):
        """Define extended command"""
        caller = self.caller
        location = caller.location
        if self.cmdstring == '@detail':
            # switch to detailing mode. This operates only on current location
            if not location:
                caller.msg("No location to detail!")
                return
            if location.db.details is None:
                caller.msg("|rThis location does not support details.|n")
                return
            if self.switches and self.switches[0] in 'del':
                # removing a detail.
                if self.lhs in location.db.details:
                    del location.db.details[self.lhs]
                caller.msg("Detail %s deleted, if it existed." % self.lhs)
                self.reset_times(location)
                return
            if not self.args:
                # No args given. Return all details on location
                string = "|wDetails on %s|n:" % location
                details = "\n".join(" |w%s|n: %s"
                                    % (key, utils.crop(text)) for key, text in location.db.details.items())
                caller.msg("%s\n%s" % (string, details) if details else "%s None." % string)
                return
            if not self.rhs:
                # no '=' used - list content of given detail
                if self.args in location.db.details:
                    string = "|wDetail '%s' on %s:\n|n" % (self.args, location)
                    string += str(location.db.details[self.args])
                    caller.msg(string)
                else:
                    caller.msg("Detail '%s' not found." % self.args)
                return
            # setting a detail
            location.db.details[self.lhs] = self.rhs
            caller.msg("Set Detail %s to '%s'." % (self.lhs, self.rhs))
            self.reset_times(location)
            return
        else:
            # we are doing a @desc call
            if not self.args:
                if location:
                    string = "|wDescriptions on %s|n:\n" % location.key
                    string += " |wspring:|n %s\n" % location.db.spring_desc
                    string += " |wsummer:|n %s\n" % location.db.summer_desc
                    string += " |wautumn:|n %s\n" % location.db.autumn_desc
                    string += " |wwinter:|n %s\n" % location.db.winter_desc
                    string += " |wgeneral:|n %s" % location.db.general_desc
                    caller.msg(string)
                    return
            if self.switches and self.switches[0] in ("spring", "summer", "autumn", "winter"):
                # a seasonal switch was given
                if self.rhs:
                    caller.msg("Seasonal descs only works with rooms, not objects.")
                    return
                switch = self.switches[0]
                if not location:
                    caller.msg("No location was found!")
                    return
                if switch == 'spring':
                    location.db.spring_desc = self.args
                elif switch == 'summer':
                    location.db.summer_desc = self.args
                elif switch == 'autumn':
                    location.db.autumn_desc = self.args
                elif switch == 'winter':
                    location.db.winter_desc = self.args
                # clear flag to force an update
                self.reset_times(location)
                caller.msg("Seasonal description was set on %s." % location.key)
            else:
                # No seasonal desc set, maybe this is not an extended room
                if self.rhs:
                    text = self.rhs
                    obj = caller.search(self.lhs)
                    if not obj:
                        return
                else:
                    text = self.args
                    obj = location
                obj.db.desc = text  # a compatibility fallback
                if obj.attributes.has("general_desc"):
                    obj.db.general_desc = text
                    self.reset_times(obj)
                    caller.msg("General description was set on %s." % obj.key)
                else:
                    # this is not an ExtendedRoom.
                    caller.msg("The description was set on %s." % obj.key)


# Simple command to view the current time and season

class CmdGameTime(default_cmds.MuxCommand):
    """
    Check the game time

    Usage:
        time

    Shows the current in-game time and season.
    """
    key = "time"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """Reads time info from current room"""
        time = gametime.gametime(absolute = True)
        location = self.caller.location
        if not location or not hasattr(location, "get_time_and_season"):
            self.caller.msg("No location available - you are outside time.")
        else:
            season, timeslot = location.get_time_and_season()
            prep = "a"
            if season == "autumn":
                prep = "an"
                self.caller.msg("It's %s %s day, in the %s. The time is %s:%s on %s, %s, %s"% (prep, season, timeslot,
                                hour, minute, month, day, year))
