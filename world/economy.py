"""
Economy module.
"""
from evennia.utils.dbserialize import _SaverDict

# Constants

#: (int) copper coins
CP = 1

#: (int) silver coins
SP = 100

#: (int) gold coins
GP = 10000

#: (int) platinum coins
PP = 100000

_WALLET_KEYS = ('PP', 'GP', 'SP', 'CP')


class InsufficientFunds(ValueError):
    """Represents an error in a financial transaction."""
    pass


def value_to_coin(value):
    """Given a base value in CC, return smallest number of coins."""
    if value:
        if isinstance(value, int):
            pp = value / PP
            value %= PP
            gp = value / GP
            sp = value / SP
            cp = value % SP
            return dict(CP=cp, SP=sp, GP=gp, PP=pp)
        elif isinstance(value, (dict, _SaverDict)):
            return {c: v for c, v in value.iteritems()
                    if c in _WALLET_KEYS}
    return None

def coin_to_value(coins):
    """Given a dict of coin: value pairs, return the total value in CP.
    Args:
        coins (int, dict): dict of coin names and values; assumes CP if an int
    """
    if coins is None:
        return None
    if not isinstance(coins, (int, dict, _SaverDict)):
        raise TypeError("'coins' must be a dict of 'coin': count pairs.")
    if isinstance(coins, int):
        coins = {'CP': coins}
    return (coins.get('PP', 0) * PP +
            coins.get('GP', 0) * GP +
            coins.get('SP', 0) * SP +
            coins.get('CP', 0))


def transfer_funds(src, dst, value_or_coin):
    """Transfers a given value from src wallet to dst wallet.
    Note:
        If either 'src' or 'dst' are None, the money is created
        or destroyed by this function.
    """
    src_val = coin_to_value(src.db.wallet) if src else 0
    dst_val = coin_to_value(dst.db.wallet) if dst else 0
    xfr_val = coin_to_value(value_or_coin)
    # check there's enough
    if src is not None and src_val < xfr_val:
        raise InsufficientFunds("Insufficient funds.")

    if src is not None:
        src.db.wallet = value_to_coin(src_val - xfr_val)

    if dst is not None:
        dst.db.wallet = value_to_coin((dst_val or 0) + xfr_val)


def format_coin(value_or_coin):
    """Returns a string representing a value as numbers of coins."""

    coins = value_to_coin(value_or_coin) or {'PP': 0, 'GP': 0, 'SP': 0, 'CP': 0}
    pp, gp, sp, cp = coins.get('PP', 0), coins.get('GP', 0), coins.get('SP', 0), coins.get('CP', 0)
    output = ""
    if pp:
        output += "|w{}|n PP".format(pp)
    if gp:
        output += "|w{}|n GP ".format(gp)
    if sp:
        output += "|w{}|n SP ".format(sp)
    if cp:
        output += "|w{}|n CP".format(cp)
    if output == "":
        output = "0 CP"
    return output.strip()