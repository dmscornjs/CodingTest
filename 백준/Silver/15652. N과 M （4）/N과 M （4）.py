from itertools import combinations_with_replacement
n, m = map(int, input().split())

set = [c for c in range(1, n+1)]

data = combinations_with_replacement(set, m)

for i in data:
    print(*i, end=' ')
    print()