# database concepts

1. clustering means you have a master database and also a lot of replica, which can be held on either a single server or many server. The master is for reading and writing, and the replica is for reading.

2. sharding means that you break your whole dataset into small parts stored in different database instances. It is a way to scale horizontally. 

# database complexity

Assuming you hold a social media app, then different types of databases is needed because of different data features.

For example, you need neo4j, a graph-based database for users' relationship graph. So a redis database can be both a cache layer database and a datatype aggregator.   
