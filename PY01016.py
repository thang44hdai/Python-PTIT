for _ in range(int(input())):
    n = input()
    for i in range(0, len(n), 2):
        for j in range(ord(n[i+1])-ord('0')):
            print(n[i], end="")
    print()
