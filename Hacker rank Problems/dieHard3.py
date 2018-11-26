#!/bin/python3

import os
import sys

# Complete the solve function below.
# I took some time just to think about the task of getting 4 litres of water from 3 and 5 litres jugs.For writing the code I just simply thought to write the whole thing of manually done work.But my lecturer asked me to make use of gcd concept for this.With that hint I solved this problem.
def solve(a, b, c):
    temp = max(a,b)
    while(b): 
       a, b = b, a % b 
    if(c < temp and c % a == 0):
        return "YES"
    else :
        return "NO"
  
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abc = input().split()

        a = int(abc[0])

        b = int(abc[1])

        c = int(abc[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()

