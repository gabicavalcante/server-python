#!/usr/bin/python

import os

# print header
print "Content-type: text/html\n\n"

query_string = os.environ["QUERY_STRING"]
print "<h2> Query string </h2>"
print "query_string: " + query_string + "<br>"

print "<h2>Argument list</h2>"
arg_list=query_string.split('&')

i=1
for arg in arg_list:
    key, value=arg.split('=')
    print "key " + str(i) + ": " + key + "<br>"
    print "value " + str(i) + ": " + value + "<br>"
    i += 1
