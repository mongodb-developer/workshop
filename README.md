# MongoDB Developer Workshops

This repository contains different workshops, each of them is composed of several modules built in git branches.

In this README, you will find information about each workshop and which branches have to be used.

## Modules

Each module lives in a git branch. Below, you will find a description of each of them.

To navigate from one branch to another, you can use the `branch` button in this Github repository.

![Github branch navigation](images/branches.png)

- The `atlas` workshop will teach you
  - how to setup a MongoDB Atlas free tier cluster,
  - how to setup the security to access your cluster,
  - how to import the sample data sets.
- The `stitch-data-enrichment` branch will teach you
  - how to create a Stitch application,
  - how to create an HTTP service and a POST webhook,
  - how to setup a trigger and enrich your data using a REST API.
- The `compass` branch will teach you
  - how to setup MongoDB Compass,
  - how to create a geo-spatial query,
  - how to use the aggregation pipeline builder.
- WIP - The `python` contains a workshop around pymongo
- WIP - The `python-solution` contains the solution of the workshop in the `python` branch
- Any other branch you might see is a WIP.

## Workshops

### #1 MongoDB Atlas and data enrichment in MongoDB Stitch

This workshop is composed of the Atlas workshop and the Stitch Data Enrichment workshop.

You will need to complete the modules in the `atlas` and the `stitch-data-enrichment` branches.

You do not need to download this Github repository to complete this workshop. You just need to follow the README files in each branch.
 
### #2 MongoDB Atlas and Compass

This workshop is composed of the Atlas workshop and the Compass workshop.

You will need to complete the modules in the `atlas` and the `compass` branches.

You do not need to download this Github repository to complete this workshop. You just need to follow the README files in each branch.

### #3 MongoDB Atlas and PyMongo workshop

This workshop is composed of the Atlas workshop and the PyMongo workshop.

You will need to complete the modules in the `atlas` and the `python` branches.

If you are stuck or you want to check that you have the most optimal solution, you will find the solution in the `python-solution` branch.

You need to clone this repository and checkout the `python` branch to complete the python code.

```sh
git clone git@github.com:mongodb-developer/workshop.git
cd workshop
git checkout python
```