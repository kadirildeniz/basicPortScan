import os
import socket
import time

print("End Port Number :")
startPort = input()
operatingSystem = os.name
for i in range(startPort):
    if operatingSystem == "posix":
        outputPortScan = os.system("nc -z -v 192.168.1.1 {0}".format(i))
    elif operatingSystem == "nt":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # 2 Second Timeout
        result = sock.connect_ex(('192.168.1.1', i))
        if result == 0:
            print 'port OPEN'
        else:
            print 'port CLOSED, connect_ex returned: ' + str(result)
    else:
        print "not support OS "


