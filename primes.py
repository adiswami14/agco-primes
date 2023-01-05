import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

def nth_prime(n):
    if n == 1:
        return 2
    counter = 1
    currnum = 2
    while counter < n:
        currnum += 1
        if is_prime(currnum):
            counter += 1

    return currnum

print(nth_prime(10001))         # 104743

def sum_prime_nums(target):
    s = 0
    for i in range(target):
        if is_prime(i):
            s += i
    return s

print(sum_prime_nums(100000))       # 454396537
