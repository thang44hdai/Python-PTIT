n = int(input())
l=[]
while True :
    x = [int(x) for x in input().split()]
    l += x
    if len(l) == n : break
chan = []
le = []
for i in range(n):
    if not l[i]%2:
        chan.append(l[i])
        l[i]=0
    else:
        le.append(l[i])
        l[i]=1
chan.sort()
le.sort(key = lambda x:x, reverse= True)
i_chan = 0
i_le = 0
for i in l:
    if not i:
        print(chan[i_chan], end = " ")
        i_chan +=1
    else:
        print(le[i_le], end = " ")
        i_le+=1
