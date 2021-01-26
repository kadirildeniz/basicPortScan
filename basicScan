import os
import time

print("Port Number :")
startPort = input()
operatingSystem = os.name
for i in range(startPort):
    if operatingSystem == "posix":
        outputPortScan = os.system("nc -z -v 192.168.1.1 {0}".format(i))
    elif operatingSystem == "nt":
        print("!!")
    else:
        print "not support OS "



