# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:59:30 2020

@author: rsu1
"""

import numpy as np

a=np.array([10,20,30,40])
b=np.arange(1,5)
print(a)
print(b)

"""
In following examples new Arrays are created with the operations
"""

#Adding a and b element wise
print(a+b)

#Subtracting a and b elemnt wise
print(a-b)

#Multipying a and b element wise
print(a*b)

#Divinding a and be element wise
print(a/b)

#Squares of elements
print(b**2)

#Element wise comparision
print(a<25)


"""
For the following operations the first matrix will be modified
"""

a=np.ones((2,3),dtype=int)
b=np.zeros((2,3),dtype=int)
print(a)
print(b)
b+=a
print(b)


a=np.ones((2,3),dtype=int)
b=np.zeros((2,3),dtype=int)
print(a)
print(b)
a*=b
print(a)