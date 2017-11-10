import time
from evennia import utils
from command import MuxCommand


class CmdHuman(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Human')"
    help_category = "commands"


class CmdElf(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Elf')"
    help_category = "commands"


class CmdDwarf(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Dwarf')"
    help_category = "commands"


class CmdGnome(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Gnome')"
    help_category = "commands"


class CmdCentaur(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Centuar')"
    help_category = "commands"


class CmdOgryn(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Ogryn')"
    help_category = "commands"


class CmdDrow(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Drow')"
    help_category = "commands"


class CmdDuergar(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Duergar')"
    help_category = "commands"


class CmdSvirfneblin(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Svirfneblin')"
    help_category = "commands"


class CmdWemic(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Wemic')"
    help_category = "commands"


class CmdDrakkar(MuxCommand):
    """
        Spell Name: Breath Weapon
           MP Cost: 10 + Level
            Syntax: breathweapon <target>
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = "breathweapon"
    locks = "cmd:attr(race, 'Drakkar')"
    help_category = "commands"


class CmdUrsine(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Ursine')"
    help_category = "commands"


class CmdFeline(MuxCommand):
    """
        Spell Name: Claw Strike 
           MP Cost: 10 + Level
            Syntax: clawstrike <target>
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = "clawstrike"
    locks = "cmd:attr(race, 'Feline')"
    help_category = "commands"


class CmdLupine(MuxCommand):
    """
        Spell Name: 
           MP Cost: 10 + Level
            Syntax: 
       Skills used: 

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = ""
    locks = "cmd:attr(race, 'Lupine')"
    help_category = "commands"


class CmdVulpine(MuxCommand):
    """
        Spell Name: Fox Fire
           MP Cost: 10 + Level
            Syntax: 
       Skills used: foxfire <target>

       Description:

       A simple spell that allows an urchin to draw upon
       their independent nature and will to survive to 
       fortify their mind against many forms of intrusion 
       or control for a short time. How effective this is 
       accomplished is based upon the focus skill.
       """

    key = "foxfire"
    locks = "cmd:attr(race, 'Vulpine')"
    help_category = "commands"


class CmdNaga(MuxCommand):
    """
            Spell Name: Constrict 
               MP Cost: 10 + Level
                Syntax: constrict <target>
           Skills used: 

           Description:

           A simple spell that allows an urchin to draw upon
           their independent nature and will to survive to 
           fortify their mind against many forms of intrusion 
           or control for a short time. How effective this is 
           accomplished is based upon the focus skill.
           """

    key = "constrict"
    locks = "cmd:attr(race, 'Naga')"
    help_category = "commands"
