import re
a= []
def check(n):
    for i in n:
        if i>="0" and i<="9":
            return False
    return True
for _ in range(int(input())):
    a += re.split("[^a-z]", input().lower())
st = {}
for i in a:
    if i!= "" and check(i)==True:
        if i not in st:
            st[i]=1
        else:
            st[i] += 1
ans = sorted(st, key = lambda x: (-st[x], x))
for i in ans:
    print(i, st[i])