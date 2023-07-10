
for i in range(int(input())):
    n = input()
    ans = 999999
    num = 0
    for j in n:
        if (j >= '0' and j <= '9'):
            num = num*10+int(j)
        else:
            if num:
                ans = min(ans, num)
                num = 0
    if num>0:
        ans = min(ans, num)
    print(ans)
