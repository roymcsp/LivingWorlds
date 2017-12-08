from objects import Object

class CursedBone(Object):

    def at_object_creation(self):
        self.key = "Cursed bone"
        self.name = "{xCursed bone{n"
        self.aliases = "Cursed bone"
        self.db.desc = "a fragment of bone that has been imbued with the energies of the netherworld"
        self.db.weight = 0.1
    
class BloodGem(Object):
    def at_object_creation(self):
        key = "Blood Gem"
        name = "{RBlood gem{n"
        self.db.desc = "Glowing with inner light, this gem is forged from the crystallized blood of a sorcerer and imbued with restorative powers"
        self.db.weight = 0.05
        #self.cmdset.add_default(CmdSetConsumable, permanent=True)