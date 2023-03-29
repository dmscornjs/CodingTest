from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j)) # 빙산의 위치를 (i, j) 형태로 ice에 저장

dx = [1,0,-1,0]
dy = [0,-1,0,1]
year = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    seali = []

    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n or 0 <= ny < m:
                if not graph[nx][ny]: #주변 바다 확인
                    sea +=1
                elif graph[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seali.append((x, y, sea))
    for x, y, sea in seali:
        graph[x][y] = max(0, graph[x][y] - sea)
    return 1
                    
while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0: # 탐색이 끝나면 바다가 된 빙산을 체크
            delList.append((i, j))
    if group > 1: # 빙산그룹이 2개 이상이면 년을 출력
        print(year)
        break
    
    # 다 녹은 빙산은 탐색할 필요가 없으므로 ice에서 제거
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)
