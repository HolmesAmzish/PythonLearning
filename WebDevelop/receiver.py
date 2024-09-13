"""
brief: UDP client socket program
date: 2024-09-13
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 8000))

while True:
    data, addr = s.recvfrom(1024)
    data = data.decode()
    print('received message:{0} from PORT {1[1]} on {1[0]}'.format(data, addr))
    if data.lower() == 'bye':
        break

s.close()