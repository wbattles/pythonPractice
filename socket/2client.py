#client.py
import socket
import threading

host = '172.16.155.3'
port = 9082

username = input('Username: ').strip()
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((host, port))


def sending():
    while True:
        send = input()
       # if send == 'quit':
           # conn.shutdown(socket.SHUT_RDWR)
           # socket.close()
           # exit()
        if send:
            user_msg = username + ': ' + send
            conn.send(user_msg.encode())


def recieving():
    while True:
        message = conn.recv(1024).decode()
        #if username in message:
            #break
        print(message)


thread_send = threading.Thread(target=sending)
thread_receive = threading.Thread(target=recieving)
thread_send.start()
thread_receive.start()


#def closing():