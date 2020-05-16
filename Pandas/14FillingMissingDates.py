# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:23:04 2020

@author: rsu1
"""

import pandas as pd

df=pd.read_csv('11weatherdata.csv',parse_dates=['date'])
df.set_index('date',inplace=True)
print(df)

dt=pd.date_range('01-01-2017','01-11-2017')
idx=pd.DatetimeIndex(dt)
df=df.reindex(dt)

print(df)
df.fillna({'event':'No event'},inplace=True)
df.interpolate(method='time',inplace=True)
print(df)