import time
from evennia import create_object, utils
from commands.command import MuxCommand


class CmdSpellCursedBone(MuxCommand):
    """
     Spell Name: Cursed Bone
        MP Cost: 10
         Syntax: cursedbone
    Skills used: none

    Description:

    A simple spell that allows a sorcerer to create
    a cursed bone that is  a material component for 
    many of the sorcerers spells. 
    """

    key = "cursedbone"
    locks = "cmd:attr(Level, '1')"
    help_category = "Sorcerer"

    def func(self):
        caller = self.caller
        lastcast = caller.db.cursedbone_lastcast
        if lastcast and time.time() - lastcast < 5 * 60:
            mess = "You cannot create another cursed bone yet"
            caller.msg(mess)
            return
        caller.db.sp.current -= 10
        mess1 = '{mYou take a fragment of bone and begin chanting.{n '
        caller.msg(mess1)
        utils.delay(5, callback=self.create_bone)

    def create_bone(self):
        caller = self.caller
        mess2 = '{Mfinishing your chant you produce a {xcursed bone.{n'
        caller.msg(mess2)
        create_object(typeclass='typeclasses.sorcobjects.CursedBone')
        # if the spell was successfully cast, store the casting time
        caller.db.cursedbone_lastcast = time.time()


'''        
class CmdSpellDeathSpike():
    """ 
    Spell Name: Death Spike
    MP Cost   : 
    Syntax    : deathspike <target>
    Skills    : 

    Description:
    a simple spell that imbues a bone that has been
    previously cursed with necrotic energies and sends
    it towards an enemy. the effectivness of the spell 
    is based off of the sorcerers skills
    """

    key = "deathspike"
    aliases = None
    locks ="cmd:attr(Level, '1')"
    help_category = "Sorcerer"

class CmdSpellBodyToMind():
    """
    Spell Name: Body To Mind
    MP Cost   : 
    Syntax    : bodytomind
    Skills    : 

    Description:
    By channels the powers of the underworld in a mystical ritual
    a sorcerer is able sacrifice their own health and convert it into
    spiritual power, the ratio of health to power is based off of the
    sorcerers skills and level.
    """

    key = "bodytomind"
    locks ="cmd:isSorcerer()"

class CmdSpellVampiricTouch():
    """
    Spell Name: Vampiric Touch
    MP Cost   : 
    Syntax    : vampirictouch <target>
    Skills    : text

    Description:
    text goes here
    """

    key = "vampirictouch"
    locks ="cmd:isSorcerer()"

class CmdSpellWeakness():
    """
    Spell Name: Curse: Weakness
    MP Cost   : 
    Syntax    : weakness <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "weakness"
    locks ="cmd:isSorcerer()"

class CmdSpellCorpseDrain():
    """
    Spell Name: Corpse Drain
    MP Cost: 
    Syntax: corpsedrain 
    Skills used: 

    Description"""

    key = "corpsedrain"
    locks ="cmd:isSorcerer()"

class CmdSpellPoison():
    """
    Spell Name: Curse: Poison
    MP Cost   : 
    Syntax    : poison <target>
    Skills    : 

    Description:
    text goes here
    """    

    key = "poison"
    locks ="cmd:isSorcerer()"

class CmdSpellSummonCorruptedMan():
    """
    Spell Name: Summon Corrupted Man
    MP Cost   : 
    Syntax    : corruptedman
    Skills    : 

    Description:
    text goes here
    """

    key = "corruptedman"
    locks ="cmd:isSorcerer()"

class CmdSpellTransferPain():
    """
    Spell Name: Transfer Pain
    MP Cost   : 
    Syntax    : transferpain
    Skills    : 

    Description:
    text goes here
    """

    key = "transferpain"
    locks ="cmd:isSorcerer()"

class CmdSpellBloodCloak():
    """
    Spell Name: Blood Cloak
    MP Cost   : 
    Syntax    : bloodcloak
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodcloak"
    locks ="cmd:isSorcerer()"

class CmdSpellCreateBloodGem():
    """
    Spell Name: Create Blood Gem
    MP Cost   : 
    Syntax    : bloodgem 
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodgem"
    locks ="cmd:isSorcerer()"

class CmdSpellCreateBoneDust():
    """
    Spell Name: Create Bone Dust
    MP Cost   : 
    Syntax    : bonedust
    Skills    : 

    Description:
    text goes here
    """

    key = "bonedust"
    locks ="cmd:isSorcerer()"

class CmdSpellFamilier():
    """
    Spell Name: Summon Familier
    MP Cost   : 
    Syntax    : familier
    Skills    : 

    Description:
    text goes here
    """

    key = "familier"
    locks ="cmd:isSorcerer()"

class CmdSpellSpectralHunter():
    """
    Spell Name: Summon: Spectral Hunter
    MP Cost   : 
    Syntax    : spectralhunter
    Skills    : 

    Description:
    text goes here
    """

    key = "spectralhunter"
    locks ="cmd:isSorcerer()"
class CmdSpellVampiricClaw():
    """
    Spell Name: Vampiric Claw
    MP Cost   : 
    Syntax    : vampiricclaw
    Skills    : 

    Description:
    text goes here
    """

    key = "vampiricclaw"
    locks ="cmd:isSorcerer()"

class CmdSpellCorpseBurst():
    """
    Spell Name: Corpse Burst
    MP Cost   : 
    Syntax    : corpseburst
    Skills    : 

    Description:
    text goes here
    """

    key = "corpseburst"
    locks ="cmd:isSorcerer()"

class CmdSpellCircleDeath():
    """
    Spell Name: Circle of Death
    MP Cost   : 
    Syntax    : circleofdeath
    Skills    : 

    Description:
    text goes here
    """

    key = "circleofdeath"
    locks ="cmd:isSorcerer()"

class CmdSpellBloodShield():
    """
    Spell Name: Blood Shield
    MP Cost   : 
    Syntax    : bloodshield
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodshield"
    locks ="cmd:isSorcerer()"

class CmdSpellImbueDeath():
    """
    Spell Name: Imbue Death Magic
    MP Cost   : 
    Syntax    : imbuedeath <weapon>; imbuedeath <armor>
    Skills    : 

    Description:
    text goes here
    """

    key = "imbuedeath"
    locks ="cmd:isSorcerer()"

class CmdSpellImbueBlood():
    """
    Spell Name: Imbue Blood
    MP Cost   : 
    Syntax    : imbueblood <weapon>; imbueblood <armor>
    Skills    : 

    Description:
    text goes here
    """

    key = "imbueblood"
    locks ="cmd:isSorcerer()"

class CmdSpellSleep():
    """
    Spell Name: Curse: Sleep
    MP Cost   : 
    Syntax    : sleep <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "sleep"
    locks ="cmd:isSorcerer()"

class CmdSpellDeathRain():
    """
    Spell Name: Death Rain
    MP Cost   : 
    Syntax    : deathrain
    Skills    : 

    Description:
    text goes here
    """

    key = "deathrain"
    locks ="cmd:isSorcerer()"
class CmdSpellDeathWard():
    """
    Spell Name: Death Ward
    MP Cost   : 
    Syntax    : deathward <direction>
    Skills    : 

    Description:
    text goes here
    """

    key = "deathward" 
    locks ="cmd:isSorcerer()"

class CmdSpellPoisonCloud():
    """
    Spell Name: Curse: Poisonous Cloud
    MP Cost   : 
    Syntax    : poisoncloud
    Skills    : 

    Description:
    text goes here
    """

    key = "poisoncloud"
    locks ="cmd:isSorcerer()"

class CmdSpellBoneStaff():
    """
    Spell Name: Bone Staff
    MP Cost   : 
    Syntax    : bonestaff
    Skills    : 

    Description:
    text goes here
    """

    key = "bonestaff"
    locks ="cmd:isSorcerer()"

class CmdSpellTeleport():
    """
    Spell Name: Teleport 
    MP Cost   : 
    Syntax    : teleport
    Skills    : 

    Description:
    text goes here
    """

    key = "teleport"
    locks ="cmd:isSorcerer()"

class CmdSpellTeleportOther():
    """
    Spell Name: Teleport Other
    MP Cost   : 
    Syntax    : teleportother <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "teleportother"
    locks ="cmd:isSorcerer()"

class CmdSpellSummon():
    """
    Spell Name: Summon 
    MP Cost   : 
    Syntax    : summon <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "summon"
    locks ="cmd:isSorcerer()"

class CmdSpellBloodWard():
    """
    Spell Name: Blood Ward 
    MP Cost   : 
    Syntax    : bloodward
    Skills    : 

    Description:
    text goes here
    """

    key = "bloodward"
    locks ="cmd:isSorcerer()"

class CmdSpellSummonReanimatedMan():
    """
    Spell Name: Summon: Reanimated Man
    MP Cost   : 
    Syntax    : reanimatedman
    Skills    : 

    Description:
    text goes here
    """

    key = "reanimatedman"
    locks ="cmd:isSorcerer()"

class CmdSpellSummonCursedMan():
    """
    Spell Name: Summon: Cursed Man
    MP Cost   : 
    Syntax    : cursedman
    Skills    : 

    Description:
    text goes here
    """

    key = "cursed"
    locks ="cmd:isSorcerer()"

class CmdSpellSummonCursedArmy():
    """
    Spell Name: Summon: Cursed Army
    MP Cost   : 
    Syntax    : cursedarmy
    Skills    : 

    Description:
    text goes here
    """

    key = "cursedarmy"
    locks ="cmd:isSorcerer()"

class CmdSpellSilence():
    """
    Spell Name: Curse: Silence
    MP Cost   : 
    Syntax    : silence <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "silence"
    locks ="cmd:isSorcerer()"

class CmdSpellMassSilence():
    """
    Spell Name: Curse: Mass Silence
    MP Cost   : 
    Syntax    : masssilence
    Skills    : 

    Description:
    text goes here
    """

    key = "masssilence"
    locks ="cmd:isSorcerer()"

class CmdSpellMassSleep():
    """
    Spell Name: Curse: Mass Sleep
    MP Cost   : 
    Syntax    : masssleep
    Skills    : 

    Description:
    text goes here
    """

    key = "masssleep"
    locks ="cmd:isSorcerer()"

class CmdSpellPlague():
    """
    Spell Name: Curse: Plague
    MP Cost   : 
    Syntax    : plague <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "plague"
    locks ="cmd:isSorcerer()"

class CmdSpellDisease():
    """
    Spell Name: Curse: Disease
    MP Cost   : 
    Syntax    : disease <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "disease"
    locks ="cmd:isSorcerer()"

class CmdSpellGloom():
    """
    Spell Name: Curse: Gloom
    MP Cost   : 
    Syntax    : gloom <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "gloom"
    locks ="cmd:isSorcerer()"

class CmdSpellAnchor():
    """
    Spell Name: Curse: Anchor
    MP Cost   : 
    Syntax    : anchor <target>
    Skills    : 

    Description:
    text goes here
    """

    key = "anchor"
    locks ="cmd:isSorcerer()"

class CmdSpellCurseDeathLink():
    """
    Spell Name: Curse Death Link
    MP Cost   : 
    Syntax    : cursedeathlink
    Skills    : 

    Description:
    text goes here
    """

    key = "cursedeathlink"
    locks ="cmd:isSorcerer()"
'''
