#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import cgi
import functionsforDRW


url = os.environ["REQUEST_URI"]
user_ID = functionsforDRW.parse_url(url, 'user_ID')
contacts = functionsforDRW.get_contacts(user_ID)
a = """Content-Type: text/html\n\n
    <head>
    </head>
    <body>
    <form action ="process_contacts.cgi">
        <div hidden>
        UserID:<br>
        <input type= "text" name="User" value=""" + str(user_ID) +""">
        <br>
        </div>
        Contact1:<br>
        <input type= "text" name="Contact1" value=""" + str(contacts[0]) +""">
        <br>
        Contact2:<br>
        <input type= "text" name="Contact2" value=""" + str(contacts[1]) +""">
        <br>
        Contact3:<br>
        <input type="text" name="Contact3" value=""" + str(contacts[2]) +""">
        <br><br>
        <input type="submit" value="Submit">
    </form>
    </body>
    </html>"""
print(a)
