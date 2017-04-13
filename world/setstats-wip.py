from evennia import default_cmds
from evennia.contrib.menusystem import *
from character.Character import setup_stats
from world import rulebook
 
class CmdSetStats(default_cmds.MuxCommand):
    """
   
   """
 
    key = "setstats"
    locks = "cmd:all()"
     
    def func(self):
        caller = self.caller
        rolls = 25
        msg1 = "Runaria uses a method of rolling the dice to create player attributes. These attributes are: strength, dexterity, constitution, intelligence, wisdom, and charisma. Choose the order of your attributes from the most important to your character to the least important.\n\nAn example is as follows: strength dexterity constitution intelligence wisdom charisma\n\nYou will only be able to roll 25 times, so when you see a decent roll you should accept it."
        if self.caller.db.stat_rolled:            
            return self.caller.msg('You may only roll your stats once.')
        elif not self.caller.db.stat_rolled:
            self.caller.msg(msg1)
            priority = input('Enter your attribute order:')
            while rolls > 0:
                setup_stats(self, priority)
                prompt_yesno(self.caller, question="Do you wish to keep this roll?",
                       yesfunc=self.OnYes,
                       nofunc=self.OnNo,
                       default="N")
        elif rolls = 0
            setup_stats(self,priority)
            return
             
    def OnYes(self, _):
        self.caller.db.stat_rolled = True
        break
     
    def OnNo(self, _):
        rolls = rolls - 1
        return "you have " + str(rolls) + " rolls remaining"