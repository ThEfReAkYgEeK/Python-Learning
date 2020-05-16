# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:03:12 2020

@author: rsu1
"""

import pandas as pd

df=pd.read_csv('11weatherdata.csv',parse_dates=['date'])
df.set_index('date',inplace=True)
print(df)

#linear interpolation
df0=df.interpolate()
print(df0)

#time interpolation
df0=df.interpolate(method='time')
print(df0)