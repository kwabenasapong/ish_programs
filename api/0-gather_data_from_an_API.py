#!/usr/bin/python3
import requests
import sys

# get the user id from the command line argument
u_id = sys.argv[1]

''' send a GET request to the API to retrieve
information about the user with the provided id
'''
try:
    user_response = requests.\
            get(f'https://jsonplaceholder.typicode.com/users/{u_id}')
    # check if the response status code is 200 (OK)
    user_response.raise_for_status()
    # get the user information in json format
    user = user_response.json()
    todos_response = requests.\
        get(f'https://jsonplaceholder.typicode.com/todos?userId={u_id}')
    # check if the response status code is 200 (OK)
    todos_response.raise_for_status()
    # get the todos information in json format
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)
    print(f"Employee {user['name']} is done with \
            tasks({done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occured: {http_err}')
except requests.exceptions.ConnectionError as conn_err:
    print(f'Error Connecting: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout Error: {timeout_err}')
except requests.exceptions.RequestException as req_err:
    print(f'Something went wrong: {req_err}')
except ValueError as value_err:
    print(f'Invalid input data: {value_err}')
