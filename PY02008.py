prime = [0]*int(1e6)
prime[0] = prime[1] = 1
for i in range(2, int(1e3)):
    if prime[i] == 0:
        for j in range(i*i, int(1e6), i):
            prime[j] = 1
vt = []
n, x = map(int, input().split())

for i in range(2, int(1e6)):
    if prime[i] == 0:
        vt.append(i)
    if len(vt) > n:
        break
print(x, end=' ')
for i in range(n):
    print(x+vt[i], end=' ')
    x += vt[i]
