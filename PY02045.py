n = input()
while len(n) > 1:
    l = len(n)//2
    n = str(int(n[0:l])+int(n[l:]))
    print(n)
