#!C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe

import cgi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json
from bson import json_util

# MongoDB server adress
uri = "mongodb://127.0.0.1:27017/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Set a proper HTML header
print("Content-type: text/html\n")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

database = client["antibodyAnnotation"]
collection = database["antibodyData"]

# Loading the json file / uncomment this only if you want to add a new document
# with open('json_files/12499.json') as file:
#     file_data = json.load(file)

# if isinstance(file_data, list):
#     collection.insert_many(file_data)
# else:
#     collection.insert_one(file_data)

# Get all data from the database
record = collection.find()

# Get the data from the HTML form
form = cgi.FieldStorage()

regex_1 = form.getvalue("Format")
control_empty = form.getvalue("Antigen")
regex_3 = form.getvalue("AbML")

print("<html><head><title>CGI Response</title></head>")
print("<body>")
print("<h2>Received Message</h2>")

# Check of the posted data from the HTML form
print(f"<p>Form: {form}</p>")

# Check the connection to the proper collection from the database
print(f"<p>Record: {collection}</p>")

# Show all the available data
for r in record:
    print(f"<p>Record: {r}</p>")

# Query data with specific conditions
anti_body_data = collection.find({"Format": {"$regex": regex_1}, "AbML": {"$regex": regex_3}}, {"Format": 1, "Antigen": 1, "AbML": 1})

print(f"<p>Limit output to three fields:</p>")
for abf in anti_body_data:
    print(f"<p>Sifted Data: {abf}</p>")

# Query again to return cursor to start position
anti_body_data = collection.find({"Format": {"$regex": regex_1}, "AbML": {"$regex": regex_3}}, {"Format": 1, "Antigen": 1, "AbML": 1})

print(f"<br>")
print(f"<p>Choose a key data:</p>")
for abf in anti_body_data:
    print(f"<p>Format: {abf['Format']}</p>")
    print(f"<p>Antigen: {abf['Antigen']}</p>")
    print(f"<p>AbML: {abf['AbML']}</p>")

print("</body></html>")
