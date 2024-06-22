for _ in range(int(input())):
    n = input()
    ans = ""
    for i in n.split():
        if len(ans) + len(i) > 100:
            break
        else:
            ans += i + " "
    print(ans)
