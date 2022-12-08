from itertools import product
n, m = map(int, input().split())

set = [c for c in range(1, n+1)]
data = product(set, repeat = m)

for i in data:
    print(*i, end=' ')
    print()