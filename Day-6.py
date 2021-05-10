# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:51:08 2021

@author: lenovo
"""

"""Question 1 (method 1): Count even numbers and odd numbers"""

even_count = 0
odd_count = 0
for i in range(1,10):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
#%%

"""Question 1 (method 2): Count even numbers and odd numbers"""

list1 = [10, 21, 4, 45, 66, 93, 1]
  
even_count, odd_count = 0, 0
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num % 2 == 0:
        even_count += 1
  
    else:
        odd_count += 1
          
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
#%%

"""Question 2 - Tell Max and Min without using inbuilt function"""

arr = [10, 21, 4, 45, 66, 93, 1]
min = arr[0]
for a in arr:
    if a < min:
        min = a
print("The minimum number in the list is: ", min)
max = arr[0]
for a in arr:
    if a > max:
        max = a
print("The maximum number in the lit is: ", max)
#%%

"""Question 3(method 1) - Check whether the list is palindrome or not"""

num = input("Enter a number: ")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")

#%%

"""Question 3(method 2) - Check whether the list is palindrome or not"""

arr = [3,6,0,6]
if arr == arr[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")
#%%

"""Question 4 (method 1) - Print the numbers which are palindrome in the list"""

li = [55,36,363,545,500,77]
for i in li:
    n = str(i)
    if n==n[::-1]:
        print(i, end = " ")
#%%

"""Question 4 (method 2) - Print the numbers which are palindrome in the list"""

for i in range(1,101):
	n = str(i) 
	if n==n[::-1]: 
		print(i,end=' ')