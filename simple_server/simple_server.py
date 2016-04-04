import socket

HOST = '127.0.0.1'
PORT = 5050

HTTP_ROOT = "index.html"
HEADER = """
HTTP/1.0 200 OK
Content-Type: text/html
"""

CONTENT = ("\n"
           "<html>\n"
           "	<head>\n"
           "		<title>L'exemple HTML le plus simple</title>\n"
           "	</head>\n"
           "	<body>\n"
           "		Boo!\n"
           "	</body>\n"
           "</html> \n")

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    if 'GET' in request:
        http_response = HEADER + CONTENT
        client_connection.sendall(http_response)
    client_connection.close()
