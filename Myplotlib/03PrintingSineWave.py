# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:34:28 2020

@author: rsu1
"""

import numpy as np
import matplotlib.pyplot as mp

x=np.arange(300)
y=np.sin(x/10)
z=np.cos(x/10)
#a=np.sec(x/10)
#b=np.cosec(x/10)
#c=np.tan(x/10)
#d=np.cot(x/10)

mp.plot(x,y)
mp.plot(x,z)
#mp.plot(x,a)
#mp.plot(x,b)
#mp.plot(x,c)
#mp.plot(x,d)
