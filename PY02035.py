n = input()
k = int(input())
st = {}
for i in range(0, len(n), 2):
    if i+1 < len(n):
        try:
            st[n[i:i+2]] += 1
        except:
            st[n[i:i+2]] = 1
ans = sorted([i for i in st if st[i] >= k])
for i in ans:
    print(i, st[i])
if len(ans) == 0:
    print("NOT FOUND")
