# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:35:10 2020

@author: rsu1
"""

import pandas as pd

df=pd.read_csv('11weatherdata.csv',parse_dates=['date'])
df.set_index('date',inplace=True)
print(df)
#Filling na with 0
df0=df.fillna(0)
print(df0)
#fill na with dictionary
df0=df.fillna({
    'temperature':0,
    'windspeed':0,
    'event':'No event'})
print(df0)

#filling na with the previous value (Forward fill)
df0=df.fillna(method='ffill')
print(df0)

#filling na with the next value (Backward fill)
df0=df.fillna(method='bfill')
print(df0)

#backfill with column value
df0=df.fillna(method='bfill',axis='columns')
print(df0)

#setting linit for ffill
df0=df.fillna(method='ffill',limit=1)
print(df0)
df0=df.fillna(method='ffill',limit=2)
print(df0)