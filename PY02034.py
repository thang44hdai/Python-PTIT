n = input()
dd = {}
for i in range(0, len(n), 2):
    if i+1<len(n):
        if dd.get(n[i:i+2])!= None:
            dd[n[i:i+2]] += 1
        else:
            dd[n[i:i+2]]=1
for i in dd:
    print(i, dd[i])