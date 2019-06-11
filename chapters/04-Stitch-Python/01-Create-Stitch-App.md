# Creating a Stitch App

In this module, we'll create a Stitch application that will be used to demonstrate how we can leverage Stitch and MongoDB from a Python script.

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