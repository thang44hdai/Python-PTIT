for _ in range(int(input())):
    n, x, m = [float(i) for i in input().split()]
    ans = 0
    while n<m:
        n = n*(1+x/100.0)
        ans +=1
    print(ans)