from collections import deque
import sys
sys.setrecursionlimit(10**6)

# 섬끼리 구분 짓기
# dfs
def dfs(i, j):
    global count
    if i < 0 or j < 0 or i >= n or j >= n:
        return False
    if graph[i][j] == 1:
        graph[i][j] = count
        for c in range(4):
            nx = i + dx[c]
            ny = j + dy[c]
            dfs(nx, ny)
        return True

# 섬과 섬 사이의 최단거리 구하기
# bfs
def bfs(z):
    global ans
    dist = [[-1] * n for _ in range(n)] # 거리가 저장될 배열
    q = deque()

    for i in range(n): #현재 땅을 q에 담고 거리 초기화
        for j in range(n):
            if graph[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 곳이면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if graph[nx][ny] > 0 and graph[nx][ny] != z:
                ans = min(ans, dist[x][y])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,-1,0,1]
count = 2
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count +=1

for i in range(2, count):
    bfs(i)
       
print(ans)