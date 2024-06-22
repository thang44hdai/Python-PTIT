n, m, p = input(), input(), int(input())
for i in range(len(n)):
    if i+1 == p:
        print(m, end="")
        print(n[i], end="")
    else:
        print(n[i], end="")
