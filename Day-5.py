# -*- coding: utf-8 -*-
"""
Created on Fri May  7 19:59:52 2021

@author: lenovo
"""
#%%
"""Question 1 - printing numbers divisible by 5 and 7 both"""

lower = int(input("Enter lower range limit: "))
upper = int(input("Enter upper range limit: "))
for i in range (lower, upper+1):
    if((i%5==0) & (i%7==0)):
        print(i)
#%%
"""Question 2 - Finding sum of a series"""

num = 5
# 2 +22 + 222 + 2222 + .. n terms
res = 0
st = '2'
for i in range(1, num+1):
    a = int(st * i)
    res += a
    print(a)

print(res)


#%%
"""Question 3 - Take integer inputs from user and print the sum"""

sum = 0

while True:
    user_input = (input("Enter a number or press 'q' to quit: "))
    if user_input == 'q':
        break
    user_input = int(user_input)
    sum = sum + user_input

print("Sum of the above numbers is: ", sum)
#%%

"Question - 4 Factorial of a number"

num = int(input("Enter a number: "))
fac = 1
i = 1

while i <= num:
    fac = fac * i
    i = i + 1
print("Factorial of", num, "is", fac)

#%%
"""Question 5 - Input 'python language is mostly used in programming' and insert '-'
after every character"""

st = 'python language is mostly used in programming'
for i in range(len(st)):
    end_value = '-'

    if st[i] == ' ' or i == len(st)-1 or st[i+1] == ' ':
        end_value = ''

    if i%2 == 0:
        print(st[i].upper(), end=end_value)
    else:
        print(st[i].lower(), end=end_value)
print()