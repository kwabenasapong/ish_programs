#!/bin/bash

# This script includes a main menu with options to login, register a new user, or quit the application. It also includes functions for the login process, the registration process, and the chat session.

# To use this script, you will need to set the server_hostname variable to the hostname or IP address of your remote server, and set the server_port variable to the port number that the chat application will use. You will also need to set the username and password variables to your desired login credentials.

# Set the hostname and port for the server
server_hostname=your_server_hostname_or_ip
server_port=5555

# Set the username and password for the chat application
username=your_username
password=your_password

# Function to display the main menu
display_menu() {
  clear
  echo "Welcome to the chat application!"
  echo
  echo "1. Login"
  echo "2. Register"
  echo "3. Quit"
  echo
  read -p "Enter your choice: " choice
}

# Function to handle the login process
login() {
  read -p "Enter your username: " login_username
  read -s -p "Enter your password: " login_password

  # Send the login credentials to the server
  echo "$login_username $login_password" | nc $server_hostname $server_port

  # Read the response from the server
  login_response=$(nc -l $server_port)

  if [ "$login_response" = "success" ]; then
    # Login was successful, start the chat session
    chat_session
  else
    # Login was unsuccessful, display an error message
    clear
    echo "Invalid username or password"
    sleep 3
  fi
}

# Function to handle the registration process
register() {
  read -p "Enter a new username: " register_username
  read -s -p "Enter a new password: " register_password

  # Send the registration credentials to the server
  echo "register $register_username $register_password" | nc $server_hostname $server_port

  # Read the response from the server
  register_response=$(nc -l $server_port)

  if [ "$register_response" = "success" ]; then
    # Registration was successful, start the chat session
    chat_session
  else
    # Registration was unsuccessful, display an error message
    clear
    echo "Username is already taken"
    sleep 3
  fi
}

# Function to handle the chat session
chat_session() {
  # Start the chat client in the background
  nc -l $server_port > /dev/null &
  client_pid=$!

  # Start the chat server in the foreground
  nc $server_hostname $server_port

  # Kill the client when the server exits
  kill $client_pid
}

# Main loop for the chat application
while true; do
  display_menu
  case $choice in
    1) login;;
    2) register;;
    3) exit;;
  esac
done
