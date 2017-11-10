"""
Character sheet EvForm template.
"""

import re

FORMCHAR = "x"
TABLECHAR = "o"

FORM = """
=-=-=-=-=-=-=-=-|C[ |rCharacter Sheet |C]|n-=-=-=-=-=-=-=-=-=-=-=-=-o
                                                           ||
||
||
||
||
||
||
||
||
||
||
||
                                                           ||
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-o
"""
FORM = re.sub(r'\|$', r'', FORM, flags=re.M)