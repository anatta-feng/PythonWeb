from socket import *
import time

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = 'send'.encode()
clientSocket.settimeout(1)
for i in range(0, 10):
    start = int(round(time.time() * 1000))
    rtt = 0
    clientSocket.sendto(msg, ('127.0.0.1', serverPort))
    try:
        message, addr = clientSocket.recvfrom(1024)
    except timeout:
        message = 'lost'.encode()
    finally:
        rtt = int(round(time.time() * 1000)) - start
    print(message.decode(), "  ", rtt)
