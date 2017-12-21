#!/usr/bin/env python3
from socket import *
import base64

def _send_log(msg):
    print('send: %s' % msg)

def _reply_log(msg):
    print('reply: %s' % msg)

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.exmail.qq.com' 
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
# Fill in end
recv = clientSocket.recv(1024).decode()
_reply_log(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'ehlo Alice\r\n'
_send_log(heloCommand)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
_reply_log(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send MAIL FROM command and print server response.
# Fill in start
auth = 'AUTH PLAIN ADFAZnhjZGV2LmNvbQBYaWFva2VuZ2JpMTIz\r\n'
_send_log(auth)
clientSocket.send(auth.encode())
recv2 = clientSocket.recv(1024).decode()
_reply_log(recv2)

from_msg = input('From:')
from_msg = ('mail FROM:<%s> \r\n' % from_msg) 
_send_log(from_msg)
clientSocket.send(from_msg.encode())
recv3 = clientSocket.recv(1024).decode()
_reply_log(recv3)
# Fill in end
# Send RCPT TO command and print server response.
to = input('To:')
to = ('rcpt To:<%s> \r\n' % to)
_send_log(to)
clientSocket.send(to.encode())
recv4 = clientSocket.recv(1024).decode()
_reply_log(recv4)
# Fill in start
# Fill in end
# Send DATA command and print server response.
data = 'data\r\n'
_send_log(data)
clientSocket.send(data.encode())
recv5 = clientSocket.recv(1024).decode()
_reply_log(recv5)
# Fill in start
# Fill in end
# Send message data.
body = input('Body: ')
_send_log(body)
clientSocket.send(base64.b64encode(body.encode()))
clientSocket.send('\r\n.\r\n'.encode())
recv6 = clientSocket.recv(1024).decode()
_reply_log(recv6)
# Fill in start
# Fill in end
# Message ends with a single period.
# Fill in start
# Fill in end
# Send QUIT command and get server response.
# Fill in start
bye = 'quit\r\n'
_send_log(bye)
clientSocket.send(bye.encode())
recv7 = clientSocket.recv(1024).decode()
_reply_log(recv7)
# Fill in end
clientSocket.close()