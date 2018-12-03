#!/usr/bin/env python3

import signal
import sys
import urllib
import webbrowser
import requests
import getpass
import os
import io 
from pyquery import PyQuery

def signal_handler(signal, frame):
        print('\nExiting program ... ')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

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

if get_info() == False:
    print("Please make an account on the Papa John's website and the run this script again")
    webbrowser.open("https://www.papajohns.com/order/create-account", new=2)
    sys.exit(1)

#name = input("What is your name? ")

#id = signIn-account-sign-in-email
#name = user
user = input("Enter your account email address: ")

#id = signIn-account-sign-in-password
#name = pass
password = getpass.getpass("Enter your account password: ")


url = 'https://www.papajohns.com/order/sign-in'
payload = { 'user': user, 'pass': password }

data = urllib.parse.urlencode(payload)

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
    if count != 4:
        print("nope, not right")
        sys.exit(0)
    #print("Title: " + r.title)

fd = open("form.html", "wb")
fd.write(r.content)
fd.close

webbrowser.open("file:///Volumes/Mac/Users/jessetatum/Documents/projects/PizzaMe/form.html")

