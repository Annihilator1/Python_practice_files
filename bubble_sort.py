# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 23:42:02 2025

@author: arpit
"""

## Bubble Sort

data = [53,76,25,98,56,42,69,81]
data_copy = data[:]
for i in range(len(data_copy)):
    for j in range(0, len(data_copy)-i-1):
        if data_copy[j] > data_copy[j+1]:
            data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]
print(data)
print(data_copy)

print(sorted(data))