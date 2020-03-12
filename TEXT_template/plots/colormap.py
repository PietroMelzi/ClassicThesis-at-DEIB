#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:13:53 2020

@author: matteo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


for it in [0,2,5,8,99]:
    dfs = [pd.read_csv('../data/visits/appE%d.csv' % d, sep=',') for d in range(6,16)]
    cdf = pd.concat(dfs, sort=True).groupby(level=0)
    df = cdf.mean()['it%d' % it]
    
    visits = np.array(df.values).reshape((5,5))
    
    cmap = 'hot_r'
    ax = sns.heatmap(visits/2000, linewidths=0.1, cmap=cmap, vmax=1, linecolor=(0,0,0
    ))
    xoff = 0.3
    yoff = 0.5
    for i,row in enumerate(visits/2000):
        for j, val in enumerate(row):
            ax.text(xoff + j, yoff+ i, '%.2f' % val, fontsize=11)
    plt.savefig('colormap%d' % it, dpi=1000)
    plt.show()