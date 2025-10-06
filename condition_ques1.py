# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:39:23 2025

@author: arpit
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''


num = int(input('Enter a number 1 & 5 inclusive:>>'))

if num == 1:
    print("One")
elif num == 2:
    print("Two") 
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
else:
    print("Invalid Input")         