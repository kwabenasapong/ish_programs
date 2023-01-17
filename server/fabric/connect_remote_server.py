from fabric.connection import Connection
# import sys

# Create an SSH connection object
conn = Connection(
    host='34.232.68.81',
    user='ubuntu',
    key_filename='~/.ssh/school'
)

# Connect to the remote server using the SSH key
conn.connect()
