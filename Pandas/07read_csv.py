# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:31:12 2020

@author: rsu1
"""

import pandas as pd

stock_data=pd.read_csv("stock_data.csv")
print('stock_data = \n',stock_data,'\n')

stock_data_1=pd.read_csv("stock_data_1.csv")
print('stock_data_1 = \n',stock_data_1,'\n')

#skipping one line from csv file
stock_data_1=pd.read_csv("stock_data_1.csv",skiprows=1)
print('stock_data_1 after skipping one row = \n',stock_data_1,'\n')

#creating dataframe from first row ( Making row 1 as a header )
stock_data_1=pd.read_csv("stock_data_1.csv",header=1)
print('stock_data_1 from the first row = \n',stock_data_1,'\n')

#Craeting the df from the file which dont have header

#Without header
stock_data_2=pd.read_csv("stock_data_2.csv",header=None)
print('stock_data_2 without header = \n',stock_data_2,'\n')

stock_data_2=pd.read_csv("stock_data_2.csv",header=None,names=['tickers','eps',
                                                               'revenue',
                                                               'price',
                                                               'people'])
print('stock_data_2 with names defined by users = \n',stock_data_2,'\n')

#To read only specific number of rows
stock_data=pd.read_csv("stock_data.csv",nrows=3)
print('stock_data only with three rows = \n',stock_data,'\n')