from typeclasses.items import item


class Currency(Item):

class CopperPiece(Currency):

    value = 1
    weight = 0.01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 )))
        self.db.value = self.value
        self.db.weight = float(self.weight)