import socket
import sys
import signal
from util.parser import build_xml

HOST = '127.0.0.1'
PORT = 5050
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

number = raw_input('Enter your a number: ')
# request_soap = request_soap.replace("unsignedLong", str(number))
request = build_xml('NumberToIncrement', 'http://localhost:5050/cgi-bin/', 'num', str(number), '/cgi-bin/incrementNumSoap', 1)
s.send(request)
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
