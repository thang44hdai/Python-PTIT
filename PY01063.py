for _ in range(int(input())):
    n = input()
    s = input()
    cnt = 0
    idx = 0
    while (idx < len(n)):
        check = n.find(s, idx)
        if check != -1:
            idx = check + len(s)
            cnt += 1
        else:
            break
    print(cnt)
