# -*- coding: utf-8 -*-
"""
Created on Sun May 10 02:27:17 2020

@author: rsu1
"""

"""
Referance : 
https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
"""

import numpy as np
import matplotlib.pyplot as mp

x=np.arange(10)
y=np.arange(10)

mp.plot(x,y)
mp.plot(x,y,"C0o",alpha=0.2)
mp.plot(x,y+1,"C1o",alpha=0.4)
mp.plot(x,y+2,"C2o",alpha=0.6)
mp.plot(x,y+3,"C3o",alpha=0.8)
mp.plot(x,y+4,"C4o",alpha=1)
mp.plot(x,y+5,"C5o",alpha=0.5)


mp.plot(x,y+6,"b,")     #blue pixel marker
mp.plot(x,y+7,"go-")    #green round marker with solid line
mp.plot(x,y+8,"+--r")   #Plus marker with dashed line in red colour
mp.plot(x,y+9,"-.cp")   #Dash dot line in cyan color with pentagon marker
mp.plot(x,y+10,"m:|")   #Magenta colour dotted lines with vline marker
mp.plot(x,y+11,color="yellow",marker='D',linestyle='')  #Yellow colour diamond marker with no line
mp.plot(x,y+12,"k")     #Simple black line
mp.plot(x,y+13,"w")     #Simple white line
#Marker size selection and colours in RGB
mp.plot(x,y+20,color='#888888',markersize=20,marker='D',linestyle='')
