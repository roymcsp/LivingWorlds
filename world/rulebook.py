import re
import random
from math import floor
from collections import defaultdict
from evennia.utils import utils, make_iter


class DiceRollError(Exception):
    """Default error class in die rolls/skill checks.
    Args:
        msg (str): a descriptive error message
    """
    def __init__(self, msg):
        self.msg = msg


def _parse_roll(xdyz):
    """Parser for XdY+Z dice roll notation.
    Args:
        xdyz (str): dice roll notation in the form of XdY[+|-Z][-DL]
            - _X_ - the number of dice to roll
            - _Y_ - the number of faces on each die
            - _+/-Z_ - modifier to add to the total after dice are rolled
            - _-DL_ - if the expression ends with literal L, sort the rolls
                and drop the lowest _D_ rolls before returning the total.
                _D_ can be omitted and will default to 1.
    """
    xdyz_re = re.compile(r'(\d+)d(\d+)([+-]\d+(?!L))?(?:-(\d*L))?')
    args = re.match(xdyz_re, xdyz)
    if not args:
        raise DiceRollError('Invalid die roll expression. Must be format `XdY[+-Z|-DL]`.')

    num, die, bonus, drop = args.groups()
    num, die = int(num), int(die)
    bonus = int(bonus or 0)
    drop = int(drop[:-1] or 1) if drop else 0

    if drop >= num:
        raise DiceRollError('Rolls to drop must be less than number of rolls.')

    return num, die, bonus, drop


def roll_max(xdyz):
    """Determines the maximum possible roll given an XdY+Z expression."""
    num, die, bonus, drop = _parse_roll(xdyz)
    return (num - drop) * die + bonus


def d_roll(xdyz, total=True):
    """Implementation of XdY+Z dice roll.
    Args:
        xdyz (str): dice roll expression in the form of XdY[+Z] or XdY[-Z]
        total (bool): if True, return a single value; if False, return a list
            of individual die values
    """
    num, die, bonus, drop = _parse_roll(xdyz)
    if bonus > 0 and not total:
        raise DiceRollError('Invalid arguments. `+-Z` not allowed when total is False.')

    rolls = [random.randint(1, die) for _ in range(num)]

    if drop:
        rolls = sorted(rolls, reverse=True)
        [rolls.pop() for _ in range(drop)]
    if total:
        return sum(rolls) + bonus
    else:
        return rolls