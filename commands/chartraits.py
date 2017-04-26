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
        self.add(CmdTraits())
        self.add(CmdSkills())
        self.add(CmdWealth())

class CmdSheet(MuxCommand):
    """
    view character status
    Usage:
      sheet[/skills]
    Switch:
      sk[ills] - also display a summary of all character skills
    Displays a detailed summary of your character's information.
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

        form = EvForm('commands.templates.charsheet', align='r')
        tr = self.caller.db.traits
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
            'S': tr.XP.level_boundaries[tr.LV.actual],
            'T': tr.ENC.actual,
            'U': tr.ENC.max,
        }
        form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        gauges = EvTable(
            "|CHP|n", "|CSP|n", "|CEP|n",
            table=[["{} / {}".format(self._format_trait_val(tr.HP.actual),
                                     self._format_trait_val(tr.HP.max))],
                   ["{} / {}".format(self._format_trait_val(tr.SP.actual),
                                     self._format_trait_val(tr.SP.max))],
                   ["{} / {}".format(self._format_trait_val(tr.EP.actual),
                                     self._format_trait_val(tr.EP.max))]],
            align='c',
            border="incols"
        )

        form.map(tables={1: gauges})

        self.caller.msg(unicode(form))

        if any(sw.startswith('sk') for sw in self.switches):
            self.caller.execute_cmd('skills')

    def _format_trait_val(self, val):
        """Format trait values as bright white."""
        return "|w{}|n".format(val)


class CmdTraits(MuxCommand):
    """
    view character status
    Usage:
      traits <traitgroup>
    Args:
        traitgroup - one of pri[mary], sec[ondary], sav[es],
                     com[bat], enc[umbrance], or car[ry]
    Displays a summary of your character's traits by group.
    """
    key = "traits"
    aliases = ["trait", "tr", "tra"]
    locks = "cmd:all()"
    arg_regex = r"\s.+|"

    def func(self):
        from world import archetypes
        # make sure the char has traits - only possible for superuser
        if len(self.caller.traits.all) == 0:
            self.caller.msg("You don't have any traits.")
            return

        table = None
        tr = self.caller.traits
        traits = []
        if self.args.startswith('pri'):
            title = 'Primary Traits'
            traits = archetypes.PRIMARY_TRAITS
        elif self.args.startswith('sav'):
            title = 'Save Rolls'
            traits = archetypes.SAVE_ROLLS
        elif self.args.startswith('com'):
            title = 'Combat Stats'
            traits = archetypes.COMBAT_TRAITS
        elif self.args.startswith('sec'):
            title = 'Secondary Traits'
            data = [["|C{:<29.29}|n : |w{:>4}|n".format(
                        tr[t].name, tr[t].actual)
                    for t in ('HP', 'SP')],
                    ["|C{:<28.28}|n : |w{:>4}|n".format(
                        tr[t].name, tr[t].actual)
                    for t in ('BM', 'WM')]]
            table = EvTable(header=False, table=data)
        elif self.args.startswith('enc') or self.args.startswith('car'):
            title = 'Encumbrance'
            data = [["|C{:<30.30s}|n : |w{:>4}|n / |w{:>5}|n".format(
                        tr.ENC.name, tr.ENC.actual, tr.ENC.max
                     ),
                     "|C{:30.30s}|n : |w{:>+12}|n".format(
                         'Encumbrance Penalty', tr.MV.mod
                     ),
                     "|C{:30.30s}|n : |w{:>12}|n".format(
                         tr.MV.name, tr.MV.actual
                     )]]
            table = EvTable(header=False, table=data)
        else:
            self.caller.msg("Usage: traits <traitgroup>")
            return
        if not table:
            data = []
            for i in xrange(3):
                data.append([self._format_trait_3col(tr[t])
                             for t in traits[i::3]])
            table = EvTable(header=False, table=data)

        self.caller.msg("  |Y{}|n".format(title))
        self.caller.msg(unicode(table))

    def _format_trait_3col(self, trait):
        """Return a trait : value pair formatted for 3col layout"""
        return "|C{:<16.16}|n : |w{:>4}|n".format(
                    trait.name, trait.actual)


class CmdSkills(MuxCommand):
    """
    view character skills
    Usage:
      skills <skillgroup>
    Args:
        skillgroup - one of str[ength], per[ception], int[elligence],
                     dex[terity], or cha[risma]
    Displays a summary of your character's skills by group.
    """
    key = "skills"
    aliases = ["skill", "sk"]
    locks = "cmd:all()"
    arg_regex = r"\s.+|"

    def func(self):
        from world import skills
        # make sure the char has skills
        if len(self.caller.skills.all) == 0:
            self.caller.msg("You don't have any skills.")
            return

        sk = self.caller.skills
        sk_list = []

        if len(self.args.strip()) > 0:
            if self.args.lower().startswith('str'):
                title = 'Strength Based Skills'
                sk_list = skills.STR_SKILLS
            elif self.args.lower().startswith('per'):
                title = 'Perception Based Skills'
                sk_list = skills.PER_SKILLS
            elif self.args.lower().startswith('int'):
                title = 'Intelligence Based Skills'
                sk_list = skills.INT_SKILLS
            elif self.args.lower().startswith('dex'):
                title = 'Dexterity Based Skills'
                sk_list = skills.DEX_SKILLS
            elif self.args.lower().startswith('cha'):
                title = 'Charisma Based Skills'
                sk_list = skills.CHA_SKILLS
            else:
                self.msg('Usage: skills [<skillgroup>]')
                return

            table = EvTable(header=False,
                            table=[[self._format_skill_3col(sk[s])]
                                  for s in sk_list])
        else:
            title = 'Skills'
            data = []
            for i in xrange(3):
                data.append([self._format_skill_3col(sk[s])
                             for s in skills.ALL_SKILLS[i::3]])

            table = EvTable(header=False, table=data)

        self.caller.msg("  |Y{}|n".format(title))
        self.caller.msg(unicode(table))

    def _format_skill_3col(self, skill):
        """Return a trait : value pair formatted for 3col layout"""
        return "|M{:<16.16}|n : |w{:>4}|n".format(
                    skill.name, skill.actual)


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