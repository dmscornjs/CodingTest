import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 2 #사과 위치하면 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

l = int(input())
dirDict = dict()
for _ in range(l):
    x, c = map(str, input().split())
    dirDict[int(x)] = c

cnt = 0 
x, y = 0, 0
graph[x][y] = 1
direction = 0
queue = deque([(0,0)])

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2: #사과
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])
    
    elif graph[x][y] == 0: #그냥 빈칸
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 1: #뱀 몸에 닿음
        break

print(cnt)