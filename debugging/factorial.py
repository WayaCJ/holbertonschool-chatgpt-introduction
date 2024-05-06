#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result


try:
    num = int(sys.argv[1])

    f = factorial(num)

print(f)