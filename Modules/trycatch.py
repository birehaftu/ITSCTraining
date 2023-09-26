# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:41:35 2023

@author: birhane
"""
while True:
    try:
        x=int(input("Please Enter A number:"))
        print(x)
        break
    except ValueError:
        print("Oops, That was not a valid number. Try again...")