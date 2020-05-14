5# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:14:18 2020

@author: rsu1
"""


import numpy as np

a=np.array([1,2,3])
print(a)
print(type(a))

b=np.arange(15).reshape(3,5)
print("b=")
print(b)
print("Shape of b")
print(b.shape)
print("Size of b")
print(b.size)
print("Number of dimentions in b")
print(b.ndim)
print("Item size of b")
print(b.itemsize)
print("Dtatype of each elements")
print(b.dtype)
print("data in b")
print(b.data)

