#!/usr/bin/python3

# Import the required module
import urllib.request

# Set the URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Use the urlopen function to fetch the URL
with urllib.request.urlopen(url) as response:
    # Read the response data
    data = response.read()

    # Print the response information
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
    print("\t- utf8 content:", data.decode("utf-8"))
