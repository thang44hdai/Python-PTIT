import math
n = int(input())
a = [int(i) for i in input().split()]
prime = [0] * int(1e6)
prime[0] = prime[1] = 1
for i in range(2, int(1e3)):
    if prime[i] == 0:
        for j in range(i*i, int(1e6), i):
            prime[j] = 1


def cnt(n):
    dem1 = 0
    dem2 = 0
    if prime[n] == 0:
        return 0
    n1 = n
    while prime[n1] == 1:
        dem1 += 1
        n1 += 1
    while prime[n] == 1:
        dem2 += 1
        n -= 1
    return min(dem1, dem2)


ans = max(cnt(i) for i in a)
print(ans)
