#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak
import random
import time

a = list(range(1, 5000000))
a1 = list(range(4999999, 1, -1))
a2 = list(range(1, 5000000))
random.shuffle(a2)
answers = [4999999]

avg_time = 0

for j in range(10):
    start_time = time.time()
    
    for i in range(10):
        res = find_peak(a)
        if res not in answers:
            print("Wrong answer {}".format(res))
            exit(1)

    for i in range(10):
        res = find_peak(a1)
        if res not in answers:
            print("Wrong answer 2 {}".format(res))
            exit(1)

    for i in range(10):
        find_peak(a2)
    
    end_time = time.time()
    avg_time += (end_time - start_time)

avg_time = avg_time / 10    

if avg_time > 5.0:
    print("Too slow")
    exit(1)

print("OK", end="")

