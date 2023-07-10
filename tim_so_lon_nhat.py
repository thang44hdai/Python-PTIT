for i in range(int(input())):
    n = input()
    ans = 0
    num = 0
    for j in n:
        if (j >= '0' and j <= '9'):
            num = num*10+int(j)
        else:
            if num:
                ans = max(ans, num)
                num = 0
    ans = max(ans, num)
    print(ans)
