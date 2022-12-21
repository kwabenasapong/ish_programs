#!/usr/bin/python3

from fabric.api import run, env
# import sys


env.hosts = ['34.232.68.81']  # [sys.argv[2]]
env.user = 'ubuntu'  # sys.argv[1]
env.key_filename = '~/.ssh/school'  # sys.argv[3]


def list_files():
    # List the files in the home directory
    run('ls -l')


def name():
    # name of the server
    run('uname -s')
