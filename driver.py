#!/usr/bin/env python3

import sys
import urllib
import webbrowser
import requests
import getpass
import os
import io 
from pyquery import PyQuery

def get_info():
    answer = input("Do you have a Papa John's account (y/n)? ")
    if len(answer) == 0:
        print("Please enter y or n")
        get_info()
    if answer == 'y' or answer == 'yes': 
        hasAccount = True
    elif answer == 'n' or answer =='no':
        hasAccount = False
    return hasAccount

print("Welcome to PizzaMe. This is in beta, so please let me know any issues that arise.")
# print("Please be reasonable with user input, this is in early development")

if get_info() == False:
    print("Please make an account on the Papa John's website and the run this script again")
    webbrowser.open("https://www.papajohns.com/order/create-account", new=2)
    sys.exit(1)

#name = input("What is your name? ")

#email
#id = signIn-account-sign-in-email
#name = user
user = input("Enter your account email address: ")

#pwd
#id = signIn-account-sign-in-password
#name = pass
password = getpass.getpass("Enter your account password: ")


url = 'https://www.papajohns.com/order/sign-in'
payload = { 'user': user, 'pass': password }

data = urllib.parse.urlencode(payload)
'''
opener = urllib.request.build_opener(
    urllib.request.HTTPRedirectHandler(),
    urllib.request.HTTPHandler(debuglevel=0),
    urllib.request.HTTPSHandler(debuglevel=0),
    urllib.request.HTTPCookieProcessor(cookies))
response = opener.open(url, data)
the_page = response.read()
http_headers = response.info()
'''
#p = requests.get(url)
#print(p.headers)

# Use 'with' to ensure the session context is closed after use.
# Session handles cookies
with requests.Session() as s:
    r = s.post(url, data=payload)
    #    p = s.get()
    buf = io.StringIO(r.text)
    count = 0
    while len(buf.readline()) <= len('\n'):
        count += 1

    print("Count: " + str(count))
#    print("Title: " + r.title)

fd = open("form.html", "wb")
fd.write(r.content)
fd.close

webbrowser.open("file:///Volumes/Mac/Users/jessetatum/Documents/projects/PizzaMe/form.html")

