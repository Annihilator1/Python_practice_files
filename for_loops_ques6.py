# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 02:22:09 2025

@author: arpit
"""

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

n=100
odd=[]
even=[]

for i in range(n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f'The evens are {even}')
print(f'The odd are {odd}')