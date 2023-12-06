import math
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(n):
    for j in range(i+1, n, 1):
        if math.gcd(a[i], a[j]) == 1:
            print(a[i], a[j])
