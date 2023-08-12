for _ in range(int(input())):
    n, m , k = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l3 = list(map(int, input().split()))
    check = False
    for i in l1:
        if i in l2:
            if i in l3:
                check = True
                print(i, end=" ")
    if not(check):
        print("NO")
    print()