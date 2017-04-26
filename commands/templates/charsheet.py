"""
Character sheet EvForm template.
"""

import re

FORMCHAR = "x"
TABLECHAR = "o"

FORM = """
-=-=-=-=-=-=-=-=-=-=-=-=-=-=|C[ |rCharacter Sheet |C]|n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-o
                                                                             ||
|YName|n: xxxxxxxxxxxxxAxxxxxxxxxxxxxx         |CStrength|n      : xLxx  ||
|YRace|n: xxxxxxxxxxxxxBxxxxxxxxxxxxxx         |CDexterity|n     : xMxx  ||
|YSex|n  : xxxxxxxxxxxxxCxxxxxxxxxxxxxx        |CConstitution|n  : xNxx  ||
|YGuild|n: xxxxxxxxxxxxxDxxxxxxxxxxxxxx        |CIntelligence|n  : xOxx  ||
|YClan|n : xxxxxxxxxxxxxExxxxxxxxxxxxxx        |CWisdom|n        : xPxx  ||
|YTitle|n: xxxxxxxxxxxxxFxxxxxxxxxxxxxx        |CCharisma|n      : xQxx  ||
|YLevel|n: xGx                                 oooooooooooooooooooooooo  ||
|YFaith|n: xxxxxxxxxxxxxHxxxxxxxxxxxxxx          ooooooooooo1oooooooooooo  ||
|YDevotion|n: xxxxxxxxxxxxxIxxxxxxxxxxxxxx         oooooooooooooooooooooooo  ||
|YNation|n: xxxxxxxxxxxxxJxxxxxxxxxxxxxx           |CExperience|n    : xxRxx / xxxxSxxxx  ||
|YBackground|n   : xxxxxxxxxxxxxKxxxxxxxxxxxxxx    |CEncumbrance|n   : xTxx (xxUxx)  || 
"""
FORM = re.sub(r'\|$', r'', FORM, flags=re.M)
