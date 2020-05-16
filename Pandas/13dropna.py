# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:13:58 2020

@author: rsu1
"""

import pandas as pd

df=pd.read_csv('11weatherdata.csv',parse_dates=['date'])
df.set_index('date',inplace=True)
print(df)

#dropping the rows with atleast one na
df0=df.dropna()
print(df0)

#dropping rows with only one na
df0=df.dropna(how='all')
print(df0)

#drop the rows not having atleat one non nan value
df0=df.dropna(thresh=1)
print(df0)

#drop the rows not having atleat two non nan value
df0=df.dropna(thresh=2)
print(df0)