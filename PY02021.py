for _ in range(int(input())):
    n, m, k = [int(i) for i in input().split()]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    dd1, dd2, dd3 = {}, {}, {}
    for i in a:
        try:
            dd1[i] += 1
        except:
            dd1[i] = 1
    for i in b:
        try:
            dd2[i] += 1
        except:
            dd2[i] = 1
    check = False
    for i in c:
        try:
            dd3[i] += 1
        except:
            dd3[i] = 1
    ans = []
    for i in dd1:
        if dd2.get(i)!= None and dd3.get(i)!= None:
            x = min(dd1[i], dd2[i], dd3[i])
            ans += [i for j in range(x)]
    if len(ans)==0:
        print("NO")
    else:
        print(*ans)