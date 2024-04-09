from fastapi import FastAPI

from routes.route import router

app = FastAPI()

app.include_router(router)



# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://ankitbansod70:Ankit@12345678@cluster0.dn3cas5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)