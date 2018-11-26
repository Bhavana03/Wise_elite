#!/bin/python3

import os
import sys

#
# Complete the halloweenParty function below.
# I solved this problem by taking different examples and by observing the pattern of the output i am getting.
def halloweenParty(k):
    temp = k // 2
    if(k % 2 == 0):
        return temp * temp
    else:
        return temp *(temp + 1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        k = int(input())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()

