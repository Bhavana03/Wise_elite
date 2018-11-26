#!/bin/python3

import os
import sys

#
# Complete the closestNumber function below.
#
def closestNumber(a, b, x):
    power = int(pow(a,b))
    if power > 0 and power <= pow(10,9):
        rem = power % x
        if rem < (x-rem):
            return power - rem
        else:
            return power+(x-rem)
    else :
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abx = input().split()

        a = int(abx[0])

        b = int(abx[1])

        x = int(abx[2])

        result = closestNumber(a, b, x)

        fptr.write(str(result) + '\n')

    fptr.close()

