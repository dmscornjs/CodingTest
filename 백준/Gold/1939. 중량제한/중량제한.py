from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c= map(int,input().split()) 
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

# 두 정점 사이의 다른 경로가 있을 수 있다
def bfs(target): # 현재 가중치로 갈 수 있는지 탐색하는 BFS
    global start, end, visited
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        if v == end:
            return True
        for nv, w in graph[v]:
            if visited[nv] == False and w >= target:
                queue.append(nv)
                visited[nv] = True
    return False


def bs(left, right): #가능한 최대값을 찾기 위한 이분탐색
    global visited
    if left >= right:
        return right
    mid = (left + right+1)//2
    visited = [False for _ in range(n+1)]
    if bfs(mid): # 현재 탐색값으로 갈 수 있다면
        return bs(mid, right)
    else:
        return bs(left, mid-1)

print(bs(1, 10**9))  