for t in range(int(input())):
    n = str(input())
    cnt = 1
    for i in range(len(n)-1):
        if (n[i] == n[i+1]):
            cnt += 1
        else:
            print(cnt, n[i], sep="", end="")
            cnt = 1
    print(cnt, n[-1], sep="", end="")
    print()
