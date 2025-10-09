# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 00:22:09 2025

@author: arpit
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''

num_1= int(input("Enter a 1st number between 1 and 100:>>"))
num_2= int(input("Enter a 2nd number between 1 and 100:>>"))

while num_1<0 or num_2<0 or num_1>100 or num_2>100 or num_1==num_2:
    print("Numbers are out of range, enter again")
    num_1= int(input("Enter a 1st number between 1 and 100:>>"))
    num_2= int(input("Enter a 2nd number between 1 and 100:>>"))
    
if num_1 < num_2:
    for i in range(num_1, num_2 + 1):
        print(i, end=' ')
         
else:
    for i in range(num_2, num_1 + 1): 
        print(i, end=' ')
    