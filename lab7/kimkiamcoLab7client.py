#!/bin/env python3

import socket

port=57854
localhost='127.0.0.1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((localhost, port))
    s.send("demo".encode())
    data = s.recv(1024)

print('Received', repr(data))


""" ----------- run --------------
Received b'Thank you for connecting'
"""