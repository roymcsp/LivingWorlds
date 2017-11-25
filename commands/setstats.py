# -*- coding: UTF-8 -*-

from evennia import CmdSet
from commands.command import MuxCommand
from evennia.utils.evmenu import EvMenu
from world import traitcalcs, rulebook

from random import randint


class StatsCmdSet(CmdSet):
    key = "setstats"

    def at_cmdset_creation(self):
        """
        Add command to the set - this set will be attached to
        the object (item or room) where setstats is to be done.
        """
        self.add(CmdSetStats())


class CmdSetStats(MuxCommand):
    """
    Sends initial mesg[0] if never rolled before, then enters into the menu
    asking for roll order, then rolls sets stats as traits and exits.
    """
    key = "setstats"
    locks = "cmd:all()"

    def func(self):
        account_caller = True
        char = self.caller
        mesg = ("Mercadia uses a method of rolling the dice to create account attributes. "
                "These attributes are: strength, dexterity, constitution, intelligence, "
                "wisdom, and charisma. Choose the order of your attributes from the most "
                "important to your character to the least important.\n\n"
                "An example is as follows: strength dexterity constitution intelligence "
                "wisdom charisma\n\n"
                "You will only be able to roll up to 25 times, so when you see a decent "
                "roll, you should accept it.", "You may only roll your stats once.")
        if char.traits.STR.actual > 5 or char.traits.INT.actual > 5 or char.traits.WIS.actual > 5 or \
           char.traits.DEX.actual > 5 or char.traits.CON > 5 or char.traits.CHA.actual > 5:
            return self.caller.msg(mesg[1])
        else:
            self.caller.msg(mesg[0])

        EvMenu(self.caller, "commands.setstats", startnode="menu_start",
               cmd_on_exit=None, persistent=False,
               stats={"STR": "Strength", "INT": "Intelligence", "WIS": "Wisdom",
                      "DEX": "Dexterity", "CON": "Constitution", "CHA": "Charisma"},
               choice=[], remaining_choices=[], rolls=[], roll_count=25)


def menu_start(caller, raw_string):
    menu = caller.ndb._menutree
    options = ()
    restart = "x" in raw_string  # Denotes restarting the stat selection process
    choice = menu.choice if menu.choice and not restart else []
    remain = menu.stats.keys() if restart or not menu.remaining_choices else menu.remaining_choices
    start_text = "Choose stat order high to low from the following:\n"
    if raw_string.strip().isdigit() and 1 <= int(raw_string.strip()) <= len(remain):
        # If a stats choice is made, ( 1 through highest choice, up to 6 )
        choice.append(remain.pop(int(raw_string.strip()) - 1))  # move the choice to list of choices.
    text = ("Current Stat order high to low is:\n|w" + ", ".join(choice) + "|n") if choice else start_text
    if len(choice) == 6 and len(remain) == 0:  # if all choices made and none remain...
        text += ("\nAll stats priorities have been chosen."
                 "\nPress [|w|lc|ltEnter|le]|n to begin rolling stat values.")
        if not restart:
            options = ({"key": "_default", "goto": "make_rolls"},)
    else:
        for each in remain:
            options += ({"desc": menu.stats[each], "goto": "menu_start"},)
        options += ({"key": "_default", "goto": "menu_start"},)
    options += ({"desc": "Start again", "key": "X", "goto": "menu_start"},)
    menu.choice = choice
    menu.remaining_choices = remain
    return text, options


def make_rolls(caller):
    menu = caller.ndb._menutree
    roll_count = menu.roll_count
    roll_count -= 1
    plural = "s" if roll_count != 1 else ""
    rolls = []
    for _ in range(6):
        rolls.append(rulebook.d_roll('4d6-1L'))
    rolls.sort(reverse=True)
    show = []
    choice = menu.choice
    for each in range(6):  # Combine sorted rolls with stat priorities.
        show.append(choice[each] + ": " + str(rolls[each]))
    text = ", ".join(show) + "\n"  # Add newline; more text to come!
    if roll_count:  # Rolls remain to be made.
        text += "You have {count} roll{plural} remaining.".format(count=roll_count, plural=plural)
        options = ({"desc": "Accept this roll.", "key": "A", "goto": "show_stats"},)
        options += ({"desc": "Press [|w|lc|ltEnter|le|n] to roll again.",
                     "key": "E", "goto": "make_rolls"},)
        options += ({"key": "_default", "goto": "make_rolls"},)
    else:  # All rolls have been used.
        text += "Last roll completed. Press enter to continue."
        options = ({"key": "_default", "goto": "show_stats"},)
    menu.rolls = rolls
    menu.roll_count = roll_count
    return text, options


def show_stats(caller):

    menu = caller.ndb._menutree
    rolls = menu.rolls
    choice = menu.choice
    text = "Stats: (before adding race modifiers)\n"

    for index, each in enumerate(choice):
        if caller.traits[each] is None:
            caller.traits.add(each, menu.stats[each], "static", rolls[index])

        else:
            caller.traits[each].base = rolls[index]

        traitcalcs.calculate_secondary_traits(caller.traits)

    text += "\n".join([str(caller.traits[each].base) for each in menu.stats.keys()])
    options = None
    return text, options
