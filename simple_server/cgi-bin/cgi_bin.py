# !/usr/bin/python
"""
Class to represents a cgi (very very very simple, thanks).

File:       cgi_bin
Created:    30/03/2016
Author:     Gabriela Cavalcante
"""
import os


class FieldStorage:
    def __init__(self, environ=os.environ):
        self.__params = {}
        self.__read_url()
        self.__method = "GET"
        if 'REQUEST_METHOD' in environ:
            self.method = environ['REQUEST_METHOD'].upper()

    def __read_url(self):
        """
        Method ("private") to read a url and create the dictionary with the arguments.
        """
        list_args = os.environ["QUERY_STRING"].split('&')
        for param in list_args:
            key, value = param.split('=')
            self.__params[key] = value

    def getvalue(self, key):
        """
        Method to return a argument (value) given a parameter (key)
        :param param: parameter
        :return: the value
        """
        if self.contains(key):
            return self.__params.get(key)
        else:
            return None

    def contains(self, param):
        """
        Method to checks if a param exists
        :param param: parameter
        :return: a flag indicating if the param exists
        """
        return param in self.__params

    def __getitem__(self, key):
        """
        built-function to return a item using []
        :param param: parameter
        :return: the value
        """
        return self.__params.__getitem__(key)
