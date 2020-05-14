# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:44:36 2020

@author: rsu1
"""

import numpy as np
import matplotlib.pyplot as mp

company=["Google","Tesla","Microsoft","Facebook"]
revenue2018=[10,4,8,7]
revenue2019=[13,5,9,5]

compindex=np.arange(4)
mp.xticks(compindex,company)

mp.xlabel("Companies")
mp.ylabel("Revwnues in Billions")
mp.title("Revenue Bar Chart")

mp.bar(compindex-0.2,revenue2018,width=0.4,label="2018")
mp.bar(compindex+0.2,revenue2019,width=0.4,label="2019")
mp.legend()