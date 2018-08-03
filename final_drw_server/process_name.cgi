#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import cgi
import functionsforDRW

formData = cgi.FieldStorage()
name= formData.getvalue('Name')
link = "/drw_server/new_user.cgi?name=" + str(name)
print("""Content-Type: text/html\n\n
    <head>
    </head>
    <body>
    <p>
    Name: """ +name+ """
    </p>
    <div><a href =" """ + link + """ "><button type="button">Confirm Name?</a></div>
    </body>
    </html>""")
