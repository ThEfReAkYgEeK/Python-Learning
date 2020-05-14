# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:09:07 2020

@author: rsu1
"""


import numpy as np

#normal way to create an array
a=np.array([1,2,3])
print(a)
print("\n\n")

#Using arange()
a=np.arange(15)
print(a)
print("\n")

#reshaping while creatin array
a=np.arange(15).reshape(3,5)
print(a)
print("\n")

a=np.arange(15).reshape(5,3)
print(a)
print("\n")

#Wrong way to create a array
#a=np.array(1,2,3)

#Creating a 2d array
a=np.array([(1,2,3),(4,5,6)])
print(a)
print("\n")

#creating array with specific datatype
a=np.array([1,2,3],dtype=complex)
print(a)
print("\n")

#creating array with specific values filled
#by default the data type is float
a=np.zeros((3,4))
print(a)
print("\n")

#creating ones as integers
a=np.ones((3,4),dtype=int)
print(a)
print("\n")

#Create array with garbage value
a=np.empty((3,4))
print(a)
print("\n")

#creating with a arange method
a=np.arange(1,101).reshape(10,10)
print(a)
print("\n")

a=np.arange(0,11,3)
print(a)
print("\n")

#creating with linspace
a=np.linspace(1,11,5)
print(a)
print("\n")