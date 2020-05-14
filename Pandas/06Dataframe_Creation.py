# -*- coding: utf-8 -*-
"""
Created on Wed May 13 05:32:29 2020

@author: rsu1
"""

import pandas as pd

#from csv file
df=pd.read_csv('input.csv')
print('df from csv : \n',df,'\n')

#from excel file
df=pd.read_excel('input.xlsx','Sheet1')
print('df from excel : \n',df,'\n')

#from dictionary
weatherdata={
    'Date':['11/20/2019','11/21/2019','11/22/2019'],
    'Temperature':[34,28,32],
    'Windspeed':[4,7,9],
    'Event':['Rain','Sunny','Fog']
    }
df=pd.DataFrame(weatherdata)
print('df from dict : \n',df,'\n')

#From list of tuples
weatherdata=[
    ('11/20/2019',34,4,'Rainy'),
    ('11/21/2019',28,7,'Sunny'),
    ('11/22/2019',32,9,'Fog')]
df=pd.DataFrame(weatherdata,columns=['Date','Temperature','Windspeed','Event'])
print('df from list of tuples : \n',df,'\n')

#From lost of Dictionaries
weatherdata=[
    {'Date':'11/20/2019','Temperature':34,'Windspeed':4,'Event':'Rainy'},
    {'Date':'11/21/2019','Temperature':28,'Windspeed':7,'Event':'Sunny'},
    {'Date':'11/22/2019','Temperature':32,'Windspeed':9,'Event':'Fog'}]
print('df from list of Dicts : \n',df,'\n')