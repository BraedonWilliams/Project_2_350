## you must use "pip install cassandra-driver" in your python environment first
## start cassandra in your terminal with "cassandra -f"
## verify cassandra is running by using "nodetool status"

from cassandra.cluster import Cluster
from uuid import uuid4

NODE_IP = ['127.0.0.1'] ##this is the IP address it usually is to run on your local machine. But, if it doesnt work, replace this with your node ip.

# Connect to cluster
cluster = Cluster(NODE_IP)
session = cluster.connect()

# Create Your Keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS mykeyspace WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1}")

# Using Keyspace
session.set_keyspace('mykeyspace')

# Create a table
session.execute("""
    CREATE TABLE IF NOT EXISTS students (
        user_id UUID PRIMARY KEY,
        name text,
        grade int
    )
""")

# Insert data into the table
session.execute("""
    INSERT INTO students (user_id, name, grade)
    VALUES (%s, %s, %s)
""", (uuid4(), 'Dana', 75))

session.execute("""
    INSERT INTO students (user_id, name, grade)
    VALUES (%s, %s, %s)
""", (uuid4(), 'Braedon', 99))

session.execute("""
    INSERT INTO students (user_id, name, grade)
    VALUES (%s, %s, %s)
""", (uuid4(), 'Megan', 100))

# Query the students table
rows = session.execute('SELECT * FROM students')
for row in rows:
    print(row.name, row.grade)


# Close the connection
cluster.shutdown()