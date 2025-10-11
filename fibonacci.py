# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 01:22:24 2025

@author: arpit
"""

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

n=20
a=0
b=1
fib_nums=[]
for i in range(n):
    fib_nums.append(a)
    a,b= b,a+b
    
print(f'The first {n} Fibinacci numbers are, {fib_nums}')
