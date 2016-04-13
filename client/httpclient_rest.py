import socket
import sys
import signal

HOST = '127.0.0.1'
PORT = 5050
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

REQUEST_REST = (
    """POST /cgi-bin/numberToWords HTTP/1.1
Host: localhost:5050
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://localhost:5050
Upgrade-Insecure-Requests: 1
Content-Type: text/xml; charset=utf-8
Referer: http://localhost:5050/form_rest.html
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.6,en;q=0.4,fr;q=0.2

ubiNum="""
)

number = raw_input('Enter your a number: ')
REQUEST_REST = REQUEST_REST + number
s.send(REQUEST_REST)
reply = s.recv(BUFFER_SIZE)
print reply


def signal_handler(sig, frame):
    """
    Signal handler to stop the program if the
    user pressed ctrl + c in the terminal
    :param sig: signal number
    :param frame: current stack frame
    source: https://docs.python.org/2/library/signal.html
    """
    print('stopping the client...')
    s.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
s.close()
