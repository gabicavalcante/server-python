import time


def build_xml(process, url, var, value, resource, flag):
    """

    :rtype: object
    """
    body = """
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <{0} xmlns="{1}">
            <{2}>{3}</{2}>
        </{0}>
    </soap:Body>
</soap:Envelope>""".format(process, url, var, value)
    if flag:
        return build_header_request(resource) + body
    else:
        return build_header_response() + body


def build_header_request(resource):
    """
    Method to build a response header
    :param status: 200 if the page was found or 400 if not
    :return: a response header
    """
    header = 'POST {0} HTTP/1.1\n'.format(resource)

    header += 'Host: http://localhost:5050/\n'
    header += 'Content-type: text/xml; charset=utf-8\n'

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


def build_version(version=1.0, encoding="utf-8"):
    return "<?xml version='{0}' encoding='{1}'?>".format(version, encoding)


# method main
# if __name__ == '__main__':
#    build_xml('NumberToWords', "http://localhost:5050/cgi-bin/", "ubiNum", 10)
