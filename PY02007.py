a = [int(i) for i in input().split()]
st = set()
for i in a:
    st.add(i%42)
print(len(st))