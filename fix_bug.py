a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = 88


def check():
    a[0][0] = 9
    b = 2


check()
print(a[0][0])
print(b)
