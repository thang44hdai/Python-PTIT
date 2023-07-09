from math import*
a, k, n = map(int, input().split())
l = []
for i in range(1, ceil(n/k)+1):
    if(i*k-a>0 and i*k <=n):
        l.append(i*k-a)
        #l.insert(len(l), i*k-a)
if(len(l)==0):
    print(-1)
else:
    for i in l:
        print(i, end = " ")

