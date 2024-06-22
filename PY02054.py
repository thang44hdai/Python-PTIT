n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
if n == m:
    for i in a:
        print(*i)
else:
    if n > m:
        k = n - m
        for i in range(n):
            if i % 2 == 0:
                if k > 0:
                    k -= 1
                else:
                    print(*a[i])
            else:
                print(*a[i])
    else:
        ans = []
        k = m - n
        for i in range(m):
            if i % 2 == 1:
                if k > 0:
                    k -= 1
                else:
                    b = []
                    for j in range(n):
                        b.append(a[j][i])
                    ans.append(b)
            else:
                b = []
                for j in range(n):
                    b.append(a[j][i])
                ans.append(b)
        for i in range(n):
            for j in range(n):
                print(ans[j][i], end=" ")
            print()
