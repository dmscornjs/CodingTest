from itertools import combinations

n = int(input())
set = [c for c in range(n)]

li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
sums = []

start = combinations(set, n//2)
for j in start:
    #print(j)
    data = combinations(j, 2)
    total = 0
    for i in data:
        a, b = i[0], i[1]
        total += li[a][b] + li[b][a]
    sums.append(total)

answer = abs(sums[-1] - sums[0])

for k in range(len(sums)//2):
    if abs(sums[k] - sums[-k-1]) <answer:
        answer = abs(sums[k] - sums[-k-1])

print(answer)