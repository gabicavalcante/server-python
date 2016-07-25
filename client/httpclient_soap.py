import socket
import sys
import signal
from util.parser import build_xml

"""
Http client to make a soap request.

Uncomment the lines to use the local server.
"""

#HOST = '127.0.0.1'
#PORT = 5050
HOST = 'dataaccess.com'
PORT = 80
BUFFER_SIZE = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

number = raw_input('Enter your a number: ')
# request = build_xml('NumberToWords', 'http://localhost:5050/cgi-bin/', 'ubiNum', str(number), '/cgi-bin/numberToWordsSoap', 'http://localhost:5050', 1)
request = build_xml('NumberToWords', 'http://www.dataaccess.com/webservicesserver/', 'ubiNum', str(number), '/webservicesserver/numberconversion.wso', 'www.dataaccess.com', 1)

encoded = request.encode()
s.sendall(encoded)

reply = s.recv(BUFFER_SIZE)
decoded = reply.decode()
s.close()
print decoded


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
