# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:30:37 2021

@author: lenovo
"""


"""Question 1 - To check whether the number is Prime or Not"""
def checkPrime(x):
    for i in range(2, x):
        if n%i==0:
            return 1

print("Enter a Number: ", end="")
n = int(input())

p = checkPrime(n)
if p==1:
    print("\n" +str(n)+ " is not a Prime Number")
else:
    print("\n" +str(n)+ " is a Prime Number")

   
#%%
"""Question 2 - To check factorial of a number"""

def factorial(n):
    
    
    return 1 if (n==1 or n==0) else n * factorial(n - 1)



