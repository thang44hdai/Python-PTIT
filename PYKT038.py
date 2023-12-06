n = input()
k = len(n) % 3
if k > 0:
    n = "0"*(3-k)+n
for i in range(0, len(n), 3):
    sum = int(n[i])*4+int(n[i+1])*2+int(n[i+2])
    print(sum, end="")
