from socket import *

server_name = '127.0.0.1'
server_port = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence')
message = message.encode()
clientSocket.sendto(message, (server_name, server_port))
modified_message, server_address = clientSocket.recvfrom(2048)
print(modified_message.decode())
clientSocket.close()
