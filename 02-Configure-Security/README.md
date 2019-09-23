## Security Configuration

Atlas only allows client connections to the cluster from entries in the project’s whitelist. Each entry is either a single IP address or a CIDR-notated range of addresses. 

MongoDB Atlas uses several mechanisms to ensure the security of your databases and collections. This section will walk you through the process of configuring these options.

### IP Whitelisting

To add an entry to the whitelist, from the Clusters view, select the Security tab, then click IP Whitelist, then Add IP Address. Atlas supports creating temporary whitelist entries that automatically expire within a user-configurable 7-day period.

![Add IP Whitelists](../images/04-add-ip-whitelist-entry.png "Add IP Whitelists")

Use the convenient `ADD CURRENT IP ADDRESS` button to automatically add your current IP Address to the list of whitelisted addresses.

### User Authentication

Create MongoDB users to provide clients access to the clusters in your project. A MongoDB user’s access is determined by the roles assigned to the user. When you create a MongoDB user, the user is added to all clusters in your Atlas project.

MongoDB users are separate from Atlas users. MongoDB users have access to MongoDB databases, while Atlas users have access to the Atlas application itself. Atlas supports creating temporary MongoDB users that automatically expire within a user-configurable 7-day period.

![Add User](../images/04-add-user.png "Add User")

Next, we'll navigate back to the main tab labeled `Overview` on your cluster management console.

Now, click the `CONNECT` button 


