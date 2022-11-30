import sys
sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려주는 코드

def dfs(V, E, r):
    global cnt
    visited[r] = cnt
    E[r].sort(reverse= True)
    for x in E[r]:
        if visited[x] == 0:
            cnt +=1
            dfs(V, E, x)

N, M, R = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for k in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# for c in range(N):
#     graph[c].sort(reverse= True)

#print(graph)
visited = [0 for _ in range(N+1)]
cnt = 1

dfs(visited, graph, R)
for u in visited[1:]:
    print(u)
#print(*visited[1:])
