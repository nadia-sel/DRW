#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe


import cgi
import functionsforDRW
import os

url = os.environ["REQUEST_URI"]
ID = functionsforDRW.parse_url(url, 'event_ID')
status = functionsforDRW.parse_url(url, 'status')
functionsforDRW.update_status(ID, status)
