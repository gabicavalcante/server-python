"""
script WSGI

source: http://pythonpaste.org/do-it-yourself-framework.html
05/05/2015
"""

from paste.request import parse_formvars


def app(environ, response):
    fields = parse_formvars(environ)
    if environ['REQUEST_METHOD'] == 'POST':
        response('200 OK', [('content-type', 'text/html')])
        return ['Hello world!', fields["type"]]
    else:
        response('200 OK', [('content-type', 'text/html')])
        return ['<form method="POST">Name: <input type="text" '
                'name="name"><input type="submit"></form>']
