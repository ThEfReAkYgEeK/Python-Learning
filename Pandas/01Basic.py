# -*- coding: utf-8 -*-
"""
Created on Tue May 12 05:46:16 2020

@author: rsu1
"""

import pandas as pd

df=pd.read_csv("MCXCLK202008052020.csv")

df.to_csv("CrudeoilOutput202008052020.csv")

#MeanValue before Data munging
print(df["Open"].mean())

#Data Munging
df.fillna(0,inplace=True)

#MeanValue after Data munging
print(df["Open"].mean())

df.to_csv("CrudeoilOutput202008052020FilledNA.csv")

#To find and min in Open
print(df["Open"].max())
print(df["Open"].min())
print(df["Open"].mean())


#To find the dates in which Volume is more than 0
print(df["Date"][df["Volume"]>0])