# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:25:17 2021

@author: lenovo
"""

"""Question 1 - Give Index values of all vowels"""

li=['a','e','i','o','u','A','E','I','O','U']
word="EduYear"
for i in range(len(word)):
   if word[i] in li:
       print (i, '-', word[i])
#%%

""" Question 2 - Reverse the words of strings"""


st = "hello world happy birthday"
txt = st.split()
print(txt)
txt = reversed(txt)
print(" ".join(txt))

#%%

"""Question 3 - Remove duplicates without Set function"""

test_list = [1,5,6,1,8,6,7,8,4,5,9,10,15,17,15]
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
print ("The original list is : " +  str(test_list))
print ("The list after removing duplicates : " + str(res))