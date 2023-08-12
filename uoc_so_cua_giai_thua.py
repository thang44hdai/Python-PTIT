for _ in range(int(input())):
    n, p = map(int, input().split())
    cnt = 0
    x = 1
    #62 7
    #7 7*2 7*3 ... 7*8
    #7**2 (49*2)%42=0 ...
    #7**3 ...
    while n/(p**x) > 1:
        cnt += int(n/(p**x))
        x += 1
    print(cnt)
