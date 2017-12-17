# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket
# Fill in start
serverHost = '127.0.0.1'
serverPort = 12000
address = (serverHost, serverPort)
# 先 bind
serverSocket.bind(address)
# 后 listen 等待
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    # 有了新的访客，新建单独链接
    connectionSocket, addr = serverSocket.accept()  # tcp 握手
    try:
        # 接收
        message = connectionSocket.recv(1024)  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()  # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print('success')
    except IOError:
        # Send response message for file not found
        # Fill in start
        print('404 error')
        connectionSocket.send('HTTP/1.1 404 not found\r\n\r\n'.encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
