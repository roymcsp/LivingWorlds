from evennia import command

class CmdBackground(Command):
    """This is the command string that will assign a background onto a character,
     and the cooresponding command set."""

    key = "choose"
    locks = "cmd:all()"

    def func (self):
        caller = self.caller
        args = self.args.strip().lower

def apply_background(character, background):
    """Causes a Character to "have" a named background.
    Args: character: the character object having a background
    background (str, Background): the name of the background to apply
    """
    if isinstance (background, Background):
        background = background.name

        character.db.background = background.race
        character.message('Your background has been set to {}.' .format(background.name))

class Background(object):
    def __init__(self):
        self.name = ""


class Urchin(Background):
    def __init__(self):
        super(Urchin, self).__init__()
        self.name = "Urchin"
        self.cmdset.add(CmdSetUrchin, permanent=True)

class Noble(Background):
    def __init__(self):
        super(Noble, self).__init__()
        self.name = 'Noble'
        self.cmdset.add(CmdSetNoble, permanent=True)

class Nomad(Background):
    def __init__(self):
        super(Nomad, self).__init__()
        self.name = "Nomad"
        self.cmdset.add(CmdSetNoble, permanent=True)


class Gypsy(Background):
    def __init__(self):
        super(Gypsy, self). __init__()
        self.name = 'Gypsy'
        self.cmdset.add(CmdSetGpysy, permanent=True)

class Farmer(Background):
    def __init__(self):
        super(Farmer, self). __init__()
        self.name = 'Farmer'
        self.cmdset.add(CmdSetFarmer, permanent=True)

class Tradesman(Background):
    def __init__(self):
        super(Tradesman, self). __init__()
        self.name = 'tradesman'
        self.cmdset.add(CmdSetTradesman, permanent=True)


