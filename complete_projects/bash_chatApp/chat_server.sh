#!/bin/bash

# This script includes functions to handle login requests, registration requests, and chat messages. It uses a users directory to store the registered user names and passwords, and a clients directory to store the IP addresses of the connected clients.

# To use this script, you will need to set the server_port variable to the same port number that the chat clients are using. You will also need to set the username and password variables to the desired login credentials.

# Set the port number for the server
server_port=5555

# Function to handle a login request
handle_login() {
  # Read the username and password from the client
  read username password

  # Check if the username and password are valid
  if [ "$username" = "your_username" ] && [ "$password" = "your_password" ]; then
    # Login was successful, send a response to the client
    echo "success" | nc -l $server_port
  else
    # Login was unsuccessful, send a response to the client
    echo "failure" | nc -l $server_port
  fi
}

# Function to handle a registration request
handle_register() {
  # Read the username and password from the client
  read command username password

  # Check if the username is already taken
  if [ -e "users/$username" ]; then
    # Username is already taken, send a response to the client
    echo "failure" | nc -l $server_port
  else
    # Create a new user file with the given username and password
    echo "$password" > "users/$username"

    # Registration was successful, send a response to the client
    echo "success" | nc -l $server_port
  fi
}

# Function to handle a chat message
handle_message() {
  # Read the message from the client
  read message

  # Send the message to all connected clients
  for client in clients/*; do
    echo "$message" | nc -w 1 $(cat $client) $server_port
  done
}

# Main loop for the server
while true; do
  # Read the first word of the incoming message
  command=$(nc -l $server_port)

  case $command in
    login) handle_login;;
    register) handle_register;;
    *) handle_message;;
  esac
done
