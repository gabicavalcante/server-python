"""
Class to handle with the get request.

File:       get_method
Created:    04/04/2016
Author:     Gabriela Cavalcante
"""

import cgi_bin.cgi_bin

public_html = "/public_html/"


class GetRequest:
    def __init__(self, request):
        self.request = request
        self.resource_request = ""
        self.arg_dynamic = []
        pass

    def handle_request(self):
        args = self.request.split(' ')[1]  # take the required file and arguments

        if len(args.split("?")) > 1:
            required_file = public_html + self._args_handler_cgi(args.split("?")[1])
        else:
            required_file = public_html + args

        if required_file == public_html + '/':
            required_file = public_html + "/index.html"

        print "required file {0}".format(required_file)
        return required_file

    @staticmethod
    def _args_handler_cgi(args):
        """
        Method to handle with the arguments by cgi_bin
        :param args: url arguments
        :return: file name
        """
        form = cgi_bin.cgi_bin.FieldStorage(args)
        if form.contains("type"):
            if form["type"] == "student":
                return "student.html"
            elif form["type"] == "teacher":
                return "teacher.html"
        elif form.contains("back"):
            return "/index.html"
        elif form.contains("form"):
            return "/form.html"
        else:
            return "non.html"
