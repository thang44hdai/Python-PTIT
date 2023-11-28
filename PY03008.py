n = int(input())
mp = {}
for i in range(1, n+1):
    mp[i] = []

for i in range(n-1):
    x, y = map(int, input().split())
    mp[x].append(y)
    mp[y].append(x)

cnt1 = cnt2 = 0
for i in range(1, n+1):
    if len(mp[i]) == 1:
        cnt1 += 1
    elif (len(mp[i]) == n-1):
        cnt2 += 1
if cnt2 == 1 and cnt1 == n-1:
    print("Yes")
else:
    print("No")
