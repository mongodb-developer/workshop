# Stitch and Python

In this module, we'll explore creating an application that uses MongoDB Stitch. MongoDB Stitch is built into MongoDB Atlas and provides the ability to create an host serverless functions and integrations. The design goal for Stitch is to alleviate the need for creating boiler-plate code to accomplish many of the features that modern applications must present.

Because MongoDB Stitch functions are JavaScript based, we will leverage a feature of Stitch which enables you to connect to your MongoDB database through Stitch. More on this below.

## Prerequisites

You should have already completed the MongoDB Atlas module of this workshop and should therefore already have a cluster available to you. If you have not yet completed this module, go back and review module 01 - MongoDB Atlas to ensure that you have a working cluster with sample data available.  Additionally, you may wish to review the [Atlas Getting Started Documentation](https://docs.atlas.mongodb.com/getting-started/).

## Set up

1. Log on to Atlas
    * To use MongoDB Stitch, you must be logged into Atlas.

1. To create an Atlas cluster to use with your MongoDB Stitch app, following these steps:

    * In the left navigation pane, click Clusters, and then click the Build New Cluster button. The Create New Cluster page opens.
    * Choose your preferred provider and region, tier, and additional settings. As you build your cluster, Atlas displays the associated costs at the bottom of the page.
    * The default cluster name is Cluster0. If you wish to change the name, do so now, as cluster names cannot be changed once configured.

1. Add a Stitch App

    * In Atlas, click Stitch Apps in the left-hand navigation.
    * Click the Create New Application.
    * In the Create a new application dialog, enter an Application Name for your Stitch app.
    * Select a cluster in your project in your project from the Link to Cluster dropdown. Stitch will automatically create a MongoDB service that is linked to this cluster.
    * Enter a name for the service that Stitch will create in the Stitch Service Name field.
    * Select a deployment model and deployment region for your application.
    * Click Create.