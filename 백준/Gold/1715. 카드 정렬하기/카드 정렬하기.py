import sys, heapq
input = sys.stdin.readline
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
heapq.heapify(li)
cnt = 0
while len(li) != 1:
        a = heapq.heappop(li)
        b = heapq.heappop(li)
        ab = a+b
        cnt += ab
        heapq.heappush(li, ab)
        if len(li) < 2:
            break
print(cnt)