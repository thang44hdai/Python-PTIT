n, k = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
cnt = 0
i = 0
while i < n:
    j = i+1
    while j < n and a[j]-a[j-1] <= k:
        j += 1
    cnt += 1
    i = j
print(cnt)
