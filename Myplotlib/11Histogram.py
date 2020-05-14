# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:51:35 2020

@author: rsu1
"""

import matplotlib.pyplot as mp

bloodsugar_men=[113,85,90,150,149,88,93,115,135,80,77,82,129]
bloodsugar_women=[6,98,89,120,133,150,84,69,89,79,120,112,100]

#mp.hist(bloodsugar_men)

#mp.hist(bloodsugar_men,rwidth=0.95)

#mp.hist(bloodsugar_men,bins=[80,100,125,150],rwidth=0.95)

#mp.hist(bloodsugar_men,bins=[70,100,125,150],color="green",histtype="step")



#mp.hist([bloodsugar_men,bloodsugar_women],bins=[70,100,125,150],color=['g','r'],
#        label=["Men","Women"])

mp.hist([bloodsugar_men,bloodsugar_women],bins=[70,100,125,150],color=['g','r'],
        label=["Men","Women"],orientation="horizontal")

mp.legend()
#mp.grid()