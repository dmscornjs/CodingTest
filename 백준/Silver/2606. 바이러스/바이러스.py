n = int(input())
m = int(input())
graph =[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    for i in graph[v]:
        visited[i] = 1
        for u in graph[i]:
            if visited[u] == 0:
                visited[u] = 1
                dfs(graph, u, visited)


visited = [0] * (n+1) 
dfs(graph, 1, visited)
print(sum(visited)-1)