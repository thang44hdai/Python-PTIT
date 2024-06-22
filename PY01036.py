for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        sum = 0
        for i in range(2, n+1, 2):
            sum += 1.0/i
    else:
        sum = 0
        for i in range(1, n+1, 2):
            sum += 1.0/i
    print("{:.6f}".format(sum))
