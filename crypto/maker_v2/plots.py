import matplotlib.pyplot as plt
import numpy as np

def plot_positions(price, positions, s=2, alpha=0.3, scatter_price=False, ax = None):
    # create new figure and axis
    if ax is None:
        _, ax = plt.subplots()
    # plot price as line with points marked with circles

    if scatter_price:
        ax.scatter(np.arange(0,len(price)), price, color='lightgray', s=s)
    else:
        ax.plot(price, color='lightgray', linestyle='-', marker='o', markersize=5)
    ax.scatter(np.where(positions == 1)[0], price[positions == 1], color='g', s=s, alpha=alpha, zorder=10)
    ax.scatter(np.where(positions == -1)[0], price[positions == -1], color='r', s=s, alpha=alpha, zorder=10)
    return ax

def adjust_xy(ax, x, xlim):
    # adjust x and y limits
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(min(x[xlim[0]:xlim[1]])*0.8, 1.1 * max(x[xlim[0]:xlim[1]]))


def plot_peaks_throughs(y, idx, s=2, alpha=0.3):
    throughs = idx[::2]
    peaks = idx[1::2]

    # plot
    plt.plot(y, color='darkgray')
    plt.scatter(throughs, y[throughs], c='r', s=s, alpha=alpha, zorder=10)
    plt.scatter(peaks, y[peaks], c='g', s=s, alpha=alpha, zorder=10)