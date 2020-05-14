# -*- coding: utf-8 -*-
"""
Created on Wed May 13 04:57:30 2020

@author: rsu1
"""


import pandas as pd

#Creating a dataframe from csv file
df=pd.read_csv("input.csv")

print("df : \n",df,'\n')

#Checking the index
print("index : ",df.index,'\n')

#Setting the index as 
print("setting index : \n",df.set_index('Date'),'\n')

#df will not get modified
print("df without index modified : \n",df,'\n')
#Because set index is not modifying the original df
#To do so we need to make inplace as True
df.set_index('Date',inplace=True)
print("df after index modified : \n",df,'\n')
print("index after modified : \n",df.index,'\n')

#To access with the indexed Date
print("Data of 11/20.2020 : \n",df.loc['11/20/2019'],'\n')

#Resetting the index
df.reset_index(inplace=True)
print("df after the index is reset : \n",df,'\n')

#Setting index with events
df.set_index('Event',inplace=True)
print('df with Event indexed : \n',df,'\n')
print("Details of the rainy days : \n",df.loc['Rain'],'\n')