Installation Requirements: 
1. Linux distribution to run Cassandra on, preferably one of the more popular
   distributions
2. Install the latest version of Java 8 or Java 11
3. To use cqlsh, you must install the latest version of Python3.6+

There are three methods for installation of Apache Cassandra:
  1. Docker Image
  2. Tarball binary file
  3. Package installation

Installing the Docker Image: 
  1. Pull the docker image with the following command:
      
      docker pull cassandra:latest

Installing the Binary Tarball:
  1. Download the binary tarball from one of the mirrors on the Apache Cassandra Download site. To download Cassandra 4.0, do the following: 
        
      curl -OL http://apache.mirror.digitalpacific.com.au/cassandra/4.0.0/apache-cassandra-4.0.0-bin.tar.gz
  
2.  Unpack the tarball:
        
      tar xzvf apache-cassandra-4.0.0-bin.tar.gz

Installing the Debian Packages:
  1.  Add the Apache repository of Cassandra to the file cassandra.sources.list. To add the repository for version 41x, do the following:
      
      echo "deb [signed-by=/etc/apt/keyrings/apache-cassandra.asc] https://debian.cassandra.apache.org 41x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list      
      deb https://debian.cassandra.apache.org 41x main

  2. Add the Apache Cassandra repository keys to the list of trusted keys on the server
  
      curl -o /etc/apt/keyrings/apache-cassandra.asc https://downloads.apache.org/cassandra/KEYS
  
  3. Update the package index from sources:
    
      sudo apt-get update
 
  4. Install Cassandra with APT:

      sudo apt-get install cassandra

