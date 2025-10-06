# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 19:09:02 2025

@author: arpit
"""

'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''

a=int(input("Enter 1st integer: "))
b=int(input("Enter 2nd integer: "))
a,b=b,a
print('Before swapping, 1st integer was',a,'and 2nd integer was',b)
print('After swapping, 1st integer is',a,'and 2nd integer is',b)
