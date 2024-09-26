"""
program: chat-client.py
description: A chat client
date: 2024-09-13
"""

import sys
import socket

HOST = '192.168.126.135'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except Exception as e:
    print('Server not found or not running')
    sys.exit()
while True:
    c = input('Input the content you want to send: ')
    s.sendall(c.encode())
    data = s.recv(1024).decode()
    print('Recevied: ', data)
    if c.lower() == 'bye':
        break
s.close()