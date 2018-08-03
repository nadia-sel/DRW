#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
import functionsforDRW
import os

url = os.environ["REQUEST_URI"]
name = functionsforDRW.parse_url(url, 'name')
functionsforDRW.create_user(name)
