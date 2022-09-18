import socket

host = '192.168.0.202'
port = 9087

name = input('Username: ')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

intro = name + 'joined'
socket.send(intro.encode())

while True:
    receive = (socket.recv(1024)).decode()
    print(receive)

    enter = input('Enter: ')
    chat_msg = name + ': ' + enter
    socket.send(chat_msg.encode())
