# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:14:41 2023

@author: birhane
"""
import re
try:
    f=open('mbox-short.txt','r')
    for line in f:
        line=line.rstrip()
        if re.search('From:', line):
            print(line)
except IOError:
    print('Error Reading File')
f.close()
# =============================================================================
# try:
#     f2=open('mbox-short.txt','r')
#     for line in f2:
#         line=line.rstrip()
#         if line.find('From:')>=0:
#             print(line)
# except IOError:
#     print('Error Reading File')
# =============================================================================
