# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 19:02:17 2025

@author: arpit
"""

'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''

print("Enter two integers between 1 and 20 \n")
a=int(input('1st integer:>>'))
b=int(input('2nd integer:>>'))

if a>15 and b>15:
    print("Product of",a, '&', b, 'is', a*b)
elif a>15 or b>15:
    print("Sum of",a, '&', b, 'is', a+b)
else:
    print("0")
