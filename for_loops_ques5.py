# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 01:06:48 2025

@author: arpit
"""

'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

seq=[]
num=input('Enter a number, type exit to stop:>>')
while num.lower() != 'exit':
    while not num.isdigit():
        print('That is not a number!, Numbers only please:>>')
        num=input('try again:>>')
    seq.append(int(num))
    num=input('Please enter next number:>>')
total = 0
for number in seq:
    total += number
print(f'Mean is{total/len(seq)}')
print(sum(seq)/len(seq))