# with open("DATA1.in") as f:
#     set1 = set(f.read().lower().split())
# with open("DATA2.in") as f:
#     set2 = set(f.read().lower().split())
# print(' '.join(sorted(set1.difference(set2))))
# print(' '.join(sorted(set2.difference(set1))))

with open("DATA1.in") as f:
    set1 = set(f.readline().strip().lower().split())
with open("DATA2.in") as f:
    set2 = set(f.readline().strip().lower().split())

a = list(set1.difference(set2))
a.sort()

b = list(set2.difference(set1))
b.sort()

print(*a)
print(*b)
