# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 01:16:21 2025

@author: arpit
"""

'''
Question 6
Write code that will calculate factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

n=input('Enter a number to print it\'s factorial:>')
while (not n.isdigit()):
    print('Please enter number only:>>')
    n=input('Enter your number:>>')
n=int(n)
fact=1
for i in range(1,n+1):
    fact = fact * i 
print(fact)