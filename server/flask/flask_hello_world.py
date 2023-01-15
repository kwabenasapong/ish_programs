#!/usr/bin/python3
'''hello world flask'''
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>hello, world!</p>'
