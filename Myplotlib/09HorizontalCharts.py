# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:08:41 2020

@author: rsu1
"""

import numpy as np
import matplotlib.pyplot as mp

company=["Google","Tesla","Microsoft","Facebook"]
revenue2018=[10,4,8,7]
revenue2019=[13,5,9,5]

compindex=np.arange(4)
mp.yticks(compindex,company)

mp.ylabel("Companies")
mp.xlabel("Revwnues in Billions")
mp.title("Revenue Bar Chart")

mp.barh(compindex-0.2,revenue2018,height=0.4,label="2018")
mp.barh(compindex+0.2,revenue2019,height=0.4,label="2019")
mp.legend()
mp.grid()