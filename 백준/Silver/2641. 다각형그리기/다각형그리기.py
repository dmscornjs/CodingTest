import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
p = deque(list(map(int, input().split())))
li = []
mobang = []
ans = []

for i in range(n): #순방향 확인하여 답에 저장
    p.rotate(1)
    mobang.append(list(p))
    # print(p)
    # if p in li:
    #     ans.append(list(p))

#역방향 패턴 만들기
p2 = deque()
for i in p:
    p2.append(((i + 1)%4)+1)   
p2.reverse()
#print()

for i in range(n): #역방향 확인하여 답에 저장
    p2.rotate(1)
    mobang.append(list(p2))
    # print(p2)
    # if p2 in li:
    #     ans.append(list(p2))

m = int(input())
for _ in range(m):
    x = list(map(int, input().split()))
    if x in mobang:
        ans.append(x)
    #li.append(deque(list(map(int, input().split()))))

print(len(ans))
for i in ans:
    print(*i)
