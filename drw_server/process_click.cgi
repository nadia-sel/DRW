#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import functionsforDRW
import os
import datetime

url = os.environ["REQUEST_URI"]
id = functionsforDRW.parse_url(url, 'user_ID')
id = str(id)
time = datetime.datetime.time(datetime.datetime.now())
time = str(time)
long = functionsforDRW.parse_url(url, 'longitude')
lat = functionsforDRW.parse_url(url, 'latitude')
status = functionsforDRW.parse_url(url, 'status')
event_ID = functionsforDRW.add_event(id, time, long, lat, status)
event_ID = str(event_ID)
functionsforDRW.contact(id, event_ID)

a = """Content-Type: text/html\n\n
<html lang='en-US'>
<head>
</head>
<body>
Successfully Processed!
</body>
</html>"""
print(a)
