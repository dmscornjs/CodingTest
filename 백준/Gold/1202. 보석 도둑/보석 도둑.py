import sys, heapq
input = sys.stdin.readline
n, k = map(int, input().split())
mv = []
c = []
for _ in range(n):
    heapq.heappush(mv,list((map(int, input().split()))))
for _ in range(k):
    c.append(int(input()))
c.sort()

ans = 0
tmp = []

for bag in c:
    while mv and bag >= mv[0][0]:
        heapq.heappush(tmp, -heapq.heappop(mv)[1])
    if tmp:
        ans -= heapq.heappop(tmp)
    elif not mv:
        break
print(ans)