import seaborn as sns
import a8c_colors
import matplotlib as mpl
from matplotlib import pylab as plt
from a8c_colors import *  # @UnusedWildImport
import numpy as np
from warnings import warn


a8c_style ={
          'axes.color_cycle': a8c_colors.default,
          'axes.edgecolor': a8c_colors.a8c_gray,
          'axes.linewidth': .5,
          'axes.facecolor': a8c_colors.a8c_gray_light,
          'axes.formatter.use_mathtext': True,
          'axes.grid': True,
          'axes.grid.which': 'major',
          'axes.hold': True,
          'axes.labelcolor':  a8c_colors.a8c_gray,
          'axes.labelsize': 11.0,
          'axes.labelweight': 'normal',
          'axes.titlesize': 12.0,
          'axes.titleweight': 'normal',
          'axes.unicode_minus': True,
          'axes.xmargin': 0.0,
          'axes.ymargin': 0.0,
          'axes3d.grid': True,
          'figure.autolayout': False,
          'figure.dpi': 120.0,
          'figure.edgecolor': 'white',
          'figure.facecolor': a8c_colors.a8c_gray_light,
          'figure.figsize': [4, 3],
          'figure.frameon': True,
          'figure.subplot.bottom': 0.1,
          'figure.subplot.hspace': 0.5,
          'figure.subplot.left': 0.125,
          'figure.subplot.right': 0.9,
          'figure.subplot.top': 0.9,
          'figure.subplot.wspace': 0.2,
          'font.family': ['sans-serif'],
          'font.monospace': ['Andale Mono',
                              'Nimbus Mono L',
                              'Courier New',
                              'Courier',
                              'Fixed',
                              'Terminal',
                              'monospace'],
          'font.sans-serif': ['Open Sans',
                              'Liberation Sans',
                              'Arial',
                              'Bitstream Vera Sans',
                              'sans-serif'],
          'font.size': 14.0,
          'grid.alpha': 1.0,
          'grid.color': 'white',
          'grid.linestyle': '-',
          'grid.linewidth': 0.5,
          'image.aspect': 'equal',
          'image.cmap': 'Greys',
          'image.interpolation': 'none',
          'image.lut': 256,
          'image.origin': 'upper',
          'interactive': True,
          'legend.borderaxespad': 0.5,
          'legend.borderpad': 0.4,
          'legend.columnspacing': 2.0,
          'legend.fancybox': True,
          'legend.fontsize': 10.0,
          'legend.framealpha': None,
          'legend.frameon': False,
          'legend.handleheight': 0.7,
          'legend.handlelength': 2.0,
          'legend.handletextpad': 0.8,
          'legend.isaxes': True,
          'legend.labelspacing': 0.5,
          'legend.loc': 'best',
          'legend.markerscale': 1.0,
          'legend.numpoints': 1,
          'legend.scatterpoints': 1,
          'legend.shadow': False,
          'lines.antialiased': True,
          'lines.color': a8c_colors.a8c_blue,
          'lines.linestyle': '-',
          'lines.linewidth': 1.5,
          'lines.marker': 'None',
          'lines.markeredgewidth': 0.0,
          'lines.markersize': 7.0,
          'savefig.dpi': 120.0,
          'savefig.edgecolor': a8c_colors.a8c_gray_light,
          'savefig.facecolor': a8c_colors.a8c_gray_light,
          'text.antialiased': True,
          'text.color': a8c_colors.a8c_gray_dark,
          'xtick.color': a8c_colors.a8c_gray,
          'xtick.direction': 'out',
          'xtick.labelsize': 10.0,
          'xtick.major.size': 0.0,
          'xtick.minor.size': 0.0,
          'ytick.color': a8c_colors.a8c_gray,
          'ytick.direction': 'out',
          'ytick.labelsize': 10.0,
          'ytick.major.size': 0.0,
          'ytick.minor.size': 0.0}
sns.set_style(a8c_style)

def fewer_axis_ticks(*args, **kwargs):
    msg = "`fewer_axis_ticks` is an alias to `cleanup` and is deprecated"
    warn(msg)
    return cleanup(*args, **kwargs)


def cleanup(ax=None, x_or_y='xy',
                     n_ticks=3, decimals=1,
                     despine=True):
    ''' Draw fewer ticks on the give axis

    @param ax: matplotlib axis object. If None, use plt.gca(). Default: None
    @param x_or_y: either "x", "y" or "xy". Default: xy
    @param n_ticks: have this number of ticks. Default: 3
    @param decimals: use this number of decimals. Default: 1
    @param despine: either a boolean or a dict.  If True (default),
        call `seaborn.despine(ax)`;
        if a dict, use it as the argument dictionary for `seaborn.despine`
        (no need to provide the `ax` element);
        if False, don't despine
    '''

    assert x_or_y in ('x', 'y', 'xy')
    if ax is None:
        ax = plt.gca()
    for lbl in ('x', 'y'):
        if lbl in x_or_y:
            getter = getattr(ax, 'get_%slim' % lbl)
            setter = getattr(ax, 'set_%sticks' % lbl)
            (mn, mx) = getter()
            tks = np.linspace(mn, mx, n_ticks)
            tks = np.round(tks, decimals=decimals)
            setter(tks)
    if bool(despine): #either `True` or a dict
        if despine is True:
            despine = dict(ax=ax)
        else: # a dict or dict-like
            despine.update(dict(ax=ax))
        sns.despine(**despine)

    return ax



ylabelparams = {'x': 0,
                    'rotation': 0,
                    'ha': 'right'}

def a8c_axes_style(style=None, rc=None):
    """Return a parameter dict for the aesthetic style of the plots.

    Similar to `sns.axes_style`, but also accepts A8C specific styles:
    "a8c_default", "a8c_white", "a8c_whitegrid", "a8c_dark", "a8c_darkgrid", "a8c_ticks"

    """
    if style is None:
        style_dict = {k: mpl.rcParams[k] for k in sns.rcmod._style_keys}

    elif isinstance(style, dict):
        style_dict = style

    else:
        styles = ["a8c_default", "a8c_white", "a8c_whitegrid", "a8c_dark", "a8c_darkgrid", "a8c_ticks"]
        if style not in styles:
            raise ValueError("style must be one of %s" % ", ".join(styles))

        if (not style.startswith('a8c')) and ('a8c_%s' % style in styles):
            # regular seaborn styles
            return sns.axes_style(style, rc)

        # Common parameters
        style_dict = a8c_style.copy()
        if style == 'a8c_default':
            return sns.rcmod._AxesStyle(style_dict)

        # Set grid on or off
        if "grid" in style:
            style_dict.update({
                "axes.grid": True,
                })
        else:
            style_dict.update({
                "axes.grid": False,
                })

        # Set the color of the background, spines, and grids
        if style.startswith("a8c_dark"):
            style_dict.update({
                "axes.facecolor": a8c_colors.a8c_gray_dark,
                "axes.edgecolor": a8c_colors.a8c_gray_light,
                "axes.linewidth": 1,
                "grid.color": a8c_colors.a8c_gray_light,
                "text.color": a8c_colors.a8c_gray_light,
                'xtick.color': a8c_colors.a8c_gray_light,
                'ytick.color': a8c_colors.a8c_gray_light,
                })

        elif style == "a8c_whitegrid":
            style_dict.update({
                "axes.facecolor": "white",
                "axes.edgecolor": a8c_colors.a8c_gray_dark,
                "axes.linewidth": 1.,
                "grid.color": a8c_colors.a8c_gray,
                })

        elif style in ["a8c_white", "a8c_ticks"]:
            style_dict.update({
                "axes.facecolor": "white",
                "axes.edgecolor": a8c_colors.a8c_gray_dark,
                "axes.linewidth": 1.,
                "grid.color": 'red', # a8c_colors.a8c_gray_dark,
                })

        # Show or hide the axes ticks
        if style == "a8c_ticks":
            style_dict.update({
                "xtick.major.size": 6,
                "ytick.major.size": 6,
                "xtick.minor.size": 3,
                "ytick.minor.size": 3,
                })
        else:
            style_dict.update({
                "xtick.major.size": 0,
                "ytick.major.size": 0,
                "xtick.minor.size": 0,
                "ytick.minor.size": 0,
                })

    # Override these settings with the provided rc dictionary
    if rc is not None:
        rc = {k: v for k, v in rc.items() if k in sns.rcmod._style_keys}
        style_dict.update(rc)

    # Wrap in an _AxesStyle object so this can be used in a with statement
    style_object = sns.rcmod._AxesStyle(style_dict)

    return style_object



def sinplot(n_series=3, flip=1):
    '''Helper function to demonstrate some graphics'''
    for i in range(1, n_series + 1):
        if i % 3 == 0:
            x = np.linspace(0, 14, 10)
            plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip, '-o', label='curve %d' % i)
        else:
            x = np.linspace(0, 14, 100)
            plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip, label='curve %d' % i)
    plt.title("Sample sine plot")
    plt.legend()
    plt.xlabel('this is X')
    plt.ylabel('this is Y')

def demo_sinplot(n_series=3, flip=1):
    sinplot(n_series, flip)
    plt.ylabel('this is Y', **ylabelparams)
    fewer_axis_ticks()
    sns.despine()
    return plt.gcf()


if __name__ == '__main__':
    sns.set_style(a8c_style)
    plt.figure()
    sinplot(3)
    plt.title('a8c default')
    styles = ["a8c_dark"]
    for s in styles:
        plt.figure()
        with a8c_axes_style(s):
            fig = sinplot(3, -1)
        plt.title(s)



