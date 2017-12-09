from items import Item


class CursedBone(Item):

    def at_object_creation(self):
        super(CursedBone, self).at_object_creation()
        self.key = "Cursed bone"
        self.name = "|xCursed bone|n"
        self.aliases = ["Cursed bone","bone"]
        self.db.desc = "a fragment of bone that has been imbued with the energies of the netherworld"
        self.db.weight = 0.1


class BloodGem(Item):

    def at_object_creation(self):
        super(BloodGem, self).at_object_creation()
        self.key = "Blood Gem"
        self.name = "|RBlood gem|n"
        self.db.desc = "Glowing with inner light, this gem is forged from the crystallized blood of a sorcerer and imbued with restorative powers"
        self.db.weight = 0.05

    def at_consume(self):
        pass


class BoneDust(Item):
    def at_object_creation(self):
        super(BoneDust,self).at_object_creation()
        self.key = ""
        self.name = ""
        self.db.desc = ""
        self.db.weight = ""

    def at_use(self):
        pass