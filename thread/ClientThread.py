import socket
import threading


class ClientThread(object):
    def __init__(self, port, host):
        self.port = port
        self.host = host
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))

        def listen(self):
            self.socket.listen(3)
            while True:
                client_connection, client_address = self.socket.accept()
                client_connection.settimeout(60)
        pass
