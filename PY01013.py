from math import gcd, sqrt


def check_nguyen_to(n):
    if n <= 1:
        return "NO"
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return "NO"
    return "YES"


for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    uc = gcd(a, b)
    total = sum(int(i) for i in str(uc))
    print(check_nguyen_to(total))
