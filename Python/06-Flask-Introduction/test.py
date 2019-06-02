from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/admin"
mongo = PyMongo(app)
# Issue the serverStatus command and print the results
serverStatusResult=mongo.db.admin.command("serverStatus")
pprint(serverStatusResult)