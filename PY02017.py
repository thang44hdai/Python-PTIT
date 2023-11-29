for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    dd = {}
    for i in a:
        try:
            dd[i] += 1
        except:
            dd[i] = 1
    for i in dd:
        if dd[i]&1:
            print(i)
            break