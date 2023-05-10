from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
nl = [c for c in range(n)]
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

ans = []
answer = []

for i in combinations(nl,n//2):
    #print(i)
    im = 0
    for j in combinations(i, 2):
        im += s[j[0]][j[1]] + s[j[1]][j[0]]
    ans.append(im)

for u in range(len(ans)//2):
    answer.append(abs(ans[u] - ans[-(u+1)]))

print(min(answer))