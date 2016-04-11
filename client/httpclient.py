import socket

HOST = '127.0.0.1'
PORT = 5050
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    number = raw_input('Enter your a number: ')
    s.send(number)
    reply = s.recv(BUFFER_SIZE)
    if reply == 'Quit':
        break
    print reply

s.close()