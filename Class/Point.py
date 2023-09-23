# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 10:38:48 2023

@author: birhane
"""
from  math import *
class Point:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def set_location(self,x,y):
        self.x=x
        self.y=y
    def distance_from_origin(self):
        return sqrt(self.x*self.y)
    def distance(self,other):
        dx=self.x-other.x
        dy=self.y-other.y
        return sqrt(dx*dx+dy*dy)
    def transalate(self,dx,dy):
        self.x=dx
        self.y=dy
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"
# =============================================================================
#     def __str__(self):
#     return "(" + str(self.x) + ", " + str(self.y) + ")"
# =============================================================================

#p=Point(3,-4)
#p.set_location(1,5)
#print(p.distance_from_origin())
#Point.set_location(p,1,5)
#print(p.distance_from_origin())
#print(p.__str__())
#print()