# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:48:07 2025

@author: arpit
"""

'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''

num = 5
guess = input('Enter a number between 1 & 10 inclusive:>>>')
if guess.isdigit():
    guess = int(guess)
    if num == guess:
        print("Guessed Correctly")
    elif guess > num and guess<=10:
        print("Guessed High")
    elif guess < num and guess>=1:
        print("Guessed Low")
    else:
        print('Out of range')
else:
    print('Enter a number not string')
