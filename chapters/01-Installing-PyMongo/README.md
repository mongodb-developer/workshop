# PyMongo Introduction - Installing PyMongo

## Introduction

[PyMongo](http://pypi.python.org/pypi/pymongo/) is the preferred driver for MongoDB.

To work with MongoDB in Python, you will need to install 2 packages:

- `pymongo` which is the MongoDB Driver.
- `dnspython` which is required to connect to a MongoDB Cluster using the [DNS seedlist connection format](https://docs.mongodb.com/manual/reference/connection-string/#dns-seedlist-connection-format). 

First of all, let's make sure you are running python 3.

```sh
$ python --version 
Python 3.7.3
```

If you have python `2.X.Y`, you need to install python 3. For my particular case, I'm running on Linux and I have to use `python3` instead of `python`.

We recommend using `pip (or pip3)` to install packages on all platforms.

```sh
$ pip install --upgrade -r requirements.txt
```

We also need to be able to connect to MongoDB Atlas using the connexion URI. Use the `connect` button on MongoDB Atlas and `export` your URI in your environment variables.

```sh
$ export MONGODB_ATLAS_URI="mongodb+srv://<username>:<password>@freesandbox-abcde.mongodb.net/test?retryWrites=true&w=majority"
```

## Testing the installation

Run the `test.py` script to check that you have done the above instructions correctly.

```sh
$ python test.py
Python version: 3.7.3
pymongo version: 3.8.0
dnspython version: 1.16.0
Connecting to: freesandbox-abcde.mongodb.net
MongoDB version running: 4.0.10
```

## Navigation

| < Back | You are Here | Next > |
| :--- | :---: | ---: |
| [<< Home](workshop) | PyMongo Introduction - Installing PyMongo | [Creating/Inserting with PyMongo >>](../02-CRUD) |