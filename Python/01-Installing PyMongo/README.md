# PyMongo Introduction - Installing PyMongo

## Introduction

PyMongo is the preferred driver for MongoDB. PyMongo is the (Python Package Index)[http://pypi.python.org/pypi/pymongo/].

We recommend installing pymongo using pip on all platforms.

```
$ python -m pip install pymongo
```

## Testing the installation

The following command will inform you as to whether or not pymongo is installed, as well as what version is installed.

```
python -c "import pymongo; print(pymongo.version); print(pymongo.has_c())"
```
## Take if for a spin

Here's output of a python session wherein we demonstrate the use of pymongo.

```
>>> import pymongo
>>> client = pymongo.MongoClient("localhost", 27017)
>>> db = client.test
>>> db.name
u'test'
>>> db.my_collection
Collection(Database(MongoClient('localhost', 27017), u'test'), u'my_collection')
>>> db.my_collection.insert_one({"x": 10}).inserted_id
ObjectId('4aba15ebe23f6b53b0000000')
>>> db.my_collection.insert_one({"x": 8}).inserted_id
ObjectId('4aba160ee23f6b543e000000')
>>> db.my_collection.insert_one({"x": 11}).inserted_id
ObjectId('4aba160ee23f6b543e000002')
>>> db.my_collection.find_one()
{u'x': 10, u'_id': ObjectId('4aba15ebe23f6b53b0000000')}
>>> for item in db.my_collection.find():
...     print(item["x"])
...
10
8
11
>>> db.my_collection.create_index("x")
u'x_1'
>>> for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
...     print(item["x"])
...
8
10
11
>>> [item["x"] for item in db.my_collection.find().limit(2).skip(1)]
[8, 11]

```
