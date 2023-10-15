import math
n = int(input())
a = [int(i) for i in input().split()]
prime = [0] * int(1e6)
prime[0] = prime[1] = 1
for i in range(2, int(1e3)):
    if prime[i] == 0:
        for j in range(i*i, int(1e6), i):
            prime[j] = 1

nt = []
dd = []
for i in range(len(a)):
    if prime[a[i]] == 0:
        nt.append(a[i])
        dd.append(0)
    else:
        dd.append(1)
nt.sort()
idx = 0
for i in range(len(a)):
    if dd[i] == 0:
        print(nt[idx], end=" ")
        idx += 1
    else:
        print(a[i], end=' ')
