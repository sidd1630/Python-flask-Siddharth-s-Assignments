# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:27:04 2021

@author: lenovo
"""

#%%

""" Numpy program to print version"""

import numpy as np
print(np.__version__)

#%%

"""Numpy program to convert a list to 2-D array"""

import numpy as np

a = [12.23, 13.32, 100, 36.32]
print(a)

b = np.array(a)
print(b)

#%%

"""Numpy program to create 3*3 matrix with values randing between 2 & 11"""

import numpy as np
a = np.random.randint(2, 11, size = (3,3) )
print(a)