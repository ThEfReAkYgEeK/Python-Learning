# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:17:09 2020

@author: rsu1
"""

import numpy as np
import matplotlib.pyplot as mp


date=["11 May 2020","12 May 2020","13 May 2020",
      "14 May 2020","15 May 2020","16 May 2020"]
dateindex=np.arange(6)
mp.yticks(dateindex,date)
GainOrLoss=[+1000,-200,+800,-100,+1500,0]

linx=np.zeros(len(date))

mp.xlim(-(max(GainOrLoss))-100,max(GainOrLoss)+100)

mp.xlabel("Gain or Loss in ₹")
mp.ylabel("Date")
mp.title("My Monthly Revenue")

mp.barh(dateindex,GainOrLoss,height=0.4)
mp.plot(linx,date,"C0-")
mp.grid()