# Reading data from MongoDB with pymongo

Reading data from MongoDB with pymongo is simple. Once again, we'll need to import the pymongo library as we did in the previous module.

```
import pymongo
```

Next, we'll establish a connection in the same manner. Now, since we're in a MongoDB Atlas workshop, let's use the proper connection string. We'll set this in a .env file that looks something like the following:

```
export MONGODB_ATLAS_URI=mongodb+srv://<username>:<password>\@myfirstcluster-zbcul.mongodb.net/test\?retryWrites=true\&w=majority
```

Of course, you will need to find the correct connection string, or URI from the Atlas console. From the main Atlas management console window, find your cluster, and click on the Connect tab. 

![Connect](https://github.com/mongodb-developer/workshop/blob/python/Python/03-Read/atlas_connect.gif "Connect to Atlas MongoDB Instance")

Once you've copied that place it into a .env file like the one above and `source .env` before running `crud.py`.

## Navigation

| < Back | You are Here | Next > |
| ---- | ------------ | ---- |
| [<< Creating](https://github.com/mongodb-developer/workshop/tree/python/modules/02-Create) | Reading | 
