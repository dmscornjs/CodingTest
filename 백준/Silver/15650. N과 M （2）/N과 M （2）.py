from itertools import combinations

n, m = map(int, input().split())
li = list(range(1, n+1))
for i in combinations(li, m):
    print(*i, end = " ")
    print()
