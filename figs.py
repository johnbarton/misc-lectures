import matplotlib.pyplot as plt
import numpy as np
import mplot as mp

# GLOBAL VARIABLES

C_CONTACT  = '#f0f0f0'
C_TRUEPOS  = '#fd8d3c'
C_FALSEPOS = '#6baed6'


# FUNCTIONS

def contact_plot_PF00014(other_contacts, true_positives, false_positives):

    fig = plt.figure(figsize=(5, 5))
    ax  = plt.subplot(111)

    pprops = {'colors': [C_CONTACT, C_CONTACT, C_TRUEPOS, C_TRUEPOS, C_FALSEPOS, C_FALSEPOS],
              'xlim': [1, 55],
              'ylim': [1, 55],
              'xticks': [0, 10, 20, 30, 40, 50, 55],
              'yticks': [0, 10, 20, 30, 40, 50, 55],
              'xlabel': 'PF00014 sites',
              'ylabel': 'PF00014 sites',
              'plotprops': {'lw': 0, 's': 25, 'marker': 'o', 'clip_on': False},
              'theme': 'boxed' }

    oc = np.array(other_contacts)
    tp = np.array(true_positives)
    fp = np.array(false_positives)

    x = [oc.T[0]+1, oc.T[1]+1, tp.T[0]+1, tp.T[1]+1, fp.T[0]+1, fp.T[1]+1]
    y = [oc.T[1]+1, oc.T[0]+1, tp.T[1]+1, tp.T[0]+1, fp.T[1]+1, fp.T[0]+1]

    mp.plot(type='scatter', ax=ax, x=x, y=y, **pprops)

    pprops['colors'] = [C_CONTACT, C_TRUEPOS, C_FALSEPOS]
    mp.scatter(ax=ax, x=[[56], [56], [56]], y=[[52], [48], [44]], **pprops)
    ax.text(57, 52, 'Other contacts', ha='left', va='center', **mp.def_labelprops)
    ax.text(57, 48, 'True positives', ha='left', va='center', **mp.def_labelprops)
    ax.text(57, 44, 'False positives', ha='left', va='center', **mp.def_labelprops)

    plt.show()