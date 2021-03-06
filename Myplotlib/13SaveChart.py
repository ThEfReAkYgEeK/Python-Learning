# -*- coding: utf-8 -*-
"""
Created on Mon May 11 02:04:47 2020

@author: rsu1
"""

import matplotlib.pyplot as mp

exp_val=["Rent","Food","Travel","Misc","Phone/Internet"]
exp=[6500,2100,1000,300,200]

mp.axis("equal")
mp.pie(exp,labels=exp_val,radius=2,autopct="%0.2f%%",shadow=True,
       explode=[0,0.2,0.5,0,0],startangle=0)

mp.savefig("MyHomeExpensesPIE.png",bbox_inches="tight",pad_inches=2,
           transparent=True)