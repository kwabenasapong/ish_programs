#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('http://www.python.org.') as response:
    html = repsonse.read()

print(html)
