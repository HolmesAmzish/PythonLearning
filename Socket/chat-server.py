"""
program: chat-server.py
description: A simple chat server
date: 2024-09-13
"""

import socket

words = {'What is your name': 'My name is Orms',
         'How old are you': '6 years'}

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Listening at port:', PORT)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print('Received message:', data)
    conn.sendall(words.get(data, 'Nothing').encode())
conn.close()
s.close()