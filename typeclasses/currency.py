from items import Item


class Currency(Item):
    pass


class CopperPiece(Currency):

    value = 1
    weight = 0.01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = "This is a small copper coin with the face of the King of the Kingdom on it."
        self.db.value = self.value
        self.db.weight = float(self.weight)

class SilverPiece(Currency):

    value = 10
    wieght = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = "This is a small silver coin with the face of the King of the Kingdom on it. "
        self.db.value = self.value
        self.db.weight = float(self.weight)

class GoldPiece(Currency):

    value = 100
    wieght = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = "This is a small gold coin with the face of the King of the Kingdom on it. "
        self.db.value = self.value
        self.db.weight = float(self.weight)

class PlatinumPiece(Currency):

    value = 1000
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = "This is a small platinum coin with the face of the King of the Kingdom on it. "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class BronzeBit(Currency):
    value = 1
    weight = 0.01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class BronzeDrachma(Currency):
    value = 10
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class SilverDirhim(Currency):
    value = 100
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class GoldDinar(Currency):
    value = 1000
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class TsuhoCoin(Currency):
    value = 1
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class GenboCoin(Currency):
    value = 10
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class ShohoCoin(Currency):
    value = 100
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)


class MonCoin(Currency):
    value = 1000
    weight = .01

    def at_object_creation(self):
        super(Item, self).at_object_creation()
        self.locks.add(";".join(("equip:false()",
                                 "get:true()",
                                 "view:all()",
                                 )))
        self.db.desc = " "
        self.db.value = self.value
        self.db.weight = float(self.weight)