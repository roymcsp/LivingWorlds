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
            statorder = input('Enter your attribute order:')
            stats_in_order = statorder.strip().split()