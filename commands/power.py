from commands.command import MuxCommand
from evennia.utils.evform import EvForm


class CmdPower(MuxCommand):
    """
    view character status
    Usage:
      sheet

    """
    key = "power"
    aliases = ["powers"]
    locks = "cmd:all()"
    help_category = "commands"

    def func(self):
        """
        Handle displaying power list.
        """

        caller = self.caller
        form = EvForm('commands.templates.powersheet', align='l')

        if 'artisan' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Artisan'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'assassin' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Assassin'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'druid' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Driuid'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'fighter' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Fighter'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'harbinger' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Harbinger'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'helotyr' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Helotyr'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'mage' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Mage'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'merchant' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Merchant'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'monk' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Monk'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'ranger' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Ranger'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'samurai' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Samurai'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'sarthoar' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Sarthoar'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'shaman' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Shaman'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'sorcerer' in caller.db.guild:
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
                'AE': 'Sorcerer'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'templar' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Templar'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'thief' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Thief'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'trader' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Trader'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        if 'warrior' in caller.db.guild:
            fields = {
                'A': '',
                'B': '',
                'C': '',
                'D': '',
                'E': '',
                'F': '',
                'G': '',
                'H': '',
                'I': '',
                'J': '',
                'K': '',
                'L': '',
                'M': '',
                'N': '',
                'O': '',
                'P': '',
                'Q': '',
                'R': '',
                'S': '',
                'T': '',
                'U': '',
                'V': '',
                'W': '',
                'X': '',
                'Y': '',
                'Z': '',
                'AA': '',
                'AB': '',
                'AC': '',
                'AD': '',
                'AE': 'Warrior'
            }
            form.map({k: self._format_trait_val(v) for k, v in fields.iteritems()})

        self.caller.msg(unicode(form))

    def _format_trait_val(self, val):
        """Format trait values as bright magenta."""
        return "|m{}|n".format(val)
