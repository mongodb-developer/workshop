import platform
import pymongo
import dns.version
import os
import sys
from pymongo import MongoClient

print("Python version:", platform.python_version())
print("pymongo version:", pymongo.version)
print("dnspython version:", dns.version.version)

if "MONGODB_ATLAS_URI" in os.environ:
    URI = os.environ.get("MONGODB_ATLAS_URI")
    print("Connecting to:", URI.split("@")[1].split("/")[0])
else:
    print("404 - MongoDB Atlas URI not found.")
    print("Please fetch your URI in MongoDB Atlas using the connect button then execute the command:")
    print(
        "export MONGODB_ATLAS_URI=\"mongodb+srv://<username>:<password>@freesandbox-abcde.mongodb.net/test?retryWrites=true&w=majority\"")
    sys.exit(1)

client = MongoClient(URI)
print("MongoDB version running:", client.server_info()["version"])
