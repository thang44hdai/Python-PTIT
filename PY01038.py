for _ in range(int(input())):
    n = int(input())
    check = True
    for i in range(1000):
        if n % 7 == 0:
            print(n)
            check = False
            break
        else:
            n += int(str(n)[::-1])
    if check == True:
        print(-1)