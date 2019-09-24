## Deploying an Atlas Cluster

Create an Account or Log In to Atas
We’ll be using MongoDB Atlas, our fully managed Database as a Service, for this workshop. Go to [https://cloud.mongodb.com](https://cloud.mongodb.com) and either create a new account or log into an existing account you may have previously created.

### Create a Free Tier Cluster
#### Click Build a Cluster

![Create a Cluster](../images/02-create-cluster.png "Create a Cluster")

Take a moment to browse the options (Provider & Region, Cluster Tier, Version, Backup, …). For our workshop, select AWS as the Cloud Provider:

![Create a Cluster - Choose AWS](../images/02-create-cluster-choose-aws.png "Create a Cluster - Choose AWS")

Leave the remaing options set to the defaults and skip down to the bottom section where you can set the Cluster Name.

Set the Cluster Name - This can be whatever you like.

Now, click create to create the cluster. 

![Click Create](..//images/02-create-cluster-click-create.png "Click Create")

Note: You may be prompted to prove that you are a human by selecting images that match a certain pattern.

![Solve Human Check](..//images/02-solve-human-check.png "Solve Human Check")

Next, you will see your cluster with a blue banner along the top indicating that changes are being deployed. This will take approximately 7 minutes to complete the provisioning process.

![Deploying Cluster](..//images/02-deploying-cluster.png "Deploying Cluster")

