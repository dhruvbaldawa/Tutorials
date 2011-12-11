#!/usr/bin/python
"""
--------------------------------------------------------------------------
Python script to send SMS using services like Way2SMS, FullOnSMS, Site2SMS
--------------------------------------------------------------------------
This script basically simulates a login, just as you would, while sending
the SMS using these websites. But, saves you time by automating stuff, plus
you can do other cool stuff with this script.

DISCLAIMER
The main intention for this script is for educational purposes only.

For clarifications, contace me at
@dhruvbaldawa on twitter
Dhruv Baldawa on Facebook/Google+

REFERENCES
http://docs.python.org/library/cookielib.html#examples
http://docs.python.org/library/urllib2.html

"""

import cookielib
import urllib2
from getpass import getpass # for unix only, comment this line if using in windows
import sys
from urllib import urlencode

# Default initializations (saves time)
username = None
password = None
message = None
number = None
TOTAL = 260

# Initializing some "so-called" constants
CONNECTION_ERROR = -1
SUCCESS = 1

def login(username, password, opener):
  '''
  This method takes care of logging onto the website
  '''
  #Logging into the SMS Site
  url = 'http://site1.way2sms.com/Login1.action'
  url_data = urlencode({'username':username,
                            'password':password,
                            'button':'Login'})
  # debug message
  # print url_data
  
  try:
  	usock = opener.open(url, url_data)
  	# debug message
  	# print usock.read()
  except IOError:
  	return CONNECTION_ERROR
  return SUCCESS

def sms_send(number, message, opener):
  # SMS sending
  send_sms_url = 'http://site1.way2sms.com/quicksms.action  '
  send_sms_data = urlencode({'Action':'dsf45asvd5', 
                                  'HiddenAction':'instantsms',
                                  'MobNo': number, 
                                  'bulidgpwd': '*******', 
                                  'bulidguid': 'username',
                                  'bulidypwd': '*******',
                                  'bulidyuid': 'username',
                                  'catnameis': 'Birthday',
                                  'chkall': 'on',
                                  'gpwd1': '*******',
                                  'guid1': 'username',
                                  'textArea': message,
                                  'ypwd1': '*******',
                                  'yuid1': 'username'})
  
  opener.addheaders = [('Referer','http://site1.way2sms.com/jsp/InstantSMS.jsp')]
  
  print "Message Length: ", len(message)
  
  try:
  	sms_sent_page = opener.open(send_sms_url,send_sms_data)
  except IOError:
  	return CONNECTION_ERROR
  return SUCCESS


print "----------------------------------------------------"
print "| SMS Sender Script                                |"
print "| Register at way2sms.com, to use this script      |"
print "| Use your username and password                   |"
print "| Make changes in this script on line 30 & line 31 |"
print "| to keep away from entering the username and      |"
print "| password repeatedly, also you can use it for your|"
print "| applications.                                    |"
print "| For suggestions: @dhruvbaldawa (twitter)         |"
print "| Comment lines 89 to 99 to stop this message      |"
print "----------------------------------------------------"


# Take the user input
if username is None: username = raw_input("Enter Username: ")
# getpass() method takes shell input, without displaying the password
# however, it may not work in windows, so use the following line in 
# windows.
#
#if password is None: password = raw_input("Enter password: ")
if password is None: password = getpass()
if number is None: number = raw_input("Enter Mobile number: ")
if message is None: message = raw_input("Enter Message: ")

# CookieJar for automatic handling of cookies
# For more information on cookielib
# http://docs.python.org/library/cookielib.html#examples
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# To fool the website as if a Web browser is visiting the site
opener.addheaders = [('User-Agent','Mozilla/5.0 (Ubuntu; X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]

# Send the SMS
return_code = login(username, password, opener)

if return_code == CONNECTION_ERROR:
  print "Error while logging in. Check your internet connection"
  sys.exit(1)
elif return_code == SUCCESS:
  print "Logged in successfully."

return_code = sms_send(number, message, opener)

if return_code == CONNECTION_ERROR:
  print "Error while sending SMS. Check your internet connection"
elif return_code == SUCCESS:
  print "SMS Sent successfully."

