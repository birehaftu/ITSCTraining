# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 08:25:26 2023

@author: birhane
"""

class MyClass:
    """A simple Example Class"""
    i=12345
    def f(self):
        return 'Hello world'
#print(MyClass().i)
#print(MyClass().f())
#print(MyClass.__doc__)
x=MyClass();
xf=x.f
print(xf())

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0, -4.5)
x.r,x.i
print(x.r,x.i)

class Reverse: 
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data): 
		self.data = data 
		self.index = len(data)
    def __iter__(self): 
		return self
    def next(self): 
		if self.index == 0:
            self.index = self.index-1 
        return self.data[self.index] 
for char in Reverse('spam'):
    print(char)
 
