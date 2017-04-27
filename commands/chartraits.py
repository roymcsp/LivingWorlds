"""
Character trait-related commands
"""

from .command import MuxCommand
from evennia import CmdSet
from evennia.utils.evform import EvForm, EvTable


class CharTraitCmdSet(CmdSet):

    key = "chartrait_cmdset"
    priority = 1

    def at_cmdset_creation(self):
        """Populate CmdSet"""
        self.add(CmdSheet())
        self.add(CmdWealth())

class CmdSheet(MuxCommand):
    """
    view character status
    Usage:
      sheet

    """
    key = "sheet"
    aliases = ["sh"]
    locks = "cmd:all()"

    def func(self):
        """
        Handle displaying status.
        """
        # make sure the char has traits - only possible for superuser
        if len(self.caller.traits.all) == 0:
            return

        form = EvForm('commands.templates.charsheet', align='l')
        tr = self.caller.traits
        fields = {
            'A': self.caller.name,
            'B': self.caller.db.race,
            'C': self.caller.db.gender,
            'D': self.caller.db.guild,
            'E': self.caller.db.clan,
            'F': self.caller.db.title,
            'G': tr.LVL.actual,
            'H': self.caller.db.faith,
            'I': self.caller.db.devotion,
            'J': self.caller.db.nation,
            'K': self.caller.db.background,
            'L': tr.STR.actual,
            'M': tr.DEX.actual,
            'N': tr.CON.actual,
            'O': tr.INT.actual,
            'P': tr.WIS.actual,
            'Q': tr.CHA.actual,
            'R': tr.XP.actual,
            'S': tr.ENC.actual,
            'T': tr.ENC.max,
            'U': tr.HP.actual,
            'V': tr.HP.max,
            'W': tr.SP.actual,
            'X': tr.SP.max,
            'Y': tr.EP.actual,
            'Z': tr.EP.max,
        }
        form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        self.caller.msg(unicode(form))

    def _format_trait_val(self, val):
        """Format trait values as bright white."""
        return "|w{}|n".format(val)

class CmdWealth(MuxCommand):
    """
    view character skills
    Usage:
      wealth
    Displays the contents of your wallet.
    """
    key = "wealth"
    aliases = ["wea", "we"]
    locks = "cmd:all()"
    arg_regex = r"\s.+|"

    def func(self):
        from world.economy import format_coin
        # make sure the char has a wallet
        if not hasattr(self.caller.db, "wallet"):
            self.caller.msg("You don't have a wallet.")
            return

        self.caller.msg('You are carrying {}'.format(
            format_coin(self.caller.db.wallet)
))