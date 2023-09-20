def check(n):
    if len(n)%2==1:
        return False
    if n[::1]!=n[::-1]:
        return False
    for i in n:
        if int(i)%2==1:
            return False
    return True
for i in range(int(input())):
    s=int(input())
    for j in range(s):
        if check(str(j)):
            print(j,end=' ')
    print()