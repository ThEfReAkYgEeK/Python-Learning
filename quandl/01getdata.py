# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:18:37 2020

@author: Sureshkumar R
"""

#import numpy as np
import quandl
import pandas as pd
#import csv

quandl.ApiConfig.api_key="ujycFWMabiKUnyVno7Gi"
data=quandl.get("MCX/CLK2020")
print(data)
googledata=quandl.get("38259P706")
print(googledata)
pddata=pd.DataFrame(data)

open("MCXCLK202008052020.csv",'wb')
pddata.to_csv("MCXCLK202008052020.csv")