# -*- coding: utf-8 -*-
"""
Created on Sun May 10 02:06:08 2020

@author: rsu1
"""

"""
Program exapmle for printing a dot for specific values
"""


import numpy as np
import matplotlib.pyplot as mp

x=np.arange(100)
y=np.sin(x/10)

mp.plot(x,y)
mp.plot(x,y,'C0o',alpha=0.5)
#mp.show()
