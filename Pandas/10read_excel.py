# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:13:00 2020

@author: rsu1
"""

import pandas as pd

def convert_people(cell):
    if cell=='n.a.':
        return 'sam walton'
    return cell

def convert_eps(cell):
    if cell=='not available':
        return None
    return cell

df1=pd.read_excel('stock_data.xlsx','Sheet1')
print('dataframe from excel : \n',df1,'\n')

#with converters
df2=pd.read_excel('stock_data.xlsx',converters=
                 {'people':convert_people,
                  'eps':convert_eps
                     })
print('dataframe from excel after cleaning : \n',df2,'\n')

#Eritting to excel
df2.to_excel('stock_data_cleaned.xlsx','Sheet1',index=False,startrow=1,startcol=2)

#To write in two sheets
with pd.ExcelWriter('stock_data_twosheets.xlsx') as writer:
    df1.to_excel(writer,sheet_name='Not Cleaned',index=False)
    df2.to_excel(writer,sheet_name='Cleaned',index=False)