#!/bin/python3

import os
import sys

# Complete the solve function below.
#At first I thought to take an array of size n and then add the all operational values to it.But for the large number of test cases it is taking a lot time.After examining the sample examples I came to conclusion that we can just simply add the operational values without the usage of arrays as in the below:
def solve(n, operations):
     sum = 0
     for i in range (0,len(operations)):
        a = operations[i][0]
        b = operations[i][1]
        k = operations[i][2]
        sum += (b - a + 1) * k
        #jug_list[a:b] = [x + k for x in jug_list[a:b]=
     return sum // n
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    operations = []

    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)

    fptr.write(str(result) + '\n')

    fptr.close()

