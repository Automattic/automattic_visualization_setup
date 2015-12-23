# Automattic-specific style improvement to `matplotlib`

Data visualization is a pivotal task in the job of a data scientist. `matplotlib` is one of the most widely used Python data visualization libraries. Being developed in late 1990's to mimic look and feel of Matlab -- then de-facto standard, `matplotlib` graphs suffer several problems. `seaborn` is an attempt to solve such problems, and to provide other improvements.  This module uses `seaborn` to create plotting themes that meet [WordPress.com color scheme](https://wordpress.com/design-handbook/colors/), as well as several other enhancements.

WorPress.com colors are based on the specifications mentioned in the [design handbook](https://wordpress.com/design-handbook/colors/). Missing colors were added using the excellent [iwanthue](http://tools.medialab.sciences-po.fr/iwanthue/) service.

## Usage

WorPress.com color definitions reside in `a8c_colors.py`.

Importing `a8c_styling` also imports `seaborn` and sets the plotting style to `a8c_styling.a8c_style`.

    import a8c_styling
    import seaborn as sns
    from matplotlib import pylab as plt

    plt.figure()
    a8c_styling.sinplot(4) #this is how a default plot looks like


This is the result:

![sample_sine](https://cloud.githubusercontent.com/assets/506547/11977212/5f1e0720-a989-11e5-960c-596e1e9f096d.png)



Some parameters cannot be changed by the means of `set_style`. Thus, `a8c_styling` provides several convenience functions and definitions:


    plt.figure()
    a8c_styling.sinplot(4)
    plt.ylabel('this is Y',
               **a8c_styling.ylabelparams) #horizontal label for
                                        #more readability
    plt.title('This is an improved title', **a8c_styling.axtitleparams)
    a8c_styling.cleanup()
    
This is the final design:

![improved_sine](https://cloud.githubusercontent.com/assets/506547/11977221/6e18783c-a989-11e5-80a5-e800f838aa64.png)


## License

[GPLv2+](http://www.gnu.org/licenses/gpl-2.0.html)
