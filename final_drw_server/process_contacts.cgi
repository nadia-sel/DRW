#!C:\Users\Nadia\AppData\Local\Programs\Python\Python37-32\python.exe

import os
import cgi
import functionsforDRW



formData = cgi.FieldStorage()
u= formData.getvalue('User')
c1 = formData.getvalue('Contact1')
c2 = formData.getvalue('Contact2')
c3 = formData.getvalue('Contact3')
link = "/drw_server/new_contact.cgi?user_ID="+ u +"&contact_1="+c1+"&contact_2="+c2+"&contact_3="+c3
print("""Content-Type: text/html\n\n
    <head>
    </head>
    <body>
    <p>
    Contact 1: """ +c1+ """
    </p>
    Contact 2: """ +c2+ """
    <p>
    Contact 3: """ +c3+ """
    </p>
    <div><a href =" """ + link + """ "><button type="button">Confirm Emergency Contact Information?</a></div>
    </body>
    </html>""")
