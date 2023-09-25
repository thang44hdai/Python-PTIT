l = int(1e6+5)
l1 = int(1e3)+1
prime = [1]*l

prime[0] = prime[1] = 0
for i in range(l1):
    if prime[i] == 1:
        for j in range(i*i, l, i):
            prime[j] = 0

n = int(input())
l = [int(i) for i in input().split()]
mp = {}
for i in l:
    if prime[i] == 1:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
for i in mp:
    print(i, mp[i], sep=" ")
