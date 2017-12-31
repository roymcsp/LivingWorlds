"""
Command sets

All commands in the game must be grouped in a cmdset.  A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.

"""

from evennia import default_cmds, CmdSet
from evennia.commands.default import general, account, system, comms
from commands import chargen, movecommands, sensorycommands, extendedcommands, equip, chartraits, comm, acct, syst
from world import races, background


class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc available on in-game Character objects. It is merged with
    the `AccountCmdSet` when an Account puppets a Character.
    """
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(CharacterCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #

        self.add(syst.CmdAbout())
        self.remove(system.CmdAbout())
        self.remove(general.CmdAccess())
        self.remove(general.CmdHome())
        self.remove(general.CmdSetDesc())
        self.add(extendedcommands.CmdExtendedLook())
        self.add(extendedcommands.CmdExtendedDesc())
        self.add(extendedcommands.CmdExtendedGet())
        self.add(extendedcommands.CmdExtendedGive())
        self.add(extendedcommands.CmdExtendedDrop())
        self.add(extendedcommands.CmdGameSeason())
        self.add(sensorycommands.SensesCmdSet)
        self.add(movecommands.ExitErrorCmdSet)
        self.add(equip.EquipCmdSet)
        self.add(chartraits.CharTraitCmdSet)


class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the cmdset available to the Account at all times. It is
    combined with the `CharacterCmdSet` when the Account puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """
    key = "DefaultAccount"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(AccountCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        # Account specific Commands
        self.remove(account.CmdOOCLook())
        self.remove(account.CmdIC())
        self.remove(account.CmdOOC())
        self.remove(account.CmdCharCreate())
        self.remove(account.CmdCharDelete())
        self.remove(account.CmdOption)
        self.remove(account.CmdQuit())
        self.remove(account.CmdPassword())
        self.remove(account.CmdColorTest())
        self.add(acct.CmdOption())
        self.add(acct.CmdQuit())
        self.add(acct.CmdPassword())
        self.add(acct.CmdColorTest())
        self.add(acct.CmdQuell())

        # Comm commands
        self.remove(comms.CmdPage())
        self.remove(comms.CmdChannels)
        self.add(comm.CmdChannels)
        self.add(comm.CmdCdestroy())
        self.add(comm.CmdChannelCreate())
        self.add(comm.CmdClock())
        self.add(comm.CmdCBoot())
        self.add(comm.CmdCemit())
        self.add(comm.CmdCWho())
        self.add(comm.CmdCdesc())
        self.add(comm.CmdTell())


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.  This
    holds commands like creating a new account, logging in, etc.
    """
    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the cmdset
        """
        super(UnloggedinCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """
    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        This is the only method defined in a cmdset, called during
        its creation. It should populate the set with command instances.

        As and example we just add the empty base `Command` object.
        It prints some info.
        """
        super(SessionCmdSet, self).at_cmdset_creation()
        #
        # any commands you add below will overload the default ones.
        #
        self.remove(account.CmdSessions())


class ChargenWelcomeCmdset(CmdSet):
    """
    This cmdset is used in character generation areas.
    """
    
    key = "Chargen"

    def at_cmdset_creation(self):
        """this is called at initialization"""
        self.add(chargen.CmdRules())


class ChargenRaceGenderCmdset(CmdSet):
    """
    This cmdset is used in character generation to set gender and race
    """
    key = "Chargen"

    def at_cmdset_creation(self):
        self.add(chargen.CmdGender())
        self.add(races.CmdRace())

class ChargenBackgroundCmdset(CmdSet):
    """
    This cmdset is used in character generation to set background 
    """
    key = 'Chargen'

    def at_cmdset_creation(self):
        self.add(background.CmdBackground())

class ChargenPassVeilCmdSet(CmdSet):
    """
    This cmdset is used to finalize character creation and enter into the game
    """
    key = 'Chargen'

    def at_cmdset_creation(self):
        self.add(chargen.PassVeil())

