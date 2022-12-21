#!/usr/bin/python3
from fabric.api import run, env, task
import sys


@task
def list_files(user=None, host=None, key=None):
    # Validate input
    if not user or not host or not key:
        print('Error: user, host, and key are required arguments')
        sys.exit(1)

    # List the files in the home directory
    env.hosts = [host]
    env.user = user
    env.key_filename = key

    run('ls -l')

# comments on run the script with fab
# fab -H 34.232.68.81 list_files:ubuntu,34.232.68.81,~/.ssh/school
# this works
