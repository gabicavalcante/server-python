"""
Class to handle with the post request.

File:       post_method
Created:    04/04/2016
Author:     Gabriela Cavalcante
"""

public_html = "/public/"


class PostRequest:
    def __init__(self, request):
        self.request = request
        pass

    def handle_request(self):
        if len(self.request.split(' ')) > 1:
            args = self.request.split(' ')[1]  # take the required file and arguments

        if len(args.split("?")) > 1:
            required_file = public_html + self._args_handler_cgi(args.split("?")[1])
        else:
            required_file = public_html + args

        if required_file == '/':
            required_file = public_html + "/index.html"

        print "required file {0}".format(required_file)
        return required_file

    @staticmethod
    def _args_handler_cgi(args):
        """
        Method to handle with the arguments by cgi-bin
        :param args: url arguments
        :return: file name
        """
        form = cgi_bin.cgi_bin.FieldStorage(args, "post")
        if form.contains("student"):
            return "student.html"
        elif form.contains("teacher"):
            return "teacher.html"
        elif form.contains("back"):
            return "/index.html"
        elif form.contains("form"):
            return "/form.html"
        else:
            return "non.html"
