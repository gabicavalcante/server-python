import time


def build_xml(process, url, var, value, resource, host, flag):
    """

    :rtype: object
    """
    body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://schemas.xmlsoap.org/soap/envelope/">
<soap12:Body>
<{0} xmlns="{1}">
<{2}>{3}</{2}>
</{0}>
</soap12:Body>
</soap12:Envelope>""".format(process, url, var, value)
    if flag:
        return build_header_request(resource, body, host) + body
    else:
        return build_header_response() + body


def build_header_request(resource, body, host):
    """
    Method to build a response header
    :param status: 200 if the page was found or 400 if not
    :return: a response header
    """
    header = 'POST {0} HTTP/1.1\n'.format(resource)
    header += 'Host: {0}\n'.format(host)
    header += 'Content-type: application/soap+xml; charset=utf-8\n'
    header += "Content-Length: "+ str(len(body)) + "\n\n"

    return header


def build_header_response():
    """
    Method to build a response header
    :param status: 200 if the page was found or 400 if not
    :return: a response header
    """
    header = 'HTTP/1.0 200 OK\n'

    current_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    header += 'Date: ' + current_time + '\n'
    header += 'Server: Unice\n'
    header += 'MIME-version: 1.0\n'
    header += 'Content-type: text/xml; charset=utf-8\n'

    return header