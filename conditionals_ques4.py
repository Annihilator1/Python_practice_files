# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:56:48 2025

@author: arpit
"""

'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''

name = input('Enter your name:>>>')
length = len(name)

if length>5:
    print('Your name is',length,'characters long')
else:
    print('Length of your name is secret')