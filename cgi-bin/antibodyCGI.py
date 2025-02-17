import cgi
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import json
from bson import json_util

uri = "mongodb+srv://ntab:test321@cluster0.wrdok.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client["database_test_1"]
collection = database["collection_test_1"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Set the header to tell the browser that this is an HTML response
print("Content-Type: text/html")
print()

# Get form data
form = cgi.FieldStorage()

# Extract form values
domain = form.getvalue("Domain")
mutation = form.getvalue("Mutation")
fusion = form.getvalue("Fusion")

# generate query
def query(domain, mutation, fusion):
    query_list = {}  # Empty dictionary to store result
    # Add non-empty fields to the query
    if domain:
        query_list["Domains"] = {"$in": [domain]} 
    if mutation:
        query_list["Mutation"] = {"$in": [mutation]} 
    if fusion:
        query_list["Fusion"] = {"$regex": fusion}
    # Return generated query 
    return query_list

result = query(domain, mutation, fusion)

# give the query output and number
output_cursor = collection.find(query(domain, mutation, fusion))
output_list = [json.loads(json_util.dumps(doc)) for doc in output_cursor]
output_num = len(output_list)


# Simple HTML response showing the submitted data
print("<html><body>")
print("<h1>Thank you for your submission!</h1>")
print("<p><strong>Here is the SQL query generated:</strong> {}</p>".format(result))
print("<p><strong>Domain:</strong> {}</p>".format(domain))
print("<p><strong>Mutation:</strong> {}</p>".format(mutation))
print("<p><strong>Fusion:</strong> {}</p>".format(fusion))
#print("<p><strong>Number of results:</strong> {}</p>".format(output_num))
#print("<p><strong>Results:</strong> {}</p>".format(output_list))
print("</body></html>")

