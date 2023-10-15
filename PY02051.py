n = int(input())
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
if n == 2:
    print(1, a[0][1]-1, end=" ")
else:
    ans = []
    fi = (a[0][1]+a[0][2]-a[1][2])//2
    ans.append(fi)
    for i in range(1, n):
        ans.append(a[0][i]-fi)
    print(*ans)
