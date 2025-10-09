# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 00:04:08 2025

@author: arpit
"""

#Modulus

#Fizzbuzz

# n=100

# for i in range(1,n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,'Fizzbuzz!!!')
#     elif i%5==0:
#         print(i, "Buzz")
#     elif i%3==0:
#         print(i, 'Fizz')
#     else:
#         print(i)
        
######################################

# print(list(range(10)))

# print(list(range(0,20,4)))

# Step 1: Initialize variables
n = 1
odd_sum = 0
# Step 2: Use a while loop to sum all odd numbers between 1 and 20
while n <= 20:
  odd_sum = odd_sum + n
  n+=2 
# Step 3: Print the total sum of odd numbers
print("The sum of odd numbers from 1 to 20 is:", odd_sum)
