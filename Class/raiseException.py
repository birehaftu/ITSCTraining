# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 11:50:06 2023

@author: birhane
"""

class BankAccount:
    def __init__(self,amount):
        if amount<0 :
            raise ValueError("Negative Amount")
BankAccount(-10)