# Command-line Program gets your data from Google+
# License: Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.(http://creativecommons.org/licenses/by-nc-sa/3.0/)
# Author: Dhruv Baldawa (http://www.dhruvb.com/)
# Copyright: Dhruv Baldawa (http://www.dhruvb.com/)

# importing urllib2 to get the URL by sending
# GET requests
import urllib2

# importing json to decode the response in JSON
# format and convert it into a Python object
import json


CLIENT_ID = ''
CLIENT_SECRET = ''
API_KEY = ''
REDIRECT_URI = ''

# this function generates the Authorization URL for the user
# The user needs to get the permission from the Google+ page
def generate_authorization_url(client_key, redirect_uri):
	print '== Copy and Paste this URL in your browser =='
	print 'https://accounts.google.com/o/oauth2/auth?client_id='+client_key+'&redirect_uri='+redirect_uri+'&scope=https://www.googleapis.com/auth/plus.me&response_type=token&xoauth_displayname=Googly'

# this function gets the user data from Google+ using GET
# requests and then decodes the JSON received from Google+
def get_user_data(access_token):
	# Sending a HTTP GET request to the server
	response = urllib2.urlopen('https://www.googleapis.com/plus/v1/people/me?access_token='+access_token)
	# Read the response from the server
	data = response.read()
	# Convert JSON response to Python objects
	data = json.loads(data)
	return data

# prints a nice message back to the user
def say_hello_world(data):
	print "========================================="
	print "  + Hello "+data['displayName']
	print "  + I am shocked you are "+data['relationshipStatus']+" !"
	print "  + I know something about you:"
	print data['aboutMe']
	print "========================================="
	print "Author: @dhruvbaldawa"

# main method
if __name__ == '__main__':
	client_id = CLIENT_ID if CLIENT_ID else raw_input("Enter your client ID: ")
	client_secret = CLIENT_SECRET if CLIENT_SECRET else raw_input("Enter your client secret: ")
	redirect_uri = REDIRECT_URI if REDIRECT_URI else raw_input("Enter the redirect URI: ")
	api_key = API_KEY if API_KEY else raw_input("Enter your API Key: ")	
	generate_authorization_url(client_id, redirect_uri)
	access_token = raw_input("Enter your access token: ")
	data = get_user_data(access_token)
	say_hello_world(data)
	
