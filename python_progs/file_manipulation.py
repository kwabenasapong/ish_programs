#!/usr/bin/python3
'''
To study how to manipulate file in python
'''
with open('workfile', encoding='utf-8') as f:
    read_data = f.readline()

print(read_data)

