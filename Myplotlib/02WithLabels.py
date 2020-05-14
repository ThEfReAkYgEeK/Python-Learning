# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:01:47 2020

@author: rsu1
"""

import numpy as np
import matplotlib.pyplot as mp

a=np.arange(16)
b=np.array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
c=np.copy(b)

where_0 = np.where(c == 0)
where_1 = np.where(c == 1)

c[where_0] = 1
c[where_1] = 0


print(a)
print(b)
print(c)

mp.xlabel("Time")
mp.ylabel("Voltage")
mp.title("Osciloscope")


mp.plot(a,b,color="red",linestyle="dotted",label="a-b plot")
mp.plot(a,c,color="green",linestyle="dashed",label="a-c plot")
mp.legend(title="Signal Desc",loc="upper right")
mp.grid()