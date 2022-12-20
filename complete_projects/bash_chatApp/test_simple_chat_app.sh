#!/usr/bin/env bash

# how it works
# To use this script, open two terminal windows and run the script in each window. The script will start a server in one window and a client in the other. You can then type messages in either window, and they will be sent to the other window.

# Note that this script uses the nc (netcat) command to create the server and client. nc is a simple networking utility that can be used to read and write data across a network

# Set the hostname and port for the server
server_hostname=localhost
server_port=5555

# Set the hostname and port for the client
client_hostname=localhost
client_port=5556

# Start the server in the background
nc -l $server_port > /dev/null &
server_pid=$!

# Start the client in the foreground
nc $client_hostname $client_port

# Kill the server when the client exits
kill $server_pid
