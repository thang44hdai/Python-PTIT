for i in range(int(input())):
    l = list(map(int, input()))
    n = len(l)
    for j in range(n-1, 0, -1):
        if(l[j]>=5):
            l[j-1] +=1
            l[j]=0
        else:
            l[j]=0
    for j in l:
        print(j, end ="")
    print()
