import math

l = int(1e6+5)
l1 = int(1e3)+1
prime = [1]*l

prime[0] = prime[1] = 0
for i in range(l1):
    if prime[i] == 1:
        for j in range(i*i, l, i):
            prime[j] = 0


def check(n):
    if prime[n] == 1 and prime[n+2] == 1 and prime[n+6] == 1:
        return True
    if prime[n] == 1 and prime[n+4] == 1 and prime[n+6] == 1:
        return True
    return False


for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(2, n):
        if i+6 < n:
            if check(i) == True:
                cnt += 1
    print(cnt)
