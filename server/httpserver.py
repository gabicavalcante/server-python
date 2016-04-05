#!/usr/bin/python

import socket  # connection support
import signal  # catch the ctrl + c
import time  # access the current time
import sys

# module cgi
import cgi_bin.cgi_bin
# module get request
from methods_requisitions import get_method, post_method

public_html = "/public_html/"


class Server:
    def __init__(self, application, port=6565):
        """
        server's constructor
        :param port: port to connection
        """
        self.application = application
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a new socket object
        # flag tells the kernel to reuse a local socket in TIME_WAIT state,
        # without waiting for its natural timeout to expire.
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = '127.0.0.1'
        self.port = port
        self.http_root = '.'  # Directory where web page files are stored

    def start_server(self):
        """
        Method to start the server
        """
        try:
            print "Serving HTTP on port %s | host %s " % (self.port, self.host)
            self.socket.bind((self.host, self.port))  # bind the socket to a local address
        except Exception as exc:
            print "Exception %s " % exc
            self.shutdown()
            sys.exit(1)

        print "Server successfully connected port %s | host %s " % (self.port, self.host)
        print "Press Ctrl + C to stop"
        self._doing_connections()

    def shutdown(self):
        """
        Method to shutdown the server
        """
        try:
            print "Adios. Shutting down the server"
            self.socket.shutdown(socket.SHUT_RDWR)
        except Exception as exc:
            print "Problems to shutdown the server, I'm sorry. Check if it was already closed, do me this favor. %s " % exc

    def _doing_connections(self):
        """
        Method to make the connection
        """
        while True:
            print "waiting request..."

            self.socket.listen(3)  # maximum number of connections

            # socket to client and clients address
            client_connection, client_address = self.socket.accept()
            # accept(): Return a new socket representing the connection, and the address of the client

            print "connection from: {0}' ".format(client_address)

            request = client_connection.recv(1024)  # receive the client data
            request_string = bytes.decode(request)  # decode the request to string

            # get the first word in the request
            method = request_string.split(' ')[0]
            print "method: %s " % method
            print "content: %s " % request_string

            if method == 'GET':
                required_file = self.http_root + get_method.GetRequest(request_string).handle_request()

                print "required file {0}".format(required_file)

                try:
                    file_response = open(required_file, 'rb')
                    response_content = file_response.read()
                    file_response.close()
                    response_headers = self._build_header(200)
                except Exception as exc:
                    print "exception to open the file in the server {0}".format(exc)
                    response_headers = self._build_header(404)
                    response_content = open('.' + public_html + '404.html', 'rb').read()

                str.replace("<% var %>", "was")
                server_response = response_headers.encode() + response_content

                client_connection.sendall(server_response)
                print "closing connection with client... bye"
                client_connection.close()

            else:
                post_method.PostRequest(request_string).handle_request()
                print "in progress"

    @staticmethod
    def _build_header(status):
        """
        Method to build a response header
        :param status: 200 if the page was found or 400 if not
        :return: a response header
        """
        header = ""
        if status == 200:
            header = 'HTTP/1.0 200 OK\n'
        elif status == 404:
            header = 'HTTP/1.1 404 Not Found\n'

        current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        header += 'Date: ' + current_time + '\n'
        header += 'Server: Unice\n'
        header += 'MIME-version: 1.0\n'
        header += 'Content-type: text/html\n'

        return header

    @staticmethod
    def _args_handler(args):
        """
        Method to split the argument and get the parameters
        to build the file name that will be send as server's answer
        :param args: url arguments
        :return: file name
        """
        list_args = args.split('&')
        file_name = ""
        for param in list_args:
            file_name += param.split('=')[1]
        return file_name + ".html"

    @staticmethod
    def _args_handler_cgi(args):
        """
        Method to handle with the arguments by cgi_bin
        :param args: url arguments
        :return: file name
        """
        form = cgi_bin.cgi_bin.FieldStorage(args)
        return form["name"] + form.getvalue("prenome") + ".html"


def signal_handler(sig, frame):
    """
    Signal handler to stop the program if the
    user pressed ctrl + c in the terminal
    :param sig: signal number
    :param frame: current stack frame
    source: https://docs.python.org/2/library/signal.html
    """
    print('stopping the program...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# method main
if __name__ == '__main__':
    print 'starting web server...'
    server = Server(5050)
    server.start_server()
