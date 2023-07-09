for i in range(int(input())):
    n = input()
    for j in range(0, len(n), 2):
        for k in range(int(n[j+1])):
            print(n[j], end="")
    print()
