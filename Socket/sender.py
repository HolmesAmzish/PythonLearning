"""
brief: UDP sender socket program
date: 2024-09-13
"""

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(sys.argv[1].encode(), ('192.168.126.135', 8000))
s.close()