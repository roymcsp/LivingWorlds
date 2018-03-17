"""
Room

Rooms are simple containers that has no location of their own.

Evennia Contribution - Griatch 2012

This is an extended Room typeclass for Evennia. It is supported
by an extended `Look` command and an extended `@desc` command, also
in this module.


Features:

1) Time-changing description slots

This allows to change the full description text the room shows
depending on larger time variations. Four seasons (spring, summer,
autumn and winter) are used by default. The season is calculated
on-demand (no Script or timer needed) and updates the full text block.

There is also a general description which is used as fallback if
one or more of the seasonal descriptions are not set when their
time comes.

An updated `@desc` command allows for setting seasonal descriptions.

The room uses the `evennia.utils.gametime.GameTime` global script. This is
started by default, but if you have deactivated it, you need to
supply your own time keeping mechanism.


2) In-description changing tags

Within each seasonal (or general) description text, you can also embed
time-of-day dependent sections. Text inside such a tag will only show
during that particular time of day. The tags looks like `<timeslot> ...
</timeslot>`. By default there are four timeslots per day - morning,
afternoon, evening and night.


3) Details

The Extended Room can be "detailed" with special keywords. This makes
use of a special `Look` command. Details are "virtual" targets to look
at, without there having to be a database object created for it. The
Details are simply stored in a dictionary on the room and if the look
command cannot find an object match for a `look <target>` command it
will also look through the available details at the current location
if applicable. An extended `@desc` command is used to set details.


4) Extra commands

  CmdExtendedLook - look command supporting room details
  CmdExtendedDesc - @desc command allowing to add seasonal descs and details,
                    as well as listing them
  CmdGameTime     - A simple `time` command, displaying the current
                    time and season.


Installation/testing:

1) Add `CmdExtendedLook`, `CmdExtendedDesc` and `CmdGameTime` to the default `cmdset`
   (see Wiki for how to do this).
2) `@dig` a room of type `contrib.extended_room.ExtendedRoom` (or make it the
   default room type)
3) Use `@desc` and `@detail` to customize the room, then play around!

"""
from __future__ import division
from evennia import utils
from evennia.contrib.extended_room import ExtendedRoom
from evennia.contrib.rpsystem import ContribRPRoom
from evennia.utils.spawner import spawn
from world.economy import transfer_funds

class Room(ExtendedRoom, ContribRPRoom):
    """Base Mercadia Room typeclass.
    Properties:
        terrain (str): The terrain type for this room
        mv_cost (int): (read-only) The movement cost to enter the room; based on
            `terrain` type
    """
    # Define terrain constants
    _TERRAINS = {
        'CHARGEN':{'cost': 0, 'delay': 0},
        'PAVEDROAD': {'cost': 2, 'delay': 0},
        'DIRTROAD': {'cost': 3, 'delay': 0},
        'FOREST': {'cost': 4, 'delay': 0},
        'MUD': {'cost': 4, 'delay': 0},
        'TUNDRA': {'cost': 4, 'delay': 0},
        'SAND': {'cost': 6, 'delay': 0},
        'SNOW': {'cost': 5, 'delay': 0},
        'PLAINS': {'cost': 3, 'delay': 0},
        'THICKET': {'cost': 3, 'delay': 0},
        'WATER': {'cost': 4, 'delay': 0},
        'DEEPWATER': {'cost': 5, 'delay': 0},
        'MOUNTAIN': {'cost': 10, 'delay': 0}
    }

    def at_object_creation(self):
        """Called when room is first created only."""
        super(Room, self).at_object_creation()
        self.db.terrain = 'PAVEDROAD'
        self.db.color_code = ""

    # Terrain property, sets self.db.terrain_type, taken from the constants dict
    @property
    def terrain(self):
        return self.db.terrain

    @terrain.setter
    def terrain(self, value):
        if value in self._TERRAINS:
            self.db.terrain = value
        else:
            raise ValueError('Invalid terrain type.')

    @property
    def mv_cost(self):
        """Returns the movement cost to enter this room."""
        return self._TERRAINS[self.terrain]['cost']

    @property
    def mv_delay(self):
        """Returns the movement delay for this room."""
        return self._TERRAINS[self.terrain]['delay']

    def get_display_name(self, looker, **kwargs):
        # grab the color code stored in db.color_code,
        # or default to "|w"
        color = self.db.color_code or "|c"
        # use the original get_display_name hook to get our name
        name = super(Room, self).get_display_name(looker, **kwargs)
        return("{color}{name}|n".format(color=color, name=name))

    def return_appearance(self, looker):
        """
         This formats a description. It is the hook a 'look' command
         should call.

         Args:
             looker (Object): Object doing the looking.
         """
        if not looker:
            return ""
        # get and identify all objects
        visible = (con for con in self.contents if con != looker and
                   con.access(looker, "view"))
        exits, users, things = [], [], []
        for con in visible:
            key = con.get_display_name(looker, pose=True)
            if con.destination:
                exits.append(key)
            elif con.has_account:
                users.append(key)
            else:
                things.append(key)
        # get description, build string
        string = "|c%s|n\n" % self.get_display_name(looker, pose=True)
        desc = self.db.desc
        if desc:
            string += "%s" % desc
        if exits:
            string += "\n|wObvious Exits:|n " + ", ".join(exits)
        if users or things:
            string += "\n\n " + "\n\n ".join(users + things)
        return string

class WildernessRoom(Room):
    def at_object_creation(self):
        super(WildernessRoom, self).at_object_creation()
        self.db.wilderness = True
        self.db.climate = None


class ChargenRoom(Room):
    """
    This room class is used by character-generation rooms. It makes
    the ChargenCmdset available.
    """
    def at_object_creation(self):
        super(ChargenRoom, self).at_object_creation()
        "this is called only at first creation"

    def at_object_receive(self, obj, source_location):
        if utils.inherits_from(obj, "typeclasses.characters.Character") and self.tags.get("item",category = 'chargen'):
            spawn({"prototype": "DAGGER", "location": self},
                  {"prototype": "SIMPLE_ROBE", "location":self})
        if utils.inherits_from(obj,"typeclasses.characters.Character") and self.tags.get("coins", category = 'chargen'):
            transfer_funds(obj, 1000)
