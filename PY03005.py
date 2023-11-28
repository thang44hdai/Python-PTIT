import re
n, k = map(int, input().split())
a = []
for i in range(n):
    a += re.split("[^a-z0-9]", input().lower())
st ={}
for i in a:
    if i!= "":
        if i not in st:
            st[i]=1
        else:
            st[i]+=1
ans = sorted(st, key = lambda x: (-st[x], x))
for i in ans:
    if st[i]>=k:
        print(i, st[i])