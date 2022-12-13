import sys
#sys.stdin=open("input.txt", "rt")
from collections import deque

N,M,R = map(int,sys.stdin.readline().split())

# graph
graph=[[] for _ in range(N+1)]

#입력받는 간선 정보 그래프화
for i in range(M):
    tmpL=list(map(int,sys.stdin.readline().split()))
    graph[tmpL[0]].append(tmpL[1])
    graph[tmpL[1]].append(tmpL[0])

# 정렬
for i in range(N+1):
    graph[i].sort()

#BFS 함수 
def bfs(graph,R,visited):
    queue=deque([R])
    visited[R]=1 #첫번째 방문 정점
    count=2 #두번째 방문 정점
    
    while queue:
        R=queue.popleft()
        
        for i in graph[R]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=count 
                count+=1 # n+1 번째 방문 정점

#정점 리스트
visited=[0]*(N+1)

bfs(graph,R,visited)

#출력
for i in visited[1::]:
    print(i)