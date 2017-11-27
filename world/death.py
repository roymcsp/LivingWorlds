"""
Death Module
Controls what happens when a character or NPC character dies
"""

from math import floor
from evennia import CmdSet
from command.commands import MuxCommand
from evennia.utils import delay
from typeclasses.scripts import Script
from world.rulebook import d_roll

# Scripts


class DeathHandler(Script):
    """ Base script for death mechanics handlers """
    def at_script_creation(self):
        super(DeathHandler, self).at_script_creation()

        self.key = "death_handler_{}".format(self.obj.id)
        self.desc = "handles character death"
        self.interval = 0
        self.repeats = 0
        self.start_delay = False
        self.persistent = True

        self.db.death_step = 0
        self.db.death_cb = None
        # subclasses define the sequence of callbacks
        self.db.death_sequence = ()

    def at_start(self):
        """Parent at_start should be called first in subclasses."""
        self.obj.cmdset.add(DeadCmdSet)
        if len(self.db.death_sequence) > 0 and self.db.death_step > 0:
            delay(3, getattr(self, self.db.death_sequence[self.db.death_step]))

    def at_stop(self):
        self.obj.cmdset.remove(DeadCmdSet)


class CharDeathHandler(DeathHandler):
    """Script that handles death mechanics for Characters"""
    def at_script_creation(self):
        super(CharDeathHandler, self).at_script_creation()
        self.db.death_sequence = ('floating', 'returning', 'pre_revive', 'revive')

    def at_start(self):
        """handles the phases of death"""
        super(CharDeathHandler, self).at_start()
        self.obj.msg("you have died")
        self.obj.location.msg_contents('{character} falls to the ground dead.',
                                       mapping={'character': self.obj},
                                       exclude=self.obj)
        self.obj.traits.XP.current -= int(floor(0.15 * self.obj.traits.XP.current))
        void = self.obj.search('Void', global_search=True)
        self.obj.move_to(void, quiet=True, move_hooks=False)
        delay(20, getattr(self, self.db.death_sequence[self.db.death_step]))

    def floating(self):
        self.obj.msg('Your awareness blinks back into existence briefly. you float in the void.')
        self.db.death_step += 1
        delay(12, getattr(self, self.db.death_sequence[self.db.death_step]))

    def returning(self):
        if self.obj.db.permadeath is False:
            self.obj.msg(
                "you feel a quickening in your spirit as you feel pulled towards the |mSpirit Realm|n."
            )

            self.db.death_step += 1
            delay(8, getattr(self, self.db.death_sequence[self.db.death_step]))
        else:
            self.obj.msg(
                "you feel a rending of your spirit as you are pulled towards the |mRealm of Eternal Death|n.")
            self.db.death_step += 1
            delay(8, getattr(self, self.db.death_sequence[self.db.death_step]))

    def pre_revive(self):
        if self.obj.db.permadeath is False:
            self.obj.msg(
                '')
            delay(10, getattr(self, self.db.death_sequence[self.db.death_step]))
        else:
            self.obj.msg(
                '')
            delay(10, getattr(self, self.db.death_sequence[self.db.death_step]))

    def revive(self):
        if self.obj.db.permadeath is False:
            self.obj.traits.HP.fill_gauge()
            self.obj.traits.SP.fill_gauge()
            self.obj.traits.EP.fill_gauge()
            spiritrealm = self.obj.search('Spirit Realm', global_search=True)
            self.obj.move_to(spiritrealm, quiet=True, move_hooks=False)

        else:
            self.obj.traits.HP.fill_gauge()
            self.obj.traits.SP.fill_gauge()
            self.obj.traits.EP.fill_gauge()
            eternaldeath = self.obj.search('Realm of Eternal Death', global_search=True)
            self.obj.move_to(eternaldeath, quiet=True, move_hooks=False)
