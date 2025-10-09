# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 23:48:51 2025

@author: arpit
"""
n=10
while n>0:
    print(n)
    n-=1

###################################

user_input = int(input('Please enter ages of class member, Type -1 to end :>>'))
ages = []
while user_input > 0:
    ages.append(user_input)
    user_input = int(input('The next age:>'))
print('The ages are', ages)


#################################################

count = 0
class_name =[]
name = input('Please enter name, type n to stop :>')
while name != 'n':
    count+=1
    class_name.append(name)
    print(f'{name} has been added.')
    name = input('Next name?:>')
    
print(f'There are {count} people in the class, they are {class_name}')