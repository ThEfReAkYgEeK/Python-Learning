# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:19:45 2020

@author: rsu1
"""

import numpy as np

a=np.array([[1,1],[0,1]])
b=np.array([[2,0],[3,4]])

print(a)
print(b)

#Elementwise multiplication
print(a*b)

#MatrixMultiplications
print(a@b)
print(a.dot(b))