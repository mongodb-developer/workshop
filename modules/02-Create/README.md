# Creating / Inserting Data with PyMongo

In order to begin inserting data into MongoDB with python... using pymongo, we must import the necessary libraries.

```
from pymongo import MongoClient
```

Next, we will establish a connection to the database using a method given to us from the pymongo library.

```
client = MongoClient('localhost:27017')
```

Now, this will connect to an instance of MongoDB running on your localhost. Since this workshop is built using MongoDB Atlas, you will need to find and copy the connection string to the free instance you created from the initial module of this workshop.

## Navigation

| < Back | You are Here | Next > |
| ---- | ------------ | ---- |
| [<< Installing](https://github.com/mongodb-developer/workshop/tree/python/modules/01-Installing-PyMongo) | Creating / Inserting | [Reading >>](https://github.com/mongodb-developer/workshop/tree/python/modules/03-Read) |
