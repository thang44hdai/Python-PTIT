while 1:
    x = int(input())
    if x == 0:
        break
    cnt = 0
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = x*3+1
        cnt += 1
    print(cnt+1)
