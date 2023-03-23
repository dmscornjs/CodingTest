import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {c: {} for c in range(1, n+1)}

for _ in range(m):
    s, e, cost = map(int, input().split())
    if e in graph[s] and graph[s][e] < cost:
        continue
    else:
        graph[s][e] = cost

start, end = map(int, input().split())

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph} # 모든 정점을 무한대로 초기화
    distances[start] = 0 # 출발점은 거리를 0으로 초기화
    queue = [(0, start, [start])] # 우선순위 큐에 (거리, 정점, 방문노드)의 튜플을 저장
    visited = {vertex : [] for vertex in graph} # 방문노드를 기록할 딕셔너리 
    visited[start] = [start]

    while queue:
        cur_dis, cur_v, cur_visit = heapq.heappop(queue) # 거리가 가장 짧은 정점 선택
        
        if cur_dis > distances[cur_v]:
            continue # 이미 처리된 정점은 건너뛰기
        
        for neighbor, weight in graph[cur_v].items():
            distance = cur_dis + weight # 현재 정점을 거쳐서 이동하는 거리 계산

            if distance < distances[neighbor]:    # 현재 정점을 거치는 것이 더 짧은 거리라면 업데이트
                distances[neighbor] = distance     
                nei_visit = cur_visit + [neighbor] # 현재 정점의 방문노드들과 지금 방문한 노드를 추가  
                visited[neighbor] = nei_visit
                heapq.heappush(queue, (distance, neighbor, nei_visit)) # 우선순위 큐에 새로운 (거리, 정점, 방문노드) 추가
    
    return (distances[end], visited[end]) # 모든 정점에 대한 최단 거리 반환

ans = dijkstra(graph, start, end)
print(ans[0])
print(len(ans[1]))
print(*ans[1])