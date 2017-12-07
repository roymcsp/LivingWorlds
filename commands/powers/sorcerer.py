import time
from math import floor
from evennia import create_object, utils, CmdSet
from commands.command import MuxCommand
from random import randint
from evennia.utils.evform import EvForm
from world.rulebook import d_roll


class SorcCmdSet(CmdSet):
    """
    This stores the input command
    """
    key = "Sorcerer"

    def at_cmdset_creation(self):
        """called once at creation"""
        #self.add(CmdPower())
        self.add(CmdCursedBone())
        #self.add(CmdDeathSpike())
        """
        self.add(CmdAnchor())
        self.add(CmdBloodCloak())
        self.add(CmdBloodShield())
        self.add(CmdBloodWard())
        self.add(CmdBodyToMind())
        self.add(CmdBoneScythe())
        self.add(CmdCircleDeath())
        self.add(CmdCorpseBurst())
        self.add(CmdCorpseDrain())
        self.add(CmdCreateBloodGem())
        self.add(CmdCurseDeathLink())
        self.add(CmdDeathRain())
        self.add(CmdDeathWard())
        self.add(CmdDisease())
        self.add(CmdBoneDust())
        self.add(CmdGloom())
        self.add(CmdImbueBlood())
        self.add(CmdImbueDeath())
        self.add(CmdMassSilence())
        self.add(CmdMassSleep())
        self.add(CmdMassAnchor())
        self.add(CmdMassWeakness())
        self.add(CmdPlague())
        self.add(CmdPoison())
        self.add(CmdPoisonCloud())
        self.add(CmdSilence())
        self.add(CmdSleep())
        self.add(CmdSpectralHunter())
        self.add(CmdSummon())
        self.add(CmdSummonCorruptedMan())
        self.add(CmdSummonCursedArmy())
        self.add(CmdSummonCursedMan())
        self.add(CmdSummonReanimatedMan())
        self.add(CmdTeleport())
        self.add(CmdTeleportOther())
        self.add(CmdTransferPain())
        self.add(CmdVampiricClaw())
        self.add(CmdVampiricTouch())
        self.add(CmdWeakness())
        """


class CmdPower(MuxCommand):
    """
    view character status
    Usage:
      sheet

    """
    key = "power"
    aliases = ["powers"]
    locks = "cmd:all()"

    def func(self):
        """
        Handle displaying power list.
        """
        form = EvForm('commands.templates.powersheet', align='l')
        fields = {
            'A': 'Cursed bone, Death spike',
            'B': 'Body to Mind, Gloom',
            'C': 'Vampiric touch',
            'D': 'Weakness',
            'E': 'Corpse drain',
            'F': 'Poison',
            'G': 'Corrupted Man',
            'H': 'Transfer Pain, Anchor',
            'I': 'Blood Cloak',
            'J': 'Corpse Burst, Bone dust',
            'K': 'Sleep, Disease',
            'L': 'Silence, Poison cloud',
            'M': 'Spectral Hunter, Blood Gem',
            'N': 'Reanimated man',
            'O': 'Teleport, Vampire Claw',
            'P': 'Bone Scythe',
            'Q': 'Curse Death Link',
            'R': 'Blood shield',
            'S': 'Circle of Death',
            'T': 'Imbue Blood, Imbue Death',
            'U': 'Cursed Man',
            'V': 'Mass Sleep',
            'W': 'Mass Silence',
            'X': 'Plague',
            'Y': 'Teleport Other, Summon',
            'Z': 'Mass Weakness',
            'AA': 'Blood Ward',
            'AB': 'Mass Anchor',
            'AC': 'Death Rain',
            'AD': 'Cursed Army',
        }
        form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        self.caller.msg(unicode(form))

    def _format_trait_val(self, val):
        """Format trait values as bright white."""
        return "|w{}|n".format(val)


class CmdCursedBone(MuxCommand):
    """
     Spell Name: Cursed Bone
        MP Cost: 10
         Syntax: cursedbone
    Skills used: none

    Description:

    A simple spell that allows a sorcerer to create
    cursed bones that are a material component for 
    many of the sorcerers spells. 
    """

    key = "cursedbone"
    locks = "cmd:attr_ge(Level, '1')"
    help_category = "Sorcerer"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lastcast = caller.db.cursedbone_lastcast

        if tr.SP.current < 10:
            caller.msg("You don't have enough power to cast this spell")
            return

        if lastcast and time.time() - lastcast < 5 * 60:
            caller.msg("You cannot create another cursed bone yet")
            return

        tr.SP.current -= 10
        caller.msg('|mYou take a fragment of bone and begin chanting.|n ')
        caller.location.msg_contents(
            "|m{actor} takes a fragment of bone and begins chanting.|n",
            mapping=dict(actor=caller),
            exclude=caller)
        utils.delay(5, callback=self.create_bone)

    def create_bone(self):
        caller = self.caller
        caller.msg('|Mfinishing your chant you produce some |xcursed bones|M.|n')
        caller.location.msg_contents(
            "|M{actor} finishes chanting and produces some cursed bones.|n",
            mapping=dict(actor=caller),
            exclude=caller)
        create_object(typeclass='typeclasses.sorcobjects.CursedBone')
        # if the spell was successfully cast, store the casting time
        caller.db.cursedbone_lastcast = time.time()


class CmdDeathSpike(MuxCommand):
    """ 
    Spell Name: Death Spike
    MP Cost   : 30
    Syntax    : deathspike <target>
    Skills    : Spellcraft, Necro Magic

    Description:
    a simple spell that imbues a bone that has been
    previously cursed with necrotic energies and sends
    it towards an enemy. the effectiveness of the spell 
    is based off of the sorcerers skills
    """

    key = "deathspike"
    locks = "cmd:attr_ge(Level, '1')"
    help_category = "Sorcerer"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        lc = caller.db.ds_lc
        item = "|xcursed bone"
        if not self.args:
            self.caller.msg("You dont have a target!")
            return

        target = self.caller.search(self.args)
        if not target:
            return

        if tr.SP.current < 30:
            caller.msg("You don't have enough power to cast this spell")
            return

        if item not in caller.contents:
            caller.msg("you don't have any cursed bones.")

        if lc and time.time() - lc < 5:
            mess = "You cannot cast that again yet"
            caller.msg(mess)
            return
        tr.SP.current -= 30
        mess1 = '|mYou take a cursed bone and begin chanting.|n '
        caller.msg(mess1)
        caller.location.msg_contents(
            "|m{actor} takes a cursed bone and begins chanting.|n",
            mapping=dict(actor=caller),
            exclude=caller)
        utils.delay(3, callback=self.death_spike)

    def death_spike(self):
        caller = self.caller
        target = self.target
        tr = target.traits
        sk = self.caller.skills
        resist = tr.MDEF.actual - sk.SPC.actual
        damage = d_roll("{}d6".format((sk.NEC.actual//3) + 1))

        self.item.delete()
        caller.msg('|MWith a wave of your hand, you send the spike of bone into {target}.|n ')
        caller.location.msg_contents(
            "|MWith a wave of <> hand,{actor} spends a spike of bone into {target}.|n",
            mapping=dict(actor=caller, target=self.target),
            exclude=caller)
        if resist >= 0:
            tr.HP.current -= damage - resist
        else:
            tr.HP.current -= damage
        # if the spell was successfully cast, store the casting time
        caller.db.ds_lc = time.time()


class CmdBodyToMind(MuxCommand):
    """
    Spell Name: Body To Mind
    HP Cost   : varies 
    Syntax    : bodytomind
    Skills    : 

    Description:
    By channeling the powers of the underworld in a mystical ritual
    a sorcerer is able sacrifice their own health and convert it into
    spiritual power, the ratio of health to power is based off of the
    sorcerers skills and level.
    """

    key = "bodytomind"
    locks = "cmd:attr_ge(Level, '2')"

    def func(self):
        caller = self.caller
        tr = self.caller.traits
        sk = self.caller.skills
        lastcast = caller.db.b2m_lastcast
        health = int(floor(0.10 * tr.HP.current))

        if lastcast and time.time() - lastcast < 2 * 60:
            caller.msg("You cannot perform this spell again so soon.")
            return

        tr.HP.current -= int(floor(0.10 * tr.HP.current))
        tr.SP += health / 2 + sk.SPL.current


'''
class CmdVampiricTouch():
    """
    Spell Name: Vampiric Touch
    MP Cost   : 
    Syntax    : vampirictouch <target>
    Skills    : text

    Description:
    text goes here
    """

    key = "vampirictouch"
    locks = "cmd:attr_ge(Level, '3')"


class CmdWeakness():
    """
    Spell Name: Curse: Weakness
    MP Cost   : 
    Syntax    : weakness <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "weakness"
    locks = "cmd:attr_ge(Level, '4')"


class CmdCorpseDrain():
    """
    Spell Name: Corpse Drain
    MP Cost: 
    Syntax: corpsedrain 
    Skills used: 

    Description"""

    key = "corpsedrain"
    locks = "cmd:attr_ge(Level, '5')"


class CmdPoison():
    """
    Spell Name: Curse: Poison
    MP Cost   : 
    Syntax    : poison <target>
    Skills    : 

    Description:
    text goes here
    """    

    key = "poison"
    locks = "cmd:attr_ge(Level, '6')"


class CmdSummonCorruptedMan():
    """
    Spell Name: Summon Corrupted Man
    MP Cost   : 
    Syntax    : corruptedman
    Skills    : 

    Description:
    text goes here
    """

    key = "corruptedman"
    locks = "cmd:attr_ge(Level, '7')"


class CmdTransferPain():
    """
    Spell Name: Transfer Pain
    MP Cost   : 
    Syntax    : transferpain
    Skills    : 

    Description:
    text goes here
    """

    key = "transferpain"
    locks = "cmd:attr_ge(Level, '8')"


class CmdBloodCloak():
    """
    Spell Name: Blood Cloak
    MP Cost   : 
    Syntax    : bloodcloak
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodcloak"
    locks = "cmd:attr_ge(Level, '9')"


class CmdCreateBloodGem():
    """
    Spell Name: Create Blood Gem
    MP Cost   : 
    Syntax    : bloodgem 
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodgem"
    locks = "cmd:attr_ge(Level, '13')"


class CmdCreateBoneDust():
    """
    Spell Name: Create Bone Dust
    MP Cost   : 
    Syntax    : bonedust
    Skills    : 

    Description:
    text goes here
    """

    key = "bonedust"
    locks = "cmd:attr_ge(Level, '10')"


class CmdSpectralHunter():
    """
    Spell Name: Summon: Spectral Hunter
    MP Cost   : 
    Syntax    : spectralhunter
    Skills    : 

    Description:
    text goes here
    """

    key = "spectralhunter"
    locks = "cmd:attr_ge(Level, '13')"
    
    
class CmdVampiricClaw():
    """
    Spell Name: Vampiric Claw
    MP Cost   : 
    Syntax    : vampiricclaw
    Skills    : 

    Description:
    text goes here
    """

    key = "vampiricclaw"
    locks = "cmd:attr_ge(Level, '15')"


class CmdCorpseBurst():
    """
    Spell Name: Corpse Burst
    MP Cost   : 
    Syntax    : corpseburst
    Skills    : 

    Description:
    text goes here
    """

    key = "corpseburst"
    locks = "cmd:attr_ge(Level, '10')"


class CmdCircleDeath():
    """
    Spell Name: Circle of Death
    MP Cost   : 
    Syntax    : circleofdeath
    Skills    : 

    Description:
    text goes here
    """

    key = "circleofdeath"
    locks = "cmd:attr_ge(Level, '19')"


class CmdBloodShield():
    """
    Spell Name: Blood Shield
    MP Cost   : 
    Syntax    : bloodshield
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodshield"
    locks = "cmd:attr_ge(Level, '18')"


class CmdImbueDeath():
    """
    Spell Name: Imbue Death Magic
    MP Cost   : 
    Syntax    : imbuedeath <weapon>; imbuedeath <armor>
    Skills    : 

    Description:
    text goes here
    """

    key = "imbuedeath"
    locks = "cmd:attr_ge(Level, '20')"


class CmdImbueBlood():
    """
    Spell Name: Imbue Blood
    MP Cost   : 
    Syntax    : imbueblood <weapon>; imbueblood <armor>
    Skills    : 

    Description:
    text goes here
    """

    key = "imbueblood"
    locks = "cmd:attr_ge(Level, '20')"


class CmdSleep():
    """
    Spell Name: Curse: Sleep
    MP Cost   : 
    Syntax    : sleep <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "sleep"
    locks = "cmd:attr_ge(Level, '11')"


class CmdDeathRain():
    """
    Spell Name: Death Rain
    MP Cost   : 
    Syntax    : deathrain
    Skills    : 

    Description:
    text goes here
    """

    key = "deathrain"
    locks = "cmd:attr_ge(Level, '29')"
    
    
class CmdDeathWard():
    """
    Spell Name: Death Ward
    MP Cost   : 
    Syntax    : deathward <direction>
    Skills    : 

    Description:
    text goes here
    """

    key = "deathward" 
    locks = "cmd:attr_ge(Level, '1')"


class CmdPoisonCloud():
    """
    Spell Name: Curse: Poisonous Cloud
    MP Cost   : 
    Syntax    : poisoncloud
    Skills    : 

    Description:
    text goes here
    """

    key = "poisoncloud"
    locks = "cmd:attr_ge(Level, '12')"


class CmdBoneScythe():
    """
    Spell Name: Bone Scythe
    MP Cost   : 
    Syntax    : bonescythe
    Skills    : 

    Description:
    text goes here
    """

    key = "bonescythe"
    locks = "cmd:attr_ge(Level, '16')"


class CmdTeleport():
    """
    Spell Name: Teleport 
    MP Cost   : 
    Syntax    : teleport
    Skills    : 

    Description:
    text goes here
    """

    key = "teleport"
    locks = "cmd:attr_ge(Level, '15')"
    

class CmdTeleportOther():
    """
    Spell Name: Teleport Other
    MP Cost   : 
    Syntax    : teleportother <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "teleportother"
    locks = "cmd:attr_ge(Level, '25')"


class CmdSummon():
    """
    Spell Name: Summon 
    MP Cost   : 
    Syntax    : summon <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "summon"
    locks = "cmd:attr_ge(Level, '25')"


class CmdBloodWard():
    """
    Spell Name: Blood Ward 
    MP Cost   : 
    Syntax    : bloodward
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodward"
    locks = "cmd:attr_ge(Level, '27')"


class CmdSummonReanimatedMan():
    """
    Spell Name: Summon: Reanimated Man
    MP Cost   : 
    Syntax    : reanimatedman
    Skills    : 

    Description:
    text goes here
    """

    key = "reanimatedman"
    locks = "cmd:attr_ge(Level, '14')"


class CmdSummonCursedMan():
    """
    Spell Name: Summon: Cursed Man
    MP Cost   : 
    Syntax    : cursedman
    Skills    : 

    Description:
    text goes here
    """

    key = "cursed"
    locks = "cmd:attr_ge(Level, '21')"


class CmdSummonCursedArmy():
    """
    Spell Name: Summon: Cursed Army
    MP Cost   : 
    Syntax    : cursedarmy
    Skills    : 

    Description:
    text goes here
    """

    key = "cursedarmy"
    locks = "cmd:attr_ge(Level, '30')"


class CmdSilence():
    """
    Spell Name: Curse: Silence
    MP Cost   : 
    Syntax    : silence <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "silence"
    locks = "cmd:attr_ge(Level, '12')"


class CmdMassSilence():
    """
    Spell Name: Curse: Mass Silence
    MP Cost   : 
    Syntax    : masssilence
    Skills    : 

    Description:
    text goes here
    """

    key = "masssilence"
    locks = "cmd:attr_ge(Level, '23')"


class CmdMassSleep():
    """
    Spell Name: Curse: Mass Sleep
    MP Cost   : 
    Syntax    : masssleep
    Skills    : 

    Description:
    text goes here
    """

    key = "masssleep"
    locks = "cmd:attr_ge(Level, '22')"


class CmdPlague():
    """
    Spell Name: Curse: Plague
    MP Cost   : 
    Syntax    : plague <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "plague"
    locks = "cmd:attr_ge(Level, '24')"


class CmdDisease():
    """
    Spell Name: Curse: Disease
    MP Cost   : 
    Syntax    : disease <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "disease"
    locks = "cmd:attr_ge(Level, '11')"


class CmdGloom():
    """
    Spell Name: Curse: Gloom
    MP Cost   : 
    Syntax    : gloom <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "gloom"
    locks = "cmd:attr_ge(Level, '2')"


class CmdAnchor():
    """
    Spell Name: Curse: Anchor
    MP Cost   : 
    Syntax    : anchor <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "anchor"
    locks = "cmd:attr_ge(Level, '8')"
    

class CmdCurseDeathLink():
    """
    Spell Name: Curse Death Link
    MP Cost   : 
    Syntax    : cursedeathlink
    Skills    : 

    Description:
    text goes here
    """

    key = "cursedeathlink"
    locks = "cmd:attr_ge(Level, '17')"
    
class CmdMassAnchor():
    """
    Spell Name: Mass Anchor
    MP Cost   : 
    Syntax    : massanchor
    Skills    : 

    Description:
    text goes here
    """

    key = "massanchor"
    locks = "cmd:attr_ge(Level, '28')"
    
class CmdMassGloom():
    """
    Spell Name: Mass Gloom
    MP Cost   : 
    Syntax    : massgloom
    Skills    : 

    Description:
    text goes here
    """

    key = "massgloom"
    locks = "cmd:attr_ge(Level, '28')"
'''
