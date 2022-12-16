#!/usr/bin/python3
import requests
import sys

url = sys.argv[1]

# send a GET request to the URL
response = requests.get(url)

# check if the X-Request-id is present in the headers
if 'X-Request-Id' in response.headers:
    # if present, retrieve the value of the X-Request-Id
    x_request_id = response.headers['X-Request-id']
    print(f'X-Request-Id: {x_request_id}')
else:
    # if not present, print a message
    print('X-Request-Id not found in the headers')
