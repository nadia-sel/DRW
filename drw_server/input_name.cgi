#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import cgi
import functionsforDRW

a = """Content-Type: text/html\n\n
    <head>
    </head>
    <body>
    <form action ="process_name.cgi">
        Name:<br>
        <input type="text" name="Name" value="">
        <br><br>
        <input type="submit" value="Submit">
    </form>
    </body>
    </html>"""
print(a)
