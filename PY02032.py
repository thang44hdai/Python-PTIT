st = set()
n = input()
for i in range(0, len(n), 2):
    if i+1<len(n):
        st.add(n[i:i+2])
print(*sorted(list(st)))