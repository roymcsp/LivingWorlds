"""
powers sheet EvForm template.
"""

import re

FORMCHAR = "x"
TABLECHAR = "o"

FORM = """
=-=-=-=-=-|C[ |rxAExxxx Guild Powers |C]|n-=-=-=-=-=-=-=-=-o
                                                    ||
      Level                   Power                 ||
        1:      xAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||                       
        2:      xBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||                   
        3:      xCxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||                       
        4:      xDxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||                      
        5:      xExxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        6:      xFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        7:      xGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        8:      xHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        9:      xIxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        10:     xJxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        11:     xKxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        12:     xLxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        13:     xMxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        14:     xNxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        15:     xOxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        16:     xPxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        17:     xQxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        18:     xRxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        19:     xSxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        20:     xTxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        21:     xUxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        22:     xVxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        23:     xWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        24:     xXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        25:     xYxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        26:     xZxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx    ||
        27:     xAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ||
        28:     xABxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ||
        29:     xACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ||
        30:     xADxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   ||
                                                    ||
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-o

"""
FORM = re.sub(r'\|$', r'', FORM, flags=re.M)
