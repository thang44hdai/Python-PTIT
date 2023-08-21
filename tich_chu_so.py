for _ in range(int(input())):
    n = input()
    mul = 1
    for i in n:
        if (i != '0'):
            mul*= int(i)
    print(mul)
