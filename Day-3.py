# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:23:44 2021

@author: lenovo
"""

""" 1. Calculate Age of a Person"""
    
doy = int(input("Enter your year of birth: "))
Age = 2021 - doy
print("Your age is", Age, "years")

#%%

""" 2. Calculation of Age using datetime class"""

import datetime
  
birth_year = int(input("Enter your year of birth: "))    
current_year = datetime.date.today().year
age_year = current_year - birth_year
print("Your age is: ", age_year, "Years")
#%%

"""Simple Calculator"""

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
div = num1 / num2
floor = num1 // num2
mod = num1 % num2
power = num1 ** num2
print("")
print("num1 + num2 = ", add)
print("num1 - num2 = ", sub)
print("num1 * num2 = ", multiply)
print("num1 / num2 = ", div)
print("num1 // num2 = ", floor)
print("num1 % num2 = ", mod)
print("num1 ** num2 = ", power)