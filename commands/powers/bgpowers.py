import time
from evennia import create_object, utils, CmdSet
from evennia.commands.default.muxcommand import MuxCommand


class CmdUrchin(MuxCommand):
    """
     Spell Name: Urchin's Willpower
        MP Cost: 10 + Level
         Syntax: willpower
    Skills used: focus

    Description:

    A simple spell that allows an urchin to draw upon
    their independent nature and will to survive to 
    fortify their mind against many forms of intrusion 
    or control for a short time. How effective this is 
    accomplished is based upon the focus skill.
    """

    key = "willpower"
    locks = "cmd:attr(background, 'Urchin')"
    help_category = "commands"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.willpower_lastcast
        if lastcast and time.time() - lastcast < 2 * 60:
            mess = "You cannot cast this again so soon"
            caller.msg(mess)
            return
        tr.SP.current -= (10 + tr.LVL.actual)
        utils.delay(1, callback=self.fortify_will)

    def fortify_will(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess1 = '|m.You focus your mind on survival|n '
        caller.msg(mess1)
        tr.WILL.mod += (sk.FOC.current / 5)
        # if the spell was successfully cast, store the casting time
        caller.db.willpower_lastcast = time.time()
        utils.delay(2 * 60, callback=self.unfortify_will)

    def unfortify_will(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess2 = '|mYou relax your focus.|n '
        caller.msg(mess2)
        tr.WILL.mod -= (sk.FOC.current / 5)


class UrchinCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "commands"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdUrchin())


class CmdNoble(MuxCommand):
    """
     Spell Name: Noble Presence
        MP Cost: 10 + level
         Syntax: presence
    Skills used: leadership

    Description:

    A simple spell that allows a noble to draw upon
    their upbringing and educations to help ward off 
    many harmful effects and powers.How effective this 
    is accomplished is based upon the focus skill.
    """

    key = "presence"
    locks = "cmd:attr(background, Noble)"
    help_category = "commands"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.presence_lastcast
        if lastcast and time.time() - lastcast < 2 * 60:
            mess = "You cannot cast this again so soon"
            caller.msg(mess)
            return
        tr.SP.current -= (10 + tr.LVL.actual)
        utils.delay(1, callback=self.fortify_defense)

    def fortify_defense(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess1 = '|mYou stand up straight exhibiting an aura of leadership.|n '
        caller.msg(mess1)
        tr.MDEF.mod += (sk.LEA.current / 5)
        # if the spell was successfully cast, store the casting time
        caller.db.presence_lastcast = time.time()
        utils.delay(2 * 60, callback=self.unfortify_defense)

    def unfortify_defense(self):
        tr = self.caller.traits
        sk = self.caller.skills
        caller = self.caller
        mess2 = '|mYour aura of leadership fades as you relax.|n '
        caller.msg(mess2)
        tr.MDEF.mod -= (sk.LEA.current / 5)


class NobleCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "commands"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdNoble())


class CmdNomad(MuxCommand):
        """
         Spell Name: Nomad's Fortitude  
            MP Cost: 10 + Level
             Syntax: fortitude
        Skills used: martial

        Description:

        A simple spell that allows a nomad to draw upon
        their training and upbringing in harsh lands to  
        fortify their bodies to shrug off many harmful 
        poisons and debilitating effects.How effective 
        this is accomplished is based upon the martial skill.
        """

        key = "fortitude"
        locks = "cmd:attr(background, 'Nomad')"
        help_category = "commands"

        def func(self):
            caller = self.caller
            tr = self.caller.traits
            sk = self.caller.skills
            lastcast = caller.db.fortitude_lastcast
            if lastcast and time.time() - lastcast < 2 * 60:
                mess = "You cannot cast this again so soon"
                caller.msg(mess)
                return
            tr.SP.current -= (10 + tr.LVL.actual)
            utils.delay(1, callback=self.fortify_fortitude)

        def fortify_fortitude(self):
            caller = self.caller
            tr = self.caller.traits
            sk = self.caller.skills
            mess1 = '|mYou take on a defensive stance.|n '
            caller.msg(mess1)
            tr.FORT.mod += (sk.MAR.current / 5)
            # if the spell was successfully cast, store the casting time
            caller.db.fortitude_lastcast = time.time()
            utils.delay(2 * 60, callback=self.unfortify_fortitude)

        def unfortify_fortitude(self):
            caller = self.caller
            tr = self.caller.traits
            sk = self.caller.skills
            mess2 = '|mYou relax your defenses.|n '
            caller.msg(mess2)
            tr.FORT.mod -= (sk.MAR.current / 5)


class NomadCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "commands"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdNomad())


class CmdGypsy(MuxCommand):
    """
     Spell Name: Gypsy Reflex
        MP Cost: 10 + Level
         Syntax: reflex
    Skills used: dodge

    Description:

    A simple spell that allows a gypsy to draw upon
    their talents of agility and dance to improve 
    their reflexes and allow them to avoid dangerous
    and harmful effects. How effective this is 
    accomplished is based upon the dodge skill.     
    """

    key = "reflex"
    locks = "cmd:attr(background, 'Gypsy')"
    help_category = "commands"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.reflex_lastcast
        if lastcast and time.time() - lastcast < 2 * 60:
            mess = "You cannot cast this again so soon"
            caller.msg(mess)
            return
        tr.SP.current -= (10 + tr.LVL.actual)
        utils.delay(1, callback=self.fortify_reflex)

    def fortify_reflex(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess1 = '|mYou move lithely as a dancer.|n '
        caller.msg(mess1)
        tr.REFL.mod += (sk.DOD.current / 5)
        # if the spell was successfully cast, store the casting time
        caller.db.reflex_lastcast = time.time()
        utils.delay(2 * 60, callback=self.unfortify_reflex)

    def unfortify_reflex(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess2 = '|mYou no longer move about lithely.|n '
        caller.msg(mess2)
        tr.REFL.mod -= (sk.DOD.current / 5)


class GypsyCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "commands"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdGypsy())


class CmdFarmer(MuxCommand):
    """
     Spell Name: Farmer Harvest
        MP Cost: 10 + Level
         Syntax: harvest
    Skills used: 

    Description:

    A simple spell that allows a farmer to create
    an edible item. 
    """

    key = "harvest"
    locks = "cmd:attr(background, 'Farmer')"
    help_category = "commands"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.harvest_lastcast
        if lastcast and time.time() - lastcast < 2 * 60:
            mess = "You cannot cast this again so soon"
            caller.msg(mess)
            return
        tr.SP.current -= (10 + tr.LVL.actual)
        utils.delay(1, callback=self.fortify_armor)

    def fortify_armor(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess1 = '|mYou take out a vial of oil and fortify your armor.|n '
        caller.msg(mess1)
        tr.PDEF.mod += (sk.FOR.current / 5)
        # if the spell was successfully cast, store the casting time
        caller.db.harvest_lastcast = time.time()
        utils.delay(2 * 60, callback=self.unfortify_armor)

    def unfortify_armor(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess2 = '|mYour armor loses its fortification.|n '
        caller.msg(mess2)
        tr.PDEF.mod -= (sk.forge.current / 5)


class FarmerCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "commands"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdFarmer())


class CmdTradesman(MuxCommand):
    """
     Spell Name: Tradesman Fortify
        MP Cost: 10 + caster level 
         Syntax:  fortify
    Skills used:  forge

    Description:

    A simple spell that allows a tradesman to fortify
    their physical defense for a short time. How well 
    this is accomplished is based upon the forge skill. 
    """

    key = "fortify"
    locks = "cmd:attr(background, 'Tradesman')"
    help_category = "commands"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.fortify_lastcast
        if lastcast and time.time() - lastcast < 2 * 60:
            mess = "You cannot cast this again so soon"
            caller.msg(mess)
            return
        tr.SP.current -= (10 + tr.LVL.actual)
        utils.delay(1, callback=self.fortify_armor)

    def fortify_armor(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess1 = '|mYou take out a vial of oil and fortify your armor.|n '
        caller.msg(mess1)
        tr.PDEF.mod += (sk.ORG.current / 5)
        # if the spell was successfully cast, store the casting time
        caller.db.fortify_lastcast = time.time()
        utils.delay(2 * 60, callback=self.unfortify_armor)

    def unfortify_armor(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        mess2 = '|mThe fortification wears off of your armor.|n '
        caller.msg(mess2)
        tr.PDEF.mod -= (sk.ORG.current / 5)


class TradesmanCmdSet(CmdSet):
    """
       This stores the input command
       """
    key = "commands"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(CmdTradesman())