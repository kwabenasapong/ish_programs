#!/bin/bash

# This script takes in a URL as its first argument
# It sends a request to the URL and displays the size of the body of the response

# Check that a URL was provided as an argument
if [ $# -eq 0 ]; then
  echo "Error: No URL provided"
  exit 1
fi

# Use curl to send a request to the URL
response=$(curl -s "$1")

# Get the size of the response body in bytes
size=$(echo -n "$response" | wc -c)

# Display the size of the response body in bytes
echo "Size of response body: $size bytes"

