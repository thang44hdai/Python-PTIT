for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    a = [] * n
    for i in range(m):
        a.append([int(x) for x in input().split()])
    b = [] * 3
    for i in range(3):
        b.append([int(x) for x in input().split()])
    sum = 0
    for i in range(2, n):
        for j in range(2, m):
            for u in range(3):
                for v in range(3):
                    sum += b[u][v]*a[i-u][j-v]
    print(sum)
