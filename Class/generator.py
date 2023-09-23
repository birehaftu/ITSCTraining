# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:01:13 2023

@author: birhane
"""

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
for char in reverse('golf'):
    print(char)