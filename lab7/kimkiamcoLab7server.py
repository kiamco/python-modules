#!/bin/python

import socket

port=57854
localhost='127.0.0.1'

try:
    print('Creating Socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
    
    s.bind((localhost, port))
    print(f"Socket binded on port {port}")
    
    s.listen(5)
    print(f"listening at {localhost}:{port}")
    
    while True: 
  
    # Establish connection with client. 
        c, addr = s.accept()      
        print('Got connection from', addr) 
        output = 'Thank you for connecting'
        c.sendall(output.encode('utf-8'))
        c.close() 
    
except socket.error as err: 
    print(f"socket creation failed with error {err}")
    
    
""" --------- run -------------------
Creating Socket
Socket created
Socket binded on port 57854
listening at 127.0.0.1:57854
Got connection from ('127.0.0.1', 58580)
"""