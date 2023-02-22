import numpy as np
import pandas as pd

from plots import *

def add_fixed_holding_periods(enex, n=None):
    """
    Add fixed holding periods to entry and exit vector `enex`.

    Parameters
    ----------
    enex : numpy.ndarray -- entry and exit vector
    n : int -- number of periods to entry/exit position
    """
    if n is None:
        n = len(enex)
    new_positions = enex.copy()
    m = len(enex)
    counter = 0
    for i in range(m):
        if new_positions[i] != 0:
            counter = n
        elif new_positions[i] == 0 and counter > 0:
            counter -= 1
            new_positions[i] = new_positions[i-1]
        elif counter > 0:
            counter = 0
    return new_positions


def debug(x, ma, pos, T1, T2):
    ax = plot_positions(x, pos, s=10)
    ax.plot(ma)
    # set x-limit
    ax.set_xlim(T1, T2)
    adjust_xy(ax, x, (T1, T2))
