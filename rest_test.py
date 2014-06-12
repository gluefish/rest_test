#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: T. Morris
# Date: June 2014
# Code Name: rest_test.py
# Function: demonstrates how a basic REST client works and uses a DOM parser
# to extract the required data

from time import gmtime, strftime
from xml.dom.minidom import parseString
import urllib

HOMEDIR = "/users/Tom/CodeProjects/WebServicesExamples/"
PROGNAME = "Rest"
BASEDIR = HOMEDIR + PROGNAME + "/"
LOGDIR = BASEDIR + "Log"
BINDIR = BASEDIR + "Bin"
DATADIR = BASEDIR + "Data"
LOGFILE = LOGDIR + "/logfile.txt"

XML_ENDPOINT = "http://maps.googleapis.com/maps/api/geocode/xml"

def get_date(): # return current date and time
        return strftime("%d-%m-%Y %H:%M:%S", gmtime())

def update_file(message,filename): # append filename with message
        f = open(filename,"a")
        f.write(message)
        f.close()

DATESTR = get_date()
STREET_ADDRESS = raw_input("Please enter the street address: ")
CITY = raw_input("Please enter the city name: ")
UNFORMATED_ADDRESS_STRING = "%s, %s" % (STREET_ADDRESS,CITY)
ADDRESS_STRING = UNFORMATED_ADDRESS_STRING.replace(" ","+")
API_ENDPOINT = XML_ENDPOINT + "?address=" + ADDRESS_STRING + "&sensor=False"

update_file("<p>INFO: now testing the Google API ... " + DATESTR + " </p>\n",LOGFILE)
update_file("Calling REST url: " + API_ENDPOINT + "\n", LOGFILE)
apiobj = urllib.urlopen(API_ENDPOINT)	
response = apiobj.read()		# read response from URL 

update_file(response,LOGFILE) # write raw response to logfile	

domtree = parseString(response)
dom = domtree.documentElement
comp_list =  dom.getElementsByTagName('address_component') # get all address components

for i in comp_list:	# step through each address component list
		
		type = i.getElementsByTagName('type')[0]
		if type.childNodes[0].data == 'postal_code':	# postcode component list identified
			
			short_name = i.getElementsByTagName('short_name')[0]    # read postcode from elelent
			postcode_string =  "Postal Code: %s" % short_name.childNodes[0].data
			print postcode_string
	
			update_file(UNFORMATED_ADDRESS_STRING + "\n",LOGFILE)
			update_file(postcode_string + "\n",LOGFILE)	

apiobj.close()


# end of file
