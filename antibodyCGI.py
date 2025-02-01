#!/usr/bin/env python3

import cgi

# Set the header to tell the browser that this is an HTML response
print("Content-Type: text/html")
print()

# Get form data
form = cgi.FieldStorage()

# Extract form values
name = form.getvalue("name")
email = form.getvalue("email")
message = form.getvalue("message")

# Simple HTML response showing the submitted data
print("<html><body>")
print("<h1>Thank you for your submission, {}!</h1>".format(name))
print("<p><strong>Email:</strong> {}</p>".format(email))
print("<p><strong>Message:</strong> {}</p>".format(message))
print("</body></html>")

