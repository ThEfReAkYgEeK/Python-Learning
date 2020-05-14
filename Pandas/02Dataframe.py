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

#Printng the shape
print(csvdf.shape,dictdf.shape)
#Storing the tules value into row and column variables
csvdfrows,csvdfcolumns=csvdf.shape
dictdfrows,dictdfcolumns=dictdf.shape
print('\ncsvdfrows=',csvdfrows,'  csvdfcolumns=',csvdfcolumns,
      '\ndictdfrows=',dictdfrows,'  dictdfcolumns=',dictdfcolumns,'\n')


#Extracting only starting few lines (5 default)
print('First 5 rows : \n',csvdf.head(),'\n')
print('First 2 rows : \n',csvdf.head(2),'\n')

#Extracting only ending few lines (5 default)
print('Last 5 rows : \n',csvdf.tail(),'\n')
print('Last 5 rows : \n',csvdf.tail(2),'\n')

#Indexig and slicing of Dataframe

#Slicing Rows 2,3,4
print("Slicing Rows 2,3,4 : \n",csvdf[2:5],'\n')

#Printing the columns name
print("Columns of csvdf are : \n",csvdf.columns,'\n')

#printing the specific entire column
print("Printing the Events Column from csvdf= \n",csvdf.Event,'\n')
print("Printing the Events Column from csvdf= \n",csvdf['Event'],'\n')