# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:25:36 2023

@author: birhane
"""

class Student: 
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name 
student = Student('V12', 'Frank Gibson', 'V')
print(student.__dict__)