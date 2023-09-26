# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:32:41 2023

@author: birhane
"""

from socket import socket, AF_INET, SOCK_STREAM
(SERVER, PORT) = ('127.0.0.1', 9999)
s = socket(AF_INET, SOCK_STREAM)
s.connect((SERVER, PORT))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print ('Received', data)
