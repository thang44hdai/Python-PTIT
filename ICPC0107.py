for _ in range(int(input())):
    n, m = map(str, input().split())
    x = input()
    if " " in x:
        x, y = x.split()
    else:
        y = input()
    p = str(min(m, n))
    q = str(max(m, n))
    print(int(x.replace(q, p)) + int(y.replace(q, p)), end=" ")
    print(int(x.replace(p, q)) + int(y.replace(p, q)))