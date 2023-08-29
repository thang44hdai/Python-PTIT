n = int(input())
a = []
for _ in range(n):
    a.append([int(i) for i in input().split()])
k = int(input())
sum = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            sum += a[i][j]
        elif i + j > n-1:
            sum -= a[i][j]
if abs(sum)<=k:
    print("YES")
else: print("NO")
print(abs(sum))