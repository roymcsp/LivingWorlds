import re
import random
from math import floor
from collections import defaultdict
from evennia.utils import utils, make_iter

LEVEL = {
    '1': {'xp': 1, 'coins': 0},
    '2': {'xp': 1, 'coins': 0},
    '3': {'xp': 1, 'coins': 0},
    '4': {'xp': 1, 'coins': 0},
    '5': {'xp': 1, 'coins': 0},
    '6': {'xp': 1, 'coins': 0},
    '7': {'xp': 1, 'coins': 0},
    '8': {'xp': 1, 'coins': 0},
    '9': {'xp': 1, 'coins': 0},
    '10': {'xp': 1, 'coins': 0},
    '11': {'xp': 1, 'coins': 0},
    '12': {'xp': 1, 'coins': 0},
    '13': {'xp': 1, 'coins': 0},
    '14': {'xp': 1, 'coins': 0},
    '15': {'xp': 1, 'coins': 0},
    '16': {'xp': 1, 'coins': 0},
    '17': {'xp': 1, 'coins': 0},
    '18': {'xp': 1, 'coins': 0},
    '19': {'xp': 1, 'coins': 0},
    '20': {'xp': 1, 'coins': 0},
    '21': {'xp': 1, 'coins': 0},
    '22': {'xp': 1, 'coins': 0},
    '23': {'xp': 1, 'coins': 0},
    '24': {'xp': 1, 'coins': 0},
    '25': {'xp': 1, 'coins': 0},
    '26': {'xp': 1, 'coins': 0},
    '27': {'xp': 1, 'coins': 0},
    '28': {'xp': 1, 'coins': 0},
    '29': {'xp': 1, 'coins': 0},
    '30': {'xp': 1, 'coins': 0},
}

SKILLLVL = {
    '1': {'experience': 1, 'coins': 0},
    '2': {'experience': 1, 'coins': 0},
    '3': {'experience': 1, 'coins': 0},
    '4': {'experience': 1, 'coins': 0},
    '5': {'experience': 1, 'coins': 0},
    '6': {'experience': 1, 'coins': 0},
    '7': {'experience': 1, 'coins': 0},
    '8': {'experience': 1, 'coins': 0},
    '9': {'experience': 1, 'coins': 0},
    '10': {'experience': 1, 'coins': 0},
    '11': {'experience': 1, 'coins': 0},
    '12': {'experience': 1, 'coins': 0},
    '13': {'experience': 1, 'coins': 0},
    '14': {'experience': 1, 'coins': 0},
    '15': {'experience': 1, 'coins': 0},
    '16': {'experience': 1, 'coins': 0},
    '17': {'experience': 1, 'coins': 0},
    '18': {'experience': 1, 'coins': 0},
    '19': {'experience': 1, 'coins': 0},
    '20': {'experience': 1, 'coins': 0},
    '21': {'experience': 1, 'coins': 0},
    '22': {'experience': 1, 'coins': 0},
    '23': {'experience': 1, 'coins': 0},
    '24': {'experience': 1, 'coins': 0},
    '25': {'experience': 1, 'coins': 0},
    '26': {'experience': 1, 'coins': 0},
    '27': {'experience': 1, 'coins': 0},
    '28': {'experience': 1, 'coins': 0},
    '29': {'experience': 1, 'coins': 0},
    '30': {'experience': 1, 'coins': 0},
    '31': {'experience': 1, 'coins': 0},
    '32': {'experience': 1, 'coins': 0},
    '33': {'experience': 1, 'coins': 0},
    '34': {'experience': 1, 'coins': 0},
    '35': {'experience': 1, 'coins': 0},
    '36': {'experience': 1, 'coins': 0},
    '37': {'experience': 1, 'coins': 0},
    '38': {'experience': 1, 'coins': 0},
    '39': {'experience': 1, 'coins': 0},
    '40': {'experience': 1, 'coins': 0},
    '41': {'experience': 1, 'coins': 0},
    '42': {'experience': 1, 'coins': 0},
    '43': {'experience': 1, 'coins': 0},
    '44': {'experience': 1, 'coins': 0},
    '45': {'experience': 1, 'coins': 0},
    '46': {'experience': 1, 'coins': 0},
    '47': {'experience': 1, 'coins': 0},
    '48': {'experience': 1, 'coins': 0},
    '49': {'experience': 1, 'coins': 0},
    '50': {'experience': 1, 'coins': 0},
    }

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

def parse_health(target):
    current = target.traits.HP.current
    max_health = target.traits.HP.max

    if max_health > 0:
        percent = int(current / max_health * 100)
    else:
        percent = 0

    if percent == 100:
        return '|040in perfect condition|n'
    elif percent > 99:
        return '|040scratched|n'
    elif percent > 95:
        return '|420bleeding lightly|n'
    elif percent > 90:
        return '|420bleeding|n'
    elif percent > 80:
        return '|420bleeding moderately|n'
    elif percent > 70:
        return '|320wounded|n'
    elif percent > 60:
        return '|320severly wounded|n'
    elif percent > 50:
        return '|320critically wounded|n'
    elif percent > 40:
        return '|510gushing blood|n'
    elif percent > 30:
        return '|510Critically Damaged|n'
    elif percent > 20:
        return '|500Critically Damaged|n'
    elif percent > 15:
        return '|500Critically Damaged|n'
    elif percent > 10:
        return '|500Critically Damaged|n'
    elif percent > 5:
        return '|500near death|n'
    else:
        return '|[300Destroyed|n'
