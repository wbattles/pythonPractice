#create server

#from site import USER_SITE
import socket
import threading

#find host ip
#host = socket.gethostbyname(socket.gethostname())
host = '172.16.155.3'
port = 9082

#create socket, ccepting connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

users = []

def accept():
    while True:
        server.listen(5)
        client, address = server.accept()
        print('Connection from: ', address)
        users.append(client)
        start_listen(client)

def start_listen(client):
    client_thread = threading.Thread(target=recieve, args=(client,))
    client_thread.start()

def recieve(client):
    while True:
        message = client.recv(1024).decode()
        #if 'quit' in message:
            #client.shutdown(socket.SHUT_RDWR)
            #client.close()
            #users.remove(client)
            #break
        print(message)
        broadcast(message)

def broadcast(message):
    for client in users:
        client.send(message.encode())

accept()