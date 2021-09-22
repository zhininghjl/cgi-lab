#!/usr/bin/env python3
# chmod +x login.py make the file executable


import cgi, cgitb
from cookie import set_cookie
import secret
from templates import after_login_incorrect, secret_page

form = cgi.FieldStorage()
username = form.getvalue("username")
password  = form.getvalue("password")

if (username == secret.username and password == secret.password):
    secret_page(username, password)
    set_cookie(username, password)
else:
    after_login_incorrect()
    
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - CGI Login Program</title>")
print("</head>")
print("<body>")
print("<p><b>username:</b> %s <b>password:</b> %s </p>" % (username, password))
print("</body>")
print("</html>")