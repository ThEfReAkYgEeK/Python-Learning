# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:32:49 2020

@author: rsu1
"""

import pandas as pd

stock_data=pd.read_csv('stock_data.csv',na_values=
                       {'eps':['n.a.','not available'],
                        'revenue':['n.a.','not available',-1],
                        'price':['n.a.','not available',-1],
                        'people':['n.a.','not available']})
print('Normal stock_data after cleaning with dictionaries : \n',
      stock_data,'\n')

#writing to csv file
stock_data.to_csv('stock_data_clean.csv',index=False)

#Writing to csv only two columns
stock_data.to_csv('stock_data_clean_twocolumns.csv',index=False,
                  columns=['tickers','eps'])

#Writing to csv without header
stock_data.to_csv('stock_data_clean_withoutheader.csv',index=False,header=False)