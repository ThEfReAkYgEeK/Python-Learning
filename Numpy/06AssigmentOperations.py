# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:24:22 2020

@author: rsu1
"""

import numpy as np

#To create a array of integers
a=np.ones((2,3),dtype=int)
#To create a array of float
b=np.random.random((2,3))

print("a = ",a)
print("b = ",b)

#Elements of a will be added with 3 and teh result will be stored in c
#But a remains the same5
c=a+3
print("a = ",a)
print("c = ",c)
    
#Elements of a is added with 3 and a is updated with the results
a+=3
print("a = ",a)

b+=a
print("b = ",b)

#integer cannot be replaced by float
#Because float is higher order
a+=b
print("c = ",a)