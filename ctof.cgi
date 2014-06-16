#!/usr/bin/python
# program name: ctof.cgi
# author: T. Morris
# date: June 2014
# comment: implements a REST API and converts Centigrade to Fahrenheit
# script deployed on http server

import sys
import cgi

LOG = "/usr/lib/cgi-bin/cgilog.txt"

# Create instance of FieldStorage 
form = cgi.FieldStorage()

def update_file(message,filename): # append filename with message
        f = open(filename,"a")
        f.write(message)
        f.close()

def isfloat(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True		# return true if value is a real number

c = form.getvalue('c')	 # read parameter 'c' from cgi command line

if isfloat(c): # arg c is a real number	

	f = (float(c)*9.0)/5.0 + 32.0 # convert to fahrenheit

	CGI_OUTPUT = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"\
	+ "<temperature>\n"\
	+ "<celsius>%s</celsius>\n" % (c)\
	+ "<fahrenheit>%s</fahrenheit>\n" % (f)\
	+ "</temperature>\n"
	print "Content-type: text/xml\n"     # o/p header
	print CGI_OUTPUT 	# o/p xml response 

	update_file("Content-type: text/xml\n\n",LOG)	# write o/p to log
	update_file(CGI_OUTPUT,LOG)
