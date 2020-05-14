# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:48:37 2020

@author: rsu1
"""


import numpy as np

#Printing one dimentional array
print(np.arange(6))
#Printing two dimentional array
print(np.arange(6).reshape(2,3))
#Pritning three simentional array
print(np.arange(24).reshape(2,3,4))


#Printing large data
print(np.arange(10000))
print(np.arange(10000).reshape(100,100))

#To print entire large data
#np.set_printoptions(threshold=np.non-VAN)
#print(np.arange(10000))
#print(np.arange(10000).reshape(100,100))