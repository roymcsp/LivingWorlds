"""
Death Module
Controls what happens when a character or NPC character dies
"""
from random import randint
from math import floor
from evennia import CmdSet
from commands.command import MuxCommand
from evennia.utils import delay
from typeclasses.scripts import Script
from world.rulebook import d_roll
from evennia.utils.spawner import spawn

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
        corpse_name = 'corpse of %s' % self.obj
        corpse_desc = "A dead body that was once %s in life." % self.obj
        corpse_proto = {'key': corpse_name, "desc": corpse_desc}
        corpse = spawn(corpse_proto)[0]
        corpse.location = self.obj.location
        for i in self.obj.equip:
            self.obj.equip.remove(i)
        for i in self.obj.contents:
            dest_chance = randint(1, 100)
            if dest_chance <= 15:
                i.delete
            else:
                i.move_to(corpse, quiet=True)

        void = self.obj.search('Void', global_search=True)
        self.obj.move_to(void, quiet=True, move_hooks=False)
        #create a corpse of the character that died Corpse of {character}
        #move the equipped,worn and inventory of character that died to corpse
        #check over each item to see what survives remove destroyed items
        delay(20, getattr(self, self.db.death_sequence[self.db.death_step]))

    def floating(self):
        self.obj.msg('')
        self.db.death_step += 1
        delay(12, getattr(self, self.db.death_sequence[self.db.death_step]))

    def returning(self):
        if self.obj.db.permadeath is False:
            self.obj.msg(
                "you feel pulled towards the |mSpirit Realm|n."
            )
            spiritrealm = self.obj.search('Spirit Realm', global_search=True)
            spiritrealm.msg_contents(
                ''
            )
            self.db.death_step += 1
            delay(8, getattr(self, self.db.death_sequence[self.db.death_step]))
        else:
            self.obj.msg(
                "you feel a rending of your spirit as you are pulled towards the |mRealm of Eternal Death|n.")
            eternaldeath = self.obj.search('Realm of Eternal Death', global_search=True)
            eternaldeath.msg_contents(
                ''
            )
            self.db.death_step += 1
            delay(8, getattr(self, self.db.death_sequence[self.db.death_step]))

    def pre_revive(self):
        if self.obj.db.permadeath is False:
            self.obj.msg(
                '')
            spiritrealm = self.obj.search('Spirit Realm', global_search=True)
            spiritrealm.msg_contents(
                ''
            )
            delay(10, getattr(self, self.db.death_sequence[self.db.death_step]))
        else:
            self.obj.msg(
                ''
            )
            eternaldeath = self.obj.search('Realm of Eternal Death', global_search=True)
            eternaldeath.msg_contents(
                ''
            )
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
