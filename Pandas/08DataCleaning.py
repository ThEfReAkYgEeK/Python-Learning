# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:05:46 2020

@author: rsu1
"""

import pandas as pd

stock_data=pd.read_csv('stock_data.csv')
print('Normal stock_data without data cleaning : \n',stock_data,'\n')

#Defining the alias for na values
stock_data=pd.read_csv('stock_data.csv',na_values=['n.a.','not available'])
print('Normal stock_data after cleaning n.a. and not available : \n',
      stock_data,'\n')

#Defining -1 as NAN because revenue cannot be in -1
stock_data=pd.read_csv('stock_data.csv',na_values=['n.a.','not available',-1])
print('Normal stock_data after cleaning n.a.,not available and -1 : \n',
      stock_data,'\n')

#eps can be -1 so no need to convert it in to NAN
#To do so we need to create an value with dictionaries
stock_data=pd.read_csv('stock_data.csv',na_values=
                       {'eps':['n.a.','not available'],
                        'revenue':['n.a.','not available',-1],
                        'price':['n.a.','not available',-1],
                        'people':['n.a.','not available']})
print('Normal stock_data after cleaning with dictionaries : \n',
      stock_data,'\n')
