import heapq
import sys
input = sys.stdin.readline
n, d = map(int, input().split())
graph = {i:{i+1: 1} for i in range(d)}
graph[d] = {}
li = []
for _ in range(n):
    s,e,l = map(int, input().split())
    if e <= d:
        if e in graph[s] and graph[s][e] < l:
            continue
        else:
            graph[s][e] = l

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}  # 모든 정점을 무한대로 초기화
    distances[start] = 0  # 출발점은 거리를 0으로 초기화
    queue = [(0, start)]  # 우선순위 큐에 (거리, 정점)의 튜플을 저장
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)  # 거리가 가장 짧은 정점 선택
        
        if current_distance > distances[current_vertex]:  # 이미 처리된 정점은 건너뛰기
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight  # 현재 정점을 거쳐서 이동하는 거리 계산
            
            if distance < distances[neighbor]:  # 더 짧은 거리가 발견되면 업데이트
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  # 우선순위 큐에 새로운 (거리, 정점) 추가
    
    return distances  # 모든 정점에 대한 최단 거리 반환


print(dijkstra(graph, 0)[d])