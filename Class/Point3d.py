# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:00:46 2023

@author: birhane
"""
from Point import *
class Point3D(Point):
    z=0
    def __init__(self,x,y,z):
        Point.__init__(self,x,y)
        self.z=z
    def transalate(self, dx, dy,dz):
        Point.transalate(self, dx, dy)
        self.z=dz
p=Point3D(4,5,6);
p.set_location(1,5)
print(p.distance_from_origin())
#print(p.translate(7,8,9))
