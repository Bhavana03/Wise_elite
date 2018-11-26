import math
def solve(n, m):
    count = 0
    for val in range(n,m):
        if isprime(val):
            if isprime(val + 2):
                count = count + 1
                print(val)
                print(val+2)
    return count
def isprime(num):
    count = 0
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            count = count + 1
    if count == 0:
        return True
    else:
        return False
k = solve(281,586)
print(k)
