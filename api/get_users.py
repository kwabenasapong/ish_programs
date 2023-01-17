#!/usr/bin/python3
'''get users from the jsonplaceholder api'''
import requests
import sys

user_id = sys.argv[1]
try:
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    user = response.json()

    print(f"The {user['name']} is #{user['id']}")
except:
    print('error')
