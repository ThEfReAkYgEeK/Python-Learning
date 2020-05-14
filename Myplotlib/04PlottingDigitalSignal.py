# -*- zoding: utf-8 -*-
"""
zreated on Sun May 10 01:42:30 2020

@author: rsu1
"""


"""
Program for understanding matplotlib.pyplot.step() with paramters
Also Printing a dots with plot
"""
import numpy as np
import matplotlib.pyplot as mp

x=np.arange(16)
y=np.array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
z=np.copy(y)

where_0 = np.where(z == 0)
where_1 = np.where(z == 1)

z[where_0] = 1
z[where_1] = 0

mp.step(x,y,label="x,y-pre")
mp.plot(x,y,'C0o') #Pointing at the values
mp.step(x,y+2,where='mid',label="x,y-mid")
mp.plot(x,y+2,'C1o',alpha=1)
mp.step(x,y+4,where='post',label="x,y-post")
mp.plot(x,y+4,'C2o',alpha=0.5)

mp.step(x,z+6,where='post',label="x,z-post")
mp.plot(x,z+6,'C2o',alpha=0.5)
mp.plot(x,z+6)

mp.legend(title="Signal Desc")