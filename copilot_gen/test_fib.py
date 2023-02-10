#!/usr/bin/python3
'''Write the Fibonacci series module with comments for each line'''


def fib(n):    # write Fibonacci series up to n
    '''Write the Fibonacci series module with comments for each line'''
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    '''Write the Fibonacci series module with comments for each line'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    result = fib(int(sys.argv[1]))
    result_2 = fib2(int(sys.argv[1]))
    print(result)
    print(result_2)
