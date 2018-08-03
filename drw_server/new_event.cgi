#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe


import cgi
import functionsforDRW
import os

url = os.environ["REQUEST_URI"]
id = functionsforDRW.parse_url(url, 'user_ID')
id = int(id)
time = functionsforDRW.parse_url(url, 'time')
long = functionsforDRW.parse_url(url, 'longitude')
lat = functionsforDRW.parse_url(url, 'latitude')
status = functionsforDRW.parse_url(url, 'status')
functionsforDRW.add_event(id, time, long, lat, status)
