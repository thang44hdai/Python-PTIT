n = input()
while len(n) > 1:
    n1 = n[:len(n)//2]
    n2 = n[len(n)//2:]
    ans = int(n1) + int(n2)
    print(ans)
    n=str(ans)