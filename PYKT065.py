
while True:
    a = [int(i) for i in input().split()]
    if len(a) == 1 and a[0] == -1:
        break
    l, r = a[0], a[1]
    n = int(input())

    def check(i, n):
        for j in range(2, n):
            if i % j == 0:
                return 0
        return 1
    
    ans = 0
    for i in range(n+1, r+1):
        if check(i, n) == 1:
            ans += 1
    print(ans)
