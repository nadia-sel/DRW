#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe


import cgi
import functionsforDRW
import os

url = os.environ["REQUEST_URI"]
user = functionsforDRW.parse_url(url, 'user')
event = functionsforDRW.parse_url(url, 'event')
functionsforDRW.contact(user, event)
