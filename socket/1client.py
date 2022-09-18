#communicate with server
#LAN connections w/ private ip

import socket

host = '192.168.0.202'
port = 9092

#create socket, connect to server
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

#send msg to server, receive response
inp = input("Enter word: ")
socket.send(inp.encode('utf-8'))
print(socket.recv(1024))
