#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: T. Morris
# Date: June 2014
# Code Name: ctof.py
# Function: demonstrates how a basic REST client works and uses a DOM parser
# to extract the required data. Calls the ctof.cgi api on another http server

from time import gmtime, strftime
from xml.dom.minidom import parseString
import urllib

HOMEDIR = "/users/Tom/CodeProjects/WebServicesExamples/"
PROGNAME = "Rest"
BASEDIR = HOMEDIR + PROGNAME + "/"
LOGDIR = BASEDIR + "Log"
BINDIR = BASEDIR + "Bin"
DATADIR = BASEDIR + "Data"
LOGFILE = LOGDIR + "/ctoflog.txt"

XML_ENDPOINT = "http://192.168.1.101/cgi-bin/ctof.cgi"

def get_date(): # return current date and time
        return strftime("%d-%m-%Y %H:%M:%S", gmtime())

def update_file(message,filename): # append filename with message
        f = open(filename,"a")
        f.write(message)
        f.close()

DATESTR = get_date()
CENTIGRADE = "100.00"
API_ENDPOINT = XML_ENDPOINT + "?c=" + CENTIGRADE

update_file("INFO: now testing the ctof API ... " + DATESTR + "\n",LOGFILE)
update_file("Calling REST url: " + API_ENDPOINT + "\n", LOGFILE)
apiobj = urllib.urlopen(API_ENDPOINT)	
response = apiobj.read()		# read response from URL 

update_file(response,LOGFILE) # write raw response to logfile	

dom = parseString(response)
		
c_response = dom.getElementsByTagName('celsius')[0].firstChild.nodeValue
f_response = dom.getElementsByTagName('fahrenheit')[0].firstChild.nodeValue
		

temp_string =  "Celsius: %s Fahrenheit: %s" % (c_response,f_response)
print temp_string
	
update_file(API_ENDPOINT + "\n",LOGFILE)
update_file(temp_string + "\n",LOGFILE)	

apiobj.close()


# end of file
