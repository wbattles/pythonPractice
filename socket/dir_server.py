import socket

host = '192.168.0.202'
port = 9087

name = input('Username: ')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))

socket.listen()
client, addresss = socket.accept()

while True:
    enter = input('Enter: ')
    chat_msg = name + ': ' + enter
    client.send(chat_msg.encode())

    receive = client.recv(1024)
    msg = receive.decode()
    print(msg)