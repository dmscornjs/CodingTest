from itertools import permutations
n, m = map(int, input().split())
li = list(range(1, n+1))
for i in permutations(li, m):
    print(*i, end = " ")
    print()