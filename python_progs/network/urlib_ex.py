#!/usr/bin/python3

import urllib.request

# Open the URL and read the contents
with urllib.request.urlopen("http://www.google.com") as url:
    s = url.read()

# Print the contents
print(s)
