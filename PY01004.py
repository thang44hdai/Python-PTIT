import math


def sol(n):
    if n <= 1:
        return "NO"
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return "NO"
    return "YES"


for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            cnt += 1
    print(sol(cnt))
