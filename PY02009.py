for _ in range(int(input())):
    n = int(input())
    dic = {}
    cnt = 0
    while n-1 >= 0:
        x = int(input())
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
        cnt = max(cnt, dic[x])
        n -= 1
    ans = 1e9
    for i in dic:
        if dic[i] == cnt:
            ans = min(ans, i)
    print(ans)
