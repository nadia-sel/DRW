#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import cgi
import functionsforDRW

url = os.environ["REQUEST_URI"]
id = functionsforDRW.parse_url(url, 'user_ID')
c1 = functionsforDRW.parse_url(url, 'contact_1')
c2 = functionsforDRW.parse_url(url, 'contact_2')
c3 = functionsforDRW.parse_url(url, 'contact_3')
functionsforDRW.add_contacts(id, c1, c2, c3)

a = """Content-Type: text/html\n\n
<html lang='en-US'>
<head>
</head>
<body>
Contact Information Successfully Processed!
</body>
</html>"""
print(a)
