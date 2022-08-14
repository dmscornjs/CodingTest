import numpy as np
def solution(N, stages):
    sc = [0]*(N+1)
    fsc = [0]*N
    for i in range(N+1):
        sc[i] = stages.count(i+1)
    print(sc)
      
    for i in range(N):
        try:
            fsc[i] = sc[i] / sum(sc[i:])
        except:
            fsc[i] = 0
    print(fsc) 
    answer = []
    li = fsc.copy()
    li.sort(reverse = True)
    while True:
        if max(fsc) == -1:
            break
        answer.append(fsc.index(max(fsc))+1)
        fsc[int(fsc.index(max(fsc)))] = -1
        
    return answer