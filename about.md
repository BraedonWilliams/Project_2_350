## About Apache Cassandra

Apache Cassandra is an open-source NoSQL distributed database. It uses the Cassandra Query Language (CQL), which is syntactically very similar to SQL.

### Strengths:
- **High fault tolerance:** Apache Cassandra replicates data accross multiple nodes in the cluster. These nodes also communicate with one another to help detect failures as they happen. Apache Cassandra calls this their "Gossip" protocol. This prevents any single point of failure, and gives Apache Cassandra databases a high fault tolerance. 
- **Dynamic Scalability (node-based, horizontal scalability):** Apache Cassandra was designed with scalability in mind. Apache Cassandra is run on "Nodes" (devices). In order to scale a Cassandra database up, you simply have to add nodes to the "Cluster". This means that it is linearly scalable, and require no downtime to increase database size.

### Shortcomings:
- **CQL:** Apache Cassandra uses its own language, CQL. This is not a mainstream language, and therefore has less documentation and support.
- **No Joins:** Because Apache Cassandra does not support joins, it can be harder to query information from multiple tables.
- **Memory Usage:** Due to Apache Cassandra replicating data across many nodes, it uses more space for memory allocation.
- **Data Updates:** Updating data takes longer since Apache Cassandra must replicate this data to nodes across the cluster, which can sometimes result in data inconsistency.

### Future Plans for Apache Cassandra:
1. Continuing to address security issues as they arise. The world is constantly changing, so it is important that software support is kept on top of. Along with this, they are hoping to increase the global collaboration on Apache Cassandra. They believe having a diverse collaborator pool will help to prepare for security issues as they arise.
2. Along with expanding their pool of contributors, they are hoping to expand their user pool. Their goal is be more welcoming to new users. 
