import sys, heapq
input = sys.stdin.readline
V, E = map(int, input().split()) 
k = int(input())
graph = {c: {} for c in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u] and graph[u][v] < w:
        continue
    else:
        graph[u][v] = w

def dijkstra(graph, start):
    distances = {ver: float('inf') for ver in graph} # 정점 거리 무한대로 초기화
    distances[start] = 0 #시작정점 초기화
    queue = [(0, start)] #우선순위 큐에 거리, 정점 저장

    while queue:
        cur_dis, cur_v = heapq.heappop(queue)
        if cur_dis > distances[cur_v]:
            continue
        for neighbor, weight in graph[cur_v].items():
            distance = cur_dis + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

ans = dijkstra(graph, k)

for i in range(V):
    if ans[i+1] == float('inf'):
        print('INF')
    else:
        print(ans[i+1])