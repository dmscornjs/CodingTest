import sys, heapq
input = sys.stdin.readline
n, e = map(int, input().split())
graph = {c: {} for c in range(1, n+1)}
for _ in range(e):
    a, b, c = map(int, input().split())
    if b in graph[a] and graph[a][b] > c:
        continue
    else:
        graph[a][b] = c
        graph[b][a] = c


v1, v2 = map(int, input().split())

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0,start)]

    while queue:
        cur_dis, cur_v = heapq.heappop(queue)
        
        if cur_dis > distances[cur_v]:
            continue
        for neighbor, weight in graph[cur_v].items():
            distance = cur_dis + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances[end]

l1 = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, n)
l2 = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, n)

if min(l1, l2) == float('inf'):
    print(-1)
else:
    print(min(l1, l2))