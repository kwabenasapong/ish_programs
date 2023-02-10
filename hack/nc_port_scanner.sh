#!/usr/bin/env bash

# Check if the IP address is passed as a command line argument
if [ $# -eq 0 ]; then
  echo "ERROR: No IP address provided."
  echo "Usage: $0 <ip_address>"
  exit 1
fi

# Store the IP address
ip=$1

# Define the range of ports to scan
start_port=$2
end_port=$3

# Loop through the range of ports and use nc (netcat) to check if the port is open
for port in $(seq $start_port $end_port); do
  nc -z -w 1 "$ip" "$port" > /dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo "Port $port is open"
  fi
echo "scanning"
done
echo "finished scan"
