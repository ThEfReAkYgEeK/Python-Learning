# -*- coding: utf-8 -*-
"""
Created on Wed May 13 04:25:19 2020

@author: rsu1
"""

import pandas as pd

#Creating a dataframe from csv file
df=pd.read_csv("input.csv")
print("df = ")
print(df,'\n')

#Indexig and slicing of Dataframe

#Slicing Rows 2,3,4
print("Slicing Rows 2,3,4 : \n",df[2:5],'\n')

#Printing the columns name
print("Columns of df are : \n",df.columns,'\n')

#printing the specific entire column
print("Printing the Events Column from df= \n",df.Event,'\n')
print("Printing the Events Column from df= \n",df['Event'],'\n')

#prtinting two different coluns together
print("Printing date and events = \n",df[['Date','Event']],'\n')

#Type of the column
print(type(df['Event']),'\n')
#It is a series

#Finding a max,min,mean,Standard deviation of specic column
print('max temp = ',df['Temperature'].max(),
      'min temp = ',df['Temperature'].min(),
      'mean temp = ',df['Temperature'].mean(),
      'std temp = ',df['Temperature'].std())

#To print the statistics of the dataframe
print(df.describe(),'\n')

#Extracting the row in which temp is max
print(df[df.Temperature==df.Temperature.max()],'\n')

#Getting the date of max temp
print(df['Date'][df.Temperature==df.Temperature.max()],'\n')

#Getting the date and temp of max temp
print(df[['Date','Temperature']][df.Temperature==df.Temperature.max()],'\n')