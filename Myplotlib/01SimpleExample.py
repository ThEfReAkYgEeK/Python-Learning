# -*- coding: utf-8 -*-
"""
Created on Sat May  9 02:03:56 2020

@author: rsu1
"""

import numpy as np
import matplotlib.pyplot as mp

fig,ax=mp.subplots()
ax.plot([1,2,3,4],[1,3,8,2])

mp.plot([1,2,3,4],[10,3,7,10])

a=np.arange(15)
b=np.arange(15,0,-1)
c=np.arange(15)
mp.plot(a,b)