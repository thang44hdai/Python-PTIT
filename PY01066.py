import math

def sol(n):
    leng = len(n)
    for i in range(int(leng/2)):
        if abs(ord(n[i])-ord(n[i+1])) != abs(ord(n[leng-1-i])-ord(n[leng-1-i-1])):
            return "NO"
    return "YES"
for _ in range(int(input())):
    print(sol(input()))
