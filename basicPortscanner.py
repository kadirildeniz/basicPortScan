def portScan():
    import socket
    print("enter ip address")
    ipAddress = raw_input()
    print("End Port Number :")
    startPort = input()
    for i in range(startPort):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex(('{0}'.format(ipAddress), i))
        if result == 0:
            print("Port open , open port {0}".format(i))
        else:
            print("Port close , close port {0}".format(i))


portScan()
