for _ in range(int(input())):
    n = int(input())
    num = 20
    while num < n:
        for i in range(num, 10**len(str(num)) , 2):
            if i>n:
                break
            s = str(i)
            if s==s[::-1]:
                print(i, end = " ")
        num *= 100
    print()
