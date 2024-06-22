for _ in range(int(input())):
    a = []
    n = input()
    sum = 0
    for i in n:
        if "0" <= i <= "9":
            sum += int(i)
        else:
            a.append(i)
    a.sort()
    for i in a:
        print(i, end="")
    print(sum)