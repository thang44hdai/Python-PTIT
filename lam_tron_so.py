t = int(input())
while t>0:
    x = input()
    n = len(x)
    if(n==1):
        print(x)
        continue
    for i in range(n-1, 1, -1):
        if(x[i]>='5'):
            x[i-1]=str(int(x[i])+1)
    if(x[1]>='5'):
        print(int(x[0])+1, end ="")
    for i in range(1, n-1, 1):
        print("0", end ="")

    