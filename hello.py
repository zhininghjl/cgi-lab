#!/usr/bin/env python3
import os, json
from templates import login_page

print("Content-type:text/html\r\n\r\n")

print("<title>Test CGI</title>")
print("<p>Hello World</p>")

"""
# Q1
print(os.environ)  # print the environment variables given to the CGI script
json_obj = json.dumps(dict(os.environ), indent=4)
print(json_obj)

# Q2
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

# Q3
for param in os.environ.keys():
    if (param=="HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
"""

# Q4
print(login_page())


