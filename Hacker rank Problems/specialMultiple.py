#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    num = 1
    while True:
        st = binary(num)
        st = st.replace('1','9')
        if (int(st)) % n == 0:
            return st
        else:
            num = num + 1
def binary(n):
    return bin(n).replace("0b","")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

