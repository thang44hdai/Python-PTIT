n = int(input())
a = [int(i) for i in input().split()]
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i]>a[j]:
            cnt += 1
print(cnt)