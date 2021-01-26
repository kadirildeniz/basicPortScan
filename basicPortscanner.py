import os
import socket
import time

print("End Port Number :")
startPort = input()
for i in range(startPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex(('192.168.1.1', i))
    if result == 0:
        print("Port open , open port {0}".format(i))
    else:
        print("Port close , close port {0}".format(i))


