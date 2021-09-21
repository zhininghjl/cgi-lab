#!/usr/bin/env python3
# chmod +x login.py make the file executable


import cgi, cgitb

form = cgi.FieldStorage()
username = form.getvalue("username")
password  = form.getvalue("password")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<p><b>username:</b> %s <b>password:</b> %s </p>" % (username, password))
print("</body>")
print("</html>")