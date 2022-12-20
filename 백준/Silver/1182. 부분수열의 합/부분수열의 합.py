from itertools import combinations

n, s = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0

for i in range(1,n+1):
    for c in list(combinations(li, i)):
        if sum(c) ==s:
            cnt +=1

print(cnt)
