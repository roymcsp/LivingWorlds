import datetime
from evennia import gametime
from evennia import default_cmds, utils
from commands.command import MuxCommand
from evennia.server.sessionhandler import SESSIONS


class CmdExtendedLook(default_cmds.CmdLook, MuxCommand):
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

    def at_post_cmd(self):
        """
        This hook is called after the command has finished executing
        (after self.func()).
        """
        "called after self.func()."
        caller = self.caller
        prompt = ">"
        caller.msg("", prompt=prompt)


# Custom build commands for setting seasonal descriptions
# and detailing extended rooms.

class CmdExtendedDesc(default_cmds.CmdDesc, MuxCommand):
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

    def at_post_cmd(self):
        """
        This hook is called after the command has finished executing
        (after self.func()).
        """
        "called after self.func()."
        caller = self.caller
        prompt = ">"
        caller.msg("", prompt=prompt)

# Simple command to view the current time and season


class CmdGameTime(MuxCommand):
    """
    Check the current time

    Usage:
        season

    Shows the current in-game time.
    """

    key = "time"
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        """Reads time info from current room"""
        location = self.caller.location
        if not location or not hasattr(location, "get_time_and_season"):
            self.caller.msg("No location available - you are outside time.")
        else:
            season, timeslot = location.get_time_and_season()
            prep = "a"
            if season == "autumn":
                prep = "an"
                self.caller.msg(datetime.datetime.now().strftime("*** The time is currently %a %b %d %H:%M:%S %Y"))
                self.caller.msg("*** It is %s %s Day in the %s***" % (prep, season, timeslot,))


class CmdExtendedGet(default_cmds.CmdGet):
    """
   pick up something
   Usage:
     get <obj>
   Picks up an object from your location and puts it in
   your inventory.
   """
    key = "get"
    aliases = "grab"
    locks = "cmd:all()"

    def func(self):
        """implements the command."""

        caller = self.caller

        if not self.args:
            caller.msg("Get what?")
            return
        result = caller.search(self.args,
                               location=caller.location,
                               quiet=True)
        if not result:
            caller.msg("{} not found".format(self.args))
            return
        else:
            obj = result[0]
        if caller == obj:
            caller.msg("You can't get yourself.")
            return
        if not obj.access(caller, 'get'):
            if obj.db.get_err_msg:
                caller.msg(obj.db.get_err_msg)
            else:
                caller.msg("You can't get that.")
            return

        obj.move_to(caller, quiet=True)
        caller.msg("You pick up %s." % obj.name)
        caller.location.msg_contents("%s picks up %s." %
                                     (caller.name,
                                      obj.name),
                                     exclude=caller)
        # calling hook method
        obj.at_get(caller)

    def at_post_cmd(self):
        """
        This hook is called after the command has finished executing
        (after self.func()).
        """
        "called after self.func()."
        caller = self.caller
        prompt = ">"
        caller.msg("", prompt=prompt)


class CmdExtendedDrop(default_cmds.CmdDrop, MuxCommand):
    """
    drop something

    Usage:
      drop <obj>

    Lets you drop an object from your inventory into the
    location you are currently in.
    """

    key = "drop"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def func(self):
        """Implement command"""

        caller = self.caller

        if not self.args:
            caller.msg("Drop what?")
            return

        # Because the DROP command by definition looks for items
        # in inventory, call the search function using location = caller
        result = caller.search(self.args, location=caller, nofound_string="You aren't carrying %s." % self.args,
                               quiet=True)
        if not result:
            return
        else:
            obj = result[0]

        obj.move_to(caller.location, quiet=True)
        caller.msg("You drop %s." % (obj.name,))
        caller.location.msg_contents("%s drops %s." %
                                     (caller.name, obj.name),
                                     exclude=caller)
        # Call the object script's at_drop() method.
        obj.at_drop(caller)

    def at_post_cmd(self):
        """
        This hook is called after the command has finished executing
        (after self.func()).
        """
        "called after self.func()."
        caller = self.caller
        prompt = ">"
        caller.msg("", prompt=prompt)


class CmdExtendedGive(default_cmds.CmdGive, MuxCommand):
    """
    give away something to someone

    Usage:
      give <inventory obj> to <target>

    Gives an items from your inventory to another character,
    placing it in their inventory.
    """
    key = "give"
    locks = "cmd:all()"
    arg_regex = r"\s|$"

    def parse(self):
        """Implement an addition parse"""
        super(CmdExtendedGive, self).parse()
        if "to" in self.args:
            self.lhs, self.rhs = self.args.split(" to ", 1)

    def func(self):
        """Implement give"""

        caller = self.caller
        if not self.args or not self.rhs:
            caller.msg("Usage: give <item> to <target>")
            return
        to_give = caller.search(self.lhs, location=caller,
                                nofound_string="You aren't carrying %s." % self.lhs, quiet=True)
        target = caller.search(self.rhs)
        if not (to_give and target):
            return
        else:
            obj = to_give[0]
        if target == caller:
            caller.msg("You keep %s to yourself." % obj.key)
            return
        if not to_give.location == caller:
            caller.msg("You are not holding %s." % obj.key)
            return
        # give object
        caller.msg("You give %s to %s." % (obj.key, target.key))
        obj.move_to(target, quiet=True)
        target.msg("%s gives you %s." % (caller.key, obj.key))
        # Call the object script's at_give() method.
        obj.at_give(caller, target)

    def at_post_cmd(self):
        """
        This hook is called after the command has finished executing
        (after self.func()).
        """
        "called after self.func()."
        caller = self.caller
        prompt = ">"
        caller.msg("", prompt=prompt)


class CmdWho(MuxCommand):
    """
    Shows the currently connected players.
    Usage:
        who
        +who
    """

    key = "who"
    aliases = []
    locks = "cmd:all()"
    help_category = "General"

    def func(self):
        session_list = SESSIONS.get_sessions()
        session_list = sorted(session_list, key=lambda ses: ses.get_puppet().name)

        titles1 = ('Artisan GM', 'Assassin GM', 'Druid GM', 'Fighter GM', 'Harbinger GM', 'Helotyr GM',
                   'Mage GM', 'Merchant GM', 'Monk GM', 'Ranger GM', 'Samurai GM', 'Sarthoar GM', 'Shaman GM',
                   'Sorcerer GM', 'Templar GM', 'Thief GM', 'Trader GM', 'Warrior GM', 'Chief',
                   'Sherrif', 'Gumi Commander', 'Editor in Chief', 'Chief Justice', 'Tribune Prime',
                   'Head Magistrate')
        titles2 = ('Artisan AGM', 'Assassin AGM', 'Druid AGM', 'Fighter AGM', 'Harbinger AGM', 'Helotyr AGM',
                   'Mage AGM', 'Merchant AGM', 'Monk AGM', 'Ranger AGM', 'Samurai AGM', 'Sarthoar AGM',
                   'Shaman AGM', 'Sorcerer AGM', 'Templar AGM', 'Thief AGM', 'Trader AGM', 'Warrior AGM',
                   'Vice Chief', 'Under-Sheriff', 'Gumi Captain', 'Editor', 'Justice', 'Tribune',
                   'Magistrate')
        titles3 = ('Medjai', 'Gumi', 'Deputy', 'Reporter', 'Kingdom Attorney', 'Aedile', 'Champion')
        titles4 = ('Barrister', 'Advocari', 'Counseler')
        titles5 = ('Field Marshal', 'Legate', 'Gensui')
        titles6 = ('General', 'Prefect', 'Taisho')
        titles7 = ('Colonel', 'Captain', 'Lieutenant', 'First Sergeant', 'Sergent', 'Corporal', 'Private',
                   'Recruit', 'First Centurion', 'Centurion', 'Decurion', 'Optio', 'Tressario', 'Decanus',
                   'Legionaire', 'Discens', 'Taisa', 'Tai', 'Chui', 'Socho', 'Gunso', 'Heicho', 'Ittohei',
                   'Nitohei')

        self.caller.msg("----------------------======]    |CMercadia|n   [======----------------------")
        self.caller.msg(datetime.datetime.now().strftime("            %a %b %d %H:%M:%S %Y Mercadian Time"))
        self.caller.msg("     Mercadia uptime: %s. " % utils.time_format(gametime.uptime(), 3))
        self.caller.msg("----------------------======]     |315Admin|n     [======----------------------")
        self.caller.msg("    Revrwn, |305Administrator|n ")
        self.caller.msg("----------------------======]     |115Staff|n     [======----------------------")
        self.caller.msg("    Jennifer, |405Chief of Staff ")
        self.caller.msg("    Dominic, |045Administrative Staff ")
        self.caller.msg("    Tiffany, |045Administrative Staff ")
        self.caller.msg("    Corry, |045Administrative Staff   ")
        self.caller.msg("----------------------======]   |550Characters|n  [======----------------------")

        for session in session_list:
            puppet = session.get_puppet()
            name = puppet.name
            gender = puppet.db.gender
            race = puppet.db.race
            guild = puppet.db.guild
            owner = puppet.db.owner
            title = puppet.db.title

            slaveentry = ", %s of %s" % (guild, owner)
            guildentry = ", %s" % guild

            if title in titles1:
                title = ", |300%s|n" % title
            elif title in titles2:
                title = ", |500%s|n" % title
            elif title in titles3:
                title = ", |510%s|n" % title
            elif title in titles4:
                title = ", |152%s|n" % title
            elif title in titles5:
                title = ", |203%s|n" % title
            elif title in titles6:
                title = ", |213%s|n" % title
            elif title in titles7:
                title = ", |223%s|n" % title
            else:
                title = " "

            if guild:
                guild = guildentry
            else:
                guild = guild
            if owner:
                guild = slaveentry
            if name in ('Roy', 'Jennifer', 'Dominic', 'Tiffany', 'Corry'):
                continue
            else:
                self.caller.msg("    %s %s %s%s %s" % (name.capitalize(), gender, race, guild, title))
        self.caller.msg("----------------------======]    |555Online|n     [======----------------------")
        self.caller.msg("           There are currently %s Players Online" % (SESSIONS.account_count()))
        self.caller.msg("----------------------======]|C***************|n[======----------------------")

        if  self.args in ("kingdom", 'caliphate', 'empire'):
            self.caller.msg("----------------------======]    |CMercadia|n   [======----------------------")
            self.caller.msg(datetime.datetime.now().strftime("            %a %b %d %H:%M:%S %Y Mercadian Time"))
            self.caller.msg("     Mercadia uptime: %s. " % utils.time_format(gametime.uptime(), 3))
            self.caller.msg("----------------------======]     |315Admin|n     [======----------------------")
            self.caller.msg("    Revrwn, |305Administrator|n ")
            self.caller.msg("----------------------======]     |115Staff|n     [======----------------------")
            self.caller.msg("    Jennifer, |405Chief of Staff ")
            self.caller.msg("    Dominic, |045Administrative Staff ")
            self.caller.msg("    Tiffany, |045Administrative Staff ")
            self.caller.msg("    Corry, |045Administrative Staff   ")
            self.caller.msg("----------------------======]   |550Characters|n  [======----------------------")

            for session in session_list:
                puppet = session.get_puppet()
                name = puppet.name
                gender = puppet.db.gender
                race = puppet.db.race
                guild = puppet.db.guild
                owner = puppet.db.owner
                title = puppet.db.title
                nation = puppet.db.nation

                slaveentry = ", %s of %s" % (guild, owner)
                guildentry = ", %s" % guild

                if title in titles1:
                    title = ", |300%s|n" % title
                elif title in titles2:
                    title = ", |500%s|n" % title
                elif title in titles3:
                    title = ", |510%s|n" % title
                elif title in titles4:
                    title = ", |152%s|n" % title
                elif title in titles5:
                    title = ", |203%s|n" % title
                elif title in titles6:
                    title = ", |213%s|n" % title
                elif title in titles7:
                    title = ", |223%s|n" % title
                else:
                    title = " "

                if guild:
                    guild = guildentry
                else:
                    guild = guild
                if owner:
                    guild = slaveentry
                if name in ('Roy', 'Jennifer', 'Dominic', 'Tiffany', 'Corry'):
                    continue
                elif self.args.capitalize() not in nation:
                    continue
                else:
                    self.caller.msg("    %s %s %s%s %s" % (name.capitalize(), gender, race, guild, title))
            self.caller.msg("----------------------======]    |555Online|n     [======----------------------")
            self.caller.msg("           There are currently %s Players Online" % (SESSIONS.account_count()))
            self.caller.msg("----------------------======]|C***************|n[======----------------------")
