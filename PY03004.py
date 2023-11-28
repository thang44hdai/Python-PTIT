import re


a = []
for i in range(int(input())):
    a += re.split("[^a-z0-9]", input().lower())
st = {}
for i in a:
    if(i!=""):
        if st.get(i)==None:
            st[i]=1
        else:
            st[i]+=1
ans = sorted(st, key = lambda x: (-st[x], x))
for i in ans:
    print(i, st[i])