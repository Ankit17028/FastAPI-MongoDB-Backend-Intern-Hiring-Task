# from pymongo import MongoClient


# client = MongoClient("mongodb+srv://ankitbansod70:Ankit@12345678@cluster0.dn3cas5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# # client = MongoClient("mongodb+srv://ankitbansod70:Ankit@12345678@cluster0.dn3cas5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")




import os
from pymongo import MongoClient

# Construct MongoDB URI using environment variables
# MONGODB_URI = f"mongodb+srv://{os.environ['MONGODB_USERNAME']}:{os.environ['MONGODB_PASSWORD']}@cluster0.dn3cas5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

from urllib.parse import quote_plus

MONGODB_USERNAME = quote_plus(os.environ['MONGODB_USERNAME'])
MONGODB_PASSWORD = quote_plus(os.environ['MONGODB_PASSWORD'])

MONGODB_URI = f"mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@cluster0.dn3cas5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Connect to MongoDB
client = MongoClient(MONGODB_URI)







db = client.todo_db

collection_name = db["todo_collection"]



# from urllib.parse import quote_plus
# from pymongo import MongoClient

# # Escape username and password
# username = "ankitbansod70"
# password = "Ankit@12345678"
# escaped_username = quote_plus(username)
# escaped_password = quote_plus(password)

# # Construct the MongoDB connection string
# connection_string = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.dn3cas5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Connect to MongoDB
# client = MongoClient(connection_string)
 

# db = client.todo_db

# collection_name = db["todo_collection"]