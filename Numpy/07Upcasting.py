# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:34:49 2020

@author: rsu1
"""

import numpy as np

#To create a array of integers
a=np.ones((2,3),dtype=int)
#To create a array of float
b=np.random.random((2,3))


print("a = ",a)
print("b = ",b)
print("Type of a = ",a.dtype.name)
print("Type of b = ",b.dtype.name)

c=a+b
#As a and be are diff types, the answer will be upcated to Float
print("c = ",c)
print("Type of c = ",c.dtype.name)

#Doing some exponential operations with the data of c
d=np.exp(c*1j)
#d will be upcasted for Complex number
print("d = ",d)
print("Type of d = ",d.dtype.name)