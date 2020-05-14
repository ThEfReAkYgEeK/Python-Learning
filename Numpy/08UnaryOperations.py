# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:42:23 2020

@author: rsu1
"""

import numpy as np

a=np.linspace(0,2,5)
print("a = \n",a)

#To get the sum of all elements of the array
print(a.sum())

#To print max number of an array
print(a.max())

#To print min number of as array
print(a.min())

#To print cumulative sum
print(a.cumsum())

"""
To do the operation in row and columnwise
"""

b=np.arange(12).reshape(3,4)
print("b = \n",b)

#To calculate sum of rows
print("Sum of rows = ",b.sum(axis=1))

#To calculate tkhe sum of columns
print("Sum of columns = ",b.sum(axis=0))

#To find minimum in row and column
print("Minimum of row = ",b.min(axis=1),"\nMinimum of column = ",b.min(axis=0))

#To find Maximum in row and column
print("Maximum of row = ",b.max(axis=1),"\nMaximum of column = ",b.max(axis=0))

#To find a cumulative sum in row and column
print("Cumluative sun in Row wise = \n",b.cumsum(axis=1))
print("Cumluative sun in Column wise = \n",b.cumsum(axis=0))