def solution(id_list, report, k):
    dic = {}
    singoed = {}
    stop = []
    answer = []
    
    for j in id_list:
        dic[j] = []
        singoed[j] = 0
        
    for i in report:
        x,y = i.split()
        if y not in dic[x]:
            dic[x].append(y)
            singoed[y] +=1  

    for id in id_list:
        if singoed[id] >=k:
            stop.append(id)

    for d in id_list:
        c = 0
        for s in stop:
            if s in dic[d]:
                c +=1
        answer.append(c)
        
    return answer