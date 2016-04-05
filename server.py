from wsgi import wsgi
from server import httpserver

if __name__ == '__main__':
    httpserver.Server(wsgi.app).start_server()
