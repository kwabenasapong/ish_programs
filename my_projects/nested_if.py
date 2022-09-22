#!/usr/bin/python3
'''
a = [1,2,3,4,5,6]
b =['m', 'n', 'k', 'g']

for i in range(len(a)):
    if a[i] == 2 and a[i + 1] == 3:
        a[i], a[i + 1] = a[i + 1], a[i]

print(a)
'''

def roman_to_int(roman_string):
    rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not roman_string:
        return 0
    else:
        sum = 0
        for k, v in rn.items():
            for ks in roman_string:
                if ks == k:
                    sum = sum + rn[k]
                else:
                    continue
                return sum
