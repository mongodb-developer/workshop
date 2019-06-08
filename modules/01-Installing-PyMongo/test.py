import pymongo
import sys
# pprint library is used to make the output look more pretty
from pprint import pprint
import os
try:  
   ATLAS_URI = os.environ.get("MONGODB_ATLAS_URI")
except KeyError: 
   pprint("Please set the environment variable MONGODB_ATLAS_URI")
   sys.exit(1)
pprint(ATLAS_URI)
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient(ATLAS_URI)
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)