from cmath import sqrt

for _ in range(int(input())):
    n = int(input())
    print("1", end ="")
    for i in range(2, round(n**0.5)):
        cnt = 0
        while n%i==0:
            cnt += 1
            n/=i
        if cnt:
            print(" * ",i, "^", cnt, sep = "", end ="")
    if n>1:
        print(" * ", int(n), "^1", sep="", end ="")
    print()
    