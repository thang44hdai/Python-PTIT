import math


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def deff(str):
    if not isprime(int(str)):
        return "No"
    sum = 0
    for i in str:
        if not isprime(int(i)):
            return 'No'
        sum += int(i)
    if not isprime(int(str)):
        return "No"
    str_rev = str[::-1]
    if not isprime(int(str_rev)):
        return "No"
    return "Yes"


for case in range(int(input())):
    print(deff(input()))