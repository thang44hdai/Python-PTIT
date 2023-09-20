n, k = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
st = set()
for i in l:
    st.add(i)
n = len(st)
l.clear()
for i in st:
    l.append(i)
a = [i for i in range(k+1)]
while True:
    i = k
    a[1] = 1
    for x in range(1, k+1):
        print(l[a[x]-1], end=' ')
    while i > 0 and a[i] >= n-k+i:
        i -= 1
    if i == 0:
        break
    a[i] += 1
    for j in range(i+1, k+1):
        a[j] = a[j-1]+1
    print()
