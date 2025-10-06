# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:44:02 2025

@author: arpit
"""

'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''

num=input('Enter a number between 1 & 5 inclusive in String format:>>>')
lower = num.lower()
if lower=="one":
    print("1")
elif lower=="two":
    print('2')
elif lower=="three":
    print('3')
elif lower=="four":
    print('4')
elif lower=="five":
    print('5')
else:
    print('Invalid input')