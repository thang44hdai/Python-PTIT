n = int(input())
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
sum = 0
k = int(input())
for i in range(n):
    for j in range(n):
        if j > i:
            sum += a[i][j]
        elif j < i:
            sum -= a[i][j]
sum = abs(sum)
if sum <= k:
    print("YES")
else:
    print("NO")
print(sum)
