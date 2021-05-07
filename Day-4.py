# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:09:25 2021

@author: lenovo
"""
"""Question 1 - Count number of y's"""

st = input(str("Enter the Text: "))
x = st.count('y')
print(x)

#%%
"""Question 2 - Swapcase the letter in a string"""

txt = "EdUyEaR"
x = txt.swapcase()
print(x)

#%%
"""Question 3 - Even Indexing in a string"""

st = input(str("Enter the Text: "))
print(st[0:len(st):2])