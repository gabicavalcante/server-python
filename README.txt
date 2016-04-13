Web Service Project
-------------------


AUTHOR
------

Name:   Gabriela Cavalcante da Silva.
ID:     cg507563
Course: SI - 3
Group:  1

ABOUT
-----

This project was made according to the constraints gave us in the TD of "Réseaux et Programmation". 

STRUCTURE
---------

We can find the following structure to this project:

$ server_http_root
.
├── cgi-bin
│   ├── __init__.py
│   ├── arguments.py
│   ├── cgi_bin.py
│   ├── form
│   ├── incr
│   ├── incrementNum
│   ├── incrementNumSoap
│   ├── numberToWords
│   ├── numberToWordsSoap
│   └── welcome
├── client
│   ├── __init__.py
│   ├── httpclient_increment_soap.py
│   ├── httpclient_rest.py
│   └── httpclient_soap.py
├── public_html
│   ├── static
│   ├── 404.html
│   ├── form.html
│   ├── form_increment_rest.html
│   ├── form_rest.html
│   ├── form_rest_test.html
│   └── index.html
├── simple_server
│   ├── __init__.py
│   └── simple_server.py 
├── thread
│   ├── __init__.py
│   ├── Client.py
│   └── ServerThread.py
├── util
│   ├── __init__.py
│   ├── parser.py 
│   └── reboot.py  
├── file_in_root.ext
├── .gitignore
├── httpserver.py
└── README.md

The index page will show a little form with two radiobutton. 
This page has a get form that will call the cgi-bin script 'welcome', and it will return a page with the chosen option.

In the index page we can find a link to a page with post form [public_form/form.html]. 
This form will call the cgi-bin script 'form' and will show the name wrote in the form.

We can find too a link to a rest form. It will can the service of the page Number Conversion Service [1].
A link to a rest form that will use the cgi-bin script 'numberToWords'. And a link to a rest form 
that will call the cgi-bin script 'incrementNum'.

In the client directory we can find a script to a soap client (the rest client was implemented in the 
form_increment_rest.html). We can find too a script to rest and soap client that will use the cgi-bin script
'numberToWords' (rest) and 'numberToWordsSoap' (soap).

There is a file with a simple server made to the first TD in 'simple_server/simple_server.py'.

FEATURES
---------

* MultiThreaded Server [thread/ServerThread.py] and Client [thread/Client] to test the server.
* I chosen the xml to the rest response. 
* I made a cgi-bin script to handle with the arguments [cgi-bin/cgi-bin.py]. This script is used by all script cgi-bin.
* There are a simple parser to create the rest and soap responses
* There are a script to reboot found in [2] 
* There is a method to handle with the Ctrl-C.


Documentation
-------------

The code is documentation was made by comments in all code.


Dependencies
------------

Will necessary install some dependences to run the projetct:

- pip install inflect 


References
----------

[1] http://www.dataaccess.com/webservicesserver/numberconversion.wso?op=NumberToWords
[2] http://stackoverflow.com/questions/7703797/need-to-close-python-socket-find-the-current-running-server-on-my-dev-environm

[error address already in use](http://stackoverflow.com/questions/29217502/socket-error-address-already-in-use)
[script python to close socket](http://stackoverflow.com/questions/7703797/need-to-close-python-socket-find-the-current-running-server-on-my-dev-environm)
[thread](http://stackoverflow.com/questions/23828264/how-to-make-a-simple-multithreaded-socket-server-in-python-that-remembers-client)
[methods python (underscore)](http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python)
[socket listening](http://stackoverflow.com/questions/15869158/python-socket-listening)
[CGI](https://docs.python.org/3/library/cgi.html)


