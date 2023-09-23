# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:50:47 2023

@author: birhane
"""
class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def next(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data(self.index)
for char in Reverse('spam'):
    print(char)