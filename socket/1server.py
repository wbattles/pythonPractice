#create server

import socket

#find host ip
#host = socket.gethostbyname(socket.gethostname())
host = '192.168.0.202'
port = 9092

#create socket, ccepting connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(5)

while True:
    # accept() returns an address and a socket
    communication_socket, address = server.accept()
    print(f'Connected to {address}')

    #recieve up to 1024 bytes
    message = communication_socket.recv(1024).decode('utf-8')
    print(f'Message from client is: {message}')
    communication_socket.send(f"Message recieved".encode('utf-8'))
    communication_socket.close()
