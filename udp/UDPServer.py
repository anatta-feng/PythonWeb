from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print('The server is already to receive')
while True:
    message, client_address = server_socket.recvfrom(2048)
    print(message)
    modifiedMessage = message.decode().upper()
    print(modifiedMessage)
    modifiedMessage = modifiedMessage.encode()
    server_socket.sendto(modifiedMessage, client_address)
