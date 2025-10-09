# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 00:41:50 2025

@author: arpit
"""

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

num=int(input('Enter a number between 1 and 12:>>'))
while((num < 1) and (num > 12)):
    print("Must be an integer between 1 and 12, please try again")
    num=int(input('Enter a number between 1 and 12:>> '))

    
for i in range(1,13):
    mul = num*i
    print(num, '*', i,'=', mul, '\n')
    
    ##########################################################
    
'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''

for i in range(1,13):
    print('__________________________________')
    print()
    print(f'This is the {i} times table')
    print()
    for j in range(1,13):
        print(f'{j} x {i} = {j*i}')
