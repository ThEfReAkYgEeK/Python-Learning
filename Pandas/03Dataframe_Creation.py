# -*- coding: utf-8 -*-
"""
Created on Wed May 13 03:50:59 2020

@author: rsu1
"""

import pandas as pd

#Creating a dataframe from csv file
csvdf=pd.read_csv("input.csv")
print("csvdf = ")
print(csvdf,'\n')

#Creating a dataframe from a dictionary
weatherdata={
    'Date':['11/20/2019','11/21/2019','11/22/2019'],
    'Temperature':[34,28,32],
    'Windspeed':[4,7,9],
    'Event':['Rain','Sunny','Fog']
    }
dictdf=pd.DataFrame(weatherdata)
print("dictdf = ")
print(dictdf)