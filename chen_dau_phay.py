from audioop import reverse
import textwrap

for _ in range(int(input())):
    n = input()
    n = n[::-1]
    l = list(textwrap.wrap(n, 3))
    ans = ','.join(l)
    print(ans[::-1])
