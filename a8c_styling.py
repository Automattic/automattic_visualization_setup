import seaborn as sns
import a8c_colors
import matplotlib as mpl
from matplotlib import pylab as plt
from a8c_colors import *  # @UnusedWildImport
import numpy as np
from warnings import warn


from seaborn import despine #for shorter typing

a8c_style_gray ={
          'axes.color_cycle':a8c_colors.default,
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
          'figure.figsize': [5.33, 3],
          'figure.frameon': True,
          'figure.subplot.bottom': 0.1,
          'figure.subplot.hspace': 0.5,
          'figure.subplot.left': 0.25,
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
          'grid.color': a8c_colors.a8c_gray_lighten20,
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
          'lines.linewidth': 1.15,
          'lines.marker': 'None',
          'lines.markeredgewidth': 0.,
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

a8c_style_white = {'axes.axisbelow': True,
 'axes.edgecolor': a8c_colors.a8c_gray_lighten10,
 'axes.facecolor': 'white',
 'axes.grid': True,
 'axes.labelcolor': a8c_colors.a8c_gray_dark,
 'axes.linewidth': 1,
 'figure.autolayout': False,
  'figure.dpi': 120.0,
  'figure.edgecolor': 'white',
  'figure.facecolor': 'white',
  'figure.figsize': [5.33, 3],
  'figure.frameon': True,
  'figure.subplot.bottom': 0.1,
  'figure.subplot.hspace': 0.5,
  'figure.subplot.left': 0.25,
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
 'grid.color': a8c_colors.a8c_gray_lighten10,
 'grid.linestyle': '-',
 'image.cmap': 'Greys',
 'legend.frameon': False,
 'legend.numpoints': 1,
 'legend.scatterpoints': 1,
 'lines.solid_capstyle': 'round',
 'text.color': a8c_colors.a8c_gray_dark,
 'xtick.color': a8c_colors.a8c_gray_dark,
 'xtick.direction': 'out',
 'xtick.major.size': 0,
 'xtick.minor.size': 0,
 'ytick.color': a8c_colors.a8c_gray_dark,
 'ytick.direction': 'out',
 'ytick.major.size': 0,
 'ytick.minor.size': 0}


def fewer_axis_ticks(*args, **kwargs):
    msg = "`fewer_axis_ticks` is an alias to `cleanup` and is deprecated"
    warn(msg)
    return cleanup(*args, **kwargs)


def cleanup(ax=None, x_or_y='xy',
                     n_ticks=3, decimals=1,
                     despine_=True):
    ''' Draw fewer ticks on the give axis

    @param ax: matplotlib axis object. If None, use plt.gca(). Default: None
    @param x_or_y: either "x", "y" or "xy". Default: xy
    @param n_ticks: have this number of ticks. Default: 3
    @param decimals: As in `numpy.around`. Default: 1
    @param despine_: either a boolean or a dict.  If True (default),
        call `seaborn.despine_(ax)`;
        if a dict, use it as the argument dictionary for `seaborn.despine_`
        (no need to provide the `ax` element);
        if False, don't despine_
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
    if bool(despine_): #either `True` or a dict
        if despine_ is True:
            despine_ = dict(ax=ax)
        else: # a dict or dict-like
            despine_.update(dict(ax=ax))
        despine(**despine_)

    return ax



ylabelparams = {'x': 0,
                'y': 1,
                'rotation': 0,
                'ha': 'right',
                'va': 'top',
                'ma': 'left'
                }
axtitleparams = {'x': 0,
                 'y': 1.1,
                 'ha': 'left',
                 'ma': 'left',
                 'va': 'bottom'}



def sinplot(n_series=3, flip=1):
    '''Helper function to demonstrate some graphics'''
    for i in range(1, n_series + 1):
        if i % 3 == 0:
            x = np.linspace(0, 14, 10)
            plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip, '-o', label='curve %d' % i)
        else:
            x = np.linspace(0, 14, 100)
            plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip, label='curve %d' % i)
    plt.title("Sample sine plot", **axtitleparams)
    plt.legend()
    plt.xlabel('this is X')
    plt.ylabel('this is Y\nlabel', **ylabelparams)
    cleanup()
    return plt.gcf()

a8c_style = a8c_style_gray
sns.set_style(a8c_style)

if __name__ == '__main__':
    plt.interactive(False)
    plt.figure()
    _ = sinplot(n_series=4)
    plt.figure()
    _ = sinplot(n_series=10)
    plt.show()





